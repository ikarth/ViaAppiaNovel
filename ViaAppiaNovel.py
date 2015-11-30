import settings
import data
import wander
import book

def go():
    wander.processWanderer(wander.makeWanderer())
    story = wander.getStory()
    return book.transcribeStory(story)