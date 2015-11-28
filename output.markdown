% Virgil's Commonplace Book
% Isaac Karth
\newpage

## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These texts were not always attributed to the original source. Lacking the modern concept of plagiarism (and our post-printing-press system of uniform citations) writers sometimes come off as careless to modern sensibilities. Quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.
 
In a way, this reuse is fortunate: many texts from the Classical period only exist in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.

Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. The closest literary ancedents of NaNoGenMo--Dada and Oulipo--have often explored similar sampling approaches. Kathryn Hume has suggested that technical constratints have lead NaNoGenMo to "align itself with poetics of recontextualization and reassembly."^[Hume, Kathryn. "NaNoGenMo: Dada 2.0". URL:\url{http://arcade.stanford.edu/blogs/nanogenmo-dada-20}. Accessed: 2015-11-28. (Archived by WebCite® at \url{http://www.webcitation.org/6dNl9xpbY>})] 

While I'd point out that NaNoGenMo also exhibits other aspects, such as the concrete poetry in thricedotted's _The Seeker_, or the way structurally-plotted works like _Hannah and The Twelve-Disk Tower of Hanoi_ evoke the chessboard constraints of _Life a User's Manual_ or _Through the Looking Glass_, there is an undeniable strand of appropreation as we teach our machines to imitate their human creators. Still, that's no reason to neglect giving credit, so this book attempts to cite the sources for the texts it borrows.

In this work, that deliberate borrowing is the intent. Unlike an age of precious codices, the information age is a time of entirely too much to read. Search engines can find anything you ask for but, like a fairy-tale mirror, can only answer the questions you know enough to ask in the first place. The serendipity of browsing through a library is lost. Extracting the stories and arranging them in a new pattern presents a new angle. Rather than an exhaustive view of the forest, it picks out one or two trees you might have otherwise overlooked.

I chose Virgil as the protagonist for three reasons: first, his works are among the source texts in the Perseus Digital Library used for much of the text here. His _Aeneid_ builds on earlier traditions, recast in a founding epic for a new age: appropriate for a work themed around appropriation and reuse in this new information age. This would not be enough to recommend him on its own: there are other authors whose works were much closer to the kind of copying and summarizing going on here. And _The Golden Ass_ by Apuleius, one of the earliest surviving novels, is closer in form to the travel tale that structures this generated novel. 

But there was also a tradition that linked Virgil and his poetry with magic and prophecy. It was no accident that Dante chose Virgil to be his guide through the _Inferno_. His memory is haunted by that touch of magic, a magic intimately linked with words and poetry. And, as Jeff Howard has pointed out,^[in _Game Magic: A Designer's Guide to Magic Systems in Theory and Practice_] programming is a form of magic. A magician-protagonist is entirely appropreate.

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
    Virgil departed from Roma, intending to travel by road to Volsinii, a 62.636682284 mile journey. 

Insert story about 413389

Virgil departed from Volsinii, intending to travel by road to Clusium, a 27.014725595999998 mile journey. 

Insert story about 413096

Virgil departed from Clusium, intending to travel by road to Arretium, a 32.675415406 mile journey. 

Insert story about 413032

Virgil departed from Arretium, intending to travel by road to Florentia, a 42.091050169000006 mile journey. 

Insert story about 413138

Virgil departed from Florentia, intending to travel on a boat heading downstream to Pisae, a 54.196599991 mile journey. 

Insert story about 403253

Virgil departed from Pisae, intending to travel on a boat heading upstream to Florentia, a 54.196599991 mile journey. 

Insert story about 413138

Virgil departed from Florentia, intending to travel by road to Arretium, a 42.091050169000006 mile journey. 

Insert story about 413032

Virgil departed from Arretium, intending to travel by road to Clusium, a 32.675415406 mile journey. 

Insert story about 413096

Virgil departed from Clusium, intending to travel by road to Volsinii, a 27.014725595999998 mile journey. 

Insert story about 413389

Virgil departed from Volsinii, intending to travel by road to Clusium, a 27.014725595999998 mile journey. 

Insert story about 413096

Virgil departed from Clusium, intending to travel by road to Volsinii, a 27.014725595999998 mile journey. 

Insert story about 413389

Virgil departed from Volsinii, intending to travel by road to Roma, a 62.636682284 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a 64.936997726 mile journey. 

Insert story about 413231

Virgil departed from Ocriculum, intending to travel on a boat heading downstream to Roma, a 64.936997726 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel on a military boat downstream to the countryside, a 17.017487577 mile journey. 

There was no story for None

Virgil departed from the countryside, intending to travel on a boat heading upstream to Roma, a 17.017487577 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel by road to Forum Appii, a 42.639720762 mile journey. 

There was no story for None

Virgil departed from Forum Appii, intending to travel on a boat heading downstream to Tarracina, a 14.712822538000001 mile journey. 

Insert story about 433143

Virgil departed from Tarracina, intending to travel by ship, down the coast to Formiae, a 24.815072256 mile journey. 

Insert story about 432839

Virgil departed from Formiae, intending to travel by ship, down the coast to Minturnae, a 18.833133639 mile journey. 

Insert story about 432940

Virgil departed from Minturnae, intending to travel by road to Teanum, a 15.72690001 mile journey. 

There was no story for None

Virgil departed from Teanum, intending to travel by road to Casinum, a 23.607127031999998 mile journey. 

Insert story about 432764

Virgil departed from Casinum, intending to travel by road to Fregellanum, a 17.855717056 mile journey. 

Insert story about 432847

Virgil departed from Fregellanum, intending to travel by road to Ferentinum, a 17.359862998 mile journey. 

Insert story about 432830

Virgil departed from Ferentinum, intending to travel by road to Roma, a 43.833374453000005 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel by road to Volsinii, a 62.636682284 mile journey. 

Insert story about 413389

Virgil departed from Volsinii, intending to travel by road to Clusium, a 27.014725595999998 mile journey. 

Insert story about 413096

Virgil departed from Clusium, intending to travel by road to Volsinii, a 27.014725595999998 mile journey. 

Insert story about 413389

Virgil departed from Volsinii, intending to travel by road to Roma, a 62.636682284 mile journey. 

Insert story about 423025

Virgil departed from Roma, intending to travel by road to Tibur, a 17.629538012 mile journey. 

Insert story about 423081

Virgil departed from Tibur, intending to travel by road to Alba Fucens, a 39.645955284 mile journey. 

Insert story about 413005

Virgil departed from Alba Fucens, intending to travel by road to Corfinium, a 24.140884721 mile journey. 

Insert story about 413105

Virgil departed from Corfinium, intending to travel by road to Interpromium, a 11.139317917 mile journey. 

Insert story about 413182

Virgil departed from Interpromium, intending to travel by road to Corfinium, a 11.139317917 mile journey. 

Insert story about 413105

Virgil departed from Corfinium, intending to travel by road to Alba Fucens, a 24.140884721 mile journey. 

Insert story about 413005

Virgil departed from Alba Fucens, intending to travel by road to Corfinium, a 24.140884721 mile journey. 

Insert story about 413105

Virgil departed from Corfinium, intending to travel by road to Alba Fucens, a 24.140884721 mile journey. 

Insert story about 413005

Virgil departed from Alba Fucens, intending to travel by road to Tibur, a 39.645955284 mile journey. 

Insert story about 423081

Virgil departed from Tibur, intending to travel by road to Alba Fucens, a 39.645955284 mile journey. 

Insert story about 413005

Virgil departed from Alba Fucens, intending to travel by road to Corfinium, a 24.140884721 mile journey. 

Insert story about 413105

Virgil departed from Corfinium, intending to travel by road to Aesernia, a 43.612787748 mile journey. 

Insert story about 432652

Virgil departed from Aesernia, intending to travel by road to Bovianum, a 15.321766118000001 mile journey. 

Insert story about 432725

Virgil departed from Bovianum, intending to travel by road to Aequum Tuticum, a 38.820774596 mile journey. 

Insert story about 442452

Virgil departed from Aequum Tuticum, intending to travel by road to Bovianum, a 38.820774596 mile journey. 

Insert story about 432725

Virgil departed from Bovianum, intending to travel by road to Aesernia, a 15.321766118000001 mile journey. 

Insert story about 432652

