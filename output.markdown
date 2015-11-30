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

# Roma to Iader

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a journey of about 64 miles. 

A breeze from an unexpected quarter cools the air. A cloud passes in front of the sun. 

Insert story about 413231

Insert story about ['42.412', '12.467']

Leaving Ocriculum, Virgil set out for Narnia by road, a distance of about 8 miles. 

Now the road is quieter. His shoes are covered in dust from the road. Along the road are graves, and a cenotaph. He passes another milestone. He set out from {from} amidst a throng travelling the same way. They pass a pillar on the right surmounted by a stone urn. By the road is a salt spring. 

Insert story about 413225

Insert story about ['42.52', '12.516']

From Narnia to Spoletium is about 22 miles away when travelling by road. 

A caravan from {destination} passed by. He left the city early, before the rising of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 413320

Insert story about ['42.745', '12.738']

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, at least 90 miles. 

Now the road is quieter. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A caravan from {destination} passed by. There is a fountain of cold water springing from the rock. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He left the city early, before the rising of the sun. 

Insert story about 413129

Insert story about ['43.845', '13.017']

From Fanum Fortunae to Ariminum is at least 38 miles when travelling by ship down the coast. 

A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Down in a heap comes a broken mountain of water. The yawning billow shows ground amid the surge, where the sea churns with sand. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 393379

Insert story about ['44.059', '12.563']

From Ariminum to Fanum Fortunae is at least 38 miles when travelling by ship down the coast. 

Black night broods on the waters. All nature, big with instant ruin, frowned destruction. Down in a heap comes a broken mountain of water. The yawning billow shows ground amid the surge, where the sea churns with sand. They hang on the wave's ridge. The helmsman is dashed away and rolled forward headlong. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 413129

Insert story about ['43.845', '13.017']

Leaving Fanum Fortunae, Virgil set out for Ancona by ship down the coast, a distance of about 42 miles. 

Then comes the creak of cables and the cries of seamen. All around from pole to pole the rattling peals resound. The oars are snapped. The south wind catches and hurls a ship on hidden rocks. Rocks amid the waves, a vast reef banking the sea. Before their eyes a vast sea descending strikes astern. 

Insert story about 413014

Insert story about ['43.616', '13.519']

Intending to travel by ship down the coast to Iader, Virgil left Ancona. It was about 107 miles away. 

A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The yawning billow shows ground amid the surge, where the sea churns with sand. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. 

Insert story about 197312

Insert story about ['44.115', '15.229']

\newpage


# Iader to Reate

From Iader to Titius (river) is a distance of about 48 miles when travelling by ship down the coast. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Black night broods on the waters. All around from pole to pole the rattling peals resound. Piteous to see, it dashes on shoals and girdles with a sandbank. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

There was no story for None

Insert story about ['43.72', '15.86']

From Titius (river) to Iader is a distance of about 48 miles when travelling by ship down the coast. 

A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The prow swings away and gives her side to the waves. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. Before their eyes a vast sea descending strikes astern. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 197312

Insert story about ['44.115', '15.229']

Virgil departed from Iader, intending to travel by road to Burnum, a journey of about 40 miles. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 197184

Insert story about ['44.032', '15.994']

Virgil departed from Burnum, intending to travel by road to Salona, about 50 miles away. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He left the city early, before the rising of the sun. 

Insert story about 197488

Insert story about ['43.54', '16.483']

Virgil departed from Salona, intending to travel by ship down the coast to Aternum, a journey of about 153 miles. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Frequent flashes light the lurid air. All nature, big with instant ruin, frowned destruction. They hang on the wave's ridge. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 413039

Insert story about ['42.465', '14.214']

From Aternum to Castrum Truentinum is about 38 miles away when travelling by ship down the coast. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Frequent flashes light the lurid air. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The oars are snapped. The prow swings away and gives her side to the waves. The east wind forces a ship from the deep into shallows and quicksands. The helmsman is dashed away and rolled forward headlong. 

Insert story about 413074

Insert story about ['42.914', '13.904']

Leaving Castrum Truentinum, Virgil set out for Asculum by road, at least 17 miles. 

He left the city early, before the rising of the sun. Above the roads are ruins, among which is a cave sacred to Asclepius. As they go up from {from}, they see the ruined walls. His shoes are covered in dust from the road. He set out from {from} amidst a throng travelling the same way. 

Insert story about 413036

Insert story about ['42.855', '13.575']

Intending to travel by road to Reate, Virgil left Asculum. It was at least 59 miles. 

He passes another milestone. Along the road are graves, and a cenotaph. They pass a pillar on the right surmounted by a stone urn. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. On the road from {from} to {destination} there is a village, in which there is a temple and grove. A caravan from {destination} passed by. There is a fountain of cold water springing from the rock. 

Insert story about 413283

Insert story about ['42.403', '12.861']

\newpage


# Reate to Formiae

Leaving Reate, Virgil set out for Roma by road, a journey of about 44 miles. 

There is a fountain of cold water springing from the rock. He set out from {from} amidst a throng travelling the same way. His shoes are covered in dust from the road. 

Insert story about 423025

Insert story about ['41.892', '12.486']

Intending to travel on a boat heading downstream to Ostia/Portus, Virgil left Roma. It was about 17 miles away. 

The countryside is quieter than the city. 

Insert story about 422995

Insert story about ['41.755', '12.288']

Intending to travel by ship down the coast to Tarracina, Virgil left Ostia/Portus. It was a journey of about 77 miles. 

A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The oars are snapped. Down in a heap comes a broken mountain of water. 

Insert story about 433143

Insert story about ['41.291', '13.249']

Leaving Tarracina, Virgil set out for Formiae by ship down the coast, a journey of about 24 miles. 

Black night broods on the waters. All around from pole to pole the rattling peals resound. Frequent flashes light the lurid air. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The oars are snapped. The south wind catches and hurls a ship on hidden rocks. The helmsman is dashed away and rolled forward headlong. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 432839

Insert story about ['41.256', '13.606']

Virgil departed from Formiae, intending to travel by ship down the coast to Minturnae, about 18 miles away. 

Then comes the creak of cables and the cries of seamen. Black night broods on the waters. All around from pole to pole the rattling peals resound. Frequent flashes light the lurid air. All nature, big with instant ruin, frowned destruction. Rocks amid the waves, a vast reef banking the sea. The helmsman is dashed away and rolled forward headlong. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. 

Insert story about 432940

Insert story about ['41.242', '13.769']

Leaving Minturnae, Virgil set out for Formiae by ship down the coast, about 18 miles away. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Black night broods on the waters. All around from pole to pole the rattling peals resound. The yawning billow shows ground amid the surge, where the sea churns with sand. Piteous to see, it dashes on shoals and girdles with a sandbank. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 432839

Insert story about ['41.256', '13.606']

Intending to travel by ship down the coast to Minturnae, Virgil left Formiae. It was about 18 miles away. 

Then comes the creak of cables and the cries of seamen. Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The prow swings away and gives her side to the waves. Down in a heap comes a broken mountain of water. The south wind catches and hurls a ship on hidden rocks. Rocks amid the waves, a vast reef banking the sea. Piteous to see, it dashes on shoals and girdles with a sandbank. Before their eyes a vast sea descending strikes astern. 

Insert story about 432940

Insert story about ['41.242', '13.769']

Leaving Minturnae, Virgil set out for Formiae by ship down the coast, a distance of about 18 miles. 

Black night broods on the waters. All nature, big with instant ruin, frowned destruction. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. 

Insert story about 432839

Insert story about ['41.256', '13.606']

\newpage


# Formiae to Ocriculum

Intending to travel by ship down the coast to Tarracina, Virgil left Formiae. It was a distance of about 24 miles. 

Then comes the creak of cables and the cries of seamen. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. Before their eyes a vast sea descending strikes astern. The helmsman is dashed away and rolled forward headlong. 

Insert story about 433143

Insert story about ['41.291', '13.249']

Virgil departed from Tarracina, intending to travel on a boat heading upstream to Forum Appii, at least 14 miles. 

Birds sing their greetings. No backward glances for the city left behind. 

There was no story for None

From Forum Appii to Tarracina is a journey of about 14 miles when travelling on a boat heading downstream. 

A breeze from an unexpected quarter cools the air. No backward glances for the city left behind. 

Insert story about 433143

Insert story about ['41.291', '13.249']

Leaving Tarracina, Virgil set out for Forum Appii on a boat heading upstream, a journey of about 14 miles. 

No backward glances for the city left behind. The sun beats down. A cloud passes in front of the sun. 

There was no story for None

Leaving Forum Appii, Virgil set out for Roma by road, a distance of about 42 miles. 

He set out from {from} amidst a throng travelling the same way. A caravan from {destination} passed by. They pass a pillar on the right surmounted by a stone urn. He left the city early, before the rising of the sun. There is a fountain of cold water springing from the rock. A cloud passes in front of the sun. 

Insert story about 423025

Insert story about ['41.892', '12.486']

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a distance of about 64 miles. 

A cloud passes in front of the sun. 

Insert story about 413231

Insert story about ['42.412', '12.467']

Leaving Ocriculum, Virgil set out for Narnia by road, about 8 miles away. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Above the roads are ruins, among which is a cave sacred to Asclepius. He passes another milestone. The sun beats down.. 

Insert story about 413225

Insert story about ['42.52', '12.516']

From Narnia to Ocriculum is about 8 miles away when travelling by road. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He passes another milestone. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 413231

Insert story about ['42.412', '12.467']

\newpage


# Ocriculum to Placentia

Leaving Ocriculum, Virgil set out for Narnia by road, a journey of about 8 miles. 

As they go up from {from}, they see the ruined walls. The sun beats down.. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 413225

Insert story about ['42.52', '12.516']

Virgil departed from Narnia, intending to travel by road to Spoletium, a distance of about 22 miles. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Now the road is quieter. By the road is a salt spring. There is a fountain of cold water springing from the rock. A caravan from {destination} passed by. On the road from {from} to {destination} there is a village, in which there is a temple and grove. 

Insert story about 413320

Insert story about ['42.745', '12.738']

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, about 90 miles away. 

He set out from {from} amidst a throng travelling the same way. His shoes are covered in dust from the road. They pass a pillar on the right surmounted by a stone urn. The sun beats down.. 

Insert story about 413129

Insert story about ['43.845', '13.017']

From Fanum Fortunae to Ariminum is at least 38 miles when travelling by ship down the coast. 

Frequent flashes light the lurid air. The oars are snapped. Scattered swimmers appear in the vast eddy; armour of men, timbers and treasure amid the water. 

Insert story about 393379

Insert story about ['44.059', '12.563']

Intending to travel by road to Faventia, Virgil left Ariminum. It was a journey of about 38 miles. 

The sun beats down.. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. As they go up from {from}, they see the ruined walls. A caravan from {destination} passed by. He passes another milestone. He left the city early, before the rising of the sun. On the road from {from} to {destination} there is a village, in which there is a temple and grove. 

Insert story about 393420

Insert story about ['44.286', '11.884']

Leaving Faventia, Virgil set out for Bononia by road, about 30 miles away. 

They pass a pillar on the right surmounted by a stone urn. There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. He left the city early, before the rising of the sun. 

Insert story about 393421

Insert story about ['44.495', '11.349']

Leaving Bononia, Virgil set out for a village on a military boat floating downstream, a journey of about 39 miles. 

A breeze from an unexpected quarter cools the air. He presses onward. 

There was no story for None

From a village to Placentia is about 140 miles away when travelling on a military boat headed upstream. 

The sun beats down. No backward glances for the city left behind. The countryside is quieter than the city. 

Insert story about 383741

Insert story about ['45.052', '9.699']

\newpage


# Placentia to Altinum

From Placentia to a village is a distance of about 11 miles when travelling by road. 

As they go up from {from}, they see the ruined walls. He left the city early, before the rising of the sun. He passes another milestone. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

There was no story for None

From a village to Mediolanum is a distance of about 27 miles when travelling by road. 

The sun beats down.. By the road is a salt spring. He passes another milestone. A cloud passes in front of the sun. He set out from {from} amidst a throng travelling the same way. As they go up from {from}, they see the ruined walls. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 383706

Insert story about ['45.464', '9.188']

Virgil departed from Mediolanum, intending to travel by road to Verona, a journey of about 101 miles. 

A caravan from {destination} passed by. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Now the road is quieter. His shoes are covered in dust from the road. On the road from {from} to {destination} there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. 

Insert story about 383816

Insert story about ['45.439', '10.994']

Leaving Verona, Virgil set out for Patavium by road, a distance of about 50 miles. 

As they go up from {from}, they see the ruined walls. Along the road are graves, and a cenotaph. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A caravan from {destination} passed by. He passes another milestone. Above the roads are ruins, among which is a cave sacred to Asclepius. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 393473

Insert story about ['45.41', '11.877']

Leaving Patavium, Virgil set out for a village by road, about 13 miles away. 

A caravan from {destination} passed by. On the road from {from} to {destination} there is a village, in which there is a temple and grove. He passes another milestone. He set out from {from} amidst a throng travelling the same way. 

There was no story for None

Leaving a village, Virgil set out for Altinum by road, a distance of about 14 miles. 

They pass a pillar on the right surmounted by a stone urn. He set out from {from} amidst a throng travelling the same way. He passes another milestone. The sun beats down.. His shoes are covered in dust from the road. 

Insert story about 393374

Insert story about ['45.579', '12.373']

Intending to travel by ship down the coast to Brundulum, Virgil left Altinum. It was a distance of about 27 miles. 

Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Black night broods on the waters. All around from pole to pole the rattling peals resound. Frequent flashes light the lurid air. Down in a heap comes a broken mountain of water. The east wind forces a ship from the deep into shallows and quicksands. Piteous to see, it dashes on shoals and girdles with a sandbank. Before their eyes a vast sea descending strikes astern. 

There was no story for None

Insert story about ['45.19', '12.31']

From Brundulum to Altinum is about 27 miles away when travelling by ship down the coast. 

Then comes the creak of cables and the cries of seamen. The oars are snapped. They hang on the wave's ridge. The east wind forces a ship from the deep into shallows and quicksands. 

Insert story about 393374

Insert story about ['45.579', '12.373']

\newpage


# Altinum to Pons Drusi

Virgil departed from Altinum, intending to travel by road to Iulia Concordia, at least 26 miles. 

Above the roads are ruins, among which is a cave sacred to Asclepius. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 393441

Insert story about ['45.757', '12.844']

Leaving Iulia Concordia, Virgil set out for Aquileia by road, about 26 miles away. 

By the road is a salt spring. Above the roads are ruins, among which is a cave sacred to Asclepius. He left the city early, before the rising of the sun. As they go up from {from}, they see the ruined walls. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A cloud passes in front of the sun. 

Insert story about 187290

Insert story about ['45.768', '13.365']

Leaving Aquileia, Virgil set out for Ad Tricesimum by road, a distance of about 28 miles. 

Along the road are graves, and a cenotaph. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187259

Insert story about ['46.158', '13.216']

Leaving Ad Tricesimum, Virgil set out for Aquileia by road, at least 28 miles. 

They pass a pillar on the right surmounted by a stone urn. A cloud passes in front of the sun. 

Insert story about 187290

Insert story about ['45.768', '13.365']

Leaving Aquileia, Virgil set out for Iulia Concordia by road, about 26 miles away. 

He left the city early, before the rising of the sun. There is a fountain of cold water springing from the rock. He set out from {from} amidst a throng travelling the same way. By the road is a salt spring. 

Insert story about 393441

Insert story about ['45.757', '12.844']

Intending to travel by road to Tridentum, Virgil left Iulia Concordia. It was about 103 miles away. 

They pass a pillar on the right surmounted by a stone urn. Now the road is quieter. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 383804

Insert story about ['46.067', '11.119']

Virgil departed from Tridentum, intending to travel by road to Endidae, about 20 miles away. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. There is a fountain of cold water springing from the rock. He set out from {from} amidst a throng travelling the same way. As they go up from {from}, they see the ruined walls. 

Insert story about 187368

Insert story about ['46.318', '11.274']

Leaving Endidae, Virgil set out for Pons Drusi by road, a distance of about 13 miles. 

The sun beats down.. His shoes are covered in dust from the road. By the road is a salt spring. Along the road are graves, and a cenotaph. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A caravan from {destination} passed by. He passes another milestone. 

Insert story about 187518

Insert story about ['46.497', '11.358']

\newpage


# Pons Drusi to Brigantium

From Pons Drusi to a village is at least 28 miles when travelling by road. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Now the road is quieter. He passes another milestone. 

There was no story for None

Leaving a village, Virgil set out for Veldidena by road, at least 41 miles. 

Along the road are graves, and a cenotaph. On the road from {from} to {destination} there is a village, in which there is a temple and grove. A caravan from {destination} passed by. Now the road is quieter. He passes another milestone. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 187608

Insert story about ['47.254', '11.4']

Leaving Veldidena, Virgil set out for a village by road, a journey of about 41 miles. 

Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from {destination} passed by. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

There was no story for None

Intending to travel by road to Pons Drusi, Virgil left a village. It was a journey of about 28 miles. 

His shoes are covered in dust from the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Now the road is quieter. The sun beats down.. 

Insert story about 187518

Insert story about ['46.497', '11.358']

Virgil departed from Pons Drusi, intending to travel by road to Maiensis Statio, a distance of about 15 miles. 

A cloud passes in front of the sun. By the road is a salt spring. 

There was no story for None

Insert story about ['0', '0']

Virgil departed from Maiensis Statio, intending to travel by road to Abodiacum, about 140 miles away. 

Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from {destination} passed by. 

Insert story about 187242

Insert story about ['47.91', '10.91']

Virgil departed from Abodiacum, intending to travel by road to Cambodunum, at least 31 miles. 

He set out from {from} amidst a throng travelling the same way. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He passes another milestone. On the road from {from} to {destination} there is a village, in which there is a temple and grove. His shoes are covered in dust from the road. The sun beats down.. Now the road is quieter. 

Insert story about 187335

Insert story about ['47.727', '10.327']

Leaving Cambodunum, Virgil set out for Brigantium by road, about 36 miles away. 

The sun beats down.. He passes another milestone. They pass a pillar on the right surmounted by a stone urn. Along the road are graves, and a cenotaph. He left the city early, before the rising of the sun. 

Insert story about 187325

Insert story about ['47.503', '9.747']

\newpage


# Brigantium to Aventicum

From Brigantium to Curia is a distance of about 50 miles when travelling by road. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There is a fountain of cold water springing from the rock. By the road is a salt spring. His shoes are covered in dust from the road. He set out from {from} amidst a throng travelling the same way. As they go up from {from}, they see the ruined walls. 

Insert story about 187357

Insert story about ['46.849', '9.531']

From Curia to Comum is about 92 miles away when travelling by road. 

As they go up from {from}, they see the ruined walls. He passes another milestone. Now the road is quieter. He set out from {from} amidst a throng travelling the same way. He left the city early, before the rising of the sun. A cloud passes in front of the sun. By the road is a salt spring. 

Insert story about 383627

Insert story about ['45.812', '9.086']

From Comum to Curia is at least 92 miles when travelling by road. 

He left the city early, before the rising of the sun. A caravan from {destination} passed by. He set out from {from} amidst a throng travelling the same way. As they go up from {from}, they see the ruined walls. The sun beats down.. By the road is a salt spring. Now the road is quieter. 

Insert story about 187357

Insert story about ['46.849', '9.531']

Intending to travel by road to Brigantium, Virgil left Curia. It was a journey of about 50 miles. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. His shoes are covered in dust from the road. Now the road is quieter. By the road is a salt spring. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The sun beats down.. 

Insert story about 187325

Insert story about ['47.503', '9.747']

Intending to travel by road to Cambodunum, Virgil left Brigantium. It was at least 36 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There is a fountain of cold water springing from the rock. On the road from {from} to {destination} there is a village, in which there is a temple and grove. 

Insert story about 187335

Insert story about ['47.727', '10.327']

Virgil departed from Cambodunum, intending to travel by road to Brigantium, at least 36 miles. 

He set out from {from} amidst a throng travelling the same way. By the road is a salt spring. On the road from {from} to {destination} there is a village, in which there is a temple and grove. Along the road are graves, and a cenotaph. He left the city early, before the rising of the sun. 

Insert story about 187325

Insert story about ['47.503', '9.747']

Leaving Brigantium, Virgil set out for Augusta Raurica on a military boat headed upstream, at least 119 miles. 

A breeze from an unexpected quarter cools the air. 

Insert story about 177494

Insert story about ['47.533', '7.722']

Intending to travel by road to Aventicum, Virgil left Augusta Raurica. It was at least 58 miles. 

Now the road is quieter. A caravan from {destination} passed by. There is a fountain of cold water springing from the rock. 

Insert story about 177495

Insert story about ['46.88', '7.041']

\newpage


# Aventicum to Veldidena

From Aventicum to Augusta Raurica is about 58 miles away when travelling by road. 

He left the city early, before the rising of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There is a fountain of cold water springing from the rock. As they go up from {from}, they see the ruined walls. He passes another milestone. 

Insert story about 177494

Insert story about ['47.533', '7.722']

From Augusta Raurica to Brigantium is at least 119 miles when travelling on a military boat floating downstream. 

The countryside is quieter than the city. A cloud passes in front of the sun. He presses onward. 

Insert story about 187325

Insert story about ['47.503', '9.747']

From Brigantium to Cambodunum is a distance of about 36 miles when travelling by road. 

Now the road is quieter. By the road is a salt spring. His shoes are covered in dust from the road. He left the city early, before the rising of the sun. A cloud passes in front of the sun. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 187335

Insert story about ['47.727', '10.327']

Intending to travel by road to Abodiacum, Virgil left Cambodunum. It was at least 31 miles. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. He set out from {from} amidst a throng travelling the same way. They pass a pillar on the right surmounted by a stone urn. There is a fountain of cold water springing from the rock. 

Insert story about 187242

Insert story about ['47.91', '10.91']

From Abodiacum to Cambodunum is about 31 miles away when travelling by road. 

The sun beats down.. His shoes are covered in dust from the road. He left the city early, before the rising of the sun. Along the road are graves, and a cenotaph. A cloud passes in front of the sun. By the road is a salt spring. 

Insert story about 187335

Insert story about ['47.727', '10.327']

From Cambodunum to Abodiacum is a distance of about 31 miles when travelling by road. 

Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He passes another milestone. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. As they go up from {from}, they see the ruined walls. His shoes are covered in dust from the road. A caravan from {destination} passed by. They pass a pillar on the right surmounted by a stone urn. 

Insert story about 187242

Insert story about ['47.91', '10.91']

Virgil departed from Abodiacum, intending to travel by road to Parthanum, a distance of about 40 miles. 

A cloud passes in front of the sun. He left the city early, before the rising of the sun. By the road is a salt spring. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Now the road is quieter. Along the road are graves, and a cenotaph. 

Insert story about 187505

Insert story about ['47.492', '11.086']

Virgil departed from Parthanum, intending to travel by road to Veldidena, about 32 miles away. 

He passes another milestone. Along the road are graves, and a cenotaph. He left the city early, before the rising of the sun. He set out from {from} amidst a throng travelling the same way. 

Insert story about 187608

Insert story about ['47.254', '11.4']

\newpage


# Veldidena to a village

Virgil departed from Veldidena, intending to travel by road to Parthanum, at least 32 miles. 

A cloud passes in front of the sun. A caravan from {destination} passed by. As they go up from {from}, they see the ruined walls. On the road from {from} to {destination} there is a village, in which there is a temple and grove. Now the road is quieter. 

Insert story about 187505

Insert story about ['47.492', '11.086']

Virgil departed from Parthanum, intending to travel by road to Veldidena, a distance of about 32 miles. 

There is a fountain of cold water springing from the rock. He left the city early, before the rising of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A cloud passes in front of the sun. Along the road are graves, and a cenotaph. As they go up from {from}, they see the ruined walls. 

Insert story about 187608

Insert story about ['47.254', '11.4']

Leaving Veldidena, Virgil set out for a village by road, a journey of about 41 miles. 

A cloud passes in front of the sun. There is a fountain of cold water springing from the rock. They pass a pillar on the right surmounted by a stone urn. He passes another milestone. 

There was no story for None

From a village to Aguntum is about 60 miles away when travelling by road. 

There is a fountain of cold water springing from the rock. His shoes are covered in dust from the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 187265

Insert story about ['46.827', '12.823']

Intending to travel by road to Iulium Carnicum, Virgil left Aguntum. It was a distance of about 33 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. His shoes are covered in dust from the road. Along the road are graves, and a cenotaph. There is a fountain of cold water springing from the rock. Now the road is quieter. 

Insert story about 187430

Insert story about ['46.461', '13.026']

Intending to travel by road to a village, Virgil left Iulium Carnicum. It was at least 9 miles. 

He left the city early, before the rising of the sun. They pass a pillar on the right surmounted by a stone urn. 

There was no story for None

Virgil departed from a village, intending to travel by road to Santicum, about 47 miles away. 

Now the road is quieter. A caravan from {destination} passed by. He passes another milestone. 

Insert story about 187537

Insert story about ['46.616', '13.849']

Intending to travel by road to a village, Virgil left Santicum. It was at least 47 miles. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. He passes another milestone. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

There was no story for None

\newpage


# a village to a village

From a village to Santicum is at least 47 miles when travelling by road. 

By the road is a salt spring. As they go up from {from}, they see the ruined walls. He passes another milestone. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 187537

Insert story about ['46.616', '13.849']

From Santicum to Virunum is at least 28 miles when travelling by road. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He left the city early, before the rising of the sun. Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. He set out from {from} amidst a throng travelling the same way. 

Insert story about 197583

Insert story about ['46.703', '14.36']

Virgil departed from Virunum, intending to travel on a boat heading downstream to Poetovio, a journey of about 96 miles. 

A cloud passes in front of the sun. Birds sing their greetings. 

Insert story about 197446

Insert story about ['46.42', '15.87']

From Poetovio to Mursa is at least 187 miles when travelling on a military boat floating downstream. 

Birds sing their greetings. 

Insert story about 197389

Insert story about ['45.56', '18.676']

Leaving Mursa, Virgil set out for Cibalae by road, a distance of about 21 miles. 

He set out from {from} amidst a throng travelling the same way. There is a fountain of cold water springing from the rock. He passes another milestone. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A cloud passes in front of the sun. He left the city early, before the rising of the sun. A caravan from {destination} passed by. 

Insert story about 197207

Insert story about ['45.291', '18.801']

Virgil departed from Cibalae, intending to travel by road to Sirmium, a journey of about 46 miles. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. He passes another milestone. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The sun beats down.. 

Insert story about 207447

Insert story about ['44.966', '19.61']

Leaving Sirmium, Virgil set out for a village by road, at least 56 miles. 

Along the road are graves, and a cenotaph. A cloud passes in front of the sun. By the road is a salt spring. 

There was no story for None

Leaving a village, Virgil set out for a village by road, a journey of about 130 miles. 

Now the road is quieter. Along the road are graves, and a cenotaph. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. The sun beats down.. A caravan from {destination} passed by. A cloud passes in front of the sun. 

There was no story for None

\newpage


# a village to Viminacium

Leaving a village, Virgil set out for Narona by road, about 15 miles away. 

Now the road is quieter. Along the road are graves, and a cenotaph. 

Insert story about 197400

Insert story about ['43.081', '17.628']

Intending to travel by road to a village, Virgil left Narona. It was about 15 miles away. 

There is a fountain of cold water springing from the rock. He left the city early, before the rising of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He set out from {from} amidst a throng travelling the same way. 

There was no story for None

Virgil departed from a village, intending to travel by road to a village, a journey of about 130 miles. 

A caravan from {destination} passed by. He left the city early, before the rising of the sun. His shoes are covered in dust from the road. On the road from {from} to {destination} there is a village, in which there is a temple and grove. 

There was no story for None

Virgil departed from a village, intending to travel by road to Domavium, a journey of about 18 miles. 

A caravan from {destination} passed by. He set out from {from} amidst a throng travelling the same way. The sun beats down.. 

Insert story about 207088

Insert story about ['44.144', '19.363']

From Domavium to a village is about 18 miles away when travelling by road. 

He passes another milestone. They pass a pillar on the right surmounted by a stone urn. Now the road is quieter. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. His shoes are covered in dust from the road. 

There was no story for None

Intending to travel by road to Sirmium, Virgil left a village. It was a distance of about 56 miles. 

A cloud passes in front of the sun. He left the city early, before the rising of the sun. On the road from {from} to {destination} there is a village, in which there is a temple and grove. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. As they go up from {from}, they see the ruined walls. His shoes are covered in dust from the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

Insert story about 207447

Insert story about ['44.966', '19.61']

Intending to travel on a military boat floating downstream to Singidunum, Virgil left Sirmium. It was a distance of about 85 miles. 

He presses onward. 

Insert story about 207443

Insert story about ['44.802', '20.466']

Virgil departed from Singidunum, intending to travel on a military boat floating downstream to Viminacium, about 49 miles away. 

The sun beats down. The journey is more tiring than you might expect. 

Insert story about 207549

Insert story about ['44.716', '21.167']

\newpage


# Viminacium to Naissus

Leaving Viminacium, Virgil set out for Tibiscum by road, at least 96 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He set out from {from} amidst a throng travelling the same way. Above the roads are ruins, among which is a cave sacred to Asclepius. 

Insert story about 207495

Insert story about ['45.459', '22.186']

Virgil departed from Tibiscum, intending to travel by road to Viminacium, a journey of about 96 miles. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. He passes another milestone. Along the road are graves, and a cenotaph. A cloud passes in front of the sun. 

Insert story about 207549

Insert story about ['44.716', '21.167']

Virgil departed from Viminacium, intending to travel on a military boat headed upstream to Singidunum, at least 49 miles. 

A breeze from an unexpected quarter cools the air. He presses onward. A cloud passes in front of the sun. 

Insert story about 207443

Insert story about ['44.802', '20.466']

Virgil departed from Singidunum, intending to travel on a military boat floating downstream to Viminacium, at least 49 miles. 

No backward glances for the city left behind. The countryside is quieter than the city. 

Insert story about 207549

Insert story about ['44.716', '21.167']

From Viminacium to Horreum Margi is about 57 miles away when travelling by road. 

The sun beats down.. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. By the road is a salt spring. Above the roads are ruins, among which is a cave sacred to Asclepius. 

There was no story for None

Leaving Horreum Margi, Virgil set out for Naissus by road, a journey of about 51 miles. 

He left the city early, before the rising of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from {destination} passed by. As they go up from {from}, they see the ruined walls. 

Insert story about 207303

Insert story about ['43.316', '21.894']

Leaving Naissus, Virgil set out for Ulpiana by road, about 80 miles away. 

By the road is a salt spring. Along the road are graves, and a cenotaph. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He passes another milestone. He left the city early, before the rising of the sun. They pass a pillar on the right surmounted by a stone urn. 

There was no story for None

Insert story about ['0', '0']

From Ulpiana to Naissus is about 80 miles away when travelling by road. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. As they go up from {from}, they see the ruined walls. 

Insert story about 207303

Insert story about ['43.316', '21.894']

\newpage


# Naissus to Taliata

Virgil departed from Naissus, intending to travel by road to Bononia (Moesia), a journey of about 76 miles. 

He left the city early, before the rising of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 206975

Insert story about ['43.993', '22.876']

From Bononia (Moesia) to Taliata is a journey of about 58 miles when travelling by road. 

Now the road is quieter. Above the roads are ruins, among which is a cave sacred to Asclepius. They pass a pillar on the right surmounted by a stone urn. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. His shoes are covered in dust from the road. 

Insert story about 207485

Insert story about ['44.444', '22.144']

Virgil departed from Taliata, intending to travel by road to Bononia (Moesia), about 58 miles away. 

A caravan from {destination} passed by. On the road from {from} to {destination} there is a village, in which there is a temple and grove. The sun beats down.. 

Insert story about 206975

Insert story about ['43.993', '22.876']

Leaving Bononia (Moesia), Virgil set out for Taliata by road, a distance of about 58 miles. 

On the road from {from} to {destination} there is a village, in which there is a temple and grove. He passes another milestone. Now the road is quieter. 

Insert story about 207485

Insert story about ['44.444', '22.144']

Virgil departed from Taliata, intending to travel by road to Drobeta, a distance of about 35 miles. 

By the road is a salt spring. A caravan from {destination} passed by. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There is a fountain of cold water springing from the rock. Along the road are graves, and a cenotaph. The sun beats down.. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

Insert story about 207100

Insert story about ['44.636', '22.66']

Leaving Drobeta, Virgil set out for Taliata by road, a distance of about 35 miles. 

As they go up from {from}, they see the ruined walls. A caravan from {destination} passed by. The sun beats down.. 

Insert story about 207485

Insert story about ['44.444', '22.144']

From Taliata to Dierna is a journey of about 22 miles when travelling on a military boat floating downstream. 

A breeze from an unexpected quarter cools the air. 

Insert story about 207078

Insert story about ['44.725', '22.396']

Leaving Dierna, Virgil set out for Taliata on a boat heading upstream, a journey of about 22 miles. 

A breeze from an unexpected quarter cools the air. No backward glances for the city left behind. He presses onward. 

Insert story about 207485

Insert story about ['44.444', '22.144']

\newpage


# Taliata to Dyrrhachium

Virgil departed from Taliata, intending to travel by road to Bononia (Moesia), a distance of about 58 miles. 

Now the road is quieter. Along the road are graves, and a cenotaph. By the road is a salt spring. On the road from {from} to {destination} there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. Above the roads are ruins, among which is a cave sacred to Asclepius. The sun beats down.. 

Insert story about 206975

Insert story about ['43.993', '22.876']

From Bononia (Moesia) to Naissus is about 76 miles away when travelling by road. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A caravan from {destination} passed by. 

Insert story about 207303

Insert story about ['43.316', '21.894']

Virgil departed from Naissus, intending to travel by road to Serdica, a distance of about 92 miles. 

He passes another milestone. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He set out from {from} amidst a throng travelling the same way. 

Insert story about 207439

Insert story about ['42.723', '23.343']

Leaving Serdica, Virgil set out for Stobi by road, at least 125 miles. 

A caravan from {destination} passed by. On the road from {from} to {destination} there is a village, in which there is a temple and grove. His shoes are covered in dust from the road. There is a fountain of cold water springing from the rock. The sun beats down.. 

Insert story about 491731

Insert story about ['41.531', '21.978']

From Stobi to Heraklea is a distance of about 54 miles when travelling by road. 

Now the road is quieter. He set out from {from} amidst a throng travelling the same way. As they go up from {from}, they see the ruined walls. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. By the road is a salt spring. 

Insert story about 481861

Insert story about ['41.032', '21.336']

Intending to travel by road to a village, Virgil left Heraklea. It was about 109 miles away. 

He set out from {from} amidst a throng travelling the same way. Along the road are graves, and a cenotaph. There is a fountain of cold water springing from the rock. As they go up from {from}, they see the ruined walls. 

There was no story for None

Leaving a village, Virgil set out for Apollonia (Epirus) by road, a distance of about 23 miles. 

By the road is a salt spring. A cloud passes in front of the sun. As they go up from {from}, they see the ruined walls. Now the road is quieter. A caravan from {destination} passed by. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He passes another milestone. 

There was no story for None

Insert story about ['40.77', '19.43']

From Apollonia (Epirus) to Dyrrhachium is a distance of about 42 miles when travelling by ship down the coast. 

All nature, big with instant ruin, frowned destruction. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. The yawning billow shows ground amid the surge, where the sea churns with sand. The south wind catches and hurls a ship on hidden rocks. Rocks amid the waves, a vast reef banking the sea. The east wind forces a ship from the deep into shallows and quicksands. Piteous to see, it dashes on shoals and girdles with a sandbank. Before their eyes a vast sea descending strikes astern. 

Insert story about 481818

Insert story about ['41.316', '19.45']

\newpage
