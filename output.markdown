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

He presses onward. The sun beats down. A breeze from an unexpected quarter cools the air. 

Insert story about 413231

Insert story about ['42.412', '12.467']

  
## Travelling by road

Virgil departed from Ocriculum, intending to travel by road to Narnia, a journey of about 8 miles. 

A grove of Minerva is hard by the road, a grove of poplar trees. Now the road is quieter. As they go up from Ocriculum, they see the ruined walls. Water has washed out the road, making for slow going. He left the city early, before the rising of the sun. 

Insert story about 413225

Insert story about ['42.52', '12.516']

  
## To Spoletium

Intending to travel by road to Spoletium, Virgil left Narnia. It was a distance of about 22 miles. 

A grove of Minerva is hard by the road, a grove of poplar trees. Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from Spoletium passed by. There is a fountain of cold water springing from the rock. The road narrows here, an orchard wall encroaching on it. Water has washed out the road, making for slow going. As they go up from Narnia, they see the ruined walls. He had set out from Narnia amidst a throng travelling the same way. 

Insert story about 413320

Insert story about ['42.745', '12.738']

  
## To Fanum Fortunae by road

Intending to travel by road to Fanum Fortunae, Virgil left Spoletium. It was at least 90 miles. 

He left the city early, before the rising of the sun. A caravan from Fanum Fortunae passed by. A cloud passes in front of the sun. An oxcart passes, loaded with grain. He had set out from Spoletium amidst a throng travelling the same way. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## Leaving Fanum Fortunae by ship

Leaving Fanum Fortunae, Virgil set out for Ariminum by ship down the coast, a distance of about 38 miles. 

The wave shuddered and gloomed.   
  
They are tossed asunder over the dreary gulf. Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
A fair harbor lies on either side of the city and the entrance is narrow. 

Insert story about 393379

Insert story about ['44.059', '12.563']

  
## After Ariminum

Virgil departed from Ariminum, intending to travel by ship down the coast to Fanum Fortunae, a distance of about 38 miles. 

A dusky shower drew up overhead carrying night and tempest. The wave shuddered and gloomed.   
  
They all have stations for their ships, each man one for himself. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## Departing from Fanum Fortunae

Leaving Fanum Fortunae, Virgil set out for Ancona by ship down the coast, at least 42 miles. 

The wave shuddered and gloomed.   
  
They are tossed asunder over the dreary gulf. Out of the clouds bursts fire fast upon fire. Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
Here they shape the thin oar-blades. 

Insert story about 413014

Insert story about ['43.616', '13.519']

  
## After Ancona

Virgil departed from Ancona, intending to travel by ship down the coast to Iader, a distance of about 107 miles. 

A dusky shower drew up overhead carrying night and tempest.   
  
Stormclouds enwrap the day, and rainy gloom blots out the sky. Out of the clouds bursts fire fast upon fire. The sails drop; they swing back to the oars.   
  
For they care not for bow or quiver, but for masts and oars of ships. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 197312

Insert story about ['44.115', '15.229']

\newpage

# Iader To Reate
  
## 48 miles to Titius (river)

From Iader to Titius (river) is at least 48 miles when travelling by ship down the coast. 

The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Black night broods on the waters. Even as he cried, the hurricane from the North struck with a roar against the sailThe shattered oars start forth. The oars are snapped. The yawning billow shows ground amid the surge, where the sea churns with sand. They hang on the wave's ridge. Piteous to see, it dashes on shoals and girdles with a sandbank.   
  
The sails drop; they swing back to the oars.   
  
Towards the deep doth stand an island, on whose jutting headlands beat the broken billows, shivered into sleet. Betwixt two rows of rocks a sylvan scene appears above, and groves for ever green. Glad at length to greet the welcome earth, the sailors leap to land. 

There was no story for None

Insert story about ['43.72', '15.86']

  
## Titius (river) to Iader by ship

Intending to travel by ship down the coast to Iader, Virgil left Titius (river). It was a distance of about 48 miles. 

A dusky shower drew up overhead carrying night and tempest. The wave shuddered and gloomed.   
  
There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 197312

Insert story about ['44.115', '15.229']

  
## After Iader

Intending to travel by road to Burnum, Virgil left Iader. It was about 40 miles away. 

A grove of Minerva is hard by the road, a grove of poplar trees. A caravan from Burnum passed by. This is a smooth road, by which many wagons were bringing wood to Burnum. His shoes are covered in dust from the road. Water has washed out the road, making for slow going. 

Insert story about 197184

Insert story about ['44.032', '15.994']

  
## 50 miles to Salona

From Burnum to Salona is at least 50 miles when travelling by road. 

Water has washed out the road, making for slow going. A cloud passes in front of the sun. This is a smooth road, by which many wagons were bringing wood to Salona. They pass a pillar on the right surmounted by a stone urn. He left the city early, before the rising of the sun. A grove of Minerva is hard by the road, a grove of poplar trees. By the road is a salt spring. The sun beats down. Workers are raising the level of the road. 

Insert story about 197488

Insert story about ['43.54', '16.483']

  
## Leaving Salona by ship

Leaving Salona, Virgil set out for Aternum by ship down the coast, a journey of about 153 miles. 

The sky all round them and all round them the deep. A dusky shower drew up overhead carrying night and tempest.   
  
Straightway the winds upturn the main, and great seas rise. Driven from our course, we go wandering on the blind waves. They sweep through the green water.   
  
Here they shape the thin oar-blades. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 413039

Insert story about ['42.465', '14.214']

  
## After Aternum

Leaving Aternum, Virgil set out for Castrum Truentinum by ship down the coast, a distance of about 38 miles. 

Straightway the winds upturn the main, and great seas rise. Driven from our course, we go wandering on the blind waves. Black night broods on the waters. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Up leaped the waves to heaven. The prow swings away and gives her side to the waves. The yawning billow shows ground amid the surge, where the sea churns with sand. They are in the wave's huge hollow. Piteous to see, it dashes on shoals and girdles with a sandbank. Before their eyes a vast sea descending strikes astern. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water.   
  
The sails drop; they swing back to the oars.   
  
Towards the deep doth stand an island, on whose jutting headlands beat the broken billows, shivered into sleet. The waters at their feet sleep hushed, and, like a curtain, frowns above, mixt with the glancing green, the darkness of the grove. A grotto is formed beneath, with mossy seats, to rest the Nereids, and exclude the heats. Down through the crannies of the living walls the crystal streams descend in murmuring falls. The sailors, worn with toils, and spent with woes, leap on the welcome land, and seek their wished-for repose. They lay their weary limbs still dripping on the sand. 

Insert story about 413074

Insert story about ['42.914', '13.904']

  
## Castrum Truentinum to Asculum by road

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a journey of about 17 miles. 

By the road is a salt spring. On the road from Castrum Truentinum to Asculum there is a village, in which there is a temple and grove. His shoes are covered in dust from the road. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 413036

Insert story about ['42.855', '13.575']

  
## Travelling by road to Reate

Leaving Asculum, Virgil set out for Reate by road, about 59 miles away. 

He had set out from Asculum amidst a throng travelling the same way. They pass a pillar on the right surmounted by a stone urn. As they go up from Asculum, they see the ruined walls. There is a fountain of cold water springing from the rock. An oxcart passes, loaded with grain. This is a smooth road, by which many wagons were bringing wood to Reate. 

Insert story about 413283

Insert story about ['42.403', '12.861']

\newpage

# Reate To Formiae
  
## Travelling by road

Leaving Reate, Virgil set out for Roma by road, a distance of about 44 miles. 

His shoes are covered in dust from the road. Workers are raising the level of the road. Now the road is quieter. There is a fountain of cold water springing from the rock. The sun beats down. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A cloud passes in front of the sun. He passes another milestone. He had set out from Reate amidst a throng travelling the same way. 

Insert story about 423025

Insert story about ['41.892', '12.486']

  
## From Roma to Ostia/Portus

Virgil departed from Roma, intending to travel on a boat heading downstream to Ostia/Portus, a distance of about 17 miles. 

Birds sing their greetings. 

Insert story about 422995

Insert story about ['41.755', '12.288']

  
## 77 miles to Tarracina

Virgil departed from Ostia/Portus, intending to travel by ship down the coast to Tarracina, a distance of about 77 miles. 

A dusky shower drew up overhead carrying night and tempest. The breezes woo the sails, and the canvas blows out to the swelling south.   
  
The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. The sails drop; they swing back to the oars.   
  
They all have stations for their ships, each man one for himself. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 433143

Insert story about ['41.291', '13.249']

  
## Travelling by ship

Virgil departed from Tarracina, intending to travel by ship down the coast to Formiae, a distance of about 24 miles. 

The sky all round them and all round them the deep. A dusky shower drew up overhead carrying night and tempest.   
  
They all have stations for their ships, each man one for himself. 

Insert story about 432839

Insert story about ['41.256', '13.606']

  
## Travelling by ship down the coast to Minturnae

Intending to travel by ship down the coast to Minturnae, Virgil left Formiae. It was a distance of about 18 miles. 

The sky all round them and all round them the deep.   
  
Here the men are busied with the tackle of their black ships, with cables and sails. 

Insert story about 432940

Insert story about ['41.242', '13.769']

  
## To Formiae

Leaving Minturnae, Virgil set out for Formiae by ship down the coast, a journey of about 18 miles. 

They spread their sails and ran over the waste sea in their hollow wood. The wave shuddered and gloomed.   
  
They all have stations for their ships, each man one for himself. 

Insert story about 432839

Insert story about ['41.256', '13.606']

  
## From Formiae to Minturnae

From Formiae to Minturnae is at least 18 miles when travelling by ship down the coast. 

The breezes woo the sails, and the canvas blows out to the swelling south.   
  
Here they shape the thin oar-blades. 

Insert story about 432940

Insert story about ['41.242', '13.769']

  
## After Minturnae

Virgil departed from Minturnae, intending to travel by ship down the coast to Formiae, about 18 miles away. 

The sky all round them and all round them the deep.   
  
The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
Here they shape the thin oar-blades. 

Insert story about 432839

Insert story about ['41.256', '13.606']

\newpage

# Formiae To Ocriculum
  
## Leaving Formiae by ship

Leaving Formiae, Virgil set out for Tarracina by ship down the coast, a journey of about 24 miles. 

The sky all round them and all round them the deep.   
  
They are tossed asunder over the dreary gulf. The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. The sails drop; they swing back to the oars.   
  
A fair harbor lies on either side of the city and the entrance is narrow. They all have stations for their ships, each man one for himself. 

Insert story about 433143

Insert story about ['41.291', '13.249']

  
## Leaving Tarracina by upriver

Leaving Tarracina, Virgil set out for Forum Appii on a boat heading upstream, a journey of about 14 miles. 

The countryside is quieter than the city. A cloud passes in front of the sun. 

There was no story for None

  
## Travelling by downstream

From Forum Appii to Tarracina is about 14 miles away when travelling on a boat heading downstream. 

He presses onward. 

Insert story about 433143

Insert story about ['41.291', '13.249']

  
## Leaving Tarracina by upriver

From Tarracina to Forum Appii is about 14 miles away when travelling on a boat heading upstream. 

He presses onward. The sun beats down. 

There was no story for None

  
## Departing from Forum Appii

From Forum Appii to Roma is a distance of about 42 miles when travelling by road. 

He had set out from Forum Appii amidst a throng travelling the same way. On the road from Forum Appii to Roma there is a village, in which there is a temple and grove. Workers are raising the level of the road. Next to the straight road that leads to Roma, there is visible a sculpted tomb. He left the city early, before the rising of the sun. This is a smooth road, by which many wagons were bringing wood to Roma. Water has washed out the road, making for slow going. As they go up from Forum Appii, they see the ruined walls. 

Insert story about 423025

Insert story about ['41.892', '12.486']

  
## To Ocriculum by upriver

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, about 64 miles away. 

The journey is more tiring than you might expect. 

Insert story about 413231

Insert story about ['42.412', '12.467']

  
## To Narnia

Virgil departed from Ocriculum, intending to travel by road to Narnia, at least 8 miles. 

A grove of Minerva is hard by the road, a grove of poplar trees. By the road is a salt spring. An oxcart passes, loaded with grain. Above the roads are ruins, among which is a cave sacred to Asclepius. Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. 

Insert story about 413225

Insert story about ['42.52', '12.516']

  
## Travelling by road

From Narnia to Ocriculum is a distance of about 8 miles when travelling by road. 

They pass a pillar on the right surmounted by a stone urn. On the road from Narnia to Ocriculum there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. There a spring wells up, and around about it is a meadow. Water has washed out the road, making for slow going. An oxcart passes, loaded with grain. Next to the straight road that leads to Ocriculum, there is visible a sculpted tomb. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 413231

Insert story about ['42.412', '12.467']

\newpage

# Ocriculum To Placentia
  
## Departing from Ocriculum

Leaving Ocriculum, Virgil set out for Narnia by road, a journey of about 8 miles. 

Above the roads are ruins, among which is a cave sacred to Asclepius. His shoes are covered in dust from the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He passes another milestone. Along the road are graves, and a cenotaph. An oxcart passes, loaded with grain. 

Insert story about 413225

Insert story about ['42.52', '12.516']

  
## From Narnia to Spoletium

From Narnia to Spoletium is about 22 miles away when travelling by road. 

There a spring wells up, and around about it is a meadow. Above the roads are ruins, among which is a cave sacred to Asclepius. A cloud passes in front of the sun. Now the road is quieter. He had set out from Narnia amidst a throng travelling the same way. 

Insert story about 413320

Insert story about ['42.745', '12.738']

  
## To Fanum Fortunae

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, a distance of about 90 miles. 

A cloud passes in front of the sun. A grove of Minerva is hard by the road, a grove of poplar trees. The road narrows here, an orchard wall encroaching on it. A caravan from Fanum Fortunae passed by. Water has washed out the road, making for slow going. There is a fountain of cold water springing from the rock. He had set out from Spoletium amidst a throng travelling the same way. By the road is a salt spring. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## Fanum Fortunae to Ariminum by ship

Leaving Fanum Fortunae, Virgil set out for Ariminum by ship down the coast, at least 38 miles. 

A dusky shower drew up overhead carrying night and tempest. The wave shuddered and gloomed.   
  
The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. They sweep through the green water.   
  
A fair harbor lies on either side of the city and the entrance is narrow. Curved ships are drawn up along the road. Here the men are busied with the tackle of their black ships, with cables and sails. 

Insert story about 393379

Insert story about ['44.059', '12.563']

  
## The journey to Faventia

Virgil departed from Ariminum, intending to travel by road to Faventia, a journey of about 38 miles. 

This is a smooth road, by which many wagons were bringing wood to Faventia. There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. The sun beats down. Next to the straight road that leads to Faventia, there is visible a sculpted tomb. 

Insert story about 393420

Insert story about ['44.286', '11.884']

  
## Leaving Faventia by road

Virgil departed from Faventia, intending to travel by road to Bononia, about 30 miles away. 

They pass a pillar on the right surmounted by a stone urn. His shoes are covered in dust from the road. Above the roads are ruins, among which is a cave sacred to Asclepius. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 393421

Insert story about ['44.495', '11.349']

  
## Departing from Bononia

Leaving Bononia, Virgil set out for a village on a military boat floating downstream, about 39 miles away. 

A cloud passes in front of the sun. 

There was no story for None

  
## Travelling on a military boat headed upstream to Placentia

Leaving a village, Virgil set out for Placentia on a military boat headed upstream, at least 140 miles. 

Birds sing their greetings. A cloud passes in front of the sun. 

Insert story about 383741

Insert story about ['45.052', '9.699']

\newpage

# Placentia To Altinum
  
## To a village by road

Leaving Placentia, Virgil set out for a village by road, at least 11 miles. 

He left the city early, before the rising of the sun. They pass a pillar on the right surmounted by a stone urn. On the road from Placentia to a village there is a village, in which there is a temple and grove. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. The road narrows here, an orchard wall encroaching on it. 

There was no story for None

  
## To Mediolanum by road

Virgil departed from a village, intending to travel by road to Mediolanum, at least 27 miles. 

As they go up from a village, they see the ruined walls. This is a smooth road, by which many wagons were bringing wood to Mediolanum. By the road is a salt spring. Now the road is quieter. 

Insert story about 383706

Insert story about ['45.464', '9.188']

  
## Travelling by road

From Mediolanum to Verona is a journey of about 101 miles when travelling by road. 

This is a smooth road, by which many wagons were bringing wood to Verona. On the road from Mediolanum to Verona there is a village, in which there is a temple and grove. Along the road are graves, and a cenotaph. The road narrows here, an orchard wall encroaching on it. There a spring wells up, and around about it is a meadow. Water has washed out the road, making for slow going. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 383816

Insert story about ['45.439', '10.994']

  
## Departing from Verona

From Verona to Patavium is at least 50 miles when travelling by road. 

The road narrows here, an orchard wall encroaching on it. A cloud passes in front of the sun. By the road is a salt spring. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. His shoes are covered in dust from the road. There a spring wells up, and around about it is a meadow. There is a fountain of cold water springing from the rock. An oxcart passes, loaded with grain. 

Insert story about 393473

Insert story about ['45.41', '11.877']

  
## To a village

Intending to travel by road to a village, Virgil left Patavium. It was about 13 miles away. 

An oxcart passes, loaded with grain. Next to the straight road that leads to a village, there is visible a sculpted tomb. A cloud passes in front of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Workers are raising the level of the road. He had set out from Patavium amidst a throng travelling the same way. 

There was no story for None

  
## Travelling by road

Leaving a village, Virgil set out for Altinum by road, at least 14 miles. 

He had set out from a village amidst a throng travelling the same way. Workers are raising the level of the road. As they go up from a village, they see the ruined walls. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. Water has washed out the road, making for slow going. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 393374

Insert story about ['45.579', '12.373']

  
## 27 miles to Brundulum

Virgil departed from Altinum, intending to travel by ship down the coast to Brundulum, a distance of about 27 miles. 

A dusky shower drew up overhead carrying night and tempest.   
  
A fair harbor lies on either side of the city and the entrance is narrow. They all have stations for their ships, each man one for himself. 

There was no story for None

Insert story about ['45.19', '12.31']

  
## The journey to Altinum

Intending to travel by ship down the coast to Altinum, Virgil left Brundulum. It was a distance of about 27 miles. 

They spread their sails and ran over the waste sea in their hollow wood. The breezes woo the sails, and the canvas blows out to the swelling south.   
  
Driven from our course, we go wandering on the blind waves. Dubious days of blind darkness we wander on the deep, nights without a star. Without delay the sailors strongly toss up the foam.   
  
For they care not for bow or quiver, but for masts and oars of ships. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 393374

Insert story about ['45.579', '12.373']

\newpage

# Altinum To Pons Drusi
  
## Altinum to Iulia Concordia by road

Virgil departed from Altinum, intending to travel by road to Iulia Concordia, at least 26 miles. 

The road narrows here, an orchard wall encroaching on it. The sun beats down. He passes another milestone. He left the city early, before the rising of the sun. Water has washed out the road, making for slow going. He had set out from Altinum amidst a throng travelling the same way. This is a smooth road, by which many wagons were bringing wood to Iulia Concordia. 

Insert story about 393441

Insert story about ['45.757', '12.844']

  
## Iulia Concordia to Aquileia by road

Intending to travel by road to Aquileia, Virgil left Iulia Concordia. It was a distance of about 26 miles. 

By the road is a salt spring. This is a smooth road, by which many wagons were bringing wood to Aquileia. Now the road is quieter. His shoes are covered in dust from the road. A caravan from Aquileia passed by. They pass a pillar on the right surmounted by a stone urn. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There is a fountain of cold water springing from the rock. 

Insert story about 187290

Insert story about ['45.768', '13.365']

  
## To Ad Tricesimum by road

Leaving Aquileia, Virgil set out for Ad Tricesimum by road, at least 28 miles. 

An oxcart passes, loaded with grain. The sun beats down. A caravan from Ad Tricesimum passed by. His shoes are covered in dust from the road. There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. By the road is a salt spring. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187259

Insert story about ['46.158', '13.216']

  
## To Aquileia by road

Leaving Ad Tricesimum, Virgil set out for Aquileia by road, at least 28 miles. 

Next to the straight road that leads to Aquileia, there is visible a sculpted tomb. Workers are raising the level of the road. A grove of Minerva is hard by the road, a grove of poplar trees. There is a fountain of cold water springing from the rock. There a spring wells up, and around about it is a meadow. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 187290

Insert story about ['45.768', '13.365']

  
## Travelling by road

Leaving Aquileia, Virgil set out for Iulia Concordia by road, about 26 miles away. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. On the road from Aquileia to Iulia Concordia there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. Along the road are graves, and a cenotaph. 

Insert story about 393441

Insert story about ['45.757', '12.844']

  
## To Tridentum

Virgil departed from Iulia Concordia, intending to travel by road to Tridentum, a journey of about 103 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He left the city early, before the rising of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. As they go up from Iulia Concordia, they see the ruined walls. This is a smooth road, by which many wagons were bringing wood to Tridentum. There is a fountain of cold water springing from the rock. 

Insert story about 383804

Insert story about ['46.067', '11.119']

  
## To Endidae by road

From Tridentum to Endidae is about 20 miles away when travelling by road. 

An oxcart passes, loaded with grain. Above the roads are ruins, among which is a cave sacred to Asclepius. He passes another milestone. Now the road is quieter. A cloud passes in front of the sun. They pass a pillar on the right surmounted by a stone urn. Water has washed out the road, making for slow going. As they go up from Tridentum, they see the ruined walls. 

Insert story about 187368

Insert story about ['46.318', '11.274']

  
## After Endidae

From Endidae to Pons Drusi is a distance of about 13 miles when travelling by road. 

There is a fountain of cold water springing from the rock. By the road is a salt spring. He had set out from Endidae amidst a throng travelling the same way. An oxcart passes, loaded with grain. A grove of Minerva is hard by the road, a grove of poplar trees. He passes another milestone. 

Insert story about 187518

Insert story about ['46.497', '11.358']

\newpage

# Pons Drusi To Brigantium
  
## To a village by road

Intending to travel by road to a village, Virgil left Pons Drusi. It was about 28 miles away. 

He passes another milestone. The sun beats down. Above the roads are ruins, among which is a cave sacred to Asclepius. This is a smooth road, by which many wagons were bringing wood to a village. Now the road is quieter. There is a fountain of cold water springing from the rock. By the road is a salt spring. He left the city early, before the rising of the sun. An oxcart passes, loaded with grain. 

There was no story for None

  
## After a village

Intending to travel by road to Veldidena, Virgil left a village. It was a journey of about 41 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Above the roads are ruins, among which is a cave sacred to Asclepius. A cloud passes in front of the sun. His shoes are covered in dust from the road. They pass a pillar on the right surmounted by a stone urn. Along the road are graves, and a cenotaph. 

Insert story about 187608

Insert story about ['47.254', '11.4']

  
## Leaving Veldidena by road

From Veldidena to a village is at least 41 miles when travelling by road. 

By the road is a salt spring. He passes another milestone. Workers are raising the level of the road. They pass a pillar on the right surmounted by a stone urn. Next to the straight road that leads to a village, there is visible a sculpted tomb. On the road from Veldidena to a village there is a village, in which there is a temple and grove. 

There was no story for None

  
## 28 miles to Pons Drusi

Virgil departed from a village, intending to travel by road to Pons Drusi, a distance of about 28 miles. 

There a spring wells up, and around about it is a meadow. His shoes are covered in dust from the road. As they go up from a village, they see the ruined walls. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. This is a smooth road, by which many wagons were bringing wood to Pons Drusi. 

Insert story about 187518

Insert story about ['46.497', '11.358']

  
## To Maiensis Statio

Intending to travel by road to Maiensis Statio, Virgil left Pons Drusi. It was at least 15 miles. 

On the road from Pons Drusi to Maiensis Statio there is a village, in which there is a temple and grove. An oxcart passes, loaded with grain. His shoes are covered in dust from the road. Now the road is quieter. There is a fountain of cold water springing from the rock. Water has washed out the road, making for slow going. Along the road are graves, and a cenotaph. This is a smooth road, by which many wagons were bringing wood to Maiensis Statio. 

There was no story for None

Insert story about ['0', '0']

  
## Departing from Maiensis Statio

Leaving Maiensis Statio, Virgil set out for Abodiacum by road, a journey of about 140 miles. 

He passes another milestone. On the road from Maiensis Statio to Abodiacum there is a village, in which there is a temple and grove. They pass a pillar on the right surmounted by a stone urn. By the road is a salt spring. A grove of Minerva is hard by the road, a grove of poplar trees. He left the city early, before the rising of the sun. A caravan from Abodiacum passed by. Workers are raising the level of the road. Water has washed out the road, making for slow going. 

Insert story about 187242

Insert story about ['47.91', '10.91']

  
## To Cambodunum

Leaving Abodiacum, Virgil set out for Cambodunum by road, a journey of about 31 miles. 

Along the road are graves, and a cenotaph. There is a fountain of cold water springing from the rock. An oxcart passes, loaded with grain. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## From Cambodunum to Brigantium

Virgil departed from Cambodunum, intending to travel by road to Brigantium, about 36 miles away. 

The road narrows here, an orchard wall encroaching on it. As they go up from Cambodunum, they see the ruined walls. Now the road is quieter. A caravan from Brigantium passed by. 

Insert story about 187325

Insert story about ['47.503', '9.747']

\newpage

# Brigantium To Aventicum
  
## 50 miles to Curia

Virgil departed from Brigantium, intending to travel by road to Curia, a distance of about 50 miles. 

Water has washed out the road, making for slow going. On the road from Brigantium to Curia there is a village, in which there is a temple and grove. A caravan from Curia passed by. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187357

Insert story about ['46.849', '9.531']

  
## Leaving Curia by road

From Curia to Comum is about 92 miles away when travelling by road. 

There is a fountain of cold water springing from the rock. Next to the straight road that leads to Comum, there is visible a sculpted tomb. There a spring wells up, and around about it is a meadow. He left the city early, before the rising of the sun. The sun beats down. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 383627

Insert story about ['45.812', '9.086']

  
## 92 miles to Curia

Virgil departed from Comum, intending to travel by road to Curia, about 92 miles away. 

An oxcart passes, loaded with grain. Along the road are graves, and a cenotaph. He left the city early, before the rising of the sun. He had set out from Comum amidst a throng travelling the same way. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. By the road is a salt spring. Next to the straight road that leads to Curia, there is visible a sculpted tomb. His shoes are covered in dust from the road. 

Insert story about 187357

Insert story about ['46.849', '9.531']

  
## To Brigantium by road

Intending to travel by road to Brigantium, Virgil left Curia. It was about 50 miles away. 

The road narrows here, an orchard wall encroaching on it. As they go up from Curia, they see the ruined walls. Next to the straight road that leads to Brigantium, there is visible a sculpted tomb. Above the roads are ruins, among which is a cave sacred to Asclepius. Now the road is quieter. Workers are raising the level of the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There a spring wells up, and around about it is a meadow. Water has washed out the road, making for slow going. 

Insert story about 187325

Insert story about ['47.503', '9.747']

  
## Brigantium to Cambodunum by road

From Brigantium to Cambodunum is at least 36 miles when travelling by road. 

A grove of Minerva is hard by the road, a grove of poplar trees. Next to the straight road that leads to Cambodunum, there is visible a sculpted tomb. An oxcart passes, loaded with grain. Workers are raising the level of the road. Along the road are graves, and a cenotaph. He passes another milestone. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## 36 miles to Brigantium

Intending to travel by road to Brigantium, Virgil left Cambodunum. It was a journey of about 36 miles. 

A caravan from Brigantium passed by. By the road is a salt spring. Next to the straight road that leads to Brigantium, there is visible a sculpted tomb. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A grove of Minerva is hard by the road, a grove of poplar trees. As they go up from Cambodunum, they see the ruined walls. On the road from Cambodunum to Brigantium there is a village, in which there is a temple and grove. Workers are raising the level of the road. There is a fountain of cold water springing from the rock. 

Insert story about 187325

Insert story about ['47.503', '9.747']

  
## Brigantium to Augusta Raurica by upstream

From Brigantium to Augusta Raurica is a distance of about 119 miles when travelling on a military boat headed upstream. 

Birds sing their greetings. He presses onward. 

Insert story about 177494

Insert story about ['47.533', '7.722']

  
## Departing from Augusta Raurica

Leaving Augusta Raurica, Virgil set out for Aventicum by road, about 58 miles away. 

Above the roads are ruins, among which is a cave sacred to Asclepius. There is a fountain of cold water springing from the rock. His shoes are covered in dust from the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. The sun beats down. 

Insert story about 177495

Insert story about ['46.88', '7.041']

\newpage

# Aventicum To Veldidena
  
## To Augusta Raurica by road

Intending to travel by road to Augusta Raurica, Virgil left Aventicum. It was at least 58 miles. 

He passes another milestone. A cloud passes in front of the sun. The sun beats down. Workers are raising the level of the road. 

Insert story about 177494

Insert story about ['47.533', '7.722']

  
## After Augusta Raurica

From Augusta Raurica to Brigantium is a journey of about 119 miles when travelling on a military boat floating downstream. 

A breeze from an unexpected quarter cools the air. No backward glances for the city left behind. The journey is more tiring than you might expect. 

Insert story about 187325

Insert story about ['47.503', '9.747']

  
## To Cambodunum by road

Virgil departed from Brigantium, intending to travel by road to Cambodunum, at least 36 miles. 

He left the city early, before the rising of the sun. On the road from Brigantium to Cambodunum there is a village, in which there is a temple and grove. This is a smooth road, by which many wagons were bringing wood to Cambodunum. They pass a pillar on the right surmounted by a stone urn. Along the road are graves, and a cenotaph. He had set out from Brigantium amidst a throng travelling the same way. Workers are raising the level of the road. The sun beats down. By the road is a salt spring. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## 31 miles to Abodiacum

From Cambodunum to Abodiacum is a distance of about 31 miles when travelling by road. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There is a fountain of cold water springing from the rock. This is a smooth road, by which many wagons were bringing wood to Abodiacum. There a spring wells up, and around about it is a meadow. Workers are raising the level of the road. Water has washed out the road, making for slow going. As they go up from Cambodunum, they see the ruined walls. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 187242

Insert story about ['47.91', '10.91']

  
## After Abodiacum

From Abodiacum to Cambodunum is about 31 miles away when travelling by road. 

The sun beats down. Now the road is quieter. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Next to the straight road that leads to Cambodunum, there is visible a sculpted tomb. The road narrows here, an orchard wall encroaching on it. Above the roads are ruins, among which is a cave sacred to Asclepius. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## After Cambodunum

From Cambodunum to Abodiacum is a journey of about 31 miles when travelling by road. 

He passes another milestone. They pass a pillar on the right surmounted by a stone urn. The road narrows here, an orchard wall encroaching on it. By the road is a salt spring. Now the road is quieter. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Workers are raising the level of the road. On the road from Cambodunum to Abodiacum there is a village, in which there is a temple and grove. His shoes are covered in dust from the road. 

Insert story about 187242

Insert story about ['47.91', '10.91']

  
## Travelling by road to Parthanum

Leaving Abodiacum, Virgil set out for Parthanum by road, a journey of about 40 miles. 

As they go up from Abodiacum, they see the ruined walls. An oxcart passes, loaded with grain. They pass a pillar on the right surmounted by a stone urn. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He passes another milestone. Now the road is quieter. Water has washed out the road, making for slow going. This is a smooth road, by which many wagons were bringing wood to Parthanum. His shoes are covered in dust from the road. 

Insert story about 187505

Insert story about ['47.492', '11.086']

  
## Parthanum to Veldidena by road

From Parthanum to Veldidena is about 32 miles away when travelling by road. 

On the road from Parthanum to Veldidena there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The sun beats down. Workers are raising the level of the road. As they go up from Parthanum, they see the ruined walls. 

Insert story about 187608

Insert story about ['47.254', '11.4']

\newpage

# Veldidena To A Village
  
## To Parthanum by road

From Veldidena to Parthanum is a journey of about 32 miles when travelling by road. 

He left the city early, before the rising of the sun. On the road from Veldidena to Parthanum there is a village, in which there is a temple and grove. Water has washed out the road, making for slow going. Next to the straight road that leads to Parthanum, there is visible a sculpted tomb. A grove of Minerva is hard by the road, a grove of poplar trees. A caravan from Parthanum passed by. 

Insert story about 187505

Insert story about ['47.492', '11.086']

  
## Travelling by road to Veldidena

From Parthanum to Veldidena is at least 32 miles when travelling by road. 

He passes another milestone. On the road from Parthanum to Veldidena there is a village, in which there is a temple and grove. As they go up from Parthanum, they see the ruined walls. There is a fountain of cold water springing from the rock. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187608

Insert story about ['47.254', '11.4']

  
## After Veldidena

Virgil departed from Veldidena, intending to travel by road to a village, about 41 miles away. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. On the road from Veldidena to a village there is a village, in which there is a temple and grove. There is a fountain of cold water springing from the rock. A caravan from a village passed by. This is a smooth road, by which many wagons were bringing wood to a village. 

There was no story for None

  
## From a village to Aguntum

Intending to travel by road to Aguntum, Virgil left a village. It was about 60 miles away. 

They pass a pillar on the right surmounted by a stone urn. On the road from a village to Aguntum there is a village, in which there is a temple and grove. Workers are raising the level of the road. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 187265

Insert story about ['46.827', '12.823']

  
## After Aguntum

From Aguntum to Iulium Carnicum is at least 33 miles when travelling by road. 

Next to the straight road that leads to Iulium Carnicum, there is visible a sculpted tomb. He left the city early, before the rising of the sun. Workers are raising the level of the road. Along the road are graves, and a cenotaph. 

Insert story about 187430

Insert story about ['46.461', '13.026']

  
## The journey to a village

Intending to travel by road to a village, Virgil left Iulium Carnicum. It was a distance of about 9 miles. 

Now the road is quieter. By the road is a salt spring. An oxcart passes, loaded with grain. Along the road are graves, and a cenotaph. He had set out from Iulium Carnicum amidst a throng travelling the same way. On the road from Iulium Carnicum to a village there is a village, in which there is a temple and grove. The sun beats down. 

There was no story for None

  
## a village to Santicum by road

Virgil departed from a village, intending to travel by road to Santicum, a distance of about 47 miles. 

A cloud passes in front of the sun. There is a fountain of cold water springing from the rock. His shoes are covered in dust from the road. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 187537

Insert story about ['46.616', '13.849']

  
## To a village

Virgil departed from Santicum, intending to travel by road to a village, a journey of about 47 miles. 

A grove of Minerva is hard by the road, a grove of poplar trees. An oxcart passes, loaded with grain. He had set out from Santicum amidst a throng travelling the same way. By the road is a salt spring. Above the roads are ruins, among which is a cave sacred to Asclepius. Next to the straight road that leads to a village, there is visible a sculpted tomb. He passes another milestone. This is a smooth road, by which many wagons were bringing wood to a village. There is a fountain of cold water springing from the rock. 

There was no story for None

\newpage

# A Village To A Village
  
## After a village

Virgil departed from a village, intending to travel by road to Santicum, about 47 miles away. 

Water has washed out the road, making for slow going. The road narrows here, an orchard wall encroaching on it. There is a fountain of cold water springing from the rock. An oxcart passes, loaded with grain. The sun beats down. They pass a pillar on the right surmounted by a stone urn. By the road is a salt spring. 

Insert story about 187537

Insert story about ['46.616', '13.849']

  
## The journey to Virunum

Virgil departed from Santicum, intending to travel by road to Virunum, a distance of about 28 miles. 

They pass a pillar on the right surmounted by a stone urn. His shoes are covered in dust from the road. Now the road is quieter. A caravan from Virunum passed by. He had set out from Santicum amidst a throng travelling the same way. As they go up from Santicum, they see the ruined walls. Workers are raising the level of the road. A grove of Minerva is hard by the road, a grove of poplar trees. He passes another milestone. 

Insert story about 197583

Insert story about ['46.703', '14.36']

  
## Travelling by downstream

Leaving Virunum, Virgil set out for Poetovio on a boat heading downstream, about 96 miles away. 

Birds sing their greetings. 

Insert story about 197446

Insert story about ['46.42', '15.87']

  
## To Mursa

Intending to travel on a military boat floating downstream to Mursa, Virgil left Poetovio. It was a distance of about 187 miles. 

The journey is more tiring than you might expect. 

Insert story about 197389

Insert story about ['45.56', '18.676']

  
## To Cibalae by road

Virgil departed from Mursa, intending to travel by road to Cibalae, a journey of about 21 miles. 

The road narrows here, an orchard wall encroaching on it. Above the roads are ruins, among which is a cave sacred to Asclepius. Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. 

Insert story about 197207

Insert story about ['45.291', '18.801']

  
## The journey to Sirmium

Virgil departed from Cibalae, intending to travel by road to Sirmium, a journey of about 46 miles. 

His shoes are covered in dust from the road. Water has washed out the road, making for slow going. There a spring wells up, and around about it is a meadow. Above the roads are ruins, among which is a cave sacred to Asclepius. The road narrows here, an orchard wall encroaching on it. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 207447

Insert story about ['44.966', '19.61']

  
## Departing from Sirmium

Intending to travel by road to a village, Virgil left Sirmium. It was a distance of about 56 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He passes another milestone. His shoes are covered in dust from the road. A cloud passes in front of the sun. Above the roads are ruins, among which is a cave sacred to Asclepius. As they go up from Sirmium, they see the ruined walls. They pass a pillar on the right surmounted by a stone urn. 

There was no story for None

  
## Leaving a village by road

From a village to a village is a distance of about 130 miles when travelling by road. 

By the road is a salt spring. There is a fountain of cold water springing from the rock. The road narrows here, an orchard wall encroaching on it. Now the road is quieter. As they go up from a village, they see the ruined walls. A grove of Minerva is hard by the road, a grove of poplar trees. Next to the straight road that leads to a village, there is visible a sculpted tomb. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The sun beats down. 

There was no story for None

\newpage

# A Village To Viminacium
  
## To Narona

Leaving a village, Virgil set out for Narona by road, a journey of about 15 miles. 

He passes another milestone. As they go up from a village, they see the ruined walls. They pass a pillar on the right surmounted by a stone urn. On the road from a village to Narona there is a village, in which there is a temple and grove. Now the road is quieter. The sun beats down. 

Insert story about 197400

Insert story about ['43.081', '17.628']

  
## 15 miles to a village

Intending to travel by road to a village, Virgil left Narona. It was a distance of about 15 miles. 

A caravan from a village passed by. On the road from Narona to a village there is a village, in which there is a temple and grove. They pass a pillar on the right surmounted by a stone urn. He had set out from Narona amidst a throng travelling the same way. This is a smooth road, by which many wagons were bringing wood to a village. He left the city early, before the rising of the sun. Now the road is quieter. Next to the straight road that leads to a village, there is visible a sculpted tomb. 

There was no story for None

  
## a village to a village by road

Virgil departed from a village, intending to travel by road to a village, about 130 miles away. 

The sun beats down. He left the city early, before the rising of the sun. This is a smooth road, by which many wagons were bringing wood to a village. His shoes are covered in dust from the road. The road narrows here, an orchard wall encroaching on it. 

There was no story for None

  
## After a village

Intending to travel by road to Domavium, Virgil left a village. It was a journey of about 18 miles. 

Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. They pass a pillar on the right surmounted by a stone urn. Water has washed out the road, making for slow going. He passes another milestone. He left the city early, before the rising of the sun. 

Insert story about 207088

Insert story about ['44.144', '19.363']

  
## To a village

Leaving Domavium, Virgil set out for a village by road, about 18 miles away. 

By the road is a salt spring. Along the road are graves, and a cenotaph. There is a fountain of cold water springing from the rock. They pass a pillar on the right surmounted by a stone urn. A caravan from a village passed by. 

There was no story for None

  
## To Sirmium by road

Virgil departed from a village, intending to travel by road to Sirmium, a distance of about 56 miles. 

There is a fountain of cold water springing from the rock. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. As they go up from a village, they see the ruined walls. 

Insert story about 207447

Insert story about ['44.966', '19.61']

  
## Travelling on a military boat floating downstream to Singidunum

Intending to travel on a military boat floating downstream to Singidunum, Virgil left Sirmium. It was a distance of about 85 miles. 

The countryside is quieter than the city. 

Insert story about 207443

Insert story about ['44.802', '20.466']

  
## After Singidunum

Leaving Singidunum, Virgil set out for Viminacium on a military boat floating downstream, at least 49 miles. 

He presses onward. A breeze from an unexpected quarter cools the air. 

Insert story about 207549

Insert story about ['44.716', '21.167']

\newpage

# Viminacium To Naissus
  
## From Viminacium to Tibiscum

From Viminacium to Tibiscum is a journey of about 96 miles when travelling by road. 

There a spring wells up, and around about it is a meadow. The road narrows here, an orchard wall encroaching on it. They pass a pillar on the right surmounted by a stone urn. His shoes are covered in dust from the road. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 207495

Insert story about ['45.459', '22.186']

  
## From Tibiscum to Viminacium

Leaving Tibiscum, Virgil set out for Viminacium by road, about 96 miles away. 

Workers are raising the level of the road. An oxcart passes, loaded with grain. On the road from Tibiscum to Viminacium there is a village, in which there is a temple and grove. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 207549

Insert story about ['44.716', '21.167']

  
## From Viminacium to Singidunum

Leaving Viminacium, Virgil set out for Singidunum on a military boat headed upstream, at least 49 miles. 

A cloud passes in front of the sun. 

Insert story about 207443

Insert story about ['44.802', '20.466']

  
## Travelling on a military boat floating downstream to Viminacium

Intending to travel on a military boat floating downstream to Viminacium, Virgil left Singidunum. It was about 49 miles away. 

The countryside is quieter than the city. 

Insert story about 207549

Insert story about ['44.716', '21.167']

  
## Travelling by road

Intending to travel by road to Horreum Margi, Virgil left Viminacium. It was a distance of about 57 miles. 

An oxcart passes, loaded with grain. The sun beats down. There a spring wells up, and around about it is a meadow. He passes another milestone. 

There was no story for None

  
## 51 miles to Naissus

Leaving Horreum Margi, Virgil set out for Naissus by road, about 51 miles away. 

A caravan from Naissus passed by. His shoes are covered in dust from the road. There is a fountain of cold water springing from the rock. By the road is a salt spring. The road narrows here, an orchard wall encroaching on it. Along the road are graves, and a cenotaph. Next to the straight road that leads to Naissus, there is visible a sculpted tomb. 

Insert story about 207303

Insert story about ['43.316', '21.894']

  
## 80 miles to Ulpiana

Virgil departed from Naissus, intending to travel by road to Ulpiana, at least 80 miles. 

On the road from Naissus to Ulpiana there is a village, in which there is a temple and grove. By the road is a salt spring. The sun beats down. A caravan from Ulpiana passed by. 

There was no story for None

Insert story about ['0', '0']

  
## To Naissus by road

Intending to travel by road to Naissus, Virgil left Ulpiana. It was a distance of about 80 miles. 

He left the city early, before the rising of the sun. As they go up from Ulpiana, they see the ruined walls. Along the road are graves, and a cenotaph. On the road from Ulpiana to Naissus there is a village, in which there is a temple and grove. A caravan from Naissus passed by. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 207303

Insert story about ['43.316', '21.894']

\newpage

# Naissus To Taliata
  
## The journey to Bononia (Moesia)

Leaving Naissus, Virgil set out for Bononia (Moesia) by road, a journey of about 76 miles. 

A caravan from Bononia (Moesia) passed by. Now the road is quieter. Water has washed out the road, making for slow going. On the road from Naissus to Bononia (Moesia) there is a village, in which there is a temple and grove. He passes another milestone. The sun beats down. 

Insert story about 206975

Insert story about ['43.993', '22.876']

  
## Bononia (Moesia) to Taliata by road

From Bononia (Moesia) to Taliata is a distance of about 58 miles when travelling by road. 

Next to the straight road that leads to Taliata, there is visible a sculpted tomb. As they go up from Bononia (Moesia), they see the ruined walls. Water has washed out the road, making for slow going. Along the road are graves, and a cenotaph. He left the city early, before the rising of the sun. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 207485

Insert story about ['44.444', '22.144']

  
## 58 miles to Bononia (Moesia)

Leaving Taliata, Virgil set out for Bononia (Moesia) by road, about 58 miles away. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. An oxcart passes, loaded with grain. There a spring wells up, and around about it is a meadow. As they go up from Taliata, they see the ruined walls. A caravan from Bononia (Moesia) passed by. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 206975

Insert story about ['43.993', '22.876']

  
## After Bononia (Moesia)

Virgil departed from Bononia (Moesia), intending to travel by road to Taliata, a journey of about 58 miles. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There is a fountain of cold water springing from the rock. On the road from Bononia (Moesia) to Taliata there is a village, in which there is a temple and grove. There a spring wells up, and around about it is a meadow. Next to the straight road that leads to Taliata, there is visible a sculpted tomb. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 207485

Insert story about ['44.444', '22.144']

  
## To Drobeta by road

Intending to travel by road to Drobeta, Virgil left Taliata. It was a distance of about 35 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The sun beats down. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. A cloud passes in front of the sun. A caravan from Drobeta passed by. 

Insert story about 207100

Insert story about ['44.636', '22.66']

  
## Travelling by road

Intending to travel by road to Taliata, Virgil left Drobeta. It was at least 35 miles. 

His shoes are covered in dust from the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There a spring wells up, and around about it is a meadow. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 207485

Insert story about ['44.444', '22.144']

  
## Travelling on a military boat floating downstream to Dierna

Virgil departed from Taliata, intending to travel on a military boat floating downstream to Dierna, a journey of about 22 miles. 

A cloud passes in front of the sun. 

Insert story about 207078

Insert story about ['44.725', '22.396']

  
## Departing from Dierna

Virgil departed from Dierna, intending to travel on a boat heading upstream to Taliata, about 22 miles away. 

The countryside is quieter than the city. A breeze from an unexpected quarter cools the air. He presses onward. 

Insert story about 207485

Insert story about ['44.444', '22.144']

\newpage

# Taliata To Dyrrhachium
  
## To Bononia (Moesia)

Leaving Taliata, Virgil set out for Bononia (Moesia) by road, a journey of about 58 miles. 

Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. The road narrows here, an orchard wall encroaching on it. The sun beats down. An oxcart passes, loaded with grain. By the road is a salt spring. He had set out from Taliata amidst a throng travelling the same way. 

Insert story about 206975

Insert story about ['43.993', '22.876']

  
## Bononia (Moesia) to Naissus by road

Virgil departed from Bononia (Moesia), intending to travel by road to Naissus, a journey of about 76 miles. 

There is a fountain of cold water springing from the rock. Along the road are graves, and a cenotaph. On the road from Bononia (Moesia) to Naissus there is a village, in which there is a temple and grove. His shoes are covered in dust from the road. Next to the straight road that leads to Naissus, there is visible a sculpted tomb. 

Insert story about 207303

Insert story about ['43.316', '21.894']

  
## Leaving Naissus by road

Leaving Naissus, Virgil set out for Serdica by road, a distance of about 92 miles. 

The sun beats down. Above the roads are ruins, among which is a cave sacred to Asclepius. There is a fountain of cold water springing from the rock. A grove of Minerva is hard by the road, a grove of poplar trees. He left the city early, before the rising of the sun. A cloud passes in front of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. On the road from Naissus to Serdica there is a village, in which there is a temple and grove. As they go up from Naissus, they see the ruined walls. 

Insert story about 207439

Insert story about ['42.723', '23.343']

  
## After Serdica

Intending to travel by road to Stobi, Virgil left Serdica. It was a distance of about 125 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. They pass a pillar on the right surmounted by a stone urn. This is a smooth road, by which many wagons were bringing wood to Stobi. A caravan from Stobi passed by. On the road from Serdica to Stobi there is a village, in which there is a temple and grove. The sun beats down. 

Insert story about 491731

Insert story about ['41.531', '21.978']

  
## Departing from Stobi

Intending to travel by road to Heraklea, Virgil left Stobi. It was about 54 miles away. 

On the road from Stobi to Heraklea there is a village, in which there is a temple and grove. The road narrows here, an orchard wall encroaching on it. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Now the road is quieter. 

Insert story about 481861

Insert story about ['41.032', '21.336']

  
## Travelling by road to a village

Leaving Heraklea, Virgil set out for a village by road, a journey of about 109 miles. 

Workers are raising the level of the road. Water has washed out the road, making for slow going. There a spring wells up, and around about it is a meadow. A cloud passes in front of the sun. A caravan from a village passed by. He left the city early, before the rising of the sun. As they go up from Heraklea, they see the ruined walls. The road narrows here, an orchard wall encroaching on it. 

There was no story for None

  
## a village to Apollonia (Epirus) by road

Intending to travel by road to Apollonia (Epirus), Virgil left a village. It was at least 23 miles. 

The road narrows here, an orchard wall encroaching on it. This is a smooth road, by which many wagons were bringing wood to Apollonia (Epirus). Water has washed out the road, making for slow going. There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from Apollonia (Epirus) passed by. 

There was no story for None

Insert story about ['40.77', '19.43']

  
## Apollonia (Epirus) to Dyrrhachium by ship

Intending to travel by ship down the coast to Dyrrhachium, Virgil left Apollonia (Epirus). It was at least 42 miles. 

The ship held the high seas, no land yet appearing. The sky all round them and all round them the deep.   
  
They all have stations for their ships, each man one for himself. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 481818

Insert story about ['41.316', '19.45']

\newpage
