import random

class DataSourceAccessProblem(Exception):
    pass

class ViaAppiaException(Exception):
    pass

# Random Generator
random.seed("Rome wasn't built in a day")


KILOMETERS_TO_MILES = 0.621371