﻿import settings
import data
import pprint
import mistune
import html2text
import bs4
import re
import hoedown
import ftfy
import random
import phrases

DISPLAY_TEXT_WHILE_WRITING = settings.DISPLAY_TEXT_WHILE_WRITING

h = html2text.HTML2Text()
h.ignore_links = False
h.unicode_snob = False
h.body_width = 0

def convertHTML(text):
    return h.handle(text.replace("\n", "<br/>"))

book_text = []

def flushBook():
    global book_text
    book_text = []

def bookIntro():
    intro_text = """% Virgil's Commonplace Book
% Isaac Karth
\n## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These texts were not always attributed to the original source. Lacking the modern concept of plagiarism (and our post-printing-press system of uniform citations) writers sometimes come off as careless to modern sensibilities. Quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.\n 
In a way, this reuse is fortunate: many texts from the Classical period only exist in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.\n
Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. The closest literary antecedents of NaNoGenMo--Dada and Oulipo--have often explored similar sampling approaches. Kathryn Hume has suggested that technical constraints have lead NaNoGenMo to "align itself with poetics of recontextualization and reassembly."^[Hume, Kathryn. "NaNoGenMo: Dada 2.0". URL:\\url{http://arcade.stanford.edu/blogs/nanogenmo-dada-20}. Accessed: 2015-11-28. (Archived by WebCite® at \\url{http://www.webcitation.org/6dNl9xpbY})] \n
NaNoGenMo has included other approaches, such as the concrete poetry in thricedotted's _The Seeker_, or the way structurally-plotted works like _Hannah and The Twelve-Disk Tower of Hanoi_ evoke the chessboard constraints of _Life a User's Manual_ or _Through the Looking Glass_. But there is an undeniable strand of appropriation as we teach our machines to imitate their human creators. Still, that's no reason to neglect giving credit, so this book attempts to cite the sources for the texts it borrows.\n
In this work, that deliberate borrowing is the intent. Unlike an age of precious codices, the information age is a time of entirely too much to read. Search engines can find anything you ask for but, like a fairy-tale mirror, can only answer the questions you know enough to ask in the first place. The serendipity of browsing through a library is lost. Extracting the stories and arranging them in a new pattern presents a new angle. Rather than an exhaustive view of the forest, it picks out one or two trees you might have otherwise overlooked.\n
I chose Virgil as the protagonist for three reasons: first, his works are among the source texts in the Perseus Digital Library used for much of the text here. His _Aeneid_ builds on earlier traditions, recast in a founding epic for a new age: appropriate for a work themed around appropriation and reuse in this new information age. This would not be enough to recommend him on its own: there are other authors whose works were much closer to the kind of copying and summarizing going on here. And _The Golden Ass_ by Apuleius, one of the earliest surviving novels, is closer in form to the travel tale that structures this generated novel. \n
But there was also a tradition that linked Virgil and his poetry with magic and prophecy. It was no accident that Dante chose Virgil to be his guide through the _Inferno_. His memory is haunted by that touch of magic, a magic intimately linked with words and poetry. And, as Jeff Howard has pointed out,^[in _Game Magic: A Designer's Guide to Magic Systems in Theory and Practice_] programming is a form of magic. A magician-protagonist is entirely appropriate.\n
Lastly, that tradition of magic lead the much-neglected Avram Davidson to pen a novel with Vergil Magus as the magician-protagonist. My own pseudo-Virgil is a humble tribute, a machine homunculus librarian of forgotten texts.\n
\n
Isaac Karth \n
2015-11-28 \n
\\newpage
\n## Technical Notes \n
The book generator that produced this novel is a Python program that outputs a Markdown text file designed to be converted into PDF form via Pandoc. The source code for the NaNoGenMo version can be found at https://github.com/ikarth/ViaAppiaNovel in a git repository. \n

~~~
pandoc output.markdown -S --normalize --toc \\
-o via_appia_test.pdf --latex-engine=xelatex \\
--template novel_template.latex \\
--variable otherlangs=polutonikogreek,greek \\
--variable lang="english" -V geometry:paperwidth=5.5in \\
-V geometry:paperheight=8.25in -V geometry:margin=.9in \\
-V geometry:inner=1.0in -V geometry:outer=0.5in \\
-V fontfamily:"DejaVu Serif" -V linestretch:1.2 \\
-V documentclass=book
~~~

This copy was generated \\today, with seeds of """ + str(settings.travel_rng_seed) + """ and """ + str(settings.text_rng_seed) + """.\n

The book generator uses data from the Perseus Digital Library, the Pelagios Project, the Pleiades Project, and ORBIS: The Stanford Geospatial Network Model of the Roman World.\n


\n
\\cleardoublepage
\n"""
    return intro_text

def writeToBook(text):
    if not text:
        return
    global book_text
    if DISPLAY_TEXT_WHILE_WRITING:
        print(text)
    book_text.append(text)

def readBook():
    all_text = bookIntro()
    for t in book_text:
        all_text += ftfy.fix_text(str(t)) + "\n"
    return all_text

def quoteIntroductions(t, v = False):
    iphrases = phrases.qintro
    if v:
        iphrases = phrases.qintrov
    phr = iphrases[:]
    return settings.TEXT_RNG.choice(phr)

def textQuotation(t):
    

    possible_story_titles = ["A story about {place}",
                             "What {author} once said about {place}",
                             "A story by {author} about {place} from _{book}_",
                             "An extract from _{book}_ by {author}",
                             "On {place}, according to {author}",
                             "On the subject of {place}",
                             "{place} in _{book}_",
                             "An account of {place}",
                             "A story about {place} by {author}",
                             "The story of {place}"
                             ]
    place_name = data.getNearestName(t['place'])
    if not place_name:
        place_name = data.getNearestName(data.hydrateLocation(t['state']['location']))
    author_name = t['author']
    title_data = {'place': place_name, 'author': author_name, 'book': t['book_title']}
    
    if author_name == "Virgil":
        intro = quoteIntroductions(t, True)
        writeToBook(intro.format(**title_data))
        writeToBook("\n## {place} in Virgil's _{book}_".format(**title_data).title())
    else:    
        intro = quoteIntroductions(t)
        writeToBook(intro.format(**title_data))
        book_string = "\n## " + str(random.choice(possible_story_titles)) + ""
        writeToBook(book_string.format(**title_data).title())
    writeToBook(convertHTML(t['text']))
    #writeToBook(t['text'])
    pass

def textTravel(t):
    if t['text']:
        writeToBook(convertHTML(t['text']))
    #writeToBook(t['text'])
    pass

def textPlaceholder(t):
    writeToBook(convertHTML(t['text']))
    pass

def textNull(t):
    pass

def addCitation(t):
    cite = ""
    for c in t:
        cite += str(c)
    #strip_whitespace = re.compile(r'\s+')
    #cite = strip_whitespace.sub(" ", cite)
    writeToBook(str(cite))


def chapterStart(t):
    writeToBook(t['text'].title())
    pass

def chapterEnd(t):
    writeToBook("\\newpage")
    pass

text_translate_table = {'quotation': textQuotation,
                       'travel': textTravel,
                       'placeholder': textPlaceholder,
                       'chapterStart': chapterStart,
                       'chapterEnd': chapterEnd,
                       'plot':textNull
                       }

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

