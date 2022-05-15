from trip import *
from typing import List
class StopSegment:
    def __init__(self, where_to, where_from):
        self.where_from = where_to
        self.where_to = where_from
        self.trips: List[Trips] = []
        self.bus_lines: List[str] = []

    def compare(self, where_from, where_to):
        if where_from == self.where_from and where_to == self.where_to:
            return True
        return False

    def addTrip(self, trip: Trips):
        self.trips.append(trip)

    def addBusLine(self, bus_line: str):
        if bus_line not in self.bus_lines:
            self.bus_lines.append(bus_line)

    def getTripCount(self):
        return len(self.trips)

    def getBusLines(self):
        return self.bus_lines

    def getWhereFrom(self):
        return self.where_from

    def getWhereTo(self):
        return self.where_to