import csv
from stop import *
from stoptime import *
from trip import *
from routes import *
from stopsegment import *

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


# Dictionary where key = stop_segment_ID, item = number of trips
segment_trip_count = {}

# Browse stop segments
for key, val in stop_segments.items():

    # Get amount of trips for stop segment
    count = val.getTripCount()
    segment_trip_count[key] = count

# Sort dictionary by values
sorted_segments = sorted(segment_trip_count.items(), key=lambda kv: kv[1], reverse=True)

# Browse 5 busiest stop segments
for segment in sorted_segments[0:5]:
    stop_segment = stop_segments[segment[0]]

    # Start stop name
    from_stop = stops[segment[0][0]].getName()

    # End stop name
    to_stop = stops[segment[0][1]].getName()

    # Route names
    route_names = stop_segments[segment[0]].getRouteShortNames()

    # Print result
    print(from_stop, "-", to_stop, "(" + str(segment[1]) + ")", route_names)
