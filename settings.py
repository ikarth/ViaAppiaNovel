import random

class DataSourceAccessProblem(Exception):
    pass

class ViaAppiaException(Exception):
    pass

# Random Generator
random.seed("Rome wasn't built in a day")

DELAY_FOR_BANDWIDTH = False #if true, sleeps a bit between tasks that might call for network resources
WRITE_THE_STORIES = True # if false, skip writing the actual stories, so we can speed up testing
DISPLAY_TEXT_WHILE_WRITING = False
DISPLAY_WANDERING_PROGRESS = True

DATA_FILEPATH = "../../data/ancient"

PICKLE_PERSEUS_CTS = True
PICKLE_PERSEUS_PLEIADES_INDEX = False
PICKLE_PERSEUS_LATLON_LIST = False

KILOMETERS_TO_MILES = 0.621371

