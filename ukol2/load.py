import csv
from stop import *
from stoptime import *
from trip import *

# Initialize dictionaries os stops
stops = {}
stop_times = {}
trips = {}

# Load stops to dictionary key = stop_id, item = stop object
with open('PID_GTFS\\stops.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        stop = Stop()
        stop.loadAttributes(row)
        stops.update({stop.getID(): stop})

# Load stop times to dictionary key = trip_id, item = stop_time object
with open('PID_GTFS\\stop_times.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        stop_time = StopTime()
        stop_time.loadAttributes(row)
        stop_times.update({stop_time.getID(): stop_time})

# Load trips to dictionary key = trip_id, item = trip_object
with open('PID_GTFS\\stop_times.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        trip = Trips()
        trip.loadAttributes(row)
        trips.update({trip.getTripID(): trip})

print(stops['U4511Z4'].getName())

stops['U4511Z4'].print()
print(stop_times)
print(trips)
