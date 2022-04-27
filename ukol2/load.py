import csv
from stop import *

# Initialize dictionaries os stops
stops = {}

# Load stop to dictionary key = stop id, item = stop_object
with open('PID_GTFS\\stops.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        stop = Stop()
        stop.loadAttributes(row)
        stops.update({stop.getId(): stop})

print(stops['U4511Z4'].getName())

stops['U4511Z4'].print()
