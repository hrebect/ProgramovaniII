class Trips:
    def __init__(self):
        self.route_id = None
        self.service_id = None
        self.trip_id = None
        self.trip_headsign = None
        self.trip_short_name = None
        self.direction_id = None
        self.block_id = None
        self.shape_id = None
        self.wheelchair_accessible = None
        self.bikes_allowed = None

    def loadAttributes(self, attributes: dict):
        # load stop attributes from given dictionary
        if 'route_id' in attributes.keys():
            self.route_id = attributes['route_id']

        if 'service_id' in attributes.keys():
            self.service_id = attributes['service_id']

        if 'trip_id' in attributes.keys():
            self.trip_id = attributes['trip_id']

        if 'trip_headsign' in attributes.keys():
            self.trip_headsign = attributes['trip_headsign']

        if 'trip_short_name' in attributes.keys():
            self.trip_short_name = attributes['trip_short_name']

        if 'direction_id' in attributes.keys():
            self.direction_id = attributes['direction_id']

        if 'block_id' in attributes.keys():
            self.block_id = attributes['block_id']

        if 'shape_id' in attributes.keys():
            self.shape_id = attributes['shape_id']

        if 'wheelchair_accessible' in attributes.keys():
            self.wheelchair_accessible = attributes['wheelchair_accessible']

        if 'bikes_allowed' in attributes.keys():
            self.bikes_allowed = attributes['bikes_allowed']

    def getTripID(self):
        return self.trip_id
