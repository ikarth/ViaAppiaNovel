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

The book generator that produced this novel is a Python program that outputs a Markdown text file designed to be converted into PDF form via Pandoc. The source code for the NaNoGenMo version can be found at https://github.com/ikarth/ViaAppiaNovel in a git repository. 


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

This copy was generated \today, with seeds of 753 and 3468.


The book generator uses data from the Perseus Digital Library, the Pelagios Project, the Pleiades Project, and ORBIS: The Stanford Geospatial Network Model of the Roman World.





\cleardoublepage


# Roma To Iader
  
## After Roma

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, about 64 miles away. 

The journey is more tiring than you might expect. By the gate of Ocriculum, these words were carved: Philoda/mus Ca/sianus / serv(u)s publi/cus fecit Fu/fia curavit. He presses onward. 

Insert story about 413231

Insert story about ['42.412', '12.467']

  
## Leaving Ocriculum By Road

Leaving Ocriculum, Virgil set out for Narnia by road, about 8 miles away. 

The road narrows here, an orchard wall encroaching on it. A grove of Minerva is hard by the road, a grove of poplar trees. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. An oxcart passes, loaded with grain. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There a spring wells up, and around about it is a meadow. 

Insert story about 413225

Insert story about ['42.52', '12.516']

  
## 22 Miles To Spoletium

Virgil departed from Narnia, intending to travel by road to Spoletium, a journey of about 22 miles. 

They pass a pillar on the right surmounted by a stone urn. The sun beats down. On the road from Narnia to Spoletium there is a village, in which there is a temple and grove. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 413320

Insert story about ['42.745', '12.738']

  
## Travelling By Road

From Spoletium to Fanum Fortunae is at least 90 miles when travelling by road. 

An oxcart passes, loaded with grain. On the road from Spoletium to Fanum Fortunae there is a village, in which there is a temple and grove. A caravan from Fanum Fortunae passed by. Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. Workers are raising the level of the road. Next to the straight road that leads to Fanum Fortunae, there is visible a sculpted tomb. There is a fountain of cold water springing from the rock. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## The Journey To Ariminum

Leaving Fanum Fortunae, Virgil set out for Ariminum by ship down the coast, a journey of about 38 miles. 

Straightway the winds upturn the main, and great seas rise. All nature, big with instant ruin, frowned destruction. The oars are snapped. Round swings the prow, and lets the waters sweep the broadside. Dark swells the sandy tide. Piteous to see, it dashes on shoals and girdles with a sandbank. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl.   
  
The sails drop; they swing back to the oars.   
  
In a far retreat there lies a haven. Down through the crannies of the living walls the crystal streams descend in murmuring falls. 

Insert story about 393379

Insert story about ['44.059', '12.563']

  
## The Journey To Fanum Fortunae

From Ariminum to Fanum Fortunae is at least 38 miles when travelling by ship down the coast. 

The wave shuddered and gloomed.   
  
Stormclouds enwrap the day, and rainy gloom blots out the sky. The sails drop; they swing back to the oars.   
  
A fair harbor lies on either side of the city and the entrance is narrow. Here they shape the thin oar-blades. For they care not for bow or quiver, but for masts and oars of ships. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## After Fanum Fortunae

Intending to travel by ship down the coast to Ancona, Virgil left Fanum Fortunae. It was at least 42 miles. 

They spread their sails and ran over the waste sea in their hollow wood. The ship held the high seas, no land yet appearing.   
  
A fair harbor lies on either side of the city and the entrance is narrow. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. 

Insert story about 413014

Insert story about ['43.616', '13.519']

  
## The Journey To Iader

Leaving Ancona, Virgil set out for Iader by ship down the coast, at least 107 miles. 

Straightway the winds upturn the main, and great seas rise. Stormclouds enwrap the day, and rainy gloom blots out the sky. Then comes the creak of cables and the cries of seamen. The oars are snapped. They hang on the wave's ridge. Onward comes a mountain heap of billows, gaunt, abrupt. They are horsed astride a surge's crest, rocking pendent over the deep. Rocks amid the waves, a vast reef banking the sea. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water.   
  
Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
In a far retreat there lies a haven. Towards the deep doth stand an island, on whose jutting headlands beat the broken billows, shivered into sleet. Two towering crags, twin giants, guard the cove, and threat the skies. A grotto is formed beneath, with mossy seats, to rest the Nereids, and exclude the heats. They lay their weary limbs still dripping on the sand. 

Insert story about 197312

Insert story about ['44.115', '15.229']

\newpage

# Iader To Reate
  
## To Titius (River)

Leaving Iader, Virgil set out for Titius (river) by ship down the coast, about 48 miles away. 

A dusky shower drew up overhead carrying night and tempest.   
  
The harbor of Titius (river) came into view over the horizon. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. For they care not for bow or quiver, but for masts and oars of ships. 

There was no story for None

Insert story about ['43.72', '15.86']

  
## To Iader

Leaving Titius (river), Virgil set out for Iader by ship down the coast, a distance of about 48 miles. 

They spread their sails and ran over the waste sea in their hollow wood.   
  
The harbor of Iader came into view over the horizon. They beheld the harbor of Iader with gladness. They all have stations for their ships, each man one for himself. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 197312

Insert story about ['44.115', '15.229']

  
## After Iader

Leaving Iader, Virgil set out for Burnum by road, a journey of about 40 miles. 

Above the roads are ruins, among which is a cave sacred to Asclepius. His shoes are covered in dust from the road. A grove of Minerva is hard by the road, a grove of poplar trees. As they go up from Iader, they see the ruined walls. On the road from Iader to Burnum there is a village, in which there is a temple and grove. This is a smooth road, by which many wagons were bringing wood to Burnum. He had set out from Iader amidst a throng travelling the same way. The road narrows here, an orchard wall encroaching on it. Water has washed out the road, making for slow going. 

Insert story about 197184

Insert story about ['44.032', '15.994']

  
## After Burnum

Leaving Burnum, Virgil set out for Salona by road, a journey of about 50 miles. 

They pass a pillar on the right surmounted by a stone urn. As they go up from Burnum, they see the ruined walls. A grove of Minerva is hard by the road, a grove of poplar trees. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. They passed by an inscription that read: $](?) / [- - -]Ϛ(?)II / [&. 

Insert story about 197488

Insert story about ['43.54', '16.483']

  
## The Journey To Aternum

Virgil departed from Salona, intending to travel by ship down the coast to Aternum, about 153 miles away. 

The sky all round them and all round them the deep.   
  
Here the men are busied with the tackle of their black ships, with cables and sails. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 413039

Insert story about ['42.465', '14.214']

  
## Departing From Aternum

Intending to travel by ship down the coast to Castrum Truentinum, Virgil left Aternum. It was a journey of about 38 miles. 

The ship held the high seas, no land yet appearing.   
  
Out of the clouds bursts fire fast upon fire. Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
The harbor of Castrum Truentinum came into view over the horizon. Curved ships are drawn up along the road. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 413074

Insert story about ['42.914', '13.904']

  
## After Castrum Truentinum

Intending to travel by road to Asculum, Virgil left Castrum Truentinum. It was at least 17 miles. 

He had set out from Castrum Truentinum amidst a throng travelling the same way. By the road is a salt spring. There a spring wells up, and around about it is a meadow. They pass a pillar on the right surmounted by a stone urn. Workers are raising the level of the road. The sun beats down. There is a fountain of cold water springing from the rock. On the road from Castrum Truentinum to Asculum there is a village, in which there is a temple and grove. As they go up from Castrum Truentinum, they see the ruined walls. 

Insert story about 413036

Insert story about ['42.855', '13.575']

  
## To Reate

Intending to travel by road to Reate, Virgil left Asculum. It was a journey of about 59 miles. 

There is a fountain of cold water springing from the rock. As they go up from Asculum, they see the ruined walls. Now the road is quieter. He left the city early, before the rising of the sun. 

Insert story about 413283

Insert story about ['42.403', '12.861']

\newpage
