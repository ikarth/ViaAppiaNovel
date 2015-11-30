import settings
import data
import random
import time
import numpy
import math
import uuid
import phrases
import copy

DELAY_FOR_BANDWIDTH = settings.DELAY_FOR_BANDWIDTH #if true, sleeps a bit between tasks that might call for network resources
WRITE_THE_STORIES = settings.WRITE_THE_STORIES # if false, skip writing the actual stories, so we can speed up testing
DISPLAY_WANDERING_PROGRESS = settings.DISPLAY_WANDERING_PROGRESS

wanderer_story = []

def writeStory(story_data:dict):
    global wanderer_story
    #print("========================")
    #print(story_data)
    wanderer_story.append(story_data)

def processStory(story):
    new_story = copy.deepcopy(story)
    for i in story:
        if str(i['type']) == "chapterEnd":
            for j in new_story:
                if j['type'] == "chapterStart":
                    if j['chapter'] == i['chapter']:
                        start_loc = j['state']['location'].name()
                        end_loc = (i['state']['destination']).name()
                        chapter_title = str(start_loc) + " to " + str(end_loc)
                        j['text'] = str("\n# " + chapter_title + "")
    return new_story

def getStory():
    return processStory(wanderer_story)

def descriptionJourneyType(type):
    type_description = type
    type_description_subs= {"fastdown":"on a military boat floating downstream",
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

def descriptionJourneyTypeName(type):
    type_description = type
    type_description_subs= {"fastdown":"river",
                            "fastup":"river, upstream",
                            "upstream":"river, upstream",
                            "downstream":"river",
                            "road":"road",
                            "coastal":"ship",
                            "overseas":"ship",
                            "slowcoast":"ship",
                            "ferry":"ferry"
                            }
    type_description = type_description_subs[type]
    return type_description

def fleshOutDescription(wander:dict, desc):
    """
    Given a paragraph of text, go through it, replacing the variables with those extracted from the wanderer state.
    """
    text_departing_from_name = data.getNearestName(data.hydrateLocation(wander['last_city']))
    text_travel_route_type = descriptionJourneyType(wander['journey']['type'])
    text_travel_route_type_name = descriptionJourneyTypeName(wander['journey']['type'])
    text_destination_name = data.getNearestName(data.hydrateLocation(wander['destination']))
    miles_distance = (float(wander['journey']['distance']) * settings.KILOMETERS_TO_MILES) # km-to-miles
    distance_text = ["a journey of about {} miles".format(str(math.floor(miles_distance))),
                     "about {} miles away".format(str(math.floor(miles_distance))),
                     "a distance of about {} miles".format(str(math.floor(miles_distance))),
                     "at least {} miles".format(str(math.floor(miles_distance)))]
    text_distance = settings.TEXT_RNG.choice(distance_text)

    variable_swap = {'from':text_departing_from_name, 'type':text_travel_route_type, 'type_name':text_travel_route_type_name, 'destination':text_destination_name, 'distance':text_distance, 'miles':str(math.floor(miles_distance))}

    output = str(desc.format(**variable_swap))
    if (output != desc):
        return fleshOutDescription(wander, output) # recurse so we can handle nested variables TODO: add nested variables
    return output

def renderSelectDestination(wander:dict):
    story_templates = ["Virgil departed from {from}, intending to travel {type} to {destination}, {distance}. ",
                       "Leaving {from}, Virgil set out for {destination} {type}, {distance}. ",
                       "From {from} to {destination} is {distance} when travelling {type}. ",
                       "Intending to travel {type} to {destination}, Virgil left {from}. It was {distance}. "]
    story_text = settings.TEXT_RNG.choice(story_templates)

    header_templates = ["The journey to {destination}",
                        "From {from} to {destination}",
                        "Departing from {from}",
                        "To {destination}",
                        "After {from}",
                        "{miles} miles to {destination}",
                        "{from} to {destination} by {type_name}",
                        "To {destination} by {type_name}",
                        "Leaving {from} by {type_name}",
                        "Travelling {type} to {destination}",
                        "Travelling by {type_name}"]
    header_choice_text = "\n## " + settings.TEXT_RNG.choice(header_templates)
    header_text = fleshOutDescription(wander, header_choice_text)
    header_data = {'type':'travel', 'text':header_text, 'metadata':[], 'state':copy.deepcopy(wander)}
    writeStory(header_data)

    story = fleshOutDescription(wander, story_text)
    story_data = {'type':'travel', 'text':story, 'metadata':[], 'state':copy.deepcopy(wander)}
    writeStory(story_data)

def renderTravelQuotation(wander:dict):
    """
    Given a travelling wanderer, come up with a quotatation from a place
    near the current location (on the travel path).
    """
    pass

def phrasesElision(input_phrases, minmum = 3):
    """
    Given a list of phrases, remove most of them and join the rest together.
    """
    iphrases = input_phrases[:]
    minumum = max(minmum,1)
    if not iphrases:
        print("PHRASE ERROR")
        print (input_phrases)
        print(iphrases)
    total_l = len(iphrases)
    if total_l < minmum:
        print(iphrases)
        return
    max_l = min(int(math.floor(total_l * 0.5)), 10)
    min_l = max(int(max_l * 0.4), 1)
    max_l = max(max_l, min_l + 1)
    length = settings.TEXT_RNG.choice(range(min_l, max_l))
    while len(iphrases) > length:
        iphrases.remove(settings.TEXT_RNG.choice(iphrases))
    return str(". ".join(iphrases)) + ". "

def phrasesShuffle(iphrases):
    phr = iphrases[:]
    settings.TEXT_RNG.shuffle(phr)
    return phr

def phrasesDeal(iphrases):
    phr = iphrases[:]
    shuf = phrasesShuffle(phr)
    return phrasesElision(shuf)

def phrasesDeck(iphrases):
    """
    Take the supplied phrase deck. 
    Remove previously used phrases. 
    Return a random phrase from the remaining set and mark it as used.
    If remaining cards in deck are too low, reshuffle deck by clearing used phrase array.
    """
    return ""

def renderTravelShipStorm(wander:dict):
    return phrasesElision(phrases.storm) + phrasesElision(phrases.wreck) + " \n\n" + phrasesElision(phrases.storm_end) + " \n\n" + phrasesElision(phrases.wreck_landing)

def renderTravelShip(wander:dict):
    if settings.TEXT_RNG.choice([True, False, False, False]):
        return renderTravelShipStorm(wander)
    if settings.TEXT_RNG.choice([True, False]):
        return phrasesElision(phrases.sailing) + " \n\n" + phrasesElision(phrases.harbor)
    return phrasesElision(phrases.sailing) + " \n\n" + phrasesElision(phrases.storm) + phrasesElision(phrases.storm_end) + " \n\n" + phrasesElision(phrases.harbor)
    
def renderTravelWalk(wander:dict):
    return phrasesDeal(phrases.walking)

def renderTravelGeneric(wander:dict):
    print (phrases.travel)
    return phrasesDeal(phrases.travel)

def renderTravelText(wander:dict):
    """
    Describe the wanderer's travels.
    """
    type_desc={"fastdown": renderTravelGeneric,
               "fastup": renderTravelGeneric,
               "upstream": renderTravelGeneric,
               "downstream": renderTravelGeneric,
               "road": renderTravelWalk,
               "coastal": renderTravelShip,
               "overseas": renderTravelShip,
               "slowcoast": renderTravelShip,
               "ferry": renderTravelShip}
                            
    desc = type_desc[str(wander['journey']['type'])](wander)
    desc = fleshOutDescription(wander, desc)
    
    writeStory({'type':'travel', 'text':desc, 'state':copy.deepcopy(wander)})
    pass

def renderNearbyPlaceQuotation(wander:dict, loc:data.Location, range:float = 0.0):
    """
    Given a latlon location, find a nearby place and 
    write a quote based on it.
    """
    if not loc.latlon or (not loc.latlon[0]) or (not loc.latlon[1]):
        print("Warning: Couldn't find latlon in {}".format([loc.orbis_id, loc.pleiades_id, loc.latlon]))
        return
    #data.findNearbyPerseusFromLatLon(loc.latlon)
    if WRITE_THE_STORIES:
        render_base = {'type':'quotation', 'state':copy.deepcopy(wander)}
        render_base.update(data.renderPerseusFromLatLon(loc.latlon)) # TODO: set range based on location
        writeStory(render_base)    
    else:
        print("Skipping story for " + str(loc.latlon))
        writeStory({'type':'placeholder', 'text':str("Insert story about " + str(loc.latlon)) , 'state':copy.deepcopy(wander)})
    

def renderPlaceQuotation(wander:dict):
    """
    Return a quotation related to the current location.
    """
    talking_about = data.hydrateLocation(wander['location']).pleiades_id
    if not talking_about:
        print("Error: place not found")
        if not WRITE_THE_STORIES:
            writeStory({'type':'placeholder', 'text':str("There was no story for " + str(talking_about)) , 'state':copy.deepcopy(wander)})
        return renderNearbyPlaceQuotation(wander, data.hydrateLocation(wander['location']))
    #    return {'type':'quotation', 'state':copy.deepcopy(wander)}.update(data.renderPerseusFromPleiades(talking_about))
    output_text = None
    if WRITE_THE_STORIES:
        output_text = data.renderPerseusFromPleiades(talking_about)
    else:
        print("Skipping story for " + str(talking_about))
        writeStory({'type':'placeholder', 'text':str("Insert story about " + str(talking_about)) , 'state':copy.deepcopy(wander)})
    #print(output_text)
    if output_text:
        render_base = {'type':'quotation', 'state':copy.deepcopy(wander)}
        render_base.update(output_text)
        writeStory(render_base)
    else:
        print("No output text found for " + str(talking_about))
        return renderNearbyPlaceQuotation(wander, data.hydrateLocation(wander['location']))
        # TODO: try to grab a nearby place quotation instead


def eventStorm(wander):
    pass

def eventShipwreck(wander):
    pass

def eventTravelWalk(wander):
    desc = fleshOutDescription(wander, renderTravelWalk(wander))
    writeStory({'type':'travel', 'text':desc, 'state':copy.deepcopy(wander)})
    pass

def eventTravelRiver(wander):
    renderTravelText(wander)
    pass

def eventTravelShip(wander):
    desc = fleshOutDescription(wander, renderTravelShip(wander))
    writeStory({'type':'travel', 'text':desc, 'state':copy.deepcopy(wander)})

def eventTravelFerry(wander):
    renderTravelText(wander)
    pass    

def eventTravel(wander):
    renderTravelText(wander)
    pass

def wanderTravel(wander):
    """
    Update the Wanderer's travelling state.
    """
    if DISPLAY_WANDERING_PROGRESS:
        print("wanderTravel")
    # TODO - travelling loop for the journey and nearby places that get passed
    # TODO - events along the way, shipwrecks, escapades, etc.

    type_desc={"fastdown": [eventTravelRiver],
               "fastup": [eventTravelRiver],
               "upstream": [eventTravelRiver],
               "downstream": [eventTravelRiver],
               "road": [eventTravelWalk],
               "coastal": [eventTravelShip],
               "overseas": [eventTravelShip],
               "slowcoast": [eventTravelShip],
               "ferry": [eventTravelFerry]}
    
    # Do events                        
    type_desc[str(wander['journey']['type'])][0](wander)
    # todo: select events from a shuffled deck
     
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
        destination = settings.TRAVEL_RNG.choice(edges, p=weighted_edges)
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

current_chapter = 0

def chapterBegin(wander:dict):
    global current_chapter
    current_chapter += 1
    writeStory({'type':'chapterStart', 'text':"\n# Chapter Title Placeholder\n" , 'state':copy.deepcopy(wander), 'chapter':current_chapter})
    

def chapterEnd(wander:dict):
    writeStory({'type':'chapterEnd', 'text':"" , 'state':copy.deepcopy(wander), 'chapter':current_chapter})
    

def wanderChapter(wander:dict):
    chapterBegin(wander)
    passage_count = 0
    chapter_done = False
    while not chapter_done:
        passage_count += 1
        if DELAY_FOR_BANDWIDTH:
            print(time.process_time())
            time.sleep(1)
        wander = wander['state'](wander)
        if (passage_count > 30) and wander['state'] == wanderSelectDestination:
            chapter_done = True
    chapterEnd(wander)
    return wander

def processWanderer(wander:dict):
    global current_chapter
    current_chapter = 0
    settings.setRNG()
    for i in range(0,16):
        wander = wanderChapter(wander)
    return wander