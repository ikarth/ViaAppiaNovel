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

The journey is more tiring than you might expect. By the gate of Ocriculum, these words were carved: Est in Arcadia Ego. He presses onward. 

Insert story about 413231

Insert story about ['42.412', '12.467']

  
## To Narnia

Intending to travel by road to Narnia, Virgil left Ocriculum. It was a journey of about 8 miles. 

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
  
The harbor of Fanum Fortunae came into view over the horizon. The people of Fanum Fortunae all have stations for their ships, each man one for himself. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## After Fanum Fortunae

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ancona, a distance of about 42 miles. 

The breezes woo the sails, and the canvas blows out to the swelling south.   
  
A fair harbor lies on either side of the city and the entrance is narrow. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 413014

Insert story about ['43.616', '13.519']

  
## To Iader By Ship

Virgil departed from Ancona, intending to travel by ship down the coast to Iader, a distance of about 107 miles. 

They spread their sails and ran over the waste sea in their hollow wood. The ship held the high seas, no land yet appearing.   
  
They are tossed asunder over the dreary gulf. Stormclouds enwrap the day, and rainy gloom blots out the sky. They sweep through the green water.   
  
They beheld the harbor of Iader with gladness. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. Here the men are busied with the tackle of their black ships, with cables and sails. 

Insert story about 197312

Insert story about ['44.115', '15.229']

\newpage

# Iader To Reate
  
## Travelling By Ship Down The Coast To Titius (River)

Virgil departed from Iader, intending to travel by ship down the coast to Titius (river), at least 48 miles. 

They spread their sails and ran over the waste sea in their hollow wood. The wave shuddered and gloomed.   
  
A fair harbor lies on either side of the city and the entrance is narrow. Curved ships are drawn up along the road. 

There was no story for None

Insert story about ['43.72', '15.86']

  
## To Iader

Virgil departed from Titius (river), intending to travel by ship down the coast to Iader, about 48 miles away. 

A dusky shower drew up overhead carrying night and tempest.   
  
They beheld the harbor of Iader with gladness. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 197312

Insert story about ['44.115', '15.229']

  
## 40 Miles To Burnum

From Iader to Burnum is at least 40 miles when travelling by road. 

On the road from Iader to Burnum there is a village, in which there is a temple and grove. Along the road are graves, and a cenotaph. By the road is a salt spring. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 197184

Insert story about ['44.032', '15.994']

  
## Leaving Burnum By Road

Leaving Burnum, Virgil set out for Salona by road, at least 50 miles. 

This is a smooth road, by which many wagons were bringing wood to Salona. They pass a pillar on the right surmounted by a stone urn. A caravan from Salona passed by. Est in Arcadia Ego was carved into the stone. 

Insert story about 197488

Insert story about ['43.54', '16.483']

  
## Departing From Salona

Intending to travel by ship down the coast to Aternum, Virgil left Salona. It was a journey of about 153 miles. 

They are tossed asunder over the dreary gulf. Stormclouds enwrap the day, and rainy gloom blots out the sky. All around from pole to pole the rattling peals resound. All nature, big with instant ruin, frowned destruction. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Round swings the prow, and lets the waters sweep the broadside. They hang on the wave's ridge. They are in the wave's huge hollow. Yawning wide, the wave lays bare the ground below. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl.   
  
The sails drop; they swing back to the oars.   
  
Two towering crags, twin giants, guard the cove, and threat the skies. The waters at their feet sleep hushed, and, like a curtain, frowns above, mixt with the glancing green, the darkness of the grove. A grotto is formed beneath, with mossy seats, to rest the Nereids, and exclude the heats. They lay their weary limbs still dripping on the sand. 

Insert story about 413039

Insert story about ['42.465', '14.214']

  
## To Castrum Truentinum

Leaving Aternum, Virgil set out for Castrum Truentinum by ship down the coast, a journey of about 38 miles. 

They spread their sails and ran over the waste sea in their hollow wood.   
  
The harbor of Castrum Truentinum came into view over the horizon. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. Here they shape the thin oar-blades. 

Insert story about 413074

Insert story about ['42.914', '13.904']

  
## Travelling By Road To Asculum

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, at least 17 miles. 

He had set out from Castrum Truentinum amidst a throng travelling the same way. By the road is a salt spring. There a spring wells up, and around about it is a meadow. They pass a pillar on the right surmounted by a stone urn. Workers are raising the level of the road. The sun beats down. There is a fountain of cold water springing from the rock. On the road from Castrum Truentinum to Asculum there is a village, in which there is a temple and grove. As they go up from Castrum Truentinum, they see the ruined walls. 

Insert story about 413036

Insert story about ['42.855', '13.575']

  
## To Reate

Intending to travel by road to Reate, Virgil left Asculum. It was a journey of about 59 miles. 

There is a fountain of cold water springing from the rock. As they go up from Asculum, they see the ruined walls. Now the road is quieter. He left the city early, before the rising of the sun. 

Insert story about 413283

Insert story about ['42.403', '12.861']

\newpage

# Reate To Formiae
  
## From Reate To Roma

Virgil departed from Reate, intending to travel by road to Roma, about 44 miles away. 

Next to the straight road that leads to Roma, there is visible a sculpted tomb. A grove of Minerva is hard by the road, a grove of poplar trees. A caravan from Roma passed by. On the road from Reate to Roma there is a village, in which there is a temple and grove. The road narrows here, an orchard wall encroaching on it. There is a fountain of cold water springing from the rock. A cloud passes in front of the sun. 

Insert story about 423025

Insert story about ['41.892', '12.486']

  
## Travelling By River

Leaving Roma, Virgil set out for Ostia/Portus on a boat heading downstream, at least 17 miles. 

The sun beats down. Birds sing their greetings. 

Insert story about 422995

Insert story about ['41.755', '12.288']

  
## From Ostia/Portus To Tarracina

Leaving Ostia/Portus, Virgil set out for Tarracina by ship down the coast, at least 77 miles. 

The sky all round them and all round them the deep.   
  
Out of the clouds bursts fire fast upon fire. Driven from our course, we go wandering on the blind waves. They sweep through the green water.   
  
A fair harbor lies on either side of the city and the entrance is narrow. Curved ships are drawn up along the road. Here they shape the thin oar-blades. 

Insert story about 433143

Insert story about ['41.291', '13.249']

  
## Travelling By Ship Down The Coast To Formiae

From Tarracina to Formiae is a journey of about 24 miles when travelling by ship down the coast. 

The ship held the high seas, no land yet appearing. A dusky shower drew up overhead carrying night and tempest.   
  
A fair harbor lies on either side of the city and the entrance is narrow. The people of Formiae all have stations for their ships, each man one for himself. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 432839

Insert story about ['41.256', '13.606']

  
## 18 Miles To Minturnae

Leaving Formiae, Virgil set out for Minturnae by ship down the coast, a journey of about 18 miles. 

The wave shuddered and gloomed. The breezes woo the sails, and the canvas blows out to the swelling south.   
  
They beheld the harbor of Minturnae with gladness. For they care not for bow or quiver, but for masts and oars of ships. 

Insert story about 432940

Insert story about ['41.242', '13.769']

  
## To Formiae

Virgil departed from Minturnae, intending to travel by ship down the coast to Formiae, a distance of about 18 miles. 

Straightway the winds upturn the main, and great seas rise. All around from pole to pole the rattling peals resound. All nature, big with instant ruin, frowned destruction. The oars are snapped. The yawning billow shows ground amid the surge, where the sea churns with sand. They are in the wave's huge hollow.   
  
Without delay the sailors strongly toss up the foam.   
  
Within a long recess there lies a bay: an island shades it from the rolling sea and forms a port secure for ships to ride. Broke by the jutting land, on either side, in double streams the briny waters glide. Down through the crannies of the living walls the crystal streams descend in murmuring falls. Ships within this happy harbor meet, the thin remainders of the scattered fleet. The sailors, worn with toils, and spent with woes, leap on the welcome land, and seek their wished-for repose. 

Insert story about 432839

Insert story about ['41.256', '13.606']

  
## Departing From Formiae

Leaving Formiae, Virgil set out for Minturnae by ship down the coast, a distance of about 18 miles. 

The sky all round them and all round them the deep. The wave shuddered and gloomed.   
  
Driven from our course, we go wandering on the blind waves. The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. They sweep through the green water.   
  
The harbor of Minturnae came into view over the horizon. Curved ships are drawn up along the road. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

Insert story about 432940

Insert story about ['41.242', '13.769']

  
## To Formiae

Virgil departed from Minturnae, intending to travel by ship down the coast to Formiae, at least 18 miles. 

They are tossed asunder over the dreary gulf. Out of the clouds bursts fire fast upon fire. Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Frequent flashes light the lurid air. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Rocks amid the waves, a vast reef banking the sea. The helmsman is dashed away and rolled forward headlong. Each loosened side through many a gaping seam lets in the baleful tide.   
  
Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
Broke by the jutting land, on either side, in double streams the briny waters glide. Betwixt two rows of rocks a sylvan scene appears above, and groves for ever green. A grotto is formed beneath, with mossy seats, to rest the Nereids, and exclude the heats. Down through the crannies of the living walls the crystal streams descend in murmuring falls. Ships within this happy harbor meet, the thin remainders of the scattered fleet. The sailors, worn with toils, and spent with woes, leap on the welcome land, and seek their wished-for repose. 

Insert story about 432839

Insert story about ['41.256', '13.606']

\newpage

# Formiae To Ocriculum
  
## From Formiae To Tarracina

Leaving Formiae, Virgil set out for Tarracina by ship down the coast, a journey of about 24 miles. 

Stormclouds enwrap the day, and rainy gloom blots out the sky. The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. Then comes the creak of cables and the cries of seamen. Black night broods on the waters. Up leaped the waves to heaven. The oars are snapped. The prow swings away and gives her side to the waves. Yawning wide, the wave lays bare the ground below. Rocks amid the waves, a vast reef banking the sea. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water.   
  
Without delay the sailors strongly toss up the foam.   
  
In a far retreat there lies a haven. Within a long recess there lies a bay: an island shades it from the rolling sea and forms a port secure for ships to ride. Broke by the jutting land, on either side, in double streams the briny waters glide. Two towering crags, twin giants, guard the cove, and threat the skies. 

Insert story about 433143

Insert story about ['41.291', '13.249']

  
## Travelling By River, Upstream

Leaving Tarracina, Virgil set out for Forum Appii on a boat heading upstream, a journey of about 14 miles. 

A breeze from an unexpected quarter cools the air. The sun beats down. 

There was no story for None

  
## Departing From Forum Appii

Virgil departed from Forum Appii, intending to travel on a boat heading downstream to Tarracina, a distance of about 14 miles. 

They passed by an inscription that read: Est in Arcadia Ego. Birds sing their greetings. 

Insert story about 433143

Insert story about ['41.291', '13.249']

  
## Travelling On A Boat Heading Upstream To Forum Appii

Leaving Tarracina, Virgil set out for Forum Appii on a boat heading upstream, at least 14 miles. 

Wondering if it was related to his journey, he read the words that were carved there: Est in Arcadia Ego. 

There was no story for None

  
## Travelling By Road To Roma

Virgil departed from Forum Appii, intending to travel by road to Roma, a journey of about 42 miles. 

There is a fountain of cold water springing from the rock. The sun beats down. There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. His shoes are covered in dust from the road. 

Insert story about 423025

Insert story about ['41.892', '12.486']

  
## Travelling By River, Upstream

From Roma to Ocriculum is about 64 miles away when travelling on a boat heading upstream. 

No backward glances for the city left behind. The countryside is quieter than the city. 

Insert story about 413231

Insert story about ['42.412', '12.467']

  
## From Ocriculum To Narnia

Virgil departed from Ocriculum, intending to travel by road to Narnia, at least 8 miles. 

This is a smooth road, by which many wagons were bringing wood to Narnia. His shoes are covered in dust from the road. Along the road are graves, and a cenotaph. He passes another milestone. The road narrows here, an orchard wall encroaching on it. Next to the straight road that leads to Narnia, there is visible a sculpted tomb. The sun beats down. He left the city early, before the rising of the sun. Water has washed out the road, making for slow going. 

Insert story about 413225

Insert story about ['42.52', '12.516']

  
## Travelling By Road

From Narnia to Ocriculum is about 8 miles away when travelling by road. 

He had set out from Narnia amidst a throng travelling the same way. Along the road are graves, and a cenotaph. Now the road is quieter. There was written there these words: Est in Arcadia Ego. 

Insert story about 413231

Insert story about ['42.412', '12.467']

\newpage

# Ocriculum To Placentia
  
## Ocriculum To Narnia By Road

From Ocriculum to Narnia is at least 8 miles when travelling by road. 

There is a fountain of cold water springing from the rock. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. On the road from Ocriculum to Narnia there is a village, in which there is a temple and grove. A caravan from Narnia passed by. He left the city early, before the rising of the sun. He passes another milestone. This is a smooth road, by which many wagons were bringing wood to Narnia. 

Insert story about 413225

Insert story about ['42.52', '12.516']

  
## From Narnia To Spoletium

Virgil departed from Narnia, intending to travel by road to Spoletium, at least 22 miles. 

Water has washed out the road, making for slow going. Along the road are graves, and a cenotaph. By the road is a salt spring. Wondering if it was related to his journey, he read the words that were carved there: Est in Arcadia Ego. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There a spring wells up, and around about it is a meadow. 

Insert story about 413320

Insert story about ['42.745', '12.738']

  
## Departing From Spoletium

Intending to travel by road to Fanum Fortunae, Virgil left Spoletium. It was a journey of about 90 miles. 

The road narrows here, an orchard wall encroaching on it. Wondering if it was related to his journey, he read the words that were carved there: Est in Arcadia Ego. There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. This is a smooth road, by which many wagons were bringing wood to Fanum Fortunae. 

Insert story about 413129

Insert story about ['43.845', '13.017']

  
## After Fanum Fortunae

From Fanum Fortunae to Ariminum is at least 38 miles when travelling by ship down the coast. 

Out of the clouds bursts fire fast upon fire. Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. They hang on the wave's ridge. Onward comes a mountain heap of billows, gaunt, abrupt. Before their eyes a vast sea descending strikes astern.   
  
Without delay the sailors strongly toss up the foam.   
  
Broke by the jutting land, on either side, in double streams the briny waters glide. The waters at their feet sleep hushed, and, like a curtain, frowns above, mixt with the glancing green, the darkness of the grove. Down through the crannies of the living walls the crystal streams descend in murmuring falls. No haulsers need to bind the vessels here. Nor bearded anchors; for no storms they fear. The sailors, worn with toils, and spent with woes, leap on the welcome land, and seek their wished-for repose. 

Insert story about 393379

Insert story about ['44.059', '12.563']

  
## 38 Miles To Faventia

Virgil departed from Ariminum, intending to travel by road to Faventia, at least 38 miles. 

He passes another milestone. The road narrows here, an orchard wall encroaching on it. Workers are raising the level of the road. They pass a pillar on the right surmounted by a stone urn. A grove of Minerva is hard by the road, a grove of poplar trees. This is a smooth road, by which many wagons were bringing wood to Faventia. He left the city early, before the rising of the sun. An oxcart passes, loaded with grain. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 393420

Insert story about ['44.286', '11.884']

  
## To Bononia By Road

Virgil departed from Faventia, intending to travel by road to Bononia, about 30 miles away. 

There is a fountain of cold water springing from the rock. As they go up from Faventia, they see the ruined walls. Workers are raising the level of the road. The road narrows here, an orchard wall encroaching on it. This is a smooth road, by which many wagons were bringing wood to Bononia. 

Insert story about 393421

Insert story about ['44.495', '11.349']

  
## Departing From Bononia

Intending to travel on a military boat floating downstream to a village, Virgil left Bononia. It was a distance of about 39 miles. 

No backward glances for the city left behind. By the gate of a village, these words were carved: Est in Arcadia Ego. The sun beats down. 

There was no story for None

  
## From A Village To Placentia

From a village to Placentia is about 140 miles away when travelling on a military boat headed upstream. 

Birds sing their greetings. A breeze from an unexpected quarter cools the air. He presses onward. 

Insert story about 383741

Insert story about ['45.052', '9.699']

\newpage

# Placentia To Altinum
  
## To A Village

Leaving Placentia, Virgil set out for a village by road, about 11 miles away. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He passes another milestone. Est in Arcadia Ego was carved into the stone. His shoes are covered in dust from the road. They pass a pillar on the right surmounted by a stone urn. This is a smooth road, by which many wagons were bringing wood to a village. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. The sun beats down. A grove of Minerva is hard by the road, a grove of poplar trees. 

There was no story for None

  
## The Journey To Mediolanum

Intending to travel by road to Mediolanum, Virgil left a village. It was at least 27 miles. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. This is a smooth road, by which many wagons were bringing wood to Mediolanum. On a pillar was written: Est in Arcadia Ego. He contemplated it. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The road narrows here, an orchard wall encroaching on it. They pass a pillar on the right surmounted by a stone urn. There is a fountain of cold water springing from the rock. 

Insert story about 383706

Insert story about ['45.464', '9.188']

  
## To Verona

Intending to travel by road to Verona, Virgil left Mediolanum. It was a journey of about 101 miles. 

Water has washed out the road, making for slow going. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. On the road from Mediolanum to Verona there is a village, in which there is a temple and grove. Wondering if it was related to his journey, he read the words that were carved there: Est in Arcadia Ego. An oxcart passes, loaded with grain. His shoes are covered in dust from the road. 

Insert story about 383816

Insert story about ['45.439', '10.994']

  
## Leaving Verona By Road

Intending to travel by road to Patavium, Virgil left Verona. It was a journey of about 50 miles. 

Water has washed out the road, making for slow going. His shoes are covered in dust from the road. He passes another milestone. Now the road is quieter. As they go up from Verona, they see the ruined walls. Above the roads are ruins, among which is a cave sacred to Asclepius. The road narrows here, an orchard wall encroaching on it. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 393473

Insert story about ['45.41', '11.877']

  
## To A Village

Intending to travel by road to a village, Virgil left Patavium. It was a journey of about 13 miles. 

This is a smooth road, by which many wagons were bringing wood to a village. Next to the straight road that leads to a village, there is visible a sculpted tomb. There a spring wells up, and around about it is a meadow. The road narrows here, an orchard wall encroaching on it. 

There was no story for None

  
## Travelling By Road To Altinum

From a village to Altinum is a distance of about 14 miles when travelling by road. 

Workers are raising the level of the road. The sun beats down. A caravan from Altinum passed by. There a spring wells up, and around about it is a meadow. 

Insert story about 393374

Insert story about ['45.579', '12.373']

  
## To Brundulum

Virgil departed from Altinum, intending to travel by ship down the coast to Brundulum, at least 27 miles. 

The ship held the high seas, no land yet appearing.   
  
They are tossed asunder over the dreary gulf. Stormclouds enwrap the day, and rainy gloom blots out the sky. Without delay the sailors strongly toss up the foam.   
  
The harbor of Brundulum came into view over the horizon. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. 

There was no story for None

Insert story about ['45.19', '12.31']

  
## Travelling By Ship

Intending to travel by ship down the coast to Altinum, Virgil left Brundulum. It was a distance of about 27 miles. 

They are tossed asunder over the dreary gulf. Out of the clouds bursts fire fast upon fire. Black night broods on the waters. All around from pole to pole the rattling peals resound. Even as he cried, the hurricane from the North struck with a roar against the sailThe shattered oars start forth. They are horsed astride a surge's crest, rocking pendent over the deep. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water.   
  
Without delay the sailors strongly toss up the foam.   
  
Broke by the jutting land, on either side, in double streams the briny waters glide. Betwixt two rows of rocks a sylvan scene appears above, and groves for ever green. The waters at their feet sleep hushed, and, like a curtain, frowns above, mixt with the glancing green, the darkness of the grove. 

Insert story about 393374

Insert story about ['45.579', '12.373']

\newpage

# Altinum To Pons Drusi
  
## To Iulia Concordia

From Altinum to Iulia Concordia is a distance of about 26 miles when travelling by road. 

He passes another milestone. There a spring wells up, and around about it is a meadow. A caravan from Iulia Concordia passed by. Now the road is quieter. Workers are raising the level of the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. On the road from Altinum to Iulia Concordia there is a village, in which there is a temple and grove. 

Insert story about 393441

Insert story about ['45.757', '12.844']

  
## 26 Miles To Aquileia

From Iulia Concordia to Aquileia is a journey of about 26 miles when travelling by road. 

The sun beats down. A grove of Minerva is hard by the road, a grove of poplar trees. This is a smooth road, by which many wagons were bringing wood to Aquileia. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. An oxcart passes, loaded with grain. They pass a pillar on the right surmounted by a stone urn. He passes another milestone. 

Insert story about 187290

Insert story about ['45.768', '13.365']

  
## Departing From Aquileia

Virgil departed from Aquileia, intending to travel by road to Ad Tricesimum, a distance of about 28 miles. 

By the road is a salt spring. He left the city early, before the rising of the sun. Water has washed out the road, making for slow going. A caravan from Ad Tricesimum passed by. The sun beats down. The road narrows here, an orchard wall encroaching on it. As they go up from Aquileia, they see the ruined walls. A cloud passes in front of the sun. 

Insert story about 187259

Insert story about ['46.158', '13.216']

  
## Departing From Ad Tricesimum

Leaving Ad Tricesimum, Virgil set out for Aquileia by road, a journey of about 28 miles. 

A caravan from Aquileia passed by. Above the roads are ruins, among which is a cave sacred to Asclepius. There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 187290

Insert story about ['45.768', '13.365']

  
## The Journey To Iulia Concordia

Leaving Aquileia, Virgil set out for Iulia Concordia by road, a journey of about 26 miles. 

By the road is a salt spring. He had set out from Aquileia amidst a throng travelling the same way. Next to the straight road that leads to Iulia Concordia, there is visible a sculpted tomb. There is a fountain of cold water springing from the rock. The sun beats down. 

Insert story about 393441

Insert story about ['45.757', '12.844']

  
## To Tridentum By Road

Leaving Iulia Concordia, Virgil set out for Tridentum by road, at least 103 miles. 

Along the road are graves, and a cenotaph. He passes another milestone. This is a smooth road, by which many wagons were bringing wood to Tridentum. There a spring wells up, and around about it is a meadow. Water has washed out the road, making for slow going. On the road from Iulia Concordia to Tridentum there is a village, in which there is a temple and grove. A cloud passes in front of the sun. As they go up from Iulia Concordia, they see the ruined walls. He had set out from Iulia Concordia amidst a throng travelling the same way. 

Insert story about 383804

Insert story about ['46.067', '11.119']

  
## To Endidae

From Tridentum to Endidae is a journey of about 20 miles when travelling by road. 

Workers are raising the level of the road. The sun beats down. They pass a pillar on the right surmounted by a stone urn. A grove of Minerva is hard by the road, a grove of poplar trees. There is a fountain of cold water springing from the rock. He passes another milestone. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Along the road are graves, and a cenotaph. He had set out from Tridentum amidst a throng travelling the same way. 

Insert story about 187368

Insert story about ['46.318', '11.274']

  
## After Endidae

Intending to travel by road to Pons Drusi, Virgil left Endidae. It was at least 13 miles. 

Workers are raising the level of the road. This is a smooth road, by which many wagons were bringing wood to Pons Drusi. The sun beats down. Water has washed out the road, making for slow going. 

Insert story about 187518

Insert story about ['46.497', '11.358']

\newpage

# Pons Drusi To Brigantium
  
## Travelling By Road

Intending to travel by road to a village, Virgil left Pons Drusi. It was at least 28 miles. 

There is a fountain of cold water springing from the rock. Next to the straight road that leads to a village, there is visible a sculpted tomb. Above the roads are ruins, among which is a cave sacred to Asclepius. The sun beats down. A grove of Minerva is hard by the road, a grove of poplar trees. He had set out from Pons Drusi amidst a throng travelling the same way. Workers are raising the level of the road. This is a smooth road, by which many wagons were bringing wood to a village. There a spring wells up, and around about it is a meadow. 

There was no story for None

  
## Departing From A Village

From a village to Veldidena is a journey of about 41 miles when travelling by road. 

The road narrows here, an orchard wall encroaching on it. Above the roads are ruins, among which is a cave sacred to Asclepius. He left the city early, before the rising of the sun. They pass a pillar on the right surmounted by a stone urn. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Now the road is quieter. A grove of Minerva is hard by the road, a grove of poplar trees. As they go up from a village, they see the ruined walls. 

Insert story about 187608

Insert story about ['47.254', '11.4']

  
## To A Village

From Veldidena to a village is about 41 miles away when travelling by road. 

The road narrows here, an orchard wall encroaching on it. Along the road are graves, and a cenotaph. Next to the straight road that leads to a village, there is visible a sculpted tomb. On a pillar was written: Est in Arcadia Ego. He contemplated it. They pass a pillar on the right surmounted by a stone urn. On the road from Veldidena to a village there is a village, in which there is a temple and grove. Workers are raising the level of the road. There a spring wells up, and around about it is a meadow. 

There was no story for None

  
## Departing From A Village

From a village to Pons Drusi is a distance of about 28 miles when travelling by road. 

There is a fountain of cold water springing from the rock. This is a smooth road, by which many wagons were bringing wood to Pons Drusi. On the road from a village to Pons Drusi there is a village, in which there is a temple and grove. A caravan from Pons Drusi passed by. 

Insert story about 187518

Insert story about ['46.497', '11.358']

  
## From Pons Drusi To Maiensis Statio

From Pons Drusi to Maiensis Statio is a journey of about 15 miles when travelling by road. 

Along the road are graves, and a cenotaph. As they go up from Pons Drusi, they see the ruined walls. His shoes are covered in dust from the road. He left the city early, before the rising of the sun. A grove of Minerva is hard by the road, a grove of poplar trees. They pass a pillar on the right surmounted by a stone urn. This is a smooth road, by which many wagons were bringing wood to Maiensis Statio. 

There was no story for None

Insert story about ['0', '0']

  
## Maiensis Statio To Abodiacum By Road

From Maiensis Statio to Abodiacum is about 140 miles away when travelling by road. 

Water has washed out the road, making for slow going. This is a smooth road, by which many wagons were bringing wood to Abodiacum. There a spring wells up, and around about it is a meadow. An oxcart passes, loaded with grain. Next to the straight road that leads to Abodiacum, there is visible a sculpted tomb. By the road is a salt spring. 

Insert story about 187242

Insert story about ['47.91', '10.91']

  
## Travelling By Road To Cambodunum

Intending to travel by road to Cambodunum, Virgil left Abodiacum. It was about 31 miles away. 

Now the road is quieter. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. By the road is a salt spring. He passes another milestone. A cloud passes in front of the sun. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## Cambodunum To Brigantium By Road

From Cambodunum to Brigantium is at least 36 miles when travelling by road. 

Along the road are graves, and a cenotaph. They pass a pillar on the right surmounted by a stone urn. There a spring wells up, and around about it is a meadow. Water has washed out the road, making for slow going. As they go up from Cambodunum, they see the ruined walls. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. His shoes are covered in dust from the road. 

Insert story about 187325

Insert story about ['47.503', '9.747']

\newpage

# Brigantium To Aventicum
  
## To Curia By Road

Intending to travel by road to Curia, Virgil left Brigantium. It was a distance of about 50 miles. 

They passed by an inscription that read: Est in Arcadia Ego. On the road from Brigantium to Curia there is a village, in which there is a temple and grove. The sun beats down. Water has washed out the road, making for slow going. Along the road are graves, and a cenotaph. He passes another milestone. 

Insert story about 187357

Insert story about ['46.849', '9.531']

  
## Travelling By Road To Comum

Virgil departed from Curia, intending to travel by road to Comum, at least 92 miles. 

An oxcart passes, loaded with grain. He had set out from Curia amidst a throng travelling the same way. On the road from Curia to Comum there is a village, in which there is a temple and grove. Above the roads are ruins, among which is a cave sacred to Asclepius. Along the road are graves, and a cenotaph. By the road is a salt spring. There a spring wells up, and around about it is a meadow. 

Insert story about 383627

Insert story about ['45.812', '9.086']

  
## 92 Miles To Curia

Intending to travel by road to Curia, Virgil left Comum. It was at least 92 miles. 

Now the road is quieter. They pass a pillar on the right surmounted by a stone urn. Next to the straight road that leads to Curia, there is visible a sculpted tomb. As they go up from Comum, they see the ruined walls. 

Insert story about 187357

Insert story about ['46.849', '9.531']

  
## Curia To Brigantium By Road

Virgil departed from Curia, intending to travel by road to Brigantium, at least 50 miles. 

By the road is a salt spring. There was written there these words: Est in Arcadia Ego. An oxcart passes, loaded with grain. This is a smooth road, by which many wagons were bringing wood to Brigantium. Now the road is quieter. 

Insert story about 187325

Insert story about ['47.503', '9.747']

  
## Brigantium To Cambodunum By Road

Leaving Brigantium, Virgil set out for Cambodunum by road, a distance of about 36 miles. 

There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. This is a smooth road, by which many wagons were bringing wood to Cambodunum. Along the road are graves, and a cenotaph. Workers are raising the level of the road. He left the city early, before the rising of the sun. He passes another milestone. Now the road is quieter. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## Leaving Cambodunum By Road

Virgil departed from Cambodunum, intending to travel by road to Brigantium, a distance of about 36 miles. 

The road narrows here, an orchard wall encroaching on it. As they go up from Cambodunum, they see the ruined walls. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He left the city early, before the rising of the sun. A cloud passes in front of the sun. Along the road are graves, and a cenotaph. Water has washed out the road, making for slow going. 

Insert story about 187325

Insert story about ['47.503', '9.747']

  
## To Augusta Raurica

Leaving Brigantium, Virgil set out for Augusta Raurica on a military boat headed upstream, at least 119 miles. 

They passed by an inscription that read: Est in Arcadia Ego. A cloud passes in front of the sun. Birds sing their greetings. 

Insert story about 177494

Insert story about ['47.533', '7.722']

  
## Travelling By Road To Aventicum

Virgil departed from Augusta Raurica, intending to travel by road to Aventicum, about 58 miles away. 

Next to the straight road that leads to Aventicum, there is visible a sculpted tomb. He left the city early, before the rising of the sun. The road narrows here, an orchard wall encroaching on it. There is a fountain of cold water springing from the rock. Along the road are graves, and a cenotaph. Workers are raising the level of the road. An oxcart passes, loaded with grain. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Water has washed out the road, making for slow going. 

Insert story about 177495

Insert story about ['46.88', '7.041']

\newpage

# Aventicum To Veldidena
  
## To Augusta Raurica

Intending to travel by road to Augusta Raurica, Virgil left Aventicum. It was about 58 miles away. 

Water has washed out the road, making for slow going. He had set out from Aventicum amidst a throng travelling the same way. His shoes are covered in dust from the road. Along the road are graves, and a cenotaph. They pass a pillar on the right surmounted by a stone urn. This is a smooth road, by which many wagons were bringing wood to Augusta Raurica. The sun beats down. On the road from Aventicum to Augusta Raurica there is a village, in which there is a temple and grove. Workers are raising the level of the road. 

Insert story about 177494

Insert story about ['47.533', '7.722']

  
## Travelling By River

Virgil departed from Augusta Raurica, intending to travel on a military boat floating downstream to Brigantium, a journey of about 119 miles. 

A breeze from an unexpected quarter cools the air. At that place is inscribed: "Est in Arcadia Ego". The sun beats down. 

Insert story about 187325

Insert story about ['47.503', '9.747']

  
## From Brigantium To Cambodunum

Leaving Brigantium, Virgil set out for Cambodunum by road, at least 36 miles. 

They pass a pillar on the right surmounted by a stone urn. By the road is a salt spring. Est in Arcadia Ego was carved into the stone. A caravan from Cambodunum passed by. He had set out from Brigantium amidst a throng travelling the same way. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Workers are raising the level of the road. The road narrows here, an orchard wall encroaching on it. Now the road is quieter. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## After Cambodunum

From Cambodunum to Abodiacum is about 31 miles away when travelling by road. 

He left the city early, before the rising of the sun. Next to the straight road that leads to Abodiacum, there is visible a sculpted tomb. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He had set out from Cambodunum amidst a throng travelling the same way. 

Insert story about 187242

Insert story about ['47.91', '10.91']

  
## The Journey To Cambodunum

Leaving Abodiacum, Virgil set out for Cambodunum by road, a journey of about 31 miles. 

He had set out from Abodiacum amidst a throng travelling the same way. Now the road is quieter. On the road from Abodiacum to Cambodunum there is a village, in which there is a temple and grove. Along the road are graves, and a cenotaph. This is a smooth road, by which many wagons were bringing wood to Cambodunum. An oxcart passes, loaded with grain. A caravan from Cambodunum passed by. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187335

Insert story about ['47.727', '10.327']

  
## After Cambodunum

Leaving Cambodunum, Virgil set out for Abodiacum by road, a journey of about 31 miles. 

Est in Arcadia Ego: he pondered the sight of this inscription. There a spring wells up, and around about it is a meadow. An oxcart passes, loaded with grain. Workers are raising the level of the road. Now the road is quieter. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. His shoes are covered in dust from the road. 

Insert story about 187242

Insert story about ['47.91', '10.91']

  
## Travelling By Road To Parthanum

Leaving Abodiacum, Virgil set out for Parthanum by road, a distance of about 40 miles. 

Workers are raising the level of the road. The road narrows here, an orchard wall encroaching on it. There a spring wells up, and around about it is a meadow. He had set out from Abodiacum amidst a throng travelling the same way. Est in Arcadia Ego was carved into the stone. 

Insert story about 187505

Insert story about ['47.492', '11.086']

  
## To Veldidena By Road

Virgil departed from Parthanum, intending to travel by road to Veldidena, about 32 miles away. 

He passes another milestone. As they go up from Parthanum, they see the ruined walls. They pass a pillar on the right surmounted by a stone urn. On the road from Parthanum to Veldidena there is a village, in which there is a temple and grove. Now the road is quieter. The sun beats down. 

Insert story about 187608

Insert story about ['47.254', '11.4']

\newpage

# Veldidena To A Village
  
## 32 Miles To Parthanum

Intending to travel by road to Parthanum, Virgil left Veldidena. It was a distance of about 32 miles. 

As they go up from Veldidena, they see the ruined walls. His shoes are covered in dust from the road. A caravan from Parthanum passed by. The road narrows here, an orchard wall encroaching on it. This is a smooth road, by which many wagons were bringing wood to Parthanum. He had set out from Veldidena amidst a throng travelling the same way. Water has washed out the road, making for slow going. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A cloud passes in front of the sun. 

Insert story about 187505

Insert story about ['47.492', '11.086']

  
## From Parthanum To Veldidena

From Parthanum to Veldidena is a journey of about 32 miles when travelling by road. 

Above the roads are ruins, among which is a cave sacred to Asclepius. The road narrows here, an orchard wall encroaching on it. They pass a pillar on the right surmounted by a stone urn. He passes another milestone. On the road from Parthanum to Veldidena there is a village, in which there is a temple and grove. There is a fountain of cold water springing from the rock. A grove of Minerva is hard by the road, a grove of poplar trees. As they go up from Parthanum, they see the ruined walls. He had set out from Parthanum amidst a throng travelling the same way. 

Insert story about 187608

Insert story about ['47.254', '11.4']

  
## Veldidena To A Village By Road

From Veldidena to a village is about 41 miles away when travelling by road. 

There a spring wells up, and around about it is a meadow. By the road is a salt spring. Now the road is quieter. There is a fountain of cold water springing from the rock. They pass a pillar on the right surmounted by a stone urn. The sun beats down. 

There was no story for None

  
## After A Village

Virgil departed from a village, intending to travel by road to Aguntum, at least 60 miles. 

As they go up from a village, they see the ruined walls. A cloud passes in front of the sun. A grove of Minerva is hard by the road, a grove of poplar trees. By the gate of Aguntum, these words were carved: Est in Arcadia Ego. Now the road is quieter. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 187265

Insert story about ['46.827', '12.823']

  
## Leaving Aguntum By Road

From Aguntum to Iulium Carnicum is a distance of about 33 miles when travelling by road. 

Next to the straight road that leads to Iulium Carnicum, there is visible a sculpted tomb. The road narrows here, an orchard wall encroaching on it. There is a fountain of cold water springing from the rock. As they go up from Aguntum, they see the ruined walls. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Workers are raising the level of the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. By the road is a salt spring. 

Insert story about 187430

Insert story about ['46.461', '13.026']

  
## To A Village

Leaving Iulium Carnicum, Virgil set out for a village by road, a journey of about 9 miles. 

They pass a pillar on the right surmounted by a stone urn. The road narrows here, an orchard wall encroaching on it. As they go up from Iulium Carnicum, they see the ruined walls. A cloud passes in front of the sun. The sun beats down. 

There was no story for None

  
## After A Village

Leaving a village, Virgil set out for Santicum by road, a distance of about 47 miles. 

He left the city early, before the rising of the sun. A cloud passes in front of the sun. An oxcart passes, loaded with grain. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. As they go up from a village, they see the ruined walls. Next to the straight road that leads to Santicum, there is visible a sculpted tomb. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A grove of Minerva is hard by the road, a grove of poplar trees. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 187537

Insert story about ['46.616', '13.849']

  
## To A Village By Road

Leaving Santicum, Virgil set out for a village by road, about 47 miles away. 

There is a fountain of cold water springing from the rock. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. This is a smooth road, by which many wagons were bringing wood to a village. Next to the straight road that leads to a village, there is visible a sculpted tomb. He had set out from Santicum amidst a throng travelling the same way. A grove of Minerva is hard by the road, a grove of poplar trees. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. His shoes are covered in dust from the road. Workers are raising the level of the road. 

There was no story for None

\newpage

# A Village To A Village
  
## Departing From A Village

Leaving a village, Virgil set out for Santicum by road, a distance of about 47 miles. 

By the road is a salt spring. The sun beats down. On the road from a village to Santicum there is a village, in which there is a temple and grove. A caravan from Santicum passed by. They pass a pillar on the right surmounted by a stone urn. Next to the straight road that leads to Santicum, there is visible a sculpted tomb. Now the road is quieter. He had set out from a village amidst a throng travelling the same way. 

Insert story about 187537

Insert story about ['46.616', '13.849']

  
## The Journey To Virunum

From Santicum to Virunum is a distance of about 28 miles when travelling by road. 

Water has washed out the road, making for slow going. They pass a pillar on the right surmounted by a stone urn. The road narrows here, an orchard wall encroaching on it. He passes another milestone. A cloud passes in front of the sun. Now the road is quieter. 

Insert story about 197583

Insert story about ['46.703', '14.36']

  
## 96 Miles To Poetovio

Leaving Virunum, Virgil set out for Poetovio on a boat heading downstream, a journey of about 96 miles. 

Birds sing their greetings. On a pillar was written: Est in Arcadia Ego. He contemplated it. 

Insert story about 197446

Insert story about ['46.42', '15.87']

  
## Leaving Poetovio By River

Intending to travel on a military boat floating downstream to Mursa, Virgil left Poetovio. It was a journey of about 187 miles. 

By the gate of Mursa, these words were carved: Est in Arcadia Ego. 

Insert story about 197389

Insert story about ['45.56', '18.676']

  
## From Mursa To Cibalae

Leaving Mursa, Virgil set out for Cibalae by road, a distance of about 21 miles. 

Workers are raising the level of the road. A cloud passes in front of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. By the road is a salt spring. A grove of Minerva is hard by the road, a grove of poplar trees. 

Insert story about 197207

Insert story about ['45.291', '18.801']

  
## After Cibalae

Intending to travel by road to Sirmium, Virgil left Cibalae. It was at least 46 miles. 

His shoes are covered in dust from the road. A cloud passes in front of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The road narrows here, an orchard wall encroaching on it. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. They pass a pillar on the right surmounted by a stone urn. He passes another milestone. There was written there these words: Est in Arcadia Ego. 

Insert story about 207447

Insert story about ['44.966', '19.61']

  
## From Sirmium To A Village

Leaving Sirmium, Virgil set out for a village by road, about 56 miles away. 

A grove of Minerva is hard by the road, a grove of poplar trees. By the road is a salt spring. There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. His shoes are covered in dust from the road. Water has washed out the road, making for slow going. 

There was no story for None

  
## Departing From A Village

From a village to a village is a distance of about 130 miles when travelling by road. 

As they go up from a village, they see the ruined walls. There is a fountain of cold water springing from the rock. The sun beats down. This is a smooth road, by which many wagons were bringing wood to a village. By the gate of a village, these words were carved: Est in Arcadia Ego. 

There was no story for None

\newpage

# A Village To Viminacium
  
## Leaving A Village By Road

Intending to travel by road to Narona, Virgil left a village. It was a distance of about 15 miles. 

He left the city early, before the rising of the sun. Above the roads are ruins, among which is a cave sacred to Asclepius. The road narrows here, an orchard wall encroaching on it. Water has washed out the road, making for slow going. They pass a pillar on the right surmounted by a stone urn. As they go up from a village, they see the ruined walls. Next to the straight road that leads to Narona, there is visible a sculpted tomb. Virgil saw this on a roadside tomb: Est in Arcadia Ego. On the road from a village to Narona there is a village, in which there is a temple and grove. 

Insert story about 197400

Insert story about ['43.081', '17.628']

  
## Departing From Narona

From Narona to a village is a distance of about 15 miles when travelling by road. 

Along the road are graves, and a cenotaph. The sun beats down. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Workers are raising the level of the road. On the road from Narona to a village there is a village, in which there is a temple and grove. 

There was no story for None

  
## Leaving A Village By Road

Intending to travel by road to a village, Virgil left a village. It was a distance of about 130 miles. 

As they go up from a village, they see the ruined walls. A caravan from a village passed by. Water has washed out the road, making for slow going. Above the roads are ruins, among which is a cave sacred to Asclepius. There a spring wells up, and around about it is a meadow. By the road is a salt spring. 

There was no story for None

  
## After A Village

Virgil departed from a village, intending to travel by road to Domavium, a distance of about 18 miles. 

He had set out from a village amidst a throng travelling the same way. He passes another milestone. There is a fountain of cold water springing from the rock. By the gate of Domavium, these words were carved: Est in Arcadia Ego. Now the road is quieter. A caravan from Domavium passed by. The sun beats down. The road narrows here, an orchard wall encroaching on it. 

Insert story about 207088

Insert story about ['44.144', '19.363']

  
## From Domavium To A Village

From Domavium to a village is about 18 miles away when travelling by road. 

The road narrows here, an orchard wall encroaching on it. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Water has washed out the road, making for slow going. There a spring wells up, and around about it is a meadow. Wondering if it was related to his journey, he read the words that were carved there: Est in Arcadia Ego. A caravan from a village passed by. They pass a pillar on the right surmounted by a stone urn. 

There was no story for None

  
## 56 Miles To Sirmium

Leaving a village, Virgil set out for Sirmium by road, a journey of about 56 miles. 

He passes another milestone. This is a smooth road, by which many wagons were bringing wood to Sirmium. A caravan from Sirmium passed by. Next to the straight road that leads to Sirmium, there is visible a sculpted tomb. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. As they go up from a village, they see the ruined walls. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There a spring wells up, and around about it is a meadow. The road narrows here, an orchard wall encroaching on it. 

Insert story about 207447

Insert story about ['44.966', '19.61']

  
## Leaving Sirmium By River

Virgil departed from Sirmium, intending to travel on a military boat floating downstream to Singidunum, a distance of about 85 miles. 

A breeze from an unexpected quarter cools the air. 

Insert story about 207443

Insert story about ['44.802', '20.466']

  
## Departing From Singidunum

Virgil departed from Singidunum, intending to travel on a military boat floating downstream to Viminacium, about 49 miles away. 

At that place is inscribed: "Est in Arcadia Ego". A cloud passes in front of the sun. 

Insert story about 207549

Insert story about ['44.716', '21.167']

\newpage

# Viminacium To Naissus
  
## Travelling By Road To Tibiscum

Leaving Viminacium, Virgil set out for Tibiscum by road, a distance of about 96 miles. 

The sun beats down. By the road is a salt spring. He passes another milestone. Along the road are graves, and a cenotaph. This is a smooth road, by which many wagons were bringing wood to Tibiscum. A grove of Minerva is hard by the road, a grove of poplar trees. Water has washed out the road, making for slow going. 

Insert story about 207495

Insert story about ['45.459', '22.186']

  
## From Tibiscum To Viminacium

Virgil departed from Tibiscum, intending to travel by road to Viminacium, at least 96 miles. 

The sun beats down. They pass a pillar on the right surmounted by a stone urn. Now the road is quieter. Above the roads are ruins, among which is a cave sacred to Asclepius. Est in Arcadia Ego was carved into the stone. His shoes are covered in dust from the road. As they go up from Tibiscum, they see the ruined walls. There is a fountain of cold water springing from the rock. 

Insert story about 207549

Insert story about ['44.716', '21.167']

  
## To Singidunum

Intending to travel on a military boat headed upstream to Singidunum, Virgil left Viminacium. It was a journey of about 49 miles. 

He presses onward. They passed by an inscription that read: Est in Arcadia Ego. 

Insert story about 207443

Insert story about ['44.802', '20.466']

  
## 49 Miles To Viminacium

From Singidunum to Viminacium is at least 49 miles when travelling on a military boat floating downstream. 

The countryside is quieter than the city. 

Insert story about 207549

Insert story about ['44.716', '21.167']

  
## To Horreum Margi By Road

Leaving Viminacium, Virgil set out for Horreum Margi by road, a journey of about 57 miles. 

As they go up from Viminacium, they see the ruined walls. By the road is a salt spring. The sun beats down. A cloud passes in front of the sun. Workers are raising the level of the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. They pass a pillar on the right surmounted by a stone urn. His shoes are covered in dust from the road. An oxcart passes, loaded with grain. 

There was no story for None

  
## To Naissus

From Horreum Margi to Naissus is at least 51 miles when travelling by road. 

Next to the straight road that leads to Naissus, there is visible a sculpted tomb. They pass a pillar on the right surmounted by a stone urn. His shoes are covered in dust from the road. He had set out from Horreum Margi amidst a throng travelling the same way. 

Insert story about 207303

Insert story about ['43.316', '21.894']

  
## 80 Miles To Ulpiana

Virgil departed from Naissus, intending to travel by road to Ulpiana, about 80 miles away. 

They pass a pillar on the right surmounted by a stone urn. A grove of Minerva is hard by the road, a grove of poplar trees. Next to the straight road that leads to Ulpiana, there is visible a sculpted tomb. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

There was no story for None

Insert story about ['0', '0']

  
## To Naissus

Intending to travel by road to Naissus, Virgil left Ulpiana. It was about 80 miles away. 

The road narrows here, an orchard wall encroaching on it. A grove of Minerva is hard by the road, a grove of poplar trees. As they go up from Ulpiana, they see the ruined walls. On the road from Ulpiana to Naissus there is a village, in which there is a temple and grove. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. They pass a pillar on the right surmounted by a stone urn. Now the road is quieter. A caravan from Naissus passed by. 

Insert story about 207303

Insert story about ['43.316', '21.894']

\newpage

# Naissus To Taliata
  
## 76 Miles To Bononia (Moesia)

Leaving Naissus, Virgil set out for Bononia (Moesia) by road, about 76 miles away. 

Water has washed out the road, making for slow going. The sun beats down. An oxcart passes, loaded with grain. Along the road are graves, and a cenotaph. By the road is a salt spring. 

Insert story about 206975

Insert story about ['43.993', '22.876']

  
## The Journey To Taliata

Leaving Bononia (Moesia), Virgil set out for Taliata by road, about 58 miles away. 

By the road is a salt spring. He had set out from Bononia (Moesia) amidst a throng travelling the same way. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. This is a smooth road, by which many wagons were bringing wood to Taliata. As they go up from Bononia (Moesia), they see the ruined walls. A cloud passes in front of the sun. They pass a pillar on the right surmounted by a stone urn. He left the city early, before the rising of the sun. Now the road is quieter. 

Insert story about 207485

Insert story about ['44.444', '22.144']

  
## Travelling By Road

Intending to travel by road to Bononia (Moesia), Virgil left Taliata. It was a journey of about 58 miles. 

His shoes are covered in dust from the road. On the road from Taliata to Bononia (Moesia) there is a village, in which there is a temple and grove. Water has washed out the road, making for slow going. They pass a pillar on the right surmounted by a stone urn. There was written there these words: Est in Arcadia Ego. 

Insert story about 206975

Insert story about ['43.993', '22.876']

  
## 58 Miles To Taliata

Intending to travel by road to Taliata, Virgil left Bononia (Moesia). It was a journey of about 58 miles. 

Now the road is quieter. An oxcart passes, loaded with grain. A grove of Minerva is hard by the road, a grove of poplar trees. As they go up from Bononia (Moesia), they see the ruined walls. The sun beats down. 

Insert story about 207485

Insert story about ['44.444', '22.144']

  
## Leaving Taliata By Road

From Taliata to Drobeta is a journey of about 35 miles when travelling by road. 

He had set out from Taliata amidst a throng travelling the same way. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Above the roads are ruins, among which is a cave sacred to Asclepius. An oxcart passes, loaded with grain. They passed by an inscription that read: Est in Arcadia Ego. There a spring wells up, and around about it is a meadow. A cloud passes in front of the sun. 

Insert story about 207100

Insert story about ['44.636', '22.66']

  
## 35 Miles To Taliata

From Drobeta to Taliata is at least 35 miles when travelling by road. 

Along the road are graves, and a cenotaph. He passes another milestone. He left the city early, before the rising of the sun. A caravan from Taliata passed by. Workers are raising the level of the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 207485

Insert story about ['44.444', '22.144']

  
## Departing From Taliata

Intending to travel on a military boat floating downstream to Dierna, Virgil left Taliata. It was at least 22 miles. 

Virgil saw this on a roadside tomb: Est in Arcadia Ego. 

Insert story about 207078

Insert story about ['44.725', '22.396']

  
## Dierna To Taliata By River, Upstream

Intending to travel on a boat heading upstream to Taliata, Virgil left Dierna. It was a distance of about 22 miles. 

Birds sing their greetings. A cloud passes in front of the sun. The countryside is quieter than the city. 

Insert story about 207485

Insert story about ['44.444', '22.144']

\newpage

# Taliata To Dyrrhachium
  
## Travelling By Road

Leaving Taliata, Virgil set out for Bononia (Moesia) by road, a journey of about 58 miles. 

He passes another milestone. He left the city early, before the rising of the sun. A cloud passes in front of the sun. His shoes are covered in dust from the road. The road narrows here, an orchard wall encroaching on it. There is a fountain of cold water springing from the rock. 

Insert story about 206975

Insert story about ['43.993', '22.876']

  
## Travelling By Road

Leaving Bononia (Moesia), Virgil set out for Naissus by road, about 76 miles away. 

The sun beats down. There is a fountain of cold water springing from the rock. He left the city early, before the rising of the sun. As they go up from Bononia (Moesia), they see the ruined walls. 

Insert story about 207303

Insert story about ['43.316', '21.894']

  
## 92 Miles To Serdica

Leaving Naissus, Virgil set out for Serdica by road, about 92 miles away. 

There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. As they go up from Naissus, they see the ruined walls. They pass a pillar on the right surmounted by a stone urn. There a spring wells up, and around about it is a meadow. Next to the straight road that leads to Serdica, there is visible a sculpted tomb. 

Insert story about 207439

Insert story about ['42.723', '23.343']

  
## To Stobi

From Serdica to Stobi is a distance of about 125 miles when travelling by road. 

A grove of Minerva is hard by the road, a grove of poplar trees. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A caravan from Stobi passed by. There was written there these words: Est in Arcadia Ego. Next to the straight road that leads to Stobi, there is visible a sculpted tomb. By the road is a salt spring. There a spring wells up, and around about it is a meadow. Along the road are graves, and a cenotaph. 

Insert story about 491731

Insert story about ['41.531', '21.978']

  
## Stobi To Heraklea By Road

Leaving Stobi, Virgil set out for Heraklea by road, a journey of about 54 miles. 

There is a fountain of cold water springing from the rock. By the road is a salt spring. He had set out from Stobi amidst a throng travelling the same way. Workers are raising the level of the road. The road narrows here, an orchard wall encroaching on it. Now the road is quieter. An oxcart passes, loaded with grain. 

Insert story about 481861

Insert story about ['41.032', '21.336']

  
## Heraklea To A Village By Road

Leaving Heraklea, Virgil set out for a village by road, at least 109 miles. 

He left the city early, before the rising of the sun. This is a smooth road, by which many wagons were bringing wood to a village. Above the roads are ruins, among which is a cave sacred to Asclepius. Wondering if it was related to his journey, he read the words that were carved there: Est in Arcadia Ego. They pass a pillar on the right surmounted by a stone urn. The road narrows here, an orchard wall encroaching on it. There a spring wells up, and around about it is a meadow. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

There was no story for None

  
## Travelling By Road To Apollonia (Epirus)

Intending to travel by road to Apollonia (Epirus), Virgil left a village. It was a distance of about 23 miles. 

Water has washed out the road, making for slow going. Next to the straight road that leads to Apollonia (Epirus), there is visible a sculpted tomb. A caravan from Apollonia (Epirus) passed by. A grove of Minerva is hard by the road, a grove of poplar trees. They pass a pillar on the right surmounted by a stone urn. 

There was no story for None

Insert story about ['40.77', '19.43']

  
## Departing From Apollonia (Epirus)

Intending to travel by ship down the coast to Dyrrhachium, Virgil left Apollonia (Epirus). It was at least 42 miles. 

Straightway the winds upturn the main, and great seas rise. They are tossed asunder over the dreary gulf. Even as he cried, the hurricane from the North struck with a roar against the sailThe shattered oars start forth. Round swings the prow, and lets the waters sweep the broadside. They hang on the wave's ridge. Each loosened side through many a gaping seam lets in the baleful tide.   
  
Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
Broke by the jutting land, on either side, in double streams the briny waters glide. The sailors, worn with toils, and spent with woes, leap on the welcome land, and seek their wished-for repose. 

Insert story about 481818

Insert story about ['41.316', '19.45']

\newpage
