import json
import csv
import codecs

csvFile = open('USvideos.csv', 'br')
jsonFile = open('file.json', 'w')
reader = csv.DictReader(codecs.iterdecode(csvFile, 'utf-8'))

out = json.dumps({"USvideos": [ row for row in reader ]}, sort_keys=True, indent=4, separators=(',', ':'))

jsonFile.write(out)
