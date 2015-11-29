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

Lastly, that tradition of magic lead the much-neglected Avram Davidson to pen a novel with Vergil Magus as the magician-protagonist. My own pseudo-Virgil is a humble tribute, a machine homunculus librarian of forgotten texts.



Isaac Karth 

2015-11-28 

\newpage

## Technical Notes 

The book generator is a Python program that outputs a Markdown text file designed to be converted into PDF form via Pandoc. 


~~~
pandoc output.markdown -S --normalize --toc \
-o via_appia_test.pdf --latex-engine=xelatex \
--template novel_template.latex \
--variable otherlangs=polutonikogreek,greek \
--variable lang="english" -V geometry:paperwidth=5.5in \
-V geometry:paperheight=8.25in -V geometry:margin=.9in \
-V geometry:inner=1.0in -V geometry:outer=0.5in \
-V fontfamily:"DejaVu Serif" -V linestretch:1.2 \
-V documentclass=book
~~~


\newpage
#Virgil's Commonplace Book 

\newpage
    Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a 64.936997726 mile journey. 

Insert story about 413231

Insert story about ['42.412', '12.467']

Virgil departed from Ocriculum, intending to travel by road to Narnia, a 8.118212115 mile journey. 

Insert story about 413225

Insert story about ['42.52', '12.516']

Virgil departed from Narnia, intending to travel by road to Spoletium, a 22.863967316 mile journey. 

Insert story about 413320

Insert story about ['42.745', '12.738']

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, a 90.170252665 mile journey. 

Insert story about 413129

Insert story about ['43.845', '13.017']

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ariminum, a 38.157771739 mile journey. 

Insert story about 393379

Insert story about ['44.059', '12.563']

Virgil departed from Ariminum, intending to travel by ship down the coast to Fanum Fortunae, a 38.157771739 mile journey. 

Insert story about 413129

Insert story about ['43.845', '13.017']

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ancona, a 42.411056234 mile journey. 

Insert story about 413014

Insert story about ['43.616', '13.519']

Virgil departed from Ancona, intending to travel by ship down the coast to Iader, a 107.75815881999999 mile journey. 

Insert story about 197312

Insert story about ['44.115', '15.229']

Virgil departed from Iader, intending to travel by ship down the coast to Titius (river), a 48.512298083 mile journey. 

There was no story for None

Insert story about ['43.72', '15.86']

Virgil departed from Titius (river), intending to travel by ship down the coast to Iader, a 48.512298083 mile journey. 

Insert story about 197312

Insert story about ['44.115', '15.229']

Virgil departed from Iader, intending to travel by road to Burnum, a 40.332570239000006 mile journey. 

Insert story about 197184

Insert story about ['44.032', '15.994']

Virgil departed from Burnum, intending to travel by road to Salona, a 50.36833326 mile journey. 

Insert story about 197488

Insert story about ['43.54', '16.483']

Virgil departed from Salona, intending to travel by ship down the coast to Aternum, a 153.083445044 mile journey. 

Insert story about 413039

Insert story about ['42.465', '14.214']

Virgil departed from Aternum, intending to travel by ship down the coast to Castrum Truentinum, a 38.822017338 mile journey. 

Insert story about 413074

Insert story about ['42.914', '13.904']

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a 17.434427518 mile journey. 

Insert story about 413036

Insert story about ['42.855', '13.575']

Virgil departed from Asculum, intending to travel by road to Reate, a 59.120965166 mile journey. 

Insert story about 413283

Insert story about ['42.403', '12.861']

Virgil departed from Reate, intending to travel by road to Roma, a 44.475872067 mile journey. 

Insert story about 423025

Insert story about ['41.892', '12.486']

Virgil departed from Roma, intending to travel on a boat heading downstream to Ostia/Portus, a 17.919718269 mile journey. 

Insert story about 422995

Insert story about ['41.755', '12.288']

Virgil departed from Ostia/Portus, intending to travel by ship down the coast to Tarracina, a 77.959069773 mile journey. 

Insert story about 433143

Insert story about ['41.291', '13.249']

Virgil departed from Tarracina, intending to travel by ship down the coast to Formiae, a 24.815072256 mile journey. 

Insert story about 432839

Insert story about ['41.256', '13.606']

Virgil departed from Formiae, intending to travel by ship down the coast to Minturnae, a 18.833133639 mile journey. 

Insert story about 432940

Insert story about ['41.242', '13.769']

Virgil departed from Minturnae, intending to travel by ship down the coast to Formiae, a 18.833133639 mile journey. 

Insert story about 432839

Insert story about ['41.256', '13.606']

Virgil departed from Formiae, intending to travel by ship down the coast to Minturnae, a 18.833133639 mile journey. 

Insert story about 432940

Insert story about ['41.242', '13.769']

Virgil departed from Minturnae, intending to travel by ship down the coast to Formiae, a 18.833133639 mile journey. 

Insert story about 432839

Insert story about ['41.256', '13.606']

Virgil departed from Formiae, intending to travel by ship down the coast to Tarracina, a 24.815072256 mile journey. 

Insert story about 433143

Insert story about ['41.291', '13.249']

Virgil departed from Tarracina, intending to travel on a boat heading upstream to Forum Appii, a 14.712822538000001 mile journey. 

There was no story for None

Virgil departed from Forum Appii, intending to travel on a boat heading downstream to Tarracina, a 14.712822538000001 mile journey. 

Insert story about 433143

Insert story about ['41.291', '13.249']

Virgil departed from Tarracina, intending to travel on a boat heading upstream to Forum Appii, a 14.712822538000001 mile journey. 

There was no story for None

Virgil departed from Forum Appii, intending to travel by road to Roma, a 42.639720762 mile journey. 

Insert story about 423025

Insert story about ['41.892', '12.486']

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a 64.936997726 mile journey. 

Insert story about 413231

Insert story about ['42.412', '12.467']

Virgil departed from Ocriculum, intending to travel by road to Narnia, a 8.118212115 mile journey. 

Insert story about 413225

Insert story about ['42.52', '12.516']

Virgil departed from Narnia, intending to travel by road to Ocriculum, a 8.118212115 mile journey. 

Insert story about 413231

Insert story about ['42.412', '12.467']

Virgil departed from Ocriculum, intending to travel by road to Narnia, a 8.118212115 mile journey. 

Insert story about 413225

Insert story about ['42.52', '12.516']

Virgil departed from Narnia, intending to travel by road to Spoletium, a 22.863967316 mile journey. 

Insert story about 413320

Insert story about ['42.745', '12.738']

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, a 90.170252665 mile journey. 

Insert story about 413129

Insert story about ['43.845', '13.017']

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ariminum, a 38.157771739 mile journey. 

Insert story about 393379

Insert story about ['44.059', '12.563']

Virgil departed from Ariminum, intending to travel by road to Faventia, a 38.639334264 mile journey. 

Insert story about 393420

Insert story about ['44.286', '11.884']

Virgil departed from Faventia, intending to travel by road to Bononia, a 30.18620318 mile journey. 

Insert story about 393421

Insert story about ['44.495', '11.349']

Virgil departed from Bononia, intending to travel on a military boat downstream to the countryside, a 39.472592775 mile journey. 

There was no story for None

Virgil departed from the countryside, intending to travel on a military boat headed upstream to Placentia, a 140.85859199 mile journey. 

Insert story about 383741

Insert story about ['45.052', '9.699']

