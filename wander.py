import settings
import data
import random

def renderSelectDestination(wander:dict) -> dict:
    text_departing_from_name = data.getNearestName(data.hydrateLocation(wander['last_city']))
    text_travel_route_type = "upriver"
    text_destination_name = data.getNearestName(data.hydrateLocation(wander['destination']))
    text_distance = str(0.0) # km-to-miles
    story = "Virgil departed from {0}, travelling {1} towards {2}, a {3} mile journey.".format(text_departing_from_name, text_travel_route_type, text_destination_name, text_distance)
    return {'type': 'travel-narration', 'text':story, 'metadata':[], 'state':wander}

def renderTravelQuotation(wander:dict):
    """
    Given a travelling wanderer, come up with a quotatation from a place
    near the current location (on the travel path).
    """
    pass

def renderPlaceQuotation(wander:dict) -> dict:
    """
    Return a quotation related to the current location.
    """
    talking_about = data.hydrateLocation(wander['location']).pleiades_id
    if not talking_about:
        print("Error: place quote not found")
    #    return {'type':'quotation', 'state':wander}.update(data.renderPerseusFromPleiades(talking_about))
    output_text = data.renderPerseusFromPleiades(talking_about)
    #print(output_text)
    render_base = {'type':'quotation', 'state':wander}
    render_base.update(output_text)
    return render_base
    

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
            'current_time': 0.0,
            'destination': data.Location(),
            'last_city': data.Location(),
            'journey':{'type':'', 'distance':'0.0', 'expense':'0.0', 'days':'0.0'}}


def processWanderer(wander:dict):
    return wander['state'](wander)