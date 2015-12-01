import settings
import data
import wander
import book
import plot

def go():
    settings.setRNG()
    wander.processWanderer(wander.makeWanderer())
    story = wander.getStory()
    return book.transcribeStory(story)