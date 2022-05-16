import csv
from stop import *
from stoptime import *
from trip import *
from routes import *
from stop_segment import *

# Initialize dictionaries os stops
stops = {}
stop_times = {}
trips = {}
routes = {}
stop_segments = {}

folder_dir = "C:\\programovani_2\\ProgramovaniII-main\\data_praha\\"

# Load stops to dictionary key = stop_id, item = stop object
with open(folder_dir + 'stops.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        stop = Stop()
        stop.loadAttributes(row)
        stops.update({stop.getID(): stop})

# Load stop times to dictionary key = trip_id, item = stop_time object
with open(folder_dir + 'stop_times.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    id = ""
    for row in reader:
        stop_time = StopTime()
        stop_time.loadAttributes(row)
        if stop_time.getID() == id:
            bus_line_stops.append(stop_time)
        else:
            if id != "":
                stop_times.update({id: bus_line_stops})

            id = stop_time.getID()
            bus_line_stops = [stop_time]
    stop_times.update({id: bus_line_stops})

# Load trips to dictionary key = trip_id, item = trip_object
with open(folder_dir + 'trips.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    id = ""
    for row in reader:
        trip = Trips()
        trip.loadAttributes(row)
        if trip.getRouteID() == id:
            route_trips.append(trip)
        else:
            if id != "":
                trips.update({id: route_trips})

            id = trip.getRouteID()
            route_trips = [trip]
    trips.update({id: route_trips})

# Load routes to dictionary key = route_id, item = route_object
with open(folder_dir + 'routes.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        route = Routes()
        route.loadAttributes(row)
        routes.update({route.getID(): route})


for route_ID, route in routes.items():
    bus_line = route.getBusLine()
    route_trips = trips[route_ID]
    for trip in route_trips:
        trip_ID = trip.getID()
        stop_time = stop_times[trip_ID]
        for i in range(len(stop_time) - 1):
            where_from = stop_time[i].getStopID()
            where_to = stop_time[i+1].getStopID()
            try:
                ss = stop_segments[where_from, where_to]
                ss.addTrip(trip)
                ss.addBusLine(bus_line)
            except:
                ss = StopSegment(where_from, where_to)
                ss.addTrip(trip)
                ss.addBusLine(bus_line)
                stop_segments[where_from, where_to] = ss


count_max = 0
ss_max = None
for ss in stop_segments.values():
    count = ss.getTripCount()
    if count > count_max:
        count_max = count
        ss_max = ss

where_from = ss_max.getWhereFrom()
where_to = ss_max.getWhereTo()
from_stop = stops[where_from].getName()
to_stop = stops[where_to].getName()
bus_lines = ss_max.getBusLines()
print("from stop", from_stop)
print("to stop", to_stop)
print("total amount of trips", count_max)
print("bus_lines", bus_lines)