import settings
import data
import wander
import book
import random

# Random Generator
random.seed("Rome wasn't built in a day")
#random.seed()



def go():
    wander.processWanderer(wander.makeWanderer())
    story = wander.getStory()
    return book.transcribeStory(story)