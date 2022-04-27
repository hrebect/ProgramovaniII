class StopTime:
    def __init__(self):
        self.trip_id = None
        self.arrival_time = None
        self.departure_time = None
        self.stop_id = None
        self.stop_sequence = None
        self.stop_headsign = None
        self.pickup_type = None
        self.drop_off_type = None
        self.continuous_pickup = None
        self.continuous_drop_off = None
        self.shape_dist_traveled = None
        self.timepoint = None

    def loadAttributes(self, attributes: dict):
        # load stop time attributes from given dictionary
        if 'trip_id' in attributes.keys():
            self.trip_id = attributes['trip_id']
        if 'arrival_time' in attributes.keys():
            self.arrival_time = attributes['arrival_time']

        if 'departure_time' in attributes.keys():
            self.departure_time = attributes['departure_time']

        if 'stop_id' in attributes.keys():
            self.stop_id = attributes['stop_id']

    # Getters
    def getID(self):
        return self.trip_id

    def getDepartureTime(self):
        return self.departure_time

    def getArrivalTime(self):
        return self.arrival_time

    def getStopID(self):
        return self.stop_id

    # add more
