from io import BytesIO
from fastapi import FastAPI, File, UploadFile
import numpy as np
import pandas as pd
from shapely.geometry import Polygon
import geopandas as gp
import psycopg2
import psycopg2.extras as extras
from psycopg2.extensions import register_adapter, AsIs

app = FastAPI()

#Variables for the boundary boxes of Europe and Nebraska
europe_Boundary = Polygon([(71.1338889, -9.49901111111111), (71.1338889, 69.03333333333333),
                            (34.8005556, -9.49901111111111), (34.8005556, 69.03333333333333)])
nebraska_Boundary = Polygon([(40, -95.31666666666666), (40, -104.06666638888889),
                              (43, -95.31666666666666), (43, -104.06666638888889)])

#connecting to the database
def connect():
    conn = psycopg2.connect(
        database="docker", user='docker', password='docker', host='db', port='5432'
    )
    cursor = conn.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()
    print("Connection established to: ", data)
    register_adapter(np.ndarray, addapt_numpy_array)
    return conn, cursor

# For later so we can save np arrays into the database
def addapt_numpy_array(numpy_array):
    return AsIs(tuple(numpy_array))

#preprocess the csv file we get from the put command
def preprocess_file(contents):
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer, header=None, usecols=range(4), names=["Ort", "Lat", "Long", "Type"])
    buffer.close()
    df = df[pd.to_numeric(df['Lat'], errors='coerce').notnull()]
    df_City = df.loc[df['Type'] == "city"]
    gdf = gp.GeoDataFrame(
        df_City, geometry=gp.points_from_xy(df_City.Lat, df_City.Long))
    gdf['Latitude/Longtitude'] = gdf['Lat'] + ', ' + gdf['Long']
    return gdf

# insert the new list into the database
def insert_into_database(df, conn, param, cursor):
    cols = df[["Ort", "Lat", "Long", "Type"]].values
    queryText = "INSERT INTO " + param + " (ort, lat, longitude, types) VALUES %s"
    extras.execute_values(cursor, queryText, cols, template=None)
    conn.commit()

# "main" function of the challange
@app.put("/update")
async def load_file(file: UploadFile = File()):
    conn, cursor = connect()

    contents = await file.read()

    gdf = preprocess_file(contents)

    df_Europe = gdf[gdf.geometry.within(europe_Boundary)]
    df_Nebraska = gdf[gdf.geometry.within(nebraska_Boundary)]

    insert_into_database(df_Europe, conn, "europe", cursor)
    insert_into_database(df_Nebraska, conn, "nebraska", cursor)

    conn.close()

    return {"message": "Successfully uploaded!"}