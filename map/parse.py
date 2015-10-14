import csv
import json

csvfile = open('DATA_Traffic_Vehicle Detector_info (1).csv', 'r')

for row in csv.reader(csvfile):

	print json.dumps({"addr":[row[1], row[2]], "text":row[0]})
	print ","