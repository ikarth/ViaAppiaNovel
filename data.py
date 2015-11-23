import settings
import requests
import json
import csv
import os

DATA_FILEPATH = "../../data/ancient"

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

orbis_sites_list = []

def getOrbisSites():
    request_sites = requests.get("http://orbis.stanford.edu/api/sites")
    global orbis_sites_list
    orbis_sites_list = request_sites.json()
    with open("orbis_sites_list.json", mode='w') as file:
        json.dump(orbis_sites_list, file, indent=3)

def checkOrbis():
    if(orbis_sites_list == []):
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

#def getPleiadesSiteList():
#    with open("../../data/ancient/pleiades/pleiades-places-20151108.csv", encoding="utf-8") as csvfile:
#        reader = csv.DictReader(csvfile)
#        global pleiades_site_list
#        for row in reader:
#            pleiades_site_list.append(row)
#    return

def checkPleiades():
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
    if(loc.pleiades_id) == -1:
        return -1
    interest = getPleiadesRecord(loc.pleiades_id)
    return interest


# Location ID Conversion
# Functions to find equivalent location ids.
# -1 indicates the data is unknown or unavailible

def getPleiadesFromOrbis(o_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if elem[1][0] == o_id), -1)
    p_id = -1
    if(orbis_record != -1):
        p_id = orbis_record[1][4]
        if(p_id == "no Pleiades ID yet"):
            p_id = -1
    return p_id

# Get the Orbis ID if we have the Pleiades ID. Note that not all ORBIS places have Pleiades IDs, and vice versa
def getOrbisFromPleiades(p_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if str(elem[1][4]) == str(p_id)), -1)
    o_id = -1
    if(orbis_record != -1):
        o_id = orbis_record[1][0]
    return o_id

def getLatLonFromOrbis(o_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if str(elem[1][0]) == str(o_id)), -1)
    latlon = -1
    if(orbis_record != -1):
        latlon = [orbis_record[1][2], orbis_record[1][3]]
    return latlon

def getLatLonFromPleiades(p_id):
    return -1

def findNearestSite(latlon):
    return -1

def latlonIsValid(latlon):
    if -1 == latlon or (not latlon):
        print("INVALID LAT/LON")
        return False
    if (0.0 == latlon[0] and 0.0 == latlon[1]):
        print("LAT/LON WAS DEFAULT")
        return False
    return True

def getSearchPelagios(lat, lon, radius = 10, search_terms = "", types = "", datasets = ""):
    if search_terms:
        search_terms = "query=" + search_terms + "&"
    if types:
        types = "types=" + types + "&"
    if datasets:
        datasets = "datasets=" + datasets + "&"
    try:
        search_query = "http://pelagios.org/peripleo/search?" + search_terms + types + datasets + "lat=" + str(lat) + "&lon=" + str(lon) + "&radius=" + str(radius)
        search_result = requests.get(search_query)
        return search_result.json()
    except Exception as err:
        raise settings.DataSourceAccessProblem("Failed to get data from Pelagios: " + str(err))

def findNearbyPelagiosCoins(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]), radius=250, datasets="dd1698f0a50440d1ac1e77fc5f303c8001db5929cc6435c30b8b29e6ba15a1e5", types="item")
    return result

def findNearbyPelagiosItem(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]))
    return result

def findNearbyPelagiosInscription(latlon):
    if not latlonIsValid(latlon): return
    result = getSearchPelagios(float(latlon[0]),float(latlon[1]),datasets="ac9dafb82ac100d90d644cd38e19a873")
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
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
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
    if -1 == start or -1 == end:
        print("Warning: Could not find lat/lon coordinates")
        return [0, 0] # one of the coordinates is invalid...
    inter = [((float(end[0]) - float(start[0])) * percent) + (float(start[0])), ((float(end[1]) - float(start[1])) * percent) + (float(start[1]))]
    return inter

def getNameFromOrbis(o_id):
    checkOrbis()
    orbis_record = next((elem for elem in orbis_sites_list if elem[1][0] == o_id), -1)
    n = "the countryside"
    if(orbis_record != -1):
        n = orbis_record[1][1]
    return n

def pickValidOrbisLocation():
    checkOrbis()
    chosen_loc = random.choice(orbis_sites_list)
    return chosen_loc

def searchOrbisRoute(start_id:str, end_id:str):
    checkOrbis()
    route = -1
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
    end_id = -1
    route = -1
    panic_escape = 0
    while route == -1:
        if panic_escape > 5:
            warnings.warn("Too many failed route searches. Failing to avoid overtaxing resources.", ResourceWarning)
            end_id = -1
            route = -1
            break
        panic_escape += 1
        end_id = pickValidOrbisLocation()[1][0]
        if end_id == start_id:
            continue
        try:
            route = searchOrbisRoute(start_id, end_id)
        except settings.DataSourceAccessProblem as err:
            print("WARNING: " + str(err))
            route = -1
        if -1 == route:
            continue
        if route:
            if route['sites']:
                print("Route OK:" + end_id)
            else:
                route = -1
        else:
            route = -1
    if route == -1:
        end_id = -1
    return end_id, route

class Location:
    def __init__(self, orbis_id=-1, pleiades_id=-1,latlon=-1):
        self.data = []
        self.orbis_id = orbis_id
        self.pleiades_id = pleiades_id
        self.latlon = latlon
    def name(self):
        return getNameFromOrbis(self.orbis_id)

def LocationToJSON(loc):
    out = json.dumps(loc)
    return out

# Based on the location data we have, find the matching ids for the other types
# Or, if we just have Lat/Lon, find the nearest site
def hydrateLocation(loc:Location) -> Location:
    if(loc.orbis_id != -1):
        loc.pleiades_id = getPleiadesFromOrbis(loc.orbis_id)
        loc.latlon = getLatLonFromOrbis(loc.orbis_id)
    else:
        if(loc.pleiades_id != -1):
            loc.orbis_id = getOrbisFromPleiades(loc.pleiades_id)
            loc.latlon = GetLatLonFromPleiades(loc.pleiades_id)
        else:
            if(loc.latlon != -1):
                loc = getNearestLocation(loc.latlon)
    return loc    

def makeOrbisLocation(o_id):
    loc = Location(orbis_id = o_id)
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

def testLocationRome():
    return makeOrbisLocation(50327)