class Routes:
    def __init__(self):
        self.route_id = None
        self.agency_id = None
        self.route_short_name = None
        self.route_long_name = None
        self.route_type = None

    def loadAttributes(self, attributes: dict):
        # load stop attributes from given dictionary
        if 'route_id' in attributes.keys():
            self.route_id = attributes['route_id']

        if 'agency_id' in attributes.keys():
            self.agency_id = attributes['agency_id']

        if 'route_short_name' in attributes.keys():
            self.route_short_name = attributes['route_short_name']

        if 'route_long_name' in attributes.keys():
            self.route_long_name = attributes['route_long_name']

        if 'route_type' in attributes.keys():
            self.route_type = attributes['route_type']

    def getID(self):
        return self.route_id

    def getBusLine(self):
        return self.route_short_name
