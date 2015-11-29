import settings
import data
import random
import time
import numpy
import math

DELAY_FOR_BANDWIDTH = settings.DELAY_FOR_BANDWIDTH #if true, sleeps a bit between tasks that might call for network resources
WRITE_THE_STORIES = settings.WRITE_THE_STORIES # if false, skip writing the actual stories, so we can speed up testing
DISPLAY_WANDERING_PROGRESS = settings.DISPLAY_WANDERING_PROGRESS
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
                            "coastal":"by ship down the coast",
                            "overseas":"by ship, crossing the sea",
                            "slowcoast":"on a local coastal ship, travelling only by day",
                            "ferry":"across by ferry"
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

def renderNearbyPlaceQuotation(wander:dict, loc:data.Location, range:float = 0.0):
    """
    Given a latlon location, find a nearby place and 
    write a quote based on it.
    """
    if not loc.latlon:
        print("Warning: Couldn't find latlon in {}".format(loc))
        return
    #data.findNearbyPerseusFromLatLon(loc.latlon)
    render_base = {'type':'quotation', 'state':wander}
    render_base.update(data.renderPerseusFromLatLon(loc.latlon)) # TODO: set range based on location
    writeStory(render_base)    

def renderPlaceQuotation(wander:dict):
    """
    Return a quotation related to the current location.
    """
    talking_about = data.hydrateLocation(wander['location']).pleiades_id
    if not talking_about:
        print("Error: place not found")
        if not WRITE_THE_STORIES:
            writeStory({'type':'placeholder', 'text':str("There was no story for " + str(talking_about)) , 'state':wander})
        return renderNearbyPlaceQuotation(wander, data.hydrateLocation(wander['location']))
    #    return {'type':'quotation', 'state':wander}.update(data.renderPerseusFromPleiades(talking_about))
    output_text = None
    if WRITE_THE_STORIES:
        output_text = data.renderPerseusFromPleiades(talking_about)
    else:
        print("Skipping story for " + str(talking_about))
        writeStory({'type':'placeholder', 'text':str("Insert story about " + str(talking_about)) , 'state':wander})
    #print(output_text)
    if output_text:
        render_base = {'type':'quotation', 'state':wander}
        render_base.update(output_text)
        writeStory(render_base)
    else:
        print("No output text found for " + str(talking_about))
        return renderNearbyPlaceQuotation(wander, data.hydrateLocation(wander['location']))
        # TODO: try to grab a nearby place quotation instead
    

def wanderTravel(wander):
    """
    Update the Wanderer's travelling state.
    """
    if DISPLAY_WANDERING_PROGRESS:
        print("wanderTravel")
    # TODO - travelling loop for the journey and nearby places that get passed
    # TODO - events along the way, shipwrecks, escapades, etc.

    # Arrived at destination
    wander['state'] = wanderArrive
    return wander

def wanderAtPlace(wander):
    """
    The wanderer is at a location; take part in any activities there.
    """
    if DISPLAY_WANDERING_PROGRESS:
        print("wanderAtPlace")
    wander['state'] = wanderSelectDestination
    return wander

def wanderArrive(wander):
    """
    The wanderer has arrived at the travel destination.
    """
    if DISPLAY_WANDERING_PROGRESS:
        print("wanderArrive")
    wander['previous_locations'].append(wander['location'])
    wander['location'] = wander['destination']
    renderPlaceQuotation(wander)    
    wander['state'] = wanderAtPlace
    return wander

def wanderDepart(wander):
    """
    The wanderer is leaving the current location.
    """
    if DISPLAY_WANDERING_PROGRESS:
        print("wanderDepart")
    wander['state'] = wanderTravel
    return wander

def countVisits(wander):
    """
    Go through the list of previously visited locations, counting how many times they occur
    """
    loc_count = {}
    for i in wander['previous_locations']:
        iid = str(i.id())
        try:
            loc_count[iid] += 1
        except KeyError:
            loc_count[iid] = 1
    return loc_count

def scoreEdgesByVisits(wander, edges) -> dict:
    visits = countVisits(wander)
    edge_loc = [data.makeOrbisLocation(i['target']) for i in edges]
    score = []
    for i in edge_loc:
        try:
            score.append(visits[i.id()])
        except KeyError:
            score.append(0)
    prob_max = max(1.0, max(score)) + 1
    prob = numpy.array([(max(0, prob_max - i) / prob_max) for i in score])
    prob /= prob.sum()
    #print(prob)
    return prob

def wanderSelectDestination(wander):
    """
    The wanderer needs to select the next destination.
    """
    if DISPLAY_WANDERING_PROGRESS:
        print("wanderSelectDestination")
    current = data.hydrateLocation(wander['location']).orbis_id
    edges = data.findOrbisEdges(current)
    weighted_edges = scoreEdgesByVisits(wander, edges)
    #weighted_edges = data.scoreByDistance(data.hydrateLocation(wander['location']), edges)
    try:
        #destination = random.choice(edges)
        destination = rng.choice(edges, p=weighted_edges)
    except Exception as err:
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
            'previous_locations': list(),
            'journey':{'type':'', 'distance':'0.0', 'expense':'0.0', 'days':'0.0'}}

rng = None
def processWanderer(wander:dict):
    global rng
    rng = numpy.random.RandomState()
    rng.seed(753)    
    for i in range(0,60):
        if DELAY_FOR_BANDWIDTH:
            print(time.process_time())
            time.sleep(1)            
        wander = wander['state'](wander)
    return wander