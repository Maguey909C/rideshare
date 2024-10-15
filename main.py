#Author: Chase Renick
#Date: October 15, 2024
#Purpose: Rideshare demo app
#Version 1.0.0

#import files
import math_ops

#import libraries
import pandas as pd
import itertools


class Location:
    """
    Sets a lat and on for a given location
    """
    def __init__(self,
                 lat,
                 lon):
        self.lat = lat
        self.lon = lon


class Driver(Location):
    """
    Assigns attributes to driver such as status, name, location
    """
    def __init__(self,
                 status,
                 driver_name,
                 location):

        # Driver's able to set their status
        self.status = status
        self.driver_name = driver_name
        self.driver_location = location

    def updateStatus(self, new_status):
        self.status = new_status
        return self.status


class DriverList(Driver):
    """
    Makes list of drivers with the attributes provided in CSV
    """
    def __init__(self,
                 drivers):

        self.drivers = drivers
        self.driver_list = self.getDriverList()

    def getDriverList(self):
        dlist = []
        for i in range(len(self.drivers)):
            driver_location = Location(self.drivers.loc[i]['latitude'], self.drivers.loc[i]['longitude'])
            d = Driver('unavailable', self.drivers.loc[i]['id'], driver_location)
            dlist.append(d)

        return dlist

def getAvailableDrivers(driver_list, status):
    """
    Input: Pass in list of drivers:
    :return: get out updated list based on those availbe
    """
    ava_drivers = []
    for drive in driver_list:
        if drive.status == status:
            ava_drivers.append(drive)
    return ava_drivers


class Rider(Location):
    """
    Assigns attributes to a rider such as name and location
    """
    def __init__(self,
                 rider_name,
                 rider_location):

        self.rider_name = rider_name
        self.rider_location = rider_location


class RiderList(Rider):
    """
    Makes list of riders with the attributes provided in CSV
    """

    def __init__(self,
                 riders):
        self.riders = riders

    def getRiderList(self):

        rid_list = []
        for i in range(len(self.riders)):
            rider_location = Location(self.riders.loc[i]['pickup_latitude'], self.riders.loc[i]['pickup_longitude'])
            rid = Rider(self.riders.loc[i]['id'], rider_location)
            rid_list.append(rid)
        return rid_list



if __name__ == '__main__':

    #Read in the files
    rider_df = pd.read_csv('/Users/chaserenick/PycharmProjects/palantirRideshare/data/riders.csv')
    driver_df = pd.read_csv('/Users/chaserenick/PycharmProjects/palantirRideshare/data/drivers.csv')

    #Creating Driver Objects based on dataframe
    d = DriverList(driver_df)
    driver_list = d.getDriverList()

    #Accessing list of driver objects
    print(driver_list[0].driver_location.lat)

    #Make two drivers available
    driver_list[3].updateStatus('available')
    driver_list[4].updateStatus('available')

    #Give me list of only available drivers
    available_drivers = getAvailableDrivers(driver_list, 'available')
    print('Available Drivers:', len(available_drivers))


    #Creating Driver Objects based on dataframe
    r = RiderList(rider_df)
    rider_list = r.getRiderList()

    #Accessing list of rider objects
    print(rider_list[2].rider_location.lat)

    #Calculating Distances between a driver and a rider
    test_dist = math_ops.Distance(driver_list[0].driver_location.lat,
                         driver_list[0].driver_location.lon,
                         rider_list[1].rider_location.lat,
                         rider_list[1].rider_location.lon)

    print("Havesine Distance:", test_dist.haversine_distance())


    for rid in rider_list:
        r_distances = []
        for i in range(len(driver_list)):
            rider1_dist = math_ops.Distance(rid.rider_location.lat,
                            rid.rider_location.lon,
                            driver_list[i].driver_location.lat,
                            driver_list[i].driver_location.lon).haversine_distance()

            r_distances.append(rider1_dist)

        # print(r_distances)
        get_min = min(r_distances)

        j = 0
        for val in range(len(r_distances)):
            if get_min == r_distances[val]:
                j = val

        print ("Driver Name:", driver_list[j].driver_name)