import settings
import data
import random
import time

DELAY_FOR_BANDWIDTH = False #if true, sleeps a bit between tasks that might call for network resources

wanderer_story = []

def writeStory(story_data:dict):
    global wanderer_story
    wanderer_story.append(story_data)

def getStory():
    return wanderer_story

def descriptionJourneyType(type):
    type_description = type
    type_description_subs= {"fastdown":"on a military boat downstream",
                            "fastup":"on a military boat headed upstream",
                            "upstream":"on a boat heading upstream",
                            "downstream":"on a boat heading downstream",
                            "road":"by road",
                            "coastal":"by ship, down the coast",
                            "overseas":"by ship, crossing the sea",
                            "slowcoast":"on a local coastal ship, travelling only by day"
                            }
    type_description = type_description_subs[type]
    return type_description


def renderSelectDestination(wander:dict):
    text_departing_from_name = data.getNearestName(data.hydrateLocation(wander['last_city']))
    text_travel_route_type = descriptionJourneyType(wander['journey']['type'])
    text_destination_name = data.getNearestName(data.hydrateLocation(wander['destination']))
    text_distance = str(float(wander['journey']['distance']) * settings.KILOMETERS_TO_MILES) # km-to-miles
    story = "Virgil departed from {0}, intending to travel {1} to {2}, a {3} mile journey.\n\n".format(text_departing_from_name, text_travel_route_type, text_destination_name, text_distance)
    writeStory({'type': 'travel-narration', 'text':story, 'metadata':[], 'state':wander})

def renderTravelQuotation(wander:dict):
    """
    Given a travelling wanderer, come up with a quotatation from a place
    near the current location (on the travel path).
    """
    pass

def renderNearbyPlaceQuotation(wander:dict, loc:data.Location):
    """
    Given a latlon location, find a nearby place and 
    write a quote based on it.
    """
    pass

def renderPlaceQuotation(wander:dict):
    """
    Return a quotation related to the current location.
    """
    talking_about = data.hydrateLocation(wander['location']).pleiades_id
    if not talking_about:
        print("Error: place not found")
        return renderNearbyPlaceQuotation(wander, data.hydrateLocation(wander['location']))
    #    return {'type':'quotation', 'state':wander}.update(data.renderPerseusFromPleiades(talking_about))
    output_text = data.renderPerseusFromPleiades(talking_about)
    #print(output_text)
    if output_text:
        render_base = {'type':'quotation', 'state':wander}
        render_base.update(output_text)
        writeStory(render_base)
    else:
        print("No output text found for " + str(talking_about))
        # TODO: try to grab a nearby place quotation instead
    

def wanderTravel(wander):
    """
    Update the Wanderer's travelling state.
    """
    # TODO - travelling loop for the journey and nearby places that get passed
    # TODO - events along the way, shipwrecks, escapades, etc.

    # Arrived at destination
    wander['state'] = wanderArrive
    return wander

def wanderAtPlace(wander):
    """
    The wanderer is at a location; take part in any activities there.
    """
    wander['state'] = wanderSelectDestination
    return wander

def wanderArrive(wander):
    """
    The wanderer has arrived at the travel destination.
    """
    wander['location'] = wander['destination']
    renderPlaceQuotation(wander)
    wander['state'] = wanderAtPlace
    return wander

def wanderDepart(wander):
    """
    The wanderer is leaving the current location.
    """
    wander['state'] = wanderTravel
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
    renderSelectDestination(wander)
    return wander

def makeWanderer():
    return {'location': data.makeOrbisLocation(50327),
            'state':wanderSelectDestination,
            'current_time': 0.0,
            'destination': data.Location(),
            'last_city': data.Location(),
            'journey':{'type':'', 'distance':'0.0', 'expense':'0.0', 'days':'0.0'}}

def processWanderer(wander:dict):
    for i in range(0,90):
        if DELAY_FOR_BANDWIDTH:
            print(time.process_time)
            time.sleep(3)            
        wander = wander['state'](wander)
    return wander