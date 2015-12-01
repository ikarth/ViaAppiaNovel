import settings
import data
import wander
import book
import plot

def go():
    wander.processWanderer(wander.makeWanderer())
    story = wander.getStory()
    return book.transcribeStory(story)