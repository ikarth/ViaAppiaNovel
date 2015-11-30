% Virgil's Commonplace Book
% Isaac Karth

## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These texts were not always attributed to the original source. Lacking the modern concept of plagiarism (and our post-printing-press system of uniform citations) writers sometimes come off as careless to modern sensibilities. Quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.
 
In a way, this reuse is fortunate: many texts from the Classical period only exist in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.

Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. The closest literary ancedents of NaNoGenMo--Dada and Oulipo--have often explored similar sampling approaches. Kathryn Hume has suggested that technical constratints have lead NaNoGenMo to "align itself with poetics of recontextualization and reassembly."^[Hume, Kathryn. "NaNoGenMo: Dada 2.0". URL:\url{http://arcade.stanford.edu/blogs/nanogenmo-dada-20}. Accessed: 2015-11-28. (Archived by WebCite® at \url{http://www.webcitation.org/6dNl9xpbY})] 

NaNoGenMo has included other approaches, such as the concrete poetry in thricedotted's _The Seeker_, or the way structurally-plotted works like _Hannah and The Twelve-Disk Tower of Hanoi_ evoke the chessboard constraints of _Life a User's Manual_ or _Through the Looking Glass_. But there is an undeniable strand of appropreation as we teach our machines to imitate their human creators. Still, that's no reason to neglect giving credit, so this book attempts to cite the sources for the texts it borrows.

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

This copy was generated \today, with seeds of 753 and 3468



\cleardoublepage

# Roma to Ancona

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a journey of about 64 miles. 

Black night broods on the waters. All nature, big with instant ruin, frowned destruction. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. Piteous to see, it dashes on shoals and girdles with a sandbank. 

Insert story about 413231

Insert story about ['42.412', '12.467']

Intending to travel by road to Narnia, Virgil left Ocriculum. It was about 8 miles away. 

Then comes the creak of cables and the cries of seamen. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Down in a heap comes a broken mountain of water. They hang on the wave's ridge. The south wind catches and hurls a ship on hidden rocks. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. Piteous to see, it dashes on shoals and girdles with a sandbank. Before their eyes a vast sea descending strikes astern. 

Insert story about 413225

Insert story about ['42.52', '12.516']

Intending to travel by road to Spoletium, Virgil left Narnia. It was a journey of about 22 miles. 

Then comes the creak of cables and the cries of seamen. Black night broods on the waters. The prow swings away and gives her side to the waves. Down in a heap comes a broken mountain of water. They hang on the wave's ridge. The east wind forces a ship from the deep into shallows and quicksands. The helmsman is dashed away and rolled forward headlong. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 413320

Insert story about ['42.745', '12.738']

Leaving Spoletium, Virgil set out for Fanum Fortunae by road, a journey of about 90 miles. 

Then comes the creak of cables and the cries of seamen. Black night broods on the waters. All around from pole to pole the rattling peals resound. Frequent flashes light the lurid air. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Down in a heap comes a broken mountain of water. The yawning billow shows ground amid the surge, where the sea churns with sand. They hang on the wave's ridge. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 413129

Insert story about ['43.845', '13.017']

From Fanum Fortunae to Ariminum is about 38 miles away when travelling by ship down the coast. 

Then comes the creak of cables and the cries of seamen. Frequent flashes light the lurid air. All nature, big with instant ruin, frowned destruction. The oars are snapped. Down in a heap comes a broken mountain of water. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. Before their eyes a vast sea descending strikes astern. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 393379

Insert story about ['44.059', '12.563']

Virgil departed from Ariminum, intending to travel by ship down the coast to Fanum Fortunae, about 38 miles away. 

The oars are snapped. The yawning billow shows ground amid the surge, where the sea churns with sand. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. 

Insert story about 413129

Insert story about ['43.845', '13.017']

Leaving Fanum Fortunae, Virgil set out for Ancona by ship down the coast, a distance of about 42 miles. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. All nature, big with instant ruin, frowned destruction. Down in a heap comes a broken mountain of water. The east wind forces a ship from the deep into shallows and quicksands. Piteous to see, it dashes on shoals and girdles with a sandbank. The helmsman is dashed away and rolled forward headlong. 

Insert story about 413014

Insert story about ['43.616', '13.519']

From Ancona to Iader is a journey of about 107 miles when travelling by ship down the coast. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Black night broods on the waters. They hang on the wave's ridge. 

\newpage
