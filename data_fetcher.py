import urllib2
import json


class LocationDataFetcher:

    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch"
        self.data_format = "json"
        self.key = "AIzaSyAbZE_S3PVeGEd0A58rLRB9yP6iHk_n7xE"
        self.radius = 500


    def build_url(self):
        return "{base_url}/{format}?key={key}&location=-33.8670,151.1957&radius={radius}"\
            .format(base_url=self.base_url, format=self.data_format, key=self.key, radius=self.radius)

    def fetch(self):
        return urllib2.urlopen(self.build_url()).read()


class LocationDataPrinter:

    def __init__(self, json):
        self.data = json

    def printPlaceNames(self):
        for entry in json.loads(self.data)["results"]:
            print entry["name"]

    def printRaw(self):
        print self.data



LocationDataPrinter(LocationDataFetcher().fetch()).printPlaceNames()
