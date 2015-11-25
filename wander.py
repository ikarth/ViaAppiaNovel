import settings
import data
import random

def renderSelectDestination(wander):
    text_departing_from_name = data.getNearestName(data.hydrateLocation(wander['last_city']))
    text_travel_route_type = "upriver"
    text_destination_name = data.getNearestName(data.hydrateLocation(wander['destination']))
    text_distance = str(0.0) # km-to-miles
    story = "I departed from {0}, travelling {1} towards {2}, a {3} mile journey.".format(text_departing_from_name, text_travel_route_type, text_destination_name, text_distance)
    return {'text':story, 'metadata':[], 'state':wander}

def wanderTravel(wander):
    """
    Update the Wanderer's travelling state.
    """
    return wander

def wanderArrive(wander):
    """
    The wanderer has arrived at the travel destination.
    """
    return wander

def wanderDepart(wander):
    """
    The wanderer is leaving the current location.
    """
    return wander

def wanderSelectDestination(wander):
    """
    The wanderer needs to select the next destination.
    """
    current = data.hydrateLocation(wander['location']).orbis_id
    edges = data.findOrbisEdges(current)
    try:
        destination = random.choice(edges)
    except ValueError as err:
        print (err)
        return
    wander['destination'] = data.hydrateLocation(data.makeOrbisLocation(destination['target']))
    wander['journey'] = destination
    wander['last_city'] = data.hydrateLocation(wander['location'])
    wander['state'] = wanderTravel
    print(renderSelectDestination(wander))
    return wander

def makeWanderer():
    return {'location': data.makeOrbisLocation(50327),
            'state':wanderSelectDestination,
            'destination': data.Location(),
            'last_city': data.Location(),
            'journey':{'type':'', 'distance':'0.0', 'expense':'0.0', 'days':'0.0'}}


def processWanderer(wander:dict):
    return wander['state'](wander)