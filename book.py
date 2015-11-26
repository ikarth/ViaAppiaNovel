import settings
import data
import pprint
import mistune
import html2text
import bs4


h = html2text.HTML2Text()
h.ignore_links = True

book_text = []

def writeToBook(text):
    global book_text
    print(text)
    book_text.append(text)

def readBook():
    all_text = ""
    for t in book_text:
        all_text += t
    return all_text

def textQuotation(t):
    possible_story_titles = ["A story about {place}",
                             "What {author} once said about {place}",
                             ""
                             ]
    title_data = {'place': data.getNearestName(data.hydrateLocation(t['state']['location']))}
    writeToBook("### A story about {place}\n".format(**title_data))
    writeToBook(h.handle(t['text']))
    pass

def textTravel(t):
    writeToBook(h.handle(t['text']))
    pass

text_translate_table = {'quotation': textQuotation,
                       'travel-narration': textTravel }

def transcribeStory(story:list):
    """
    Takes a list of dicts that contain the story text and metadata and
    transcribes it into the formatted book.
    """
    #renderer = mistune.Renderer(escape=True, hard_wrap=True)
    #markdown = mistune.Markdown(renderer = renderer)
    for t in story:
        text_translate_table[(t['type'])](t)
    
    result = readBook()
    with open("output.markdown", 'wt') as file:
        file.write(result)
    return result

