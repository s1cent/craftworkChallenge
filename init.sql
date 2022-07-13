GRANT ALL PRIVILEGES ON DATABASE docker TO docker;

CREATE TABLE europe (
  ort varchar(250) NOT NULL,
  lat float(53) NOT NULL,
  longitude float(53) NOT NULL,
  types varchar(250) NOT NULL
);

CREATE TABLE nebraska (
  ort varchar(250) NOT NULL,
  lat float(53) NOT NULL,
  longitude float(53) NOT NULL,
  types varchar(250) NOT NULL
);