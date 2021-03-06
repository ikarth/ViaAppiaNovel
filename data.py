﻿import settings
import requests
import json
import csv
import os
import xml
import xml.etree.ElementTree
import sqlite3
import rdflib
import re
import pickle
import uuid
from heapq import nlargest
import ftfy
from bs4 import BeautifulSoup
import bs4
import numpy
import math
import itertools

import random


DATA_FILEPATH = settings.DATA_FILEPATH

PREFIX="""
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX p: <http://research.data.gov.uk/def/project/>
PREFIX aiiso: <http://purl.org/vocab/aiiso/schema#>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX oac: <http://www.openannotation.org/ns/>
PREFIX cnt: <http://www.w3.org/2008/content#>
"""


def iter_sample_fast(iterable, samplesize):
    results = []
    iterator = iter(iterable)
    # Fill in the first samplesize elements:
    try:
        for _ in xrange(samplesize):
            results.append(iterator.next())
    except StopIteration:
        raise ValueError("Sample larger than population.")
    random.shuffle(results)  # Randomize their positions
    for i, v in enumerate(iterator, samplesize):
        r = random.randint(0, i)
        if r < samplesize:
            results[r] = v  # at a decreasing rate, replace random items
    return results

def sample_from_iterable(iterable, samplesize):
    return (x for _, x in nlargest(samplesize, ((random.random(), x) for x in iterable)))



## Data Retreval

# ORBIS returns the sites as a JSON with:
# orbis_id
# name
# latitude
# longitude
# Pleiades id (some are unknown)
# contributor
# isPort? (t/f)
# size rank, 6-10

orbis_sites_list = None

def getOrbisSites():
    global orbis_sites_list
    try:
        with open("orbis_sites_list.json", mode='r') as file:
            orbis_sites_list = json.load(file)
    except FileNotFoundError as err:
        request_sites = requests.get("http://orbis.stanford.edu/api/sites")
        orbis_sites_list = request_sites.json()
        with open("orbis_sites_list.json", mode='w') as file:
            json.dump(orbis_sites_list, file, indent=3)

def checkOrbis():
    if not orbis_sites_list:
        try:
            getOrbisSites()
        except Exception as err:
            print("Failed to access Orbis Site List")
            raise settings.DataSourceAccessProblem("Failed to get data from ORBIS: " + str(err))

# Can request specific data from ORBIS:
# /site/{site_id} - returns site page
# /sites - all sites JSON
# /sites/{site_id} - one specific site
# /route/{fromsite}/{tosite}/{month}/{priority}      use ORBIS IDs
# /route_pl/{fromsite}/{tosite}/{month}/{priority}   use Pleiades IDs
#
# {site_id} is an integer. Enter either an ORBIS or Pleiades ID.
# {fromsite}, and {tosite} are integers. 
# Use pairs of ORBIS site IDs or Pleiades place IDs as indicated above.
# {month} is an integer from 1 to 12, like 6 for June
# {priority} is either 1 or 2 (fastest or shortest, respectively)

pleiades_site_list = []

def getPleiadesSiteList():
    global pleiades_site_list
    pleiades_site_list = []
    with open(DATA_FILEPATH + os.sep + "pleiades" + os.sep + "pleiades-places-20151122.csv", mode = 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pleiades_site_list.append(row)
    return

pleiades_locations_list = []
def getPleiadesLocationsList():
    global pleiades_locations_list
    pleiades_locations_list = []
    with open(DATA_FILEPATH + os.sep + "pleiades" + os.sep + "pleiades-locations-20151122.csv", mode = 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            pleiades_locations_list.append(row)
    return

def checkPleiades():
    if not pleiades_site_list:
        getPleiadesSiteList()
    if not pleiades_locations_list:
        getPleiadesLocationsList()
    return

def getPleiadesRecord(pleiades_id):
    try:
        r = requests.get("http://pleiades.stoa.org/places/" + str(pleiades_id) + "/json2")
        return r.json()
    except (ConnectionError, requests.packages.urllib3.exceptions.NewConnectionError, requests.packages.urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError) as err:
        raise settings.DataSourceAccessProblem("Could not get data from Pleiades: " + str(err))
    except Exception as err:
        raise settings.DataSourceAccessProblem("Could not get data from Pleiades: " + str(err))

# given a location, return a Pleiades record of something interesting nearby
def getInteresting(loc):
    return

def getPleiadesData(loc):
    if not loc.pleiades_id:
        return None
    interest = getPleiadesRecord(loc.pleiades_id)
    return interest

# Location ID Conversion
# Functions to find equivalent location ids.
# None indicates the data is unknown or unavailible

def getPleiadesFromOrbis(o_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if str(elem[1][0]) == str(o_id)), None)
    p_id = None
    if orbis_record:
        p_id = orbis_record[1][4]
        if(p_id == "no Pleiades ID yet"):
            p_id = None
    return p_id

# Get the Orbis ID if we have the Pleiades ID. Note that not all ORBIS places have Pleiades IDs, and vice versa
def getOrbisFromPleiades(p_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if str(elem[1][4]) == str(p_id)), None)
    o_id = None
    if orbis_record:
        o_id = orbis_record[1][0]
    return o_id

def getLatLonFromOrbis(o_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if str(elem[1][0]) == str(o_id)), None)
    latlon = None
    if orbis_record:
        latlon = [orbis_record[1][2], orbis_record[1][3]]
    return latlon

def getLatLonFromLocalPleiades(p_id):
    checkPleiades()
    p = [i for i in pleiades_site_list if str(i['id']) == str(p_id)]
    if not p:
        p = [i for i in pleiades_locations_list if int(i['pid']) == int(p_id)]
        if not p:
            print("Record not found: " + str(p_id) + " - " + str(p))
            return getLatLonFromRemotePleiadesDisambiguate(p_id)
        return p
    return [p[0]['reprLat'] , p[0]['reprLong']]

def getLatLonFromRemotePleiadesDisambiguate(p_id):
    """
    Some Pleiades ids are obsolete and we need to figure out what they're actually supposed to point at.
    TODO: This just grabs the lat/lon from the json; it'd be nice to figure out the replacement pleiades id.
    """
    checkPleiades()
    r = None
    try:
        r = requests.get("http://pleiades.stoa.org/places/" + str(p_id) + "#this")
    except (ConnectionError, requests.packages.urllib3.exceptions.NewConnectionError, requests.packages.urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError) as err:
        raise settings.DataSourceAccessProblem("Could not get data from Pleiades: " + str(err))
    except Exception as err:
        raise settings.DataSourceAccessProblem("Could not get data from Pleiades: " + str(err))
    soup = BeautifulSoup(r.text, "html")
    try:
        updated_link = soup.find('fieldset', {'id':'relatedItemBox'}).find('a')
        if updated_link:
            r = requests.get(updated_link['href'] + "/json")
            return r.json()['reprPoint']
    except AttributeError as err:
        print(str(p_id) + " - " + str(err))
        return

def getLatLonFromRemotePleiades(p_id):
    checkPleiades()
    p = getPleiadesRecord(p_id)
    if not p:
        return None
    #print( p['reprPoint'])
    return p['reprPoint']

def getLatLonFromPleiades(p_id):
    try:
        ll = getLatLonFromLocalPleiades(p_id)
        if not ll:
            ll = getLatLonFromRemotePleiades(p_id)
        return ll
    except Exception as err:
        print("Exception: " + str(err))
        raise #return err #getLatLonFromRemotePleiades(p_id)

def findNearestSite(latlon):
    return None # TODO - find nearest site

def latlonIsValid(latlon):
    if None == latlon or (not latlon):
        print("INVALID LAT/LON")
        raise settings.InvalidLatLon
        return False
    if (0.0 == latlon[0] and 0.0 == latlon[1]):
        print("LAT/LON WAS DEFAULT")
        return False
    if (None == latlon[0]) or (None == latlon[1]):
        print("BLANK LAT/LON IS INVALID")
        return False
    return True

def cleanLatLon(latlon):
    if not latlonIsValid(latlon):
        return [0,0]
    if isinstance(latlon, str):
        if latlon != None:
            latlon = latlon.strip("[] ").split(", ")
        else:
            return [0,0]
    if isinstance(latlon, list) or isinstance(latlon, tuple):
        return [ float(latlon[0]), float(latlon[1]) ]

###########################
#
#   DARE
#
###########################
#
#Parameters		Description
#
#	Places by Bounding Box
#	----------------------
#	Returns: coordinates, id, name, country, ancient name, type and precision
#
# ?bbox=‹bbox›		bounding box, expressed as lower left corner (lon1, lat1) and upper right corner (lon2, lat2), decimal degrees. Default -15,20,70,60 (entire area). Example: area around Rome, Italy ?bbox=10.44,40.78,14.53,42.98
#
# &callback=‹callback› 	Required for JSONP
#
# &zoom=‹zoomlevel›	Zoom level. More places are displayed on the map as the zoom level increases. At zoom 10, all placetypes are rendered. At zoom 6 (default) only cities and legionary fortresses are rendered, e.g. ?zoom=6
#
# &typeid=‹typeid›	Optional Numerical placetype id: city (11), town (12), zoom is ignored, e.g. Roman villa (14), ?typeid=14. see the legend for a complete list of placetype identifiers.
#
# &layer=‹layer›	Optional Selection of places based on a collection of external identifiers, zoom is ignored, e.g. the Peutinger map, ?layer=TPPlace. Available layers are described here
#
# &cc=‹countrycode› 	Optional Modern country (ISO 3166), e.g. France ?cc=FR.
#
# &mss=‹string›	Optional UTF-8 encoded search string of modern placename, for instance, ?mss=court return all places containing the lemma court. Zoom parameter is ignored
#
# &ass=‹string›	Optional UTF-8 encoded search string of ancient placename, for instance, ?ass=briga return all places containing the Celtic lemma briga. Zoom parameter is ignored
# 	 
# 	Nearest place(s) by Point
#	-------------------------
#
#?point=‹lon,lat›	Returns one or more places around the longitude/latitude point, ordered by distance from that point.
#
# &callback=‹callback›	Required for JSONP
#
# &count=‹count›		Optional Number of places to return. Default is one.
#
# &radius=‹radius›	Optional The radius of the area to search. Default is 0.2 degrees (both latitude and longitude)
#...	Other parameters, used by the bbox method described above, can also be used by the point method, i.e. zoom, typeid, layer, etc.
# 	 
# 	Single place by identifier
#	--------------------------
#
# ?id=‹id›		    Return extended information about a place by DARE identifier, e.g. Rome ?id=1438
#
# ?pleiades=‹pleiadesid›	Alternate Single place by Pleiades identifier, id is ignored, e.g. Rome ?pleiades=423025
#
#####################################

def getSearchDARE(lat, lon, radius = 5, count = "", zoom = "10", typeid = "", layer = "", mss = "", ass = ""):
    """
    Access the API for the Digital Atlas of the Roman Empire (DARE)
    http://dare.ht.lu.se/

    Radius is in degrees
    """
    if count:
        count = "count=" + str(count) + "&"
    if zoom:
        zoom = "zoom=" + str(zoom) + "&"
    if typeid:
        typeid = "typeid=" + str(typeid) + "&"
    if layer:
        layer = "layer=" + str(layer) + "&"
    if mss:
        typeid = "mss=" + str(mss) + "&"
    if ass:
        typeid = "ass=" + str(ass) + "&"
    if radius:
        radius = "radius=" + str(radius) + ""
    try:
        search_query = "http://dare.ht.lu.se/api/geojson.php?point=" + str(lon) + "," + str(lat) + count + zoom + typeid + layer + mss + ass + radius
        search_result = requests.get(search_query)
        return search_result.json()
    except Exception as err:
        raise settings.DataSourceAccessProblem("Failed to get data from DARE: " + str(err))


def getSearchPelagios(lat, lon, radius = 10, search_terms = "", types = "", datasets = "", limit = "", offset = "", api_url = "peripleo"):
    if search_terms:
        search_terms = "query=" + search_terms + "&"
    if types:
        types = "types=" + types + "&"
    if datasets:
        datasets = "datasets=" + datasets + "&"
    if limit:
        limit = "limit=" + str(limit) + "&"
    if offset:
        offset = "offset=" + str(offset) + "&"
    if not api_url:
        api_url = "peripleo"
    try:
        search_query = "http://pelagios.org/" + api_url + "/search?" + search_terms + types + datasets + limit + offset + "lat=" + str(lat) + "&lon=" + str(lon) + "&radius=" + str(radius)
        search_result = requests.get(search_query)
        return search_result.json()
    except Exception as err:
        raise settings.DataSourceAccessProblem("Failed to get data from Pelagios: " + str(err))

#http://pelagios.dme.ait.ac.at/api/datasets/cf3baed0f33f28c02dbed50a96b663af/annotations

def findNearbyPelagiosCoins(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]), radius=250, datasets="dd1698f0a50440d1ac1e77fc5f303c8001db5929cc6435c30b8b29e6ba15a1e5", types="item")
    return result

def findNearbyPelagiosThing(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]))
    return result

def findNearbyPelagiosItem(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]), radius = 40, types = "item")
    return result

def findNearbyPelagiosPlace(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]), limit = 40, types = "place")
    return result

def findNearbyPelagiosInscription(latlon):
    if not latlonIsValid(latlon): return
    #result = getSearchPelagios(float(latlon[0]),float(latlon[1]),datasets="ac9dafb82ac100d90d644cd38e19a873")
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]),datasets="21b2d56d90bd192834aea9d8ad9d61b21a94d85f15f7cab1c458d4eebf599b73", radius=100, limit=200)
    return result

def extractPossibleField(dataset, field):
    if not dataset:
        return
    value = None
    try:
        value = dataset[field]
    except KeyError:
        value = None
    return value


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

# Intermediate point on a great circle (lat/lon)
# Formula:	a = sin((1?f)??) / sin ?
# b = sin(f??) / sin ?
# x = a ? cos ?1 ? cos ?1 + b ? cos ?2 ? cos ?2
# y = a ? cos ?1 ? sin ?1 + b ? cos ?2 ? sin ?2
# z = a ? sin ?1 + b ? sin ?2
# ?i = atan2(z, ?x� + y�)
# ?i = atan2(y, x)
# where	f is fraction along great circle route (f=0 is point 1, f=1 is point 2), ? is the angular distance d/R between the two points.

# given a starting point, an ending point, and a percentage, return the latlon of the waypoint
# very naive currently, assumes planar geometry.
# if you want better results, implement the above formula.
def findIntermediatePointLatLon(start, end, percent):
    if None == start or None == end:
        print("Warning: Could not find lat/lon coordinates")
        return [0, 0] # one of the coordinates is invalid...
    inter = [((float(end[0]) - float(start[0])) * percent) + (float(start[0])), ((float(end[1]) - float(start[1])) * percent) + (float(start[1]))]
    return inter


def getNameFromOrbis(o_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if str(elem[1][0]) == str(o_id)), None)
    n = "the countryside"
    if orbis_record:
        n = str(orbis_record[1][1])
    return n

def getNameFromPleiades(p_id):
    p_record = getPleiadesRecord(p_id)
    return p_id['title']

def pickValidOrbisLocation():
    checkOrbis()
    chosen_loc = settings.TEXT_RNG.choice(orbis_sites_list)
    return chosen_loc

def searchOrbisRoute(start_id:str, end_id:str):
    checkOrbis()
    route = None
    try:
        request_route = requests.get("http://orbis.stanford.edu/api/route/" + start_id + "/" + end_id + "/6/1")
        if request_route:
            #print(request_route)
            if request_route.json():
                route = request_route.json()
            return route
        else:
            return None
    except Exception as err:
        print("No valid route found: " + start_id + " to " + end_id + " because: " + str(err))
        raise settings.DataSourceAccessProblem("Could not get valid route from ORBIS: " + str(err))

def pickValidOrbisRoute(start_id):
    checkOrbis()
    end_id = None
    route = None
    panic_escape = 0
    while not route:
        if panic_escape > 5:
            warnings.warn("Too many failed route searches. Failing to avoid overtaxing resources.", ResourceWarning)
            end_id = None
            route = None
            break
        panic_escape += 1
        end_id = pickValidOrbisLocation()[1][0]
        if end_id == start_id:
            continue
        try:
            route = searchOrbisRoute(start_id, end_id)
        except settings.DataSourceAccessProblem as err:
            print("WARNING: " + str(err))
            route = None
        if None == route:
            continue
        if route:
            if route['sites']:
                print("Route OK:" + end_id)
            else:
                route = None
        else:
            route = None
    if route == None:
        end_id = None
    return end_id, route

def getNearbyPerseusName(latlon):
    latlon = cleanLatLon(latlon)
    quotes, places = findNearbyPerseusFromLatLon(latlon, radius = 20.0)
    n = ""
    try:
        choice = settings.TEXT_RNG.choice(list(places.keys()), p = list(places.values()))
        loc = makePleiadesLocation(choice)
        n = getNameFromPleiades(loc)
        if n:
            n = " near " + str(n)
    except ValueError as err:
        print("getNearbyPerseusName Exception: " + str(err))
    return n

def getNearbyPleiadesName(p_id):
    latlon = getLatLonFromPleiades(p_id)
    quotes, places = findNearbyPerseusFromLatLon(latlon, radius = 20.0) # todo: extend this to all pleiades records

    try:
        choice = settings.TEXT_RNG.choice(list(places.keys()), p = list(places.values()))
        loc = makePleiadesLocation(choice)
        n = getNameFromPleiades(loc)
        if n:
            n = " near " + str(n)
        return n
    except ValueError as err:
        print("getNearbyPleiadesName Exception: " + str(err))
        return " near that place"


class Location:
    def __init__(self, orbis_id=None, pleiades_id=None,latlon=None):
        self.data = []
        self.orbis_id = orbis_id
        self.pleiades_id = pleiades_id
        self.latlon = latlon
    def name(self):
        try:
            n = getNameFromOrbis(self.orbis_id)
            if "the countryside" == str(n):
                #print("---")
                #print(self.orbis_id)
                #print(self.pleiades_id)
                #print(self.latlon)
                if self.pleiades_id:
                    n = n + getNearbyPleiadesName(self.pleiades_id)
                elif self.latlon:
                    n = n + getNearbyPerseusName(self.latlon)
                elif self.orbis_id:
                    n = n + getNearbyPerseusName(getLatLonFromOrbis(self.orbis_id))
        except settings.InvalidLatLon as err:
            n = "a village"
        return n
    def id(self):
        return getLocationId(self)

def getLocationId(loc:Location) -> str:
    if loc.orbis_id:
        return "orb:" + str(loc.orbis_id)
    if loc.pleiades_id:
        return "ple:" + str(loc.pleiades_id)
    if loc.latlon:
        return "lat:" + str(loc.latlon)
    return ""

def LocationToJSON(loc):
    out = json.dumps(loc)
    return out

def getNearestName(loc:Location):
    # TODO: try to get names from other sources as well...
    #print(loc.orbis_id)
    n = loc.name()
    return n

def getNameFromLoc(loc:Location):
    n = None
    n = getNameFromOrbis(loc.orbis_id)
    if not n or "the countryside" == n:
        n = getNameFromPleiades(loc.pleiades_id)
    # TODO: get name from latlon
    return n

def locationFromId(id:str) -> Location:
    ident = id.split(":")
    routingTable = {'orb':makeOrbisLocation, 'ple':makePleiadesLocation, 'lat':makeLatLonLocation}
    return routingTable[ident[0]](ident[1])

# Based on the location data we have, find the matching ids for the other types
# Or, if we just have Lat/Lon, find the nearest site
def hydrateLocation(loc:Location) -> Location:
    if loc.orbis_id:
        loc.pleiades_id = getPleiadesFromOrbis(loc.orbis_id)
        loc.latlon = getLatLonFromOrbis(loc.orbis_id)
    else:
        if loc.pleiades_id:
            loc.orbis_id = getOrbisFromPleiades(loc.pleiades_id)
            loc.latlon = getLatLonFromPleiades(loc.pleiades_id)
        else:
            if loc.latlon:
                loc = getNearestLocation(loc.latlon)
    return loc    

def makeOrbisLocation(o_id):
    if isinstance(o_id, str):
        o_id = int(o_id)
    loc = Location(orbis_id = o_id)
    hydrateLocation(loc)
    return loc

def makeLatLonLocation(latlon):
    if isinstance(latlon, str):
        latlonarray = latlon.strip('[] ').split(', ')
        latlon = [ float(latlonarray[0]), float(latlonarray[1]) ]
    loc = Location(latlon = latlon)
    hydrateLocation(loc)
    return loc

def makePleiadesLocation(pleia):
    if isinstance(pleia, str):
        pleia = int(pleia)
    loc = Location(pleiades_id = pleia)
    hydrateLocation(loc)
    return loc

orbis_connections = []
orbis_nodes = []
def loadOrbisConnections():
    global orbis_connections
    global orbis_nodes
    with open(DATA_FILEPATH + os.sep + "orbis" + os.sep + "orbis_edges_0514.csv", mode='r') as file:
        csv_reader = csv.reader(file)
        orbis_connections = [{'source':rows[0], 'target':rows[1], 'distance':rows[2],'days':rows[3],'expense':rows[4],'type':rows[5]} for rows in csv_reader]
    with open(DATA_FILEPATH + os.sep + "orbis" + os.sep + "orbis_nodes_0514.csv", mode='r') as file:
        csv_reader = csv.reader(file)
        orbis_nodes = [{'id':rows[0], 'label':rows[1], 'x':rows[2],'y':rows[3]} for rows in csv_reader]

def checkOrbisConnections():
    if (not orbis_connections) and (not orbis_nodes):
        loadOrbisConnections()

def findOrbisEdges(orbis_id) -> list:
    """
    Given an orbis location ID, return a list of the edges on the
    Orbis graph.
    """
    checkOrbisConnections()
    edges = [x for x in orbis_connections if str(x['source']) == str(orbis_id)]
    return edges

def testLocationRome():
    getOrbisSites()
    return makeOrbisLocation(50327)


already_used_inscriptions = set()
def translateInscription(input):
    """
    Take the raw data and extract the bits that we can use to generate text.
    """
    global already_used_inscriptions
    poss_list = set([i['homepage'] for i in input['items']])
    possible_inscriptions = poss_list
    possible_inscriptions = possible_inscriptions.difference(already_used_inscriptions)
    if len(possible_inscriptions) == 0:
        return "SPQR"
    # TODO: weight inscriptions by distance...
    inscription_data_id = settings.TEXT_RNG.choice(list(possible_inscriptions))
    already_used_inscriptions.add(inscription_data_id)
    inscription_data = [j for j in input['items'] if str(j['homepage']) == str(inscription_data_id)][0]
    if not inscription_data:
        return "Lucius Pinxit"
    heidelberg_data_url = inscription_data['homepage'] + ".xml"
    heidelberg_data = requests.get(heidelberg_data_url)
    #eltree = xml.etree.ElementTree.ElementTree(xml.etree.ElementTree.fromstring(heidelberg_data.text))
    #root = eltree.getroot().find(".")
    #print(root.findall(".//{http://www.tei-c.org/ns/1.0}ab"))
    find_inscription = heidelberg_data.text.split("<!--")[1].split("-->")[0].strip()
    return find_inscription
    #return {'data_url': input['items'][0]['homepage'] + ".xml",
    #        'transcription': find_inscription,
    #        'eltree': eltree}

def getInscription(latlon):
    latlon = cleanLatLon(latlon)
    return translateInscription(findNearbyPelagiosInscription(latlon))

def testXML():
    eltree = xml.etree.ElementTree.parse("HD006837.xml")
    root = eltree.getroot()
    for child in root:
        print(child.tag, child.attrib)
    print(root.findall(".//{http://www.tei-c.org/ns/1.0}ab")[0])
    return root


def openRDF(rdf_name) -> rdflib.Graph:
    g = rdflib.Graph()
    if not isinstance(rdf_name, str):
        rdf_name = str(rdf_name)
    filepath = DATA_FILEPATH + os.sep + str(rdf_name)
    if not os.path.isfile(filepath):
        print("Warning: " + str(filepath) + " does not exist")
        return
    #g.load(filepath)
    with open(filepath, mode="rt") as file:
        g.parse(file, format='application/rdf+xml')
    return g

# http://www.perseus.tufts.edu/hopper/CTS?request=GetCapabilities
# http://www.perseus.tufts.edu/hopper/CTS?request=GetValidReff&urn=urn:cts:latinLit:phi0914
#
# urn:cts:latinLit:phi0914
#
# Anatomy of the URN format used by Perseus
#    urn:cts:latinLit:phi0914.phi0011.perseus-lat1:4.2
#    {1}:{2}:   {3}  :   {4} . {5}   .  {6}       :{7}
#
# {1} It’s a urn. This part is fixed.
# {2} The urn is part of the ‘cts’ namespace. This part is fixed.
# {3} The Latin Literature namespace. Would be ‘greekLit’ for Greek texts, 
#     and possibly other values.
# {4} The textgroup’s identifier. It’s normally either the TLG or PHI 
#     author index value. In the catalogue it’s contained in the ‘projid’ 
#     attribute of the ‘textgroup’ element, stripped of the namespace.
# {5} The work’s identifier. This may map to an author’s title or to an 
#     individual book in a larger collection of texts. This also apparently
#     comes from either TLG or PHI indices (I’ve not verified this fact 
#     for sure). In the catalogue it’s contained in the ‘projid’ attribute 
#     of the ‘work’ element, stripped of the namespace.
# {6} The edition of the work. This may also be a translation. This is a 
#     Perseus-specific value. In the catalogue it’s contained in the 
#     ‘projid’ attribute of the ‘edition’ or ‘translation’ element, 
#     stripped of the namespace.
# {7} The text reference. This will be specific to the work and edition 
#     you are referencing. You can find out a simple unadorned list of 
#     what’s available by querying the reference validation service with 
#     the URN up to this point at the argument.
# http://inlustre.net/2013/04/how-to-retrieve-ancient-text-data-from-perseus/

def testPerseusText():
    #eltree = xml.etree.ElementTree.ElementTree()
    #parser = xml.etree.ElementTree.XMLParser()
    #parser.parser.UseForeignDTD(True)
    #with open(DATA_FILEPATH + "\\perseus\\Classics\\Caesar\\opensource\\caes.bg_eng.xml", mode='rt') as file:
    #    eltree = xml.etree.ElementTree.parse(file, parser=parser)
    #root = eltree.getroot()
    #return eltree
    xmldoc = xml.dom.minidom.parse(DATA_FILEPATH + "\\perseus\\Classics\\Caesar\\opensource\\caes.bg_eng.xml")
    #print(xmldoc.childNodes[1].childNodes[3].childNodes[1].toxml())
    paralist = xmldoc.getElementsByTagName('p')
    
    for n in paralist:
        print(n)
    #namelist = xmldoc.getElementsByTagName('name')
    #for n in namelist:
    #    print(n.toxml())
    return xmldoc

perseus_cts = None
def loadPerseusCTS():
    try:
        if not perseus_cts:
            with open("data" + os.sep + "perseus_cts.pickle", mode='rb') as file:
                perseus_cts = pickle.load(file)
        return perseus_cts
    except FileNotFoundError as err:
        print("data" + os.sep + "perseus_cts.pickle not found")
        input_string = ""
        with open(DATA_FILEPATH + os.sep + "perseus" + os.sep + "CTS.xml", mode='rt') as file:
            input_string = file.read()
        soup = BeautifulSoup(input_string, 'xml')
        perseus_cts = soup
        if settings.PICKLE_PERSEUS_CTS:
            with open("data" + os.sep + "perseus_cts.pickle", mode='wb') as file:
                pickle.dump(perseus_cts, file)
        return soup

def testPerseusTextTwo():
    input_string = ""
    with open(DATA_FILEPATH + "\\perseus\\Classics\\Caesar\\opensource\\caes.bg_eng.xml", mode='r') as file:
        input_string = file.read()
    soup = BeautifulSoup(input_string, 'xml')
    #print(soup.prettify())
    return soup

perseus_pleiades_index = None
def perseusPleiadesMetadata():
    global perseus_pleiades_index
    if not perseus_pleiades_index:
        try:
            print("Accessing pickle...")
            with open("data" + os.sep + "perseus_pleiades_index.pickle", mode='rb') as file:
                perseus_pleiades_index = pickle.load(file)
        except FileNotFoundError as err:
            print("Using RDF")
            perseus_pleiades_index = openRDF("perseus" + os.sep + "Perseus-collection-Greco-Roman.pleiades.rdf")
        if settings.PICKLE_PERSEUS_PLEIADES_INDEX:
            with open("data" + os.sep + "perseus_pleiades_index.pickle", mode='wb') as file:
                pickle.dump(perseus_pleiades_index, file)
    return perseus_pleiades_index

def findPleiadesInPerseus(pleiades_number):
    r = perseusPleiadesMetadata()
    place_ref = "http://pleiades.stoa.org/places/{}#this".format(str(pleiades_number))
    #t = r.triples( (None,
    #                rdflib.term.URIRef('http://www.openannotation.org/ns/hasBody'),
    #                rdflib.term.URIRef(place_ref)))
    #tl = list(r.query(PREFIX+"SELECT ?x WHERE { ?x rdf:resource } LIMIT 50"))
    return list(r.query(PREFIX + """ SELECT ?yo WHERE {?s oac:hasBody <""" + """http://pleiades.stoa.org/places/""" + str(pleiades_number) + """#this""" + """>; oac:hasTarget ?yo} LIMIT 15"""))
    
def getAllPleiadesInPerseus():
    r = perseusPleiadesMetadata()
    pleiades_in_perseus_list = list(r.query(PREFIX + """ SELECT ?xo WHERE {?s oac:hasBody ?xo; oac:hasTarget ?yo}"""))
    pleiades_in_perseus_list = [i[0].toPython().split("/places/")[1].strip("#this ") for i in pleiades_in_perseus_list]
    #print(pleiades_in_perseus_list)
    return pleiades_in_perseus_list


def distanceToLatLon(one, two):
    """
    Returns the distance between two lat/lon coordinates.
    Takes two [lat, lon] arrays as input.
    Return value is in km.
    """
    if one and two:
        try:
            #print(one)
            #print(two)
            return haversine(float(one[0]), float(one[1]), float(two[0]), float(two[1]))
        except IndexError as err:
            print(err)
            return None

def distanceBetweenPleiadesAndLatLon(p_id, latlon):
    return distanceToLatLon(latlon, getLatLonFromLocalPleiades(p_id))

all_pleiades_in_perseus_list = []
pleiades_latlon_list = {}

def getPleiadesPerseusLatLonList():
    global pleiades_in_perseus_list
    global pleiades_latlon_list
    if not pleiades_latlon_list:
        try:
            with open("data" + os.sep + "pleiades_latlon_list.pickle", "rb") as file:
                pleiades_latlon_list = pickle.load(file)
        except Exception as err:
            print("getPleiadesPerseusLatLonList Exception: " + str(err))
            if not all_pleiades_in_perseus_list:
                pleiades_in_perseus_list = getAllPleiadesInPerseus()
            [pleiades_latlon_list.update({str(i):getLatLonFromLocalPleiades(i)}) for i in set(pleiades_in_perseus_list)]
    #pleiades_list = []
    #pleiades_list = [print(str(i) + " " + str(getLatLonFromPleiades(i))) for i in pleiades_in_perseus_list]
    #pleiades_list = [{'id':i, 'latlon':getLatLonFromLocalPleiades(i), 'distance':distanceBetweenPleiadesAndLatLon(i, latlon)} for i in pleiades_in_perseus_list]
    if pleiades_latlon_list:
        if settings.PICKLE_PERSEUS_LATLON_LIST:
            with open("data" + os.sep + "pleiades_latlon_list.pickle", "wb") as file:
                pickle.dump(pleiades_latlon_list, file)
    return pleiades_latlon_list

def getDistancesToPerseus(latlon, cutoff_radius = 0.0):
    latlon = cleanLatLon(latlon)
    getPleiadesPerseusLatLonList()
    #distance_list = [i.update({'distance':distanceToLatLon(i['latlon'], latlon)}) for i in pleiades_latlon_list]
    list_with_distances = {k:{'latlon':v, 'distance':distanceToLatLon(v, latlon)} for k,v in pleiades_latlon_list.items()}
    distances = {k:distanceToLatLon(v, latlon) for k,v in pleiades_latlon_list.items() if v}
    if cutoff_radius > 0.0:
        distances = dict((k, v) for k,v in distances.items() if (float(v) < cutoff_radius))
    return distances

def getProbabilitiesFromCounts(distances:dict):
    """
    Takes a dict of ids and their frequency.
    Returns a dict with frequency replaced by
    a scaled (inverse square law) probabilty
    that choice will be chosen, normalized
    to sum to 1.0.
    """
    try:
        prob_max = max(max(list(distances.values())), 0) + 1
        probabilities = numpy.array([max(0, (prob_max ** 2) - (i ** 2)) for i in distances.values()])
        total_prob = probabilities.sum()
        #print(probabilities)
        #print(total_prob)
        if total_prob == 0:
            print ("Error: No probabilities listed.")
            return
        probabilities /= total_prob
        #print(probabilities)
        #print(probabilities.sum())
        return dict(zip(distances.keys(), probabilities))
    except ValueError as err:
        print("getProbabilitiesFromCounts Exception: " + str(err))
        return
        


def findNearbyPerseusFromLatLon(latlon, radius = 200.0):
    """
    Returns list of perseus quotes weighted by inv sq distance,
    suitable for use by numpy.random.choice()
    """
    latlon = cleanLatLon(latlon)
    if [0,0] == latlon:
        print("Warning: default Lat/Lon")
    distances = getDistancesToPerseus(latlon, radius)
    local_perseus = {}
    map_quotes_to_pleiades = {}
    for i in distances.items():
        t = findPleiadesInPerseus(i[0])
        if len(t) == 0: continue
        #[print(j[0].toPython()) for j in t]
        #local_perseus.update( dict([str(j[0].toPython())]:i[0] for j in t))
        local_perseus.update(dict(zip([j[0].toPython() for j in t if not (str(j[0].toPython()) in previously_used_perseus_extracts)], itertools.repeat(i[1]))))
        map_quotes_to_pleiades.update(dict(zip([j[0].toPython() for j in t if not (str(j[0].toPython()) in previously_used_perseus_extracts)], itertools.repeat(i[0]))))

    probs = getProbabilitiesFromCounts(local_perseus)
    if not probs:
        if radius < 3000.0:
            probs, map_quotes_to_pleiades = findNearbyPerseusFromLatLon(latlon, (radius * 2) + 1.0)
        else:
            raise ValueError("No Perseus records within {} km of {} latlon".format(str(radius), str(latlon)))
    return probs, map_quotes_to_pleiades


# list(r.query(data.PREFIX + """SELECT ?o WHERE {?s oac:hasBody ?o} LIMIT 15"""))
# list(r.query(data.PREFIX + """SELECT ?yo WHERE {?s oac:hasBody ?o. ?ys oac:hasTarget ?yo} LIMIT 15"""))
# list(r.query(data.PREFIX + """SELECT ?yo WHERE {?s oac:hasBody <http://pleiades.stoa.org/places/432839#this>; oac:hasTarget ?yo} LIMIT 15"""))

def stripTags(soup, valid_tags):
    for tag in soup.find_all(True):
        if not (tag.name in valid_tags):
            s = ""
            for c in tag.contents:
                if not isinstance(c, bs4.NavigableString):
                    c = stripTags(c, valid_tags)
                s += str(c)
            tag.replace_with(s)
    return soup

def processPerseusText(soup:BeautifulSoup):

    fragments = ""
    if 0 == len(soup.find_all('p')):
        if 0 == len(soup.find_all('l')):
            print(soup)
            print("WARNING: Couldn't find p or l in this text...")
            pass
        else:
            content = "<p>"
            for section in soup.find_all('l'):
                milestone = True
                while milestone:
                    if not section.find('milestone'):
                        milestone = False
                        break
                    milestone = section.find('milestone', {'unit':'para'})
                    if milestone:
                        section.find('milestone', {'unit':'para'}).replace_with(str("<br/>"))
                    else:
                        milestone = section.find('milestone').extract()
                note = True
                while note:
                    if not section.find('note'):
                        note = False
                        break
                    note_text = section.find('note').text
                    section.find('note').replace_with(str("^[" + note_text + "]"))
                content += " ".join(section.text.split()).strip().replace("\n", " ")
                content += "<br/>"
            content = content.replace(" ^[", "^[").replace("\n", " ")
            content += "</p>"
            fragments += content

    else:
        for section in soup.find_all('p'):
            div2 = True
            while div2:
                if not section.find('div2', {'type':'commline'}):
                    div2 = False
                    break
                tag = section.find('div2', {'type':'commline'})
                sec_mark = soup.new_tag("span")
                sec_mark.string = str(tag['n']) + ". "
                section.find('div2', {'type':'commline'}).find('p').insert(0, sec_mark)
                section.find('div2', {'type':'commline'}).unwrap()            
            milestone = True
            while milestone:
                if not section.find('milestone'):
                    milestone = False
                    break
                #note_text = section.find('milestone').text
                #section.find('milestone').replace_with(str("[" + note_text + "]"))
                milestone = section.find('milestone').extract()
            lang_la = True
            while lang_la:
                if not section.find('foreign', {'lang':'la'}):
                    lang_la = False
                    break
                note_text = section.find('foreign', {'lang':'la'}).text
                section.find('foreign', {'lang':'la'}).replace_with(str("_" + note_text + "_"))
            lang_gr = True
            while lang_gr:
                if not section.find('foreign', {'lang':'greek'}):
                    lang_gr = False
                    break
                note_text = section.find('foreign', {'lang':'greek'}).text
                section.find('foreign', {'lang':'greek'}).replace_with(str("\\rendergreek{" + note_text + "}"))
            note = True
            while note:
                if section.find('note',{'place':'marg'}):
                    section.find('note',{'place':'marg'}).extract()
                    continue
                if not section.find('note'):
                    note = False
                    break
                note_text = section.find('note').text
                section.find('note').replace_with(str("^[" + note_text + "]"))
            qt = True
            while qt:
                if not section.find('q'):
                    qt = False
                    break
                note_text = section.find('q').text
                section.find('q').replace_with(str("\"" + note_text + "\""))
            #cit = True
            #while cit:
            #    if not section.find('cit'):
            #        cit = False
            #        break
            #    note_text = section.find('cit').text
            #    section.find('cit').replace_with(str("^[" + note_text + "]"))
            #bibl = True
            #while bibl:
            #    if not section.find('bibl'):
            #        bibl = False
            #        break
            #    note_text = section.find('bibl').text
            #    section.find('bibl').replace_with(str("^[" + note_text + "]"))

            content = "<p>"
            content += " ".join(section.text.split()).strip()
            content += "</p>"
            content = content.replace(" ^[", "^[") # clean up space in front of inline cite
            fragments += content

    output_string = ""
    output_string = fragments
    return output_string

def getPerseusCatalogData(doc_url, no_urn = False):
    catalog_metadata = {'author':'Unknown','book_title':'Unknown','description':'Perseus Digital Library'}
    catalog_status_code = None
    if not no_urn:
        #print(doc_url)
        urn = doc_url.split("urn:")[1] # Perseus URN identifier
        #print(urn)
        urn = urn.rsplit(":", 1)[0]
        book_urn = "urn:" + urn.rsplit(".", 1)[0]
        author_urn = "urn:" + urn.rsplit(".", 2)[0]
        catalog_urn_url = "http://data.perseus.org/catalog/urn:" + str(urn) + "/atom"
        #print(catalog_urn_url)
        catalog_data = requests.get(catalog_urn_url, "xml")
        catalog_status_code = catalog_data.status_code
    if (not no_urn) and catalog_status_code == 200:
        catalog_metadata['urn'] = catalog_urn_url
        soup_metadata_atom = BeautifulSoup(catalog_data.text, "xml")
        md = soup_metadata_atom.find("textgroup", {'urn':author_urn})
        catalog_metadata['author'] = md.find("groupname").text.strip()
        if catalog_metadata['author'].endswith("."):
            catalog_metadata['author'] = catalog_metadata['author'][:-1]
        catalog_metadata['book_title'] = md.find("title").text.strip()
        catalog_metadata['label'] = md.find("label").text
        catalog_metadata['description'] = md.find("description").text
    else: # record not found...try to at least grab the author...
        book_page_data = requests.get(doc_url, "xml")
        soup_metadata_page = BeautifulSoup(book_page_data.text, "html")
        page_title = soup_metadata_page.find('h1')
        catalog_metadata['author'] = page_title.text.split(",")[0].strip()
        book_title = page_title.find(class_='title')
        catalog_metadata['book_title'] = book_title.text
    catalog_metadata['author_raw'] = catalog_metadata['author']
    if catalog_metadata['author'].count(",") > 0:
        flip_name = catalog_metadata['author'].strip(".").split(", ", 1)
        if flip_name[1].isalpha():
            catalog_metadata['author_reordered'] = flip_name[1] + " " + flip_name[0]
            catalog_metadata['author'] = catalog_metadata['author_reordered']
    #print(catalog_metadata)

    return catalog_metadata

previously_used_perseus_extracts = []

def renderPerseus(choice, pleiades_number, is_retry = False):
    base_choice = choice.split(", ")[0].strip()
    previously_used_perseus_extracts.append(str(choice))
    #print(previously_used_perseus_extracts)
    #print("---")

    xml_url = None #str(base_choice).replace("text", "xmlchunk", 1)

    textmetadata = {}
    if "xmlchunk" in base_choice:
        html_url = base_choice.replace("xmlchunk", "text")
        textmetadata = getPerseusCatalogData(html_url, no_urn = True)
        xml_url = base_choice
    else:
        textmetadata = getPerseusCatalogData(base_choice)
    

    output_string = ""
    sresult = None
    soup = None
        
    if not xml_url:
        try:
            rqst = requests.get(base_choice)
            soup = BeautifulSoup(rqst.text, "xml")
            #def class_is_text_container(x):
            #    return re.compile("text_container").search(x)
            sresult = soup.find(class_=re.compile("text_container"))

            link = soup.find_all("a", class_="xml")
            for i in link:
                if i.has_attr('href'):
                    if "xmlchu" == str(i['href'])[0:6]:
                        xml_url = "http://www.perseus.tufts.edu/hopper/" + i['href']
        except requests.exceptions.ConnectionError as err:
            print("renderPerseus Exception: " + str(err))
            print(base_choice)
            if not is_retry:
                return renderPerseus(choice, pleiades_number, True)
            raise


    #print(link)
    #print(xml_url)
    if(xml_url):
        xml_rqst = requests.get(xml_url)
        xml_soup = BeautifulSoup(xml_rqst.text, "xml")
        output_string = processPerseusText(xml_soup)
    else:
        if sresult:
            for tex in sresult:
                output_string += " ".join(tex.text.split()).strip()
                print(tex.text)

    cite_name = str(uuid.uuid4()).replace("-", "")
    output_string = output_string[:-4] + "[^{cite_name}]</p>".format(cite_name=cite_name)
    output_string = ftfy.fix_text(output_string)
    
    cite = ""
    if (not soup) and textmetadata:
        cite = ftfy.fix_text("[^{citation_name}]: From the Perseus Digital Library: ".format(citation_name=cite_name) + textmetadata['description'] + " \\url{" + base_choice + "} \n\r")
    if soup:
        find_cite_first_p = "Perseus Digital Library"
        if soup.find("div", id="text_footer"):
            if soup.find("div", id="text_footer").find(id="text_desc"):
                find_cite = re.sub('[\t+]', ' ', (soup.find("div", id="text_footer").find(id="text_desc").text))
                find_cite_first_p = find_cite.splitlines()[1]
        cite = ftfy.fix_text("[^{citation_name}]: From the Perseus Digital Library: ".format(citation_name=cite_name) + find_cite_first_p + " \\url{" + base_choice + "} \n\r")
    if settings.DISPLAY_CITES_WHILE_RENDERING:
        print({'cite': cite, 'uuid': cite_name, 'author':textmetadata['author'],'book_title':textmetadata['book_title'], 'metadata':textmetadata, 'place':pleiades_number })
    return {'text':output_string, 'cite': cite, 'uuid': cite_name, 'author':textmetadata['author'],'book_title':textmetadata['book_title'], 'metadata':textmetadata, 'place':makePleiadesLocation(pleiades_number) }

def renderPerseusFromLatLon(latlon, range = 200.0, retry = False):
    quotes, pleiades_mapping = findNearbyPerseusFromLatLon(latlon, range)
    if len(quotes) == 0:
        print ("Warning: no quotations found")
        return
    choice = settings.TEXT_RNG.choice(list(quotes.keys()), p = list(quotes.values()))
    r = None
    try:
        r = renderPerseus(choice, pleiades_mapping[choice])
    except requests.exceptions.ConnectionError as err:
        print("renderPerseusFromLatLon Exception: " + str(err))
        if not retry:
            r = renderPerseusFromLatLon(latlon, range, retry=True)
    return r

def renderPerseusFromPleiades(pleiades_number):
    t = findPleiadesInPerseus(pleiades_number)
    if len(t) == 0:
        print ("Warning: no quotations found")
        return
    
    t_restricted = [i for i in t if not (str(i[0].toPython()) in previously_used_perseus_extracts)]
    if len(t_restricted) > 0:
        t = t_restricted
    else:
        print ("Warning: all quotations have already been used")
        return # todo: grab a story from a nearby location instead
    #print(t)
    #print(t[0])
    #print(t[0][0])
    #print(t[0][0].toPython())
    #print(len(t))

    choice = None
    try:
        choice = settings.TEXT_RNG.choice(t)[0].toPython()
    except ValueError:
        tc = [i[0] for i in t]
        choice = settings.TEXT_RNG.choice(tc)


    return renderPerseus(choice, pleiades_number)
    

#    triple_list = list()
#    t = findPleiadesInPerseus(pleiades_number)
#    for s, p, o in t:
#        triple_list.append([s,p,o])
#    return t