import settings
import data
import pprint
import mistune
import html2text
import bs4
import re
import hoedown
import ftfy


h = html2text.HTML2Text()
h.ignore_links = False
h.unicode_snob = False
h.body_width = 0

book_text = []

def flushBook():
    global book_text
    book_text = []

def bookIntro():
    intro_text = """% Virgil's Commonplace Book
% Isaac Karth
% November 26, 2015
\\newpage
\n
\\newpage
# Virgil's Commonplace Book
\\newpage
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n
&nbsp;\n\n
Virgil's Commonplace Book\n
2015\n\n
Portions of the text are based on extracts from texts provided by the Perseus Digital Library, used under a Creative Commons Attribution-ShareAlike 3.0 United States License\n
\\newpage
\n## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These uses were not always attributed to the original source. Lacking the modern concept of plagiarism (or regular citation) quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.\n 
In a way, this reuse is fortunate: many texts from the Classical period only survive in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.\n
Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. Still, that's no reason to neglect giving credit, so this book also attempts to cite the sources for the works it borrows from.\n
That deliberate borrowing is the intent, here. Unlike an age of precious codices, the information age is a time of entirely too much to read. Search engines can find anything you ask for but, like a fairy-tale mirror, can only answer the questions you know enough to ask in the first place. The serendipity of browsing through a library is lost. Extracting the stories and arranging them in a new pattern presents a new angle. Rather than an exhaustive view of the forest, it picks out one or two trees you might have otherwise overlooked.\n
I chose Virgil as the protagonist for three reasons: first, his works are among the source texts in the Perseus Digital Library used for much of the text here. His epic built on the earlier traditions, appropriate for a work themed around appropriation and reuse. This would not be enough to recommend him on its own: there are other authors whose works were much closer to the kind of copying and summarizing going on here. But there was also a tradition that linked Virgil and his poetry with magic and prophecy. It was no accident that Dante chose Virgil to be his guide through the _Inferno_. Lastly, that tradition of magic lead the much-neglected Avram Davidson to pen a novel with Vergil Magus as the magician-protagonist. My own pseudo-Virgil is a humble tribute, a machine homunculus librarian to forgotten texts.\n

\\newpage
    """
    return intro_text

def writeToBook(text):
    global book_text
    pprint.pprint(text)
    book_text.append(text)

def readBook():
    all_text = bookIntro()
    for t in book_text:
        all_text += ftfy.fix_encoding(str(t)) + "\n"
    return all_text

def textQuotation(t):
    possible_story_titles = ["A story about {place}",
                             "What {author} once said about {place}",
                             ""
                             ]
    place_name = data.getNearestName(t['place'])
    if not place_name:
        place_name = data.getNearestName(data.hydrateLocation(t['state']['location']))
    title_data = {'place': place_name}
    writeToBook("### A story about {place}\n".format(**title_data))
    writeToBook(h.handle(t['text']))
    #writeToBook(t['text'])
    pass

def textTravel(t):
    writeToBook(h.handle(t['text']))
    #writeToBook(t['text'])
    pass

def addCitation(t):
    cite = ""
    for c in t:
        cite += str(c)
    #strip_whitespace = re.compile(r'\s+')
    #cite = strip_whitespace.sub(" ", cite)
    writeToBook(str(cite))

text_translate_table = {'quotation': textQuotation,
                       'travel-narration': textTravel }

def transcribeStory(story:list):
    """
    Takes a list of dicts that contain the story text and metadata and
    transcribes it into the formatted book.
    """
    flushBook()
    #renderer = mistune.Renderer(escape=True, hard_wrap=True)
    #markdown = mistune.Markdown(renderer = renderer)
    for t in story:
        text_translate_table[(t['type'])](t)
    for c in story:
        try:
            addCitation([c['cite']])
        except KeyError as err:
            continue
    
    result = readBook()
    with open("output.markdown", mode='wt', encoding="utf-8") as file:
        file.write(result)
    
    renderer = mistune.Renderer(escape=True, hard_wrap=False)
    markdown = mistune.Markdown(renderer = renderer)
    htmltext = ftfy.fix_text(markdown(result))
    with open("output.html", mode='wt', encoding="utf-8") as file:
        file.write(htmltext)
    return result

