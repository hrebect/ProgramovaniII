from trip import *
from typing import List


class StopSegment:
    def __init__(self, where_from, where_to):
        self.where_from: str = where_from
        self.where_to: str = where_to
        self.trips: List[Trip] = []
        self.route_short_names: List[str] = []

    def addTrip(self, trip: Trip):
        # Adds trip to list of trips
        self.trips.append(trip)

    def addRouteShortName(self, short_name: str):
        # If short name is not in the list, append short name to the list
        if short_name not in self.route_short_names:
            self.route_short_names.append(short_name)

    # Getters
    def getTripCount(self):
        return len(self.trips)

    def getRouteShortNames(self):
        return self.route_short_names

    def getWhereFrom(self):
        return self.where_from

    def getWhereTo(self):
        return self.where_to