#Author: Chase Renick
#Date: October 15, 2024
#Purpose: Rideshare demo app
#Version 1.0.0

#Libraries

class Distance:
    """
    Calcualte distance between two different
    latitude and longitude points using haversine distance
    """
    def __init__(self,
                 lat1,
                 lon1,
                 lat2,
                 lon2):

        self.lat1 = lat1
        self.lon1 = lon1
        self.lat2 = lat2
        self.lon2 = lon2

        self.distance = self.haversine_distance()

    def haversine_distance(self):

        from math import sin, cos, sqrt, atan2, radians

        lat1 = radians(self.lat1)
        lon1 = radians(self.lon1)
        lat2 = radians(self.lat2)
        lon2 = radians(self.lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Approximate radius of earth in km
        R = 6373.0

        dist = R * c
        return round(dist, 2)