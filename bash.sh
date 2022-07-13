#!/bin/bash
INPUT=challenge/challenge.csv

split -d -l 10000 $INPUT chunk --additional-suffix=.csv

for tempFile in chunk*
do
  content=$(curl -X PUT -F file=@$tempFile "http://localhost/update")
  rm $tempFile
  echo $content
done

$SHELL