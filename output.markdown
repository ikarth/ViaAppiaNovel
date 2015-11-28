% Virgil's Commonplace Book
% Isaac Karth
\newpage

## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These texts were not always attributed to the original source. Lacking the modern concept of plagiarism (and our post-printing-press system of uniform citations) writers sometimes come off as careless to modern sensibilities. Quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.
 
In a way, this reuse is fortunate: many texts from the Classical period only exist in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.

Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. The closest literary ancedents of NaNoGenMo--Dada and Oulipo--have often explored similar sampling approaches. Kathryn Hume has suggested that technical constratints have lead NaNoGenMo to "align itself with poetics of recontextualization and reassembly."^[Hume, Kathryn. "NaNoGenMo: Dada 2.0". URL:<http://arcade.stanford.edu/blogs/nanogenmo-dada-20>. Accessed: 2015-11-28. (Archived by WebCite® at <http://www.webcitation.org/6dNl9xpbY>)] 

While I'd point out that NaNoGenMo also exhibits other aspects, such as the concrete poetry in thricedotted's _The Seeker_, or the way structurally-plotted works like _Hannah and The Twelve-Disk Tower of Hanoi_ evoke the chessboard constraints of _Life a User's Manual_ or _Through the Looking Glass_, there is an undeniable strand of appropreation as we teach our machines to imitate their human creators. Still, that's no reason to neglect giving credit, so this book attempts to cite the sources for the texts it borrows.

In this work, that deliberate borrowing is the intent. Unlike an age of precious codices, the information age is a time of entirely too much to read. Search engines can find anything you ask for but, like a fairy-tale mirror, can only answer the questions you know enough to ask in the first place. The serendipity of browsing through a library is lost. Extracting the stories and arranging them in a new pattern presents a new angle. Rather than an exhaustive view of the forest, it picks out one or two trees you might have otherwise overlooked.

I chose Virgil as the protagonist for three reasons: first, his works are among the source texts in the Perseus Digital Library used for much of the text here. His _Aeneid_ builds on earlier traditions, recast in a founding epic for a new age: appropriate for a work themed around appropriation and reuse in this new information age. This would not be enough to recommend him on its own: there are other authors whose works were much closer to the kind of copying and summarizing going on here. And _The Golden Ass_ by Apuleius, one of the earliest surviving novels, is closer in form to the travel tale that structures this generated novel. 

But there was also a tradition that linked Virgil and his poetry with magic and prophecy. It was no accident that Dante chose Virgil to be his guide through the _Inferno_. That touch of magic, a magic intimately linked with words and poetry. And, as Jeff Howard has pointed out,^[in _Game Magic: A Designer's Guide to Magic Systems in Theory and Practice_] programming is a form of magic. A magician-protagonist is entirely appropreate.

Lastly, that tradition of magic lead the much-neglected Avram Davidson to pen a novel with Vergil Magus as the magician-protagonist. My own pseudo-Virgil is a humble tribute, a machine homunculus librarian to forgotten texts.



Isaac Karth 

2015-11-28 

\newpage

## Technical Notes 

The book generator is a Python program that outputs a Markdown text file designed to be converted into PDF form via Pandoc. 


~~~
pandoc output.markdown -S --normalize --toc \
 -o via_appia.pdf --latex-engine=xelatex \
 --template novel_template.latex \
  --variable otherlangs=polutonikogreek,greek \
  --variable lang="english" -V geometry:paperwidth=5.5in \
  -V geometry:paperheight=8.25in -V geometry:margin=.7in \
  -V geometry:inner=1.0in -V geometry:outer=0.5in \
  -V fontfamily:"DejaVu Serif" -V linestretch:1.2
~~~


\newpage
    Virgil departed from Roma, intending to travel on a military boat downstream to the countryside, a 17.017487577 mile journey. 

There was no story for None

Virgil departed from the countryside, intending to travel on a boat heading upstream to Roma, a 17.017487577 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel by road to Volsinii, a 62.636682284 mile journey. 

Insert story about 413389

Virgil departed from Volsinii, intending to travel by road to Roma, a 62.636682284 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel by road to Tibur, a 17.629538012 mile journey. 

Insert story about 423081

Virgil departed from Tibur, intending to travel by road to Roma, a 17.629538012 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel on a boat heading downstream to Ostia/Portus, a 17.919718269 mile journey. 

Insert story about 422995

Virgil departed from Ostia/Portus, intending to travel by ship, down the coast to Cosa, a 81.81094860200001 mile journey. 

Insert story about 413107

Virgil departed from Cosa, intending to travel by ship, down the coast to Ostia/Portus, a 81.81094860200001 mile journey. 

Insert story about 422995

Virgil departed from Ostia/Portus, intending to travel by ship, down the coast to Palinurus Pr., a 197.493451785 mile journey. 

There was no story for None

Virgil departed from Palinurus Pr., intending to travel by ship, down the coast to Regium, a 168.075884532 mile journey. 

Insert story about 452416

Virgil departed from Regium, intending to travel across by ferry to Messana, a 11.504684065000001 mile journey. 

There was no story for None

Virgil departed from Messana, intending to travel across by ferry to Regium, a 11.504684065000001 mile journey. 

Insert story about 452416

Virgil departed from Regium, intending to travel by ship, down the coast to Heracleum Pr., a 44.766052324 mile journey. 

There was no story for None

Virgil departed from Heracleum Pr., intending to travel by ship, down the coast to Regium, a 44.766052324 mile journey. 

Insert story about 452416

Virgil departed from Regium, intending to travel on a local coastal ship, travelling only by day to Vibo Valentia, a 73.847457866 mile journey. 

Insert story about 452337

Virgil departed from Vibo Valentia, intending to travel by ship, down the coast to Regium, a 73.847457866 mile journey. 

Insert story about 452416

Virgil departed from Regium, intending to travel across by ferry to Messana, a 11.504684065000001 mile journey. 

There was no story for None

Virgil departed from Messana, intending to travel by ship, crossing the sea to Apollonia-Sozousa, a 532.731184108 mile journey. 

There was no story for None

Virgil departed from Apollonia-Sozousa, intending to travel by road to Cyrene, a 9.984189228000002 mile journey. 

Insert story about 373778

Virgil departed from Cyrene, intending to travel by road to Ptolemais, a 61.977407653 mile journey. 

Insert story about 373879

Virgil departed from Ptolemais, intending to travel by road to Cyrene, a 61.977407653 mile journey. 

Insert story about 373778

Virgil departed from Cyrene, intending to travel by road to Apollonia-Sozousa, a 9.984189228000002 mile journey. 

There was no story for None

Virgil departed from Apollonia-Sozousa, intending to travel by ship, down the coast to Darnis, a 64.985464664 mile journey. 

Insert story about 373780

Virgil departed from Darnis, intending to travel by road to Cyrene, a 46.277226596 mile journey. 

Insert story about 373778

Virgil departed from Cyrene, intending to travel by road to Darnis, a 46.277226596 mile journey. 

Insert story about 373780

Virgil departed from Darnis, intending to travel by ship, down the coast to Apollonia-Sozousa, a 64.985464664 mile journey. 

There was no story for None

Virgil departed from Apollonia-Sozousa, intending to travel by ship, crossing the sea to Messana, a 555.323612297 mile journey. 

There was no story for None

Virgil departed from Messana, intending to travel by ship, crossing the sea to Gades, a 1345.3974601680002 mile journey. 

Insert story about 256177

Virgil departed from Gades, intending to travel by ship, crossing the sea to Messana, a 1431.16654204 mile journey. 

There was no story for None

Virgil departed from Messana, intending to travel by ship, crossing the sea to Gades, a 1345.3974601680002 mile journey. 

Insert story about 256177

Virgil departed from Gades, intending to travel by ship, crossing the sea to Caralis, a 1061.762103911 mile journey. 

There was no story for None

Virgil departed from Caralis, intending to travel by ship, crossing the sea to Gades, a 990.7133010289999 mile journey. 

Insert story about 256177

Virgil departed from Gades, intending to travel by ship, crossing the sea to Caralis, a 1061.762103911 mile journey. 

There was no story for None

Virgil departed from Caralis, intending to travel by ship, crossing the sea to Galata, a 125.241053276 mile journey. 

There was no story for None

Virgil departed from Galata, intending to travel by ship, crossing the sea to Caralis, a 125.241053276 mile journey. 

There was no story for None

Virgil departed from Caralis, intending to travel by ship, crossing the sea to Palma, a 397.229431509 mile journey. 

There was no story for None

Virgil departed from Palma, intending to travel by ship, down the coast to Ebusus, a 92.429557621 mile journey. 

There was no story for None

Virgil departed from Ebusus, intending to travel by ship, crossing the sea to Iol Caesarea, a 173.477462635 mile journey. 

Insert story about 295279

Virgil departed from Iol Caesarea, intending to travel by ship, crossing the sea to Ebusus, a 173.477462635 mile journey. 

There was no story for None

Virgil departed from Ebusus, intending to travel by ship, crossing the sea to Iol Caesarea, a 173.477462635 mile journey. 

Insert story about 295279

Virgil departed from Iol Caesarea, intending to travel by road to Sufasar, a 45.669525758000006 mile journey. 

Insert story about 295346

Virgil departed from Sufasar, intending to travel by road to Albulae, a 231.13882732200003 mile journey. 

Insert story about 285412

Virgil departed from Albulae, intending to travel by road to Sufasar, a 231.13882732200003 mile journey. 

Insert story about 295346

Virgil departed from Sufasar, intending to travel by road to Iol Caesarea, a 45.669525758000006 mile journey. 

Insert story about 295279

