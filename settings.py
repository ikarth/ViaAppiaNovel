import random
import numpy

class DataSourceAccessProblem(Exception):
    pass

class ViaAppiaException(Exception):
    pass

class InvalidLatLon(Exception):
    pass

# Random Generator
random.seed("Rome wasn't built in a day")

DELAY_FOR_BANDWIDTH = False #if true, sleeps a bit between tasks that might call for network resources
WRITE_THE_STORIES = False # if false, skip writing the actual stories, so we can speed up testing
DISPLAY_TEXT_WHILE_WRITING = False
DISPLAY_WANDERING_PROGRESS = True
DISPLAY_CITES_WHILE_RENDERING = False

DATA_FILEPATH = "../../data/ancient"

# These control if the pickle data files should be overwritten
PICKLE_PERSEUS_CTS = True
PICKLE_PERSEUS_PLEIADES_INDEX = False
PICKLE_PERSEUS_LATLON_LIST = False

KILOMETERS_TO_MILES = 0.621371

travel_rng_seed = 753
text_rng_seed = 3468
TRAVEL_RNG = None
TEXT_RNG = None

def setRNG():
    global TRAVEL_RNG
    global TEXT_RNG
    TRAVEL_RNG = numpy.random.RandomState(travel_rng_seed)
    TEXT_RNG = numpy.random.RandomState(text_rng_seed)

setRNG()