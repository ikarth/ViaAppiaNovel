import random

class DataSourceAccessProblem(Exception):
    pass

class ViaAppiaException(Exception):
    pass

# Random Generator
random.seed("Rome wasn't built in a day")

DELAY_FOR_BANDWIDTH = True #if true, sleeps a bit between tasks that might call for network resources
WRITE_THE_STORIES = True # if false, skip writing the actual stories, so we can speed up testing
DISPLAY_TEXT_WHILE_WRITING = False

DATA_FILEPATH = "../../data/ancient"

KILOMETERS_TO_MILES = 0.621371

