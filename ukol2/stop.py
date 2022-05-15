class Stop:
    def __init__(self):
        self.stop_id = None
        self.stop_code = None
        self.stop_name = None
        self.stop_desc = None
        self.stop_lat = None
        self.stop_lon = None
        self.zone_id = None
        self.stop_url = None
        self.location_type = None
        self.parent_station = None
        self.stop_timezone = None
        self.wheelchair_boarding = None
        self.level_id = None
        self.platform_code = None

    def loadAttributes(self, attributes: dict):
        # load stop attributes from given dictionary
        if 'stop_id' in attributes.keys():
            self.stop_id = attributes['stop_id']

        if 'stop_code' in attributes.keys():
            self.stop_code = attributes['stop_code']

        if 'stop_name' in attributes.keys():
            self.stop_name = attributes['stop_name']

        if 'stop_desc' in attributes.keys():
            self.stop_desc = attributes['stop_desc']

        if 'stop_lat' in attributes.keys():
            self.stop_lat = attributes['stop_lat']

        if 'stop_lon' in attributes.keys():
            self.stop_lon = attributes['stop_lon']

        if 'zone_id' in attributes.keys():
            self.zone_id = attributes['zone_id']

        if 'stop_url' in attributes.keys():
            self.stop_url = attributes['stop_url']

        if 'location_type' in attributes.keys():
            self.location_type = attributes['location_type']

        if 'parent_station' in attributes.keys():
            self.parent_station = attributes['parent_station']

        if 'stop_timezone' in attributes.keys():
            self.stop_timezone = attributes['stop_timezone']

        if 'wheelchair_boarding' in attributes.keys():
            self.wheelchair_boarding = attributes['wheelchair_boarding']

        if 'level_id' in attributes.keys():
            self.level_id = attributes['level_id']

        if 'platform_code' in attributes.keys():
            self.platform_code = attributes['platform_code']

    # Getters
    def getID(self):
        return self.stop_id

    def getCode(self):
        return self.stop_code

    def getName(self):
        return self.stop_name

    def getDesc(self):
        return self.stop_desc

    def getLat(self):
        return self.stop_lat

    def getLon(self):
        return self.stop_lon

    def getZoneId(self):
        return self.zone_id

    def getUrl(self):
        return self.stop_url

    def getLocationType(self):
        return self.location_type

    def getParentStation(self):
        return self.parent_station

    def getTimezone(self):
        return self.stop_timezone

    # here add more getters if needed


