import csv
from stop import *
from stoptime import *
from trip import *
from routes import *
from stop_segment import *

# Initialize dictionaries for each class
stops = {}
stop_times = {}
trips = {}
routes = {}
stop_segments = {}

# Load stops to dictionary by primary key = stop_id, item = Stop object
with open('stops.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        stop = Stop()
        stop.loadAttributes(row)
        stops.update({stop.getID(): stop})

# Load routes to dictionary by primary key = route_id, item = Route object
with open('routes.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    for row in reader:
        route = Route()
        route.loadAttributes(row)
        routes.update({route.getID(): route})

# Load stop times to dictionary by foreign key = trip_id, item = StopTime object
with open('stop_times.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    id = ""
    for row in reader:
        stop_time = StopTime()
        stop_time.loadAttributes(row)
        if stop_time.getTripID() == id:
            bus_line_stops.append(stop_time)
        else:
            if id != "":
                stop_times.update({id: bus_line_stops})
            # Foreign key
            id = stop_time.getTripID()
            bus_line_stops = [stop_time]
    stop_times.update({id: bus_line_stops})

# Load trips to dictionary by foreign key = route_id, item = Trip object
with open('trips.txt', newline='', encoding="utf-8") as data_csv:
    reader = csv.DictReader(data_csv, delimiter=',')
    id = ""
    for row in reader:
        trip = Trip()
        trip.loadAttributes(row)
        if trip.getRouteID() == id:
            route_trips.append(trip)
        else:
            if id != "":
                trips.update({id: route_trips})
            # Foreign key
            id = trip.getRouteID()
            route_trips = [trip]
    trips.update({id: route_trips})


# Browse all routes
for route_ID, route in routes.items():

    # Route name (number code)
    route_name = route.getShortName()

    # List of trips on the route
    route_trips = trips[route_ID]

    # Browse all those trips
    for trip in route_trips:

        # Trip ID
        trip_ID = trip.getID()

        # List of stop times (stops) of the trip
        stop_time = stop_times[trip_ID]

        # Browse all stop times
        for i in range(len(stop_time) - 1):

            # ID of previous stop
            where_from = stop_time[i].getStopID()

            # ID of next stop
            where_to = stop_time[i+1].getStopID()

            # Try if current segment already exists
            try:
                # Existing stop segment
                ss = stop_segments[where_from, where_to]

                # Add trip to segment
                ss.addTrip(trip)

                # Add route name to segment
                ss.addRouteShortName(route_name)

            except:
                # Create stop segment
                ss = StopSegment(where_from, where_to)

                # Add trip to segment
                ss.addTrip(trip)

                # Add route name to segment
                ss.addRouteShortName(route_name)

                # Add new stop segment into list of stop segments
                stop_segments[where_from, where_to] = ss

# Inicialize variables to get the busiest stop segment
count_max = 0
ss_max = None

# Browse stop segments
for ss in stop_segments.values():

    # Get amount of trips for stop segment
    count = ss.getTripCount()

    # Update variables if condition is True
    if count > count_max:
        count_max = count
        ss_max = ss

# ID of start stop of stop segment
where_from = ss_max.getWhereFrom()

# ID of end stop of stop segment
where_to = ss_max.getWhereTo()

# Start stop name
from_stop = stops[where_from].getName()

# End stop name
to_stop = stops[where_to].getName()

# Route names
route_names = ss_max.getRouteShortNames()

print("from stop", from_stop)
print("to stop", to_stop)
print("total amount of trips", count_max)
print("route short names:", route_names)