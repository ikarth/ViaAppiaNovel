% Virgil's Commonplace Book
% Isaac Karth

## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These texts were not always attributed to the original source. Lacking the modern concept of plagiarism (and our post-printing-press system of uniform citations) writers sometimes come off as careless to modern sensibilities. Quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.
 
In a way, this reuse is fortunate: many texts from the Classical period only exist in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.

Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. The closest literary antecedents of NaNoGenMo--Dada and Oulipo--have often explored similar sampling approaches. Kathryn Hume has suggested that technical constraints have lead NaNoGenMo to "align itself with poetics of recontextualization and reassembly."^[Hume, Kathryn. "NaNoGenMo: Dada 2.0". URL:\url{http://arcade.stanford.edu/blogs/nanogenmo-dada-20}. Accessed: 2015-11-28. (Archived by WebCite® at \url{http://www.webcitation.org/6dNl9xpbY})] 

NaNoGenMo has included other approaches, such as the concrete poetry in thricedotted's _The Seeker_, or the way structurally-plotted works like _Hannah and The Twelve-Disk Tower of Hanoi_ evoke the chessboard constraints of _Life a User's Manual_ or _Through the Looking Glass_. But there is an undeniable strand of appropriation as we teach our machines to imitate their human creators. Still, that's no reason to neglect giving credit, so this book attempts to cite the sources for the texts it borrows.

In this work, that deliberate borrowing is the intent. Unlike an age of precious codices, the information age is a time of entirely too much to read. Search engines can find anything you ask for but, like a fairy-tale mirror, can only answer the questions you know enough to ask in the first place. The serendipity of browsing through a library is lost. Extracting the stories and arranging them in a new pattern presents a new angle. Rather than an exhaustive view of the forest, it picks out one or two trees you might have otherwise overlooked.

I chose Virgil as the protagonist for three reasons: first, his works are among the source texts in the Perseus Digital Library used for much of the text here. His _Aeneid_ builds on earlier traditions, recast in a founding epic for a new age: appropriate for a work themed around appropriation and reuse in this new information age. This would not be enough to recommend him on its own: there are other authors whose works were much closer to the kind of copying and summarizing going on here. And _The Golden Ass_ by Apuleius, one of the earliest surviving novels, is closer in form to the travel tale that structures this generated novel. 

But there was also a tradition that linked Virgil and his poetry with magic and prophecy. It was no accident that Dante chose Virgil to be his guide through the _Inferno_. His memory is haunted by that touch of magic, a magic intimately linked with words and poetry. And, as Jeff Howard has pointed out,^[in _Game Magic: A Designer's Guide to Magic Systems in Theory and Practice_] programming is a form of magic. A magician-protagonist is entirely appropriate.

Lastly, that tradition of magic lead the much-neglected Avram Davidson to pen a novel with Vergil Magus as the magician-protagonist. My own pseudo-Virgil is a humble tribute, a machine homunculus librarian of forgotten texts.



Isaac Karth 

2015-11-28 

\newpage

## Technical Notes 

The book generator that produced this novel is a Python program that outputs a Markdown text file designed to be converted into PDF form via Pandoc. The source code for the NaNoGenMo version can be found at https://github.com/ikarth/ViaAppiaNovel in a git repository. 


~~~
pandoc output.markdown -S --normalize \
--toc -o via_appia_novel.pdf --latex-engine=xelatex \
--template novel_template.latex \
-V otherlangs=polutonikogreek,greek \
--variable lang="english" -V geometry:paperwidth=6in \
-V geometry:paperheight=9in -V geometry:margin=.9in \
-V fontfamily:"DejaVu Serif" -V linestretch:1.2 \
-V documentclass=book
~~~

This copy was generated November 30, 2015, with seeds of 753 and 3468.


The book generator uses data from the Perseus Digital Library, the Pelagios Project, the Pleiades Project, and ORBIS: The Stanford Geospatial Network Model of the Roman World.





\cleardoublepage


# Roma To Iader
  
## After Roma

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, about 64 miles away. 

The journey is more tiring than you might expect. By the gate of Ocriculum, these words were carved: Hermo(lai) Macrino et Cel/so co(n)s(ulibus) ex r(atione) Sextti(?) et Her(mae?). He presses onward. 

All of this brought to his mind what Cornelius Tacitus had said about Ocriculum:

## What Cornelius Tacitus Once Said About Ocriculum


While these successes were being achieved on the side of Vitellius, the army of Vespasian had left Narnia, and was passing the holiday of the Saturnalia in idleness at Ocriculum. The reason alleged for so injurious a delay was that they might wait for Mucianus. Some persons indeed there were who assailed Antonius with insinuations, that he lingered with treacherous intent, after receiving private letters from Vitellius, which conveyed to him the offer of the consulship and of the Emperor's daughter in marriage with a vast dowry, as the price of treason. Others asserted that this was all a fiction, invented to please Mucianus. Some again alleged that the policy agreed upon by all the generals was to threaten rather than actually to attack the capital, as Vitellius' strongest cohorts had revolted from him, and it seemed likely that, deprived of all support, he would abdicate the throne, but that the whole plan was ruined by the impatience and subsequent cowardice of Sabinus, who, after rashly taking up arms, had not been able to defend against three cohorts the great stronghold of the Capitol, which might have defied even the mightiest armies. One cannot, however, easily fix upon one man the blame which belongs to all. Mucianus did in fact delay the conquerors by ambig- uously-worded dispatches; Antonius, by a perverse acquiescence, or by an attempt to throw the odium upon another, laid himself open to blame; the other generals, by imagining that the war was over, contrived a distinction for its closing scene. Even Petilius Cerialis, though he had been sent on with a thousand cavalry by cross roads through the Sabine district so as to enter Rome by the Via Salaria, had not been sufficiently prompt in his movements, when the report of the siege of the Capitol put all alike on the alert.[^8cd27d4de0744700b482aeceda589443]

  
## Leaving Ocriculum By Road

Leaving Ocriculum, Virgil set out for Narnia by road, about 8 miles away. 

The road narrows here, an orchard wall encroaching on it. A grove of Minerva is hard by the road, a grove of poplar trees. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. An oxcart passes, loaded with grain. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There a spring wells up, and around about it is a meadow. 

While he visited his friend at Narnia, he was pleased to discover _Historiae_, by Cornelius Tacitus. Picking it up, he read:

## A Story By Cornelius Tacitus About Narnia From _Historiae_


Finding all their hopes cut off, the troops of Vitellius, intending to pass over to the side of the conqueror, but to do so with honour, marched down with their standards and colours into the plains beneath Narnia. The army of Vespasian, prepared and equipped as if for action, was drawn up in dense array on both sides of the road. The Vitellianists were received between the two columns; when they were thus surrounded, Antonius addressed them kindly. One division was ordered to remain at Narnia, another at Interamna; with them were left some of the victorious legions, which would not be formidable to them if they remained quiet, but were strong enough to crush all turbulence. At the same time Primus and Varus did not neglect to forward continual messages to Vitellius, offering him personal safety, the enjoyment of wealth, and a quiet retreat in Campania, provided he would lay down his arms and surrender himself and his children to Vespasian. Mucianus also wrote to him to the same effect, and Vitellius was often disposed to trust these overtures, and even discussed the number of his household and the choice of a residence on the coast. Such a lethargy had come over his spirit, that, had not others remembered he had been an Emperor, he would have himself forgotten it.[^fb5d69db56b34e41b73b5448942ccd02]

  
## 22 Miles To Spoletium

Virgil departed from Narnia, intending to travel by road to Spoletium, a journey of about 22 miles. 

They pass a pillar on the right surmounted by a stone urn. The sun beats down. On the road from Narnia to Spoletium there is a village, in which there is a temple and grove. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

While he was visiting Spoletium, he made a point of copying down what E. T. Merrill had written.

## Spoletium In _Commentary On Catullus_


On a certain unpopular Cominins, perhaps one of two brothers from Spoletium, P. and C. or L. Cominius, who are mentioned by Cicero (Cic. Cluent. 100) as prosecutors. In the year 66 B.C. a popular tumult terrified them into giving up their prosecution of C. Cornelius, though one of them, in spite of general unpopularity, resumed it the following year, on which occasion Cornelius was defended by Cicero.

cana senectus: cf. Catul. 61.162 cana anilitas .

spurcata impuris moribus: the hoary head that should be a crown of glory is to him but a mark of confirmed infamy.

bonorum: perhaps in the sense of _optimatium_ (as often in Cicero), if this Cominius was one of the prosecutors.

lingua exsecta: cf. Cic. Cluent. 187 Stratonem in crucem esse actum exsecta scitote lingua .

sit data: perfect, followed by the present _voret_, since the loss of the tongue, as a punishment for his perjuries, would be inflicted upon him before his execution and the throwing of his body to the crows and their associates.

vulturio: cf. Catul. 68.124n.

effossos oculos: etc., cf. Vulg. Proverb. 30.17 oculum … effodiant cum corvi de torrentibus, et comedant eum filii aquilae , Hor. Ep. 1.16.48 non pasces in cruce corvos . With vv. 5 and 6 Statius compares Ov. Ib. 167ff.

canes: cf. Hor. Ep. 17.11 addictum feris alitibus atque canibus .

lupi: cf. Hor. Ep. 5.99f., _post insepulta membra different lupi et Esquilinae alites_.[^9106d3e0c33a4bc68e76fa67e72e1a79]

  
## Leaving Spoletium By Road

From Spoletium to Fanum Fortunae is at least 90 miles when travelling by road. 

An oxcart passes, loaded with grain. On the road from Spoletium to Fanum Fortunae there is a village, in which there is a temple and grove. A caravan from Fanum Fortunae passed by. Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. Workers are raising the level of the road. Next to the straight road that leads to Fanum Fortunae, there is visible a sculpted tomb. There is a fountain of cold water springing from the rock. 

While he was visiting Fanum Fortunae, he made a point of copying down what Vitruvius Pollio had written.

## On The Subject Of Fanum Fortunae


1\. TIMBER should be felled between early Autumn and the time when Favonius begins to blow. For in Spring all trees become pregnant, and they are all employing their natural vigour in the production of leaves and of the fruits that return every year. The requirements of that season render them empty and swollen, and so they are weak and feeble because of their looseness of texture. This is also the case with women who have conceived. Their bodies are not considered perfectly healthy until the child is born; hence, pregnant slaves, when offered for sale, are not warranted sound, because the fetus as it grows within the body takes to itself as nourishment all the best qualities of the mother's food, and so the stronger it becomes as the full time for birth approaches, the less compact it allows that body to be from which it is produced. After the birth of the child, what was heretofore taken to promote the growth of another creature is now set free by the delivery of the newborn, and the channels being now empty and open, the body will take it in by lapping up its juices, and thus becomes compact and returns to the natural strength which it had before.

2\. On the same principle, with the ripening of the fruits in Autumn the leaves begin to wither and the trees, taking up their sap from the earth through the roots, recover themselves and are restored to their former solid texture. But the strong air of winter compresses and solidifies them during the time above mentioned. Consequently, if the timber is felled on the principle and at the time above mentioned, it will be felled at the proper season.

3\. In felling a tree we should cut into the trunk of it to the very heart, and then leave it standing so that the sap may drain out drop by drop throughout the whole of it. In this way the useless liquid which is within will run out through the sapwood instead of having to die in a mass of decay, thus spoiling the quality of the timber. Then and not till then, the tree being drained dry and the sap no longer dripping, let it be felled and it will be in the highest state of usefulness.

4\. That this is so may be seen in the case of fruit trees. When these are tapped at the base and pruned, each at the proper time, they pour out from the heart through the tapholes all the superfluous and corrupting fluid which they contain, and thus the draining process makes them durable. But when the juices of trees have no means of escape, they clot and rot in them, making the trees hollow and good for nothing. Therefore, if the draining process does not exhaust them while they are still alive, there is no doubt that, if the same principle is followed in felling them for timber, they will last a long time and be very useful in buildings.

5\. Trees vary and are unlike one another in their qualities. Thus it is with the oak, elm, poplar, cypress, fir, and the others which are most suitable to use in buildings. The oak, for instance, has not the efficacy of the fir, nor the cypress that of the elm. Nor in the case of other trees, is it natural that they should be alike; but the individual kinds are effective in building, some in one way, some in another, owing to the different properties of their elements.

6\. To begin with fir: it contains a great deal of air and fire with very little moisture and the earthy, so that, as its natural properties are of the lighter class, it is not heavy. Hence, its consistence being naturally stiff, it does not easily bend under the load, and keeps its straightness when used in the framework. But it contains so much heat that it generates and encourages decay, which spoils it; and it also kindles fire quickly because of the air in its body, which is so open that it takes in fire and so gives out a great flame.

7\. The part which is nearest to the earth before the tree is cut down takes up moisture through the roots from the immediate neighbourhood and hence is without knots and is "clear." But the upper part, on account of the great heat in it, throws up branches into the air through the knots; and this, when it is cut off about twenty feet from the ground and then hewn, is called "knotwood" because of its hardness and knottiness. The lowest part, after the tree is cut down and the sapwood of the same thrown away, is split up into four pieces and prepared for joiner's work, and so is called "clearstock."

8\. Oak, on the other hand, having enough and to spare of the earthy among its elements, and containing but little moisture, air, and fire, lasts for an unlimited period when buried in underground structures. It follows that when exposed to moisture, as its texture is not loose and porous, it cannot take in liquid on account of its compactness, but, withdrawing from the moisture, it resists it and warps, thus making cracks in the structures in which it is used.

9\. The winter oak, being composed of a moderate amount of all the elements, is very useful in buildings, but when in a moist place, it takes in water to its centre through its pores, its air and fire being expelled by the influence of the moisture, and so it rots. The Turkey oak and the beech, both containing a mixture of moisture, fire, and the earthy, with a great deal of air, through this loose texture take in moisture to their centre and soon decay. White and black poplar, as well as willow, linden, and the agnus castus, containing an abundance of fire and air, a moderate amount of moisture, and only a small amount of the earthy, are composed of a mixture which is proportionately rather light, and so they are of great service from their stiffness. Although on account of the mixture of the earthy in them they are not hard, yet their loose texture makes them gleaming white, and they are a convenient material to use in carving.

10\. The alder, which is produced close by river banks, and which seems to be altogether useless as building material, has really excellent qualities. It is composed of a very large proportion of air and fire, not much of the earthy, and only a little moisture. Hence, in swampy places, alder piles driven close together beneath the foundations of buildings take in the water which their own consistence lacks and remain imperishable forever, supporting structures of enormous weight and keeping them from decay. Thus a material which cannot last even a little while above ground, endures for a long time when covered with moisture.

11\. One can see this at its best in Ravenna; for there all the buildings, both public and private, have piles of this sort beneath their foundations. The elm and the ash contain a very great amount of moisture, a minimum of air and fire, and a moderate mixture of the earthy in their composition. When put in shape for use in buildings they are tough and, having no stiffness on account of the weight of moisture in them, soon bend. But when they become dry with age, or are allowed to lose their sap and die standing in the open, they get harder, and from their toughness supply a strong material for dowels to be used in joints and other articulations.

12\. The hornbeam, which has a very small amount of fire and of the earthy in its composition, but a very great proportion of air and moisture, is not a wood that breaks easily, and is very convenient to handle. Hence, the Greeks call it "zygia," because they make of it yokes for their draught-animals, and their word for yoke is \rendergreek{ζυγά}. Cypress and pine are also just as admirable; for although they contain an abundance of moisture mixed with an equivalent composed of all the other elements, and so are apt to warp when used in buildings on account of this superfluity of moisture, yet they can be kept to a great age without rotting, because the liquid contained within their substances has a bitter taste which by its pungency prevents the entrance of decay or of those little creatures which are destructive. Hence, buildings made of these kinds of wood last for an unending period of time.

13\. The cedar and the juniper tree have the same uses and good qualities, but, while the cypress and pine yield resin, from the cedar is produced an oil called cedar-oil. Books as well as other things smeared with this are not hurt by worms or decay. The foliage of this tree is like that of the cypress but the grain of the wood is straight. The statue of Diana in the temple at Ephesus is made of it, and so are the coffered ceilings both there and in all other famous fanes, because that wood is everlasting. The tree grows chiefly in Crete, Africa, and in some districts of Syria.

14\. The larch, known only to the people of the towns on the banks of the river Po and the shores of the Adriatic, is not only preserved from decay and the worm by the great bitterness of its sap, but also it cannot be kindled with fire nor ignite of itself, unless like stone in a limekiln it is burned with other wood. And even then it does not take fire nor produce burning coals, but after a long time it slowly consumes away. This is because there is a very small proportion of the elements of fire and air in its composition, which is a dense and solid mass of moisture and the earthy, so that it has no open pores through which fire can find its way; but it repels the force of fire and does not let itself be harmed by it quickly. Further, its weight will not let it float in water, so that when transported it is loaded on shipboard or on rafts made of fir.

15\. It is worth while to know how this wood was discovered. The divine Caesar, being with his army in the neighbourhood of the Alps, and having ordered the towns to furnish supplies, the inhabitants of a fortified stronghold there, called Larignum, trusting in the natural strength of their defences, refused to obey his command. So the general ordered his forces to the assault. In front of the gate of this stronghold there was a tower, made of beams of this wood laid in alternating directions at right angles to each other, like a funeral pyre, and built high, so that they could drive off an attacking party by throwing stakes and stones from the top. When it was observed that they had no other missiles than stakes, and that these could not be hurled very far from the wall on account of the weight, orders were given to approach and to throw bundles of brushwood and lighted torches at this outwork. These the soldiers soon got together.

16\. The flames soon kindled the brushwood which lay about that wooden structure and, rising towards heaven, made everybody think that the whole pile had fallen. But when the fire had burned itself out and subsided, and the tower appeared to view entirely uninjured, Caesar in amazement gave orders that they should be surrounded with a palisade, built beyond the range of missiles. So the townspeople were frightened into surrendering, and were then asked where that wood came from which was not harmed by fire. They pointed to trees of the kind under discussion, of which there are very great numbers in that vicinity. And so, as that stronghold was called Larignum, the wood was called larch. It is transported by way of the Po to Ravenna, and is to be had in Fano, Pesaro, Ancona, and the other towns in that neighbourhood. If there were only a ready method of carrying this material to Rome, it would be of the greatest use in buildings; if not for general purposes, yet at least if the boards used in the eaves running round blocks of houses were made of it, the buildings would be free from the danger of fire spreading across to them, because such boards can neither take fire from flames or from burning coals, nor ignite spontaneously.

17\. The leaves of these trees are like those of the pine; timber from them comes in long lengths, is as easily wrought in joiner's work as is the clearwood of fir, and contains a liquid resin, of the colour of Attic honey, which is good for consumptives. With regard to the different kinds of timber, I have now explained of what natural properties they appear to be composed, and how they were produced. It remains to consider the question why the highland fir, as it is called in Rome, is inferior, while the lowland fir is extremely useful in buildings so far as durability is concerned; and further to explain how it is that their bad or good qualities seem to be due to the peculiarities of their neighbourhood, so that this subject may be clearer to those who examine it.[^3425c35a991c4abb9e28a729c55a6a3a]

  
## Travelling By Ship

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ariminum, about 38 miles away. 

They are tossed asunder over the dreary gulf. Frequent flashes light the lurid air. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. They are in the wave's huge hollow. The south wind catches and hurls a ship on hidden rocks. The east wind forces a ship from the deep into shallows and quicksands. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl. Each loosened side through many a gaping seam lets in the baleful tide.   
  
They sweep through the green water.   
  
Two towering crags, twin giants, guard the cove, and threat the skies. The sailors, worn with toils, and spent with woes, leap on the welcome land, and seek their wished-for repose. Glad at length to greet the welcome earth, the sailors leap to land. 

He would later record what Julius Caesar had said about Ariminum.

## A Story About Ariminum


Being assured of the good will of the soldiers, he marched with that legion to Rimini, where he was met by the tribunes of the people, who had fled to him for protection He ordered the other legions to quit their winter quarters, and follow him with all expedition. While he was at Rimini, young L. Caesar, whose father was one of his lieutenants, came to him; and after acquainting him with the occasion of his journey, added, that he had a private message to him from Pompey, "who was desirous of clearing himself to Caesar, that he might not interpret those actions as designed to affront him, which had no other aim but the good of the commonwealth: that it had been his constant maxim, to prefer the interest of the republic to any private engagement: that it was worthy of Caesar, to sacrifice his passion and resentment to the same noble motive; and not prejudice the commonwealth, by pushing too far his revenge against his private enemies." He added something more to the same purpose, mingled with excuses for Pompey. The pretor Roscius joined likewise in the negotiation, declaring he was commissioned so to do.[^d392fd190949443cad9c7ac1924d8d42]

  
## From Ariminum To Fanum Fortunae

Virgil departed from Ariminum, intending to travel by ship down the coast to Fanum Fortunae, a distance of about 38 miles. 

The sky all round them and all round them the deep. The wave shuddered and gloomed.   
  
Out of the clouds bursts fire fast upon fire. The sails drop; they swing back to the oars.   
  
The harbor of Fanum Fortunae came into view over the horizon. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. 

He would later record what Julius Caesar had said about Fanum Fortunae.

## A Story About Fanum Fortunae


It was, by no means, a fair proposal, that Caesar should be obliged to quite Rimini and return to Gaul, while Pompey held provinces and legions that were none of his: that he should dismiss his army, whilst the other was levying troops: and, that only a general promise of going into Spain should be given, without fixing a day for his departure; by which evasion, was he to be found in Italy, even at the expiration of Caesar's consulship, he could not yet be charged with breach of faith. His forbearing too to appoint a time for a conference, and declining to approach nearer, gave little reason to hope for a peace. He therefore sent Antony to Arretium, with five cohorts; remained himself at Rimini, with two, where he resolved to levy troops; and seizing Pisaurum, Fanum, and Ancona, left a cohort in each for a garrison.[^6c98eda8b3504d4db04506bafd3c7e79]

  
## Departing From Fanum Fortunae

From Fanum Fortunae to Ancona is a journey of about 42 miles when travelling by ship down the coast. 

The wave shuddered and gloomed.   
  
They beheld the harbor of Ancona with gladness. The people of Ancona all have stations for their ships, each man one for himself. Here they shape the thin oar-blades. 

The library at Ancona happened to have a copy of _Geography_, where Virgil encountered it.

## What Strabo Once Said About Ancona


Now that I have traversed the regions of Old Italy^[i.e., Oenotria (see 6. 1. 15 and 5. 1. 1).] as far as Metapontium, I must speak of those that border on them. And Iapygia borders on them. The Greeks call it Messapia, also, but the natives, dividing it into two parts, call one part (that about the Iapygian Cape)^[Cape Leuca.] the country of the Salentini, and the other the country of the Calabri. Above these latter, on the north, are the Peucetii and also those people who in the Greek language are called Daunii, but the natives give the name Apulia to the whole country that comes after that of the Calabri, though some of them, particularly the Peucetii, are called Poedicli also. Messapia forms a sort of peninsula, since it is enclosed by the isthmus that extends from Brentesium^[See 5. 3. 6 and footnote.] as far as Taras, three hundred and ten stadia. And the voyage thither^[From Brentesium to Taras.] around the Iapygian Cape is, all told, about four hundred^[This figure is wrong. Strabo probably wrote 1,200; Groskurd thinks that he wrote 1,400, but in section 5 (below) the figures for the intervals of the same voyage total 1,220 stadia.] stadia. The distance from Metapontium^[To Taras.] is about two hundred and twenty stadia, and the voyage to it is towards the rising sun. But though the whole Tarantine Gulf, generally speaking, is harborless, yet at the city there is a very large and beautiful harbor,^[Mare Piccolo.] which is enclosed by a large bridge and is one hundred stadia in circumference. In that part of the harbor which lies towards the innermost recess,^[i.e., the part that is immediately to the east of the city, as Tozer (op. cit., p. 183) points out.] the harbor, with the outer sea, forms an isthmus, and therefore the city is situated on a peninsula; and since the neck of land is low-lying, the ships are easily hauled overland from either side. The ground of the city, too, is low-lying, but still it is slightly elevated where the acropolis is. The old wall has a large circuit, but at the present time the greater part of the city—the part that is near the isthmus—has been forsaken, but the part that is near the mouth of the harbor, where the acropolis is, still endures and makes up a city of noteworthy size. And it has a very beautiful gymnasium, and also a spacious market-place, in which is situated the bronze colossus of Zeus, the largest in the world except the one that belongs to the Rhodians. Between the marketplace and the mouth of the harbor is the acropolis, which has but few remnants of the dedicated objects that in early times adorned it, for most of them were either destroyed by the Carthaginians when they took the city or carried off as booty by the Romans when they took the place by storm.^[Tarentum revolted from Rome to Hannibal during the Second Punic War, but was recaptured (209 B.C.) and severely dealt with.] Among this booty is the Heracles in the Capitol, a colossal bronze statue, the work of Lysippus, dedicated by Maximus Fabius, who captured the city. In speaking of the founding of Taras, Antiochus says: After the Messenian war^[743-723 B.C.] broke out, those of the Lacedaemonians who did not take part in the expedition were adjudged slaves and were named Helots,^[On the name and its origin, see 8. 5. 4; also Pauly-Wissowa, Real-Encycl. s.v. "Heloten."] and all children who were born in the time of the expedition were called Partheniae^["Children of Virgins."] and judicially deprived of the rights of citizenship, but they would not tolerate this, and since they were numerous formed a plot against the free citizens; and when the latter learned of the plot they sent secretly certain men who, through a pretence of friendship, were to report what manner of plot it was; among these was Phalanthus, who was reputed to be their champion, but he was not pleased, in general, with those who had been named to take part in the council. It was agreed, however, that the attack should be made at the Hyacinthian festival in the Amyclaeum^[The temple of Amyclaean Apollo.] when the games were being celebrated, at the moment when Phalanthus should put on his leather cap (the free citizens were recognizable by their hair^[i.e., by the length of it. According to Plut. Lys. 1 the wearing of long hair by the Spartans dated back to Lycurgus (the ninth century B.C.), but according to Hdt. 1.82 they wore their hair short till the battle of Thyrea (in the sixth century B.C.), when by legal enactment they began to wear it long.]); but when Phalanthus and his men had secretly reported the agreement, and when the games were in progress, the herald came forward and forbade Phalanthus to put on a leather cap; and when the plotters perceived that the plot had been revealed, some of them began to run away and others to beg for mercy; but they were bidden to be of good cheer and were given over to custody; Phalanthus, however, was sent to the temple of the god^[At Delphi.] to consult with reference to founding a colony; and the god responded, "I give to thee Satyrium, both to take up thine abode in the rich land of Taras and to become a bane to the Iapygians." Accordingly, the Partheniae went thither with Phalanthus, and they were welcomed by both the barbarians and the Cretans who had previously taken possession of the place. These latter, it is said, are the people who sailed with Minos to Sicily, and, after his death, which occurred at the home of Cocalus in Camici,^[Cp. 6. 2. 6.] set sail from Sicily; but on the voyage back^[Back to Crete.] they were driven out of their course to Taras, although later some of them went afoot around the Adrias^[The Adriatic.] as far as Macedonia and were called Bottiaeans. But all the people as far as Daunia, it is said, were called Iapyges, after Iapyx, who is said to have been the son of Daedalus by a Cretan woman and to have been the leader of the Cretans. The city of Taras, however, was named after some hero. But Ephorus describes the founding of the city thus: The Lacedaemonians were at war with the Messenians because the latter had killed their king Teleclus when he went to Messene to offer sacrifice, and they swore that they would not return home again until they either destroyed Messene or were all killed; and when they set out on the expedition, they left behind the youngest and the oldest of the citizens to guard the city; but later on, in the tenth year of the war, the Lacedaemonian women met together and sent certain of their own number to make complaint to their husbands that they were carrying on the war with the Messenians on unequal terms, for the Messenians, staying in their own country, were begetting children, whereas they, having abandoned their wives to widowhood, were on an expedition in the country of the enemy, and they complained that the fatherland was in danger of being in want of men; and the Lacedaemonians, both keeping their oath and at the same time bearing in mind the argument of the women, sent the men who were most vigorous and at the same time youngest, for they knew that these had not taken part in the oaths, because they were still children when they went out to war along with the men who were of military age; and they ordered them to cohabit with the maidens, every man with every maiden, thinking that thus the maidens would bear many more children; and when this was done, the children were named Partheniae. But as for Messene, it was captured after a war of nineteen years, as Tyrtaeus says: "About it they fought for nineteen years, relentlessly, with heart ever steadfast, did the fathers of our fathers, spearmen they; and in the twentieth the people forsook their fertile farms and fled from the great mountains of Ithome." Now the Lacedaemonians divided up Messenia among themselves, but when they came on back home they would not honor the Partheniae with civic rights like the rest, on the ground that they had been born out of wedlock; and the Partheniae, leaguing with the Helots, formed a plot against the Lacedaemonians and agreed to raise a Laconian cap in the market-place as a signal for the attack. But though some of the Helots had revealed the plot, the Lacedaemonians decided that it would be difficult to make a counter-attack against them, for the Helots were not only numerous but were all of one mind, regarding themselves as virtually brothers of one another, and merely charged those who were about to raise the signal to go away from the marketplace. So the plotters, on learning that the undertaking had been betrayed, held back, and the Lacedaemonians persuaded them, through the influence of their fathers, to go forth and found a colony, and if the place they took possession of sufficed them, to stay there, but if not, to come on back and divide among themselves the fifth part of Messenia. And they, thus sent forth, found the Achaeans at war with the barbarians, took part in their perils, and founded Taras. At one time the Tarantini were exceedingly powerful, that is, when they enjoyed a democratic government; for they not only had acquired the largest fleet of all peoples in that part of the world but were wont to send forth an army of thirty thousand infantry, three thousand cavalry, and one thousand commanders of cavalry. Moreover, the Pythagorean philosophy was embraced by them, but especially by Archytas,^[Archytas (about 427-347 B.C.), besides being chosen seven times as chief magistrate ("strategus") of Tarentum, was famous as general, Pythagorean philosopher, mathematician, and author. Aristotle and Aristoxenus wrote works on his life and writings, but both of these works are now lost.] who presided over the city for a considerable time. But later, because of their prosperity, luxury prevailed to such an extent that the public festivals celebrated among them every year were more in number than the days of the year; and in consequence of this they also were poorly governed. One evidence of their bad policies is the fact that they employed foreign generals; for they sent for Alexander^[Alexander I was appointed king of Epeirus by Philip of Macedonia about 342 B.C., and was killed by a Luecanian about 330 B.C. (cp. 6. 1. 5).] the Molossian to lead them in their war against the Messapians and Leucanians, and, still before that, for Archidamus,^[Archidamus III, king of Sparta, was born about 400 B.C. and lost his life in 338 B.C. in this war.] the son of Agesilaüs, and, later on, for Cleonymus,^[Little is know of this Cleonymus, save that he was the son of Cleomenes II, who reigned at Sparta 370-309 B.C.] and Agathocles,^[Agathocles (b. about 361 B.C.—d. 289 B.C.) was a tyrant of Syracuse. He appears to have led the Tarantini about 300 B.C.] and then for Pyrrhus,^[Pyrrhus (about 318-272 B.C.), king of Epeirus, accepted the invitation of Tarentum in 281 B.C.] at the time when they formed a league with him against the Romans. And yet even to those whom they called in they could not yield a ready obedience, and would set them at enmity. At all events, it was out of enmity that Alexander tried to transfer to Thurian territory the general festival assembly of all Greek peoples in that part of the world—the assembly which was wont to meet at Heracleia in Tarantine territory, and that he began to urge that a place for the meetings be fortified on the Acalandrus River. Furthermore, it is said that the unhappy end which befell him^[6. 1. 5.] was the result of their ingratitude. Again, about the time of the wars with Hannibal, they were deprived of their freedom, although later they received a colony of Romans, and are now living at peace and better than before. In their war against the Messapians for the possession of Heracleia, they had the co-operation of the king of the Daunians and the king of the Peucetians. That part of the country of the Iapygians which comes next is fine, though in an unexpected way; for although on the surface it appears rough, it is found to be deep-soiled when ploughed, and although it is rather lacking in water, it is manifestly none the less good for pasturage and for trees. The whole of this district was once extremely populous; and it also had thirteen cities; but now, with the exception of Taras and Brentesium, all of them are so worn out by war that they are merely small towns. The Salentini are said to be a colony of the Cretans. The temple of Athene, once so rich, is in their territory, as also the look-out-rock called Cape Iapygia, a huge rock which extends out into the sea towards the winter sunrise,^[i.e., south-east.] though it bends approximately towards the Lacinium, which rises opposite to it on the west and with it bars the mouth of the Tarantine Gulf. And with it the Ceraunian Mountains, likewise, bar the mouth of the Ionian Gulf; the passage across from it both to the Ceraunian Mountains and to the Lacinium is about seven hundred stadia. But the distance by sea from Taras around to Brentesium is as follows: First, to the small town of Baris, six hundred stadia; Baris is called by the people of today Veretum, is situated at the edge of the Salentine territory, and the trip thither from Taras is for the most part easier to make on foot than by sailing. Thence to Leuca eighty stadia; this, too, is a small town, and in it is to be seen a fountain of malodorous water; the mythical story is told that those of the Giants who survived at the Campanian Phlegra^[See 5. 4. 4 and 5. 4. 6.] and are called the Leuternian Giants were driven out by Heracles, and on fleeing hither for refuge were shrouded by Mother Earth, and the fountain gets its malodorous stream from the ichor of their bodies; and for this reason, also, the seaboard here is called Leuternia. Again, from Leuca to Hydrus,^[Also called Hydruntum; now Otranto.] a small town, one hundred and fifty stadia. Thence to Brentesium four hundred; and it is an equal distance to the island Sason,^[Now Sasena.] which is situated about midway of the distance across from Epeirus to Brentesium. And therefore those who cannot accomplish the straight voyage sail to the left of Sason and put in at Hydrus; and then, watching for a favorable wind, they hold their course towards the harbors of the Brentesini, although if they disembark, they go afoot by a shorter route by way of Rodiae,^[Also called Rudiae; now Rugge.] a Greek city, where the poet Ennius was born. So then, the district one sails around in going from Taras to Brentesium resembles a peninsula, and the overland journey from Brentesium to Taras, which is only a one day's journey for a man well-girt, forms the isthmus of the aforesaid peninsula;^[6. 3. 1.] and this peninsula most people call by one general name Messapia, or Iapygia, or Calabria, or Salentina, although some divide it up, as I have said before.^[6. 3. 1.] So much, then, for the towns on the seacoast. In the interior are Rodiae and Lupiae, and, slightly above the sea, Aletia; and at the middle of the isthmus, Uria, in which is still to be seen the palace of one of the chieftains. When Herodotus^[7. 170.] states that Hyria is in Iapygia and was founded by the Cretans who strayed from the fleet of Minos when on its way to Sicily,^[Cp. 6. 3. 2.] we must understand Hyria to be either Uria or Veretum. Brentesium, they say, was further colonized by the Cretans, whether by those who came over with Theseus from Cnossus or by those who set sail from Sicily with Iapyx (the story is told both ways), although they did not stay together there, it is said, but went off to Bottiaea.^[Cp. 6. 3. 2, where Antiochus says that some of them went to Bottiaea.] Later on, however, when ruled by kings, the city lost much of its country to the Lacedaemonians who were under the leadership of Phalanthus; but still, when he was ejected from Taras, he was admitted by the Brentesini, and when he died was counted by them worthy of a splendid burial. Their country is better than that of the Tarantini, for, though the soil is thin, it produces good fruits, and its honey and wool are among those that are strongly commended. Brentesium is also better supplied with harbors; for here many harbors are closed in by one mouth; and they are sheltered from the waves, because bays are formed inside in such a way as to resemble in shape a stag's horns;^[So, too, the gulf, or bay, at Byzantium resembles a stag's horn (7. 6. 2).] and hence the name, for, along with the city, the place very much resembles a stag's head, and in the Messapian language the head of the stag is called "brentesium."^[Stephanus Byzantinus says: "According to Seleucus, in his second book on Languages, 'brentium' is the Messapian word for 'the head of the stag.'" Hence the editors who emend "brentesium" to "brentium" are almost certainly correct.] But the Tarantine harbor, because of its wide expanse, is not wholly sheltered from the waves; and besides there are some shallows in the innermost part of it.^[Here, as in 6. 3. 1., Strabo is speaking of the inner harbor (Mare Piccolo), not the outer, of which, as Tozer (p. 184) says, Strabo takes no account.] In the case of those who sail across from Greece or Asia, the more direct route is to Brentesium, and, in fact, all who propose to go to Rome by land put into port here. There are two roads^[On these roads see Ashby and Gardner, The Via Trajana, Paper of the British School at Rome, 1916, Vol.VIII, No. 5, pp. 107 ff.] from here: one, a mule-road through the countries of the Peucetii (who are called Poedicli),^[Cp. 6. 3. 1.] the Daunii, and the Samnitae as far as Beneventum; on this road is the city of Egnatia,^[Also spelled Gnathia, Gnatia, and Ignatia; now Torre d'Agnazzo.] and then, Celia,^[Also spelled Caelia; now Ceglie di Bari.] Netium,^[Now Noja.] Canusium, and Herdonia.^[Now Ordona.] But the road by way of Taras, lying slightly to the left of the other, though as much as one day's journey out of the way when one has made the circuit,^[i.e., to the point where it meets the other road, near Beneventum.] what is called the Appian Way, is better for carriages. On this road are the cities of Uria and Venusia, the former between Taras and Brentesium and the latter on the confines of the Samnitae and the Leucani. Both the roads from Brentesium meet near Beneventum and Campania. And the common road from here on, as far as Rome, is called the Appian Way, and passes through Caudium,^[Now Montesarchio.] Calatia,^[Now Galazze.] Capua,^[The old Santa Maria di Capua, now in ruins; not the Capua of today, which is on the site of Casilinum.] and Casilinum to Sinuessa.^[Now Mondragone.] And the places from there on I have already mentioned. The total length of the road from Rome to Brentesium is three hundred and sixty miles. But there is also a third road, which runs from Rhegium through the countries of the Brettii, the Leucani, and the Samnitae into Campania, where it joins the Appian Way; it passes through the Apennine Mountains and it requires three or four days more than the road from Brentesium. The voyage from Brentesium to the opposite mainland is made either to the Ceraunian Mountains and those parts of the seaboard of Epeirus and of Greece which come next to them, or else to Epidamnus; the latter is longer than the former, for it is one thousand eight hundred stadia.^[Strabo has already said the the voyage from Brentesium to Epeirus by way of Sason (Saseno) was about 800 stadia (6. 3. 5). But Strabo was much out of the way, and apparently was not on the regular route. Again, Epidamnus (now Durazzo) is in fact only about 800 stadia distant, not 1,800 as the text makes Strabo say. It is probable, therefore, that Strabo said either simply " for it is 800 stadia," or "for it is 1,000 stadia, while the former is 800.] And yet the latter is the usual route, because the city has a good position with reference both to the tribes of the Illyrians and to those of the Macedonians. As one sails from Brentesium along the Adriatic seaboard, one comes to the city of Egnatia, which is the common stopping-place for people who are travelling either by sea or land to Barium;^[Now Bari.] and the voyage is made with the south wind. The country of the Peucetii extends only thus far^[To Barium.] on the sea, but in the interior as far as Silvium.^[Silvium appears to have been on the site of what is now Garagone.] All of it is rugged and mountainous, since it embraces a large portion of the Apennine Mountains; and it is thought to have admitted Arcadians as colonists. From Brentesium to Barium is about seven hundred stadia, and Taras is about an equal distance from each. The adjacent country is inhabited by the Daunii; and then come the Apuli, whose country extends as far as that of the Frentani. But since the terms "Peucetii" and "Daunii" are not at all used by the native inhabitants, except in early times, and since this country as a whole is now called Apulia, necessarily the boundaries of these tribes cannot be told to a nicety either, and for this reason neither should I myself make positive assertions about them. From Barium to the Aufidus River, on which is the Emporium of the Canusitae^[This Emporium should probably be identified with the Canne of today (see Ashby and Gardner, op. cit., p. 156).] is four hundred stadia and the voyage inland to Emporium is ninety. Near by is also Salapia,^[Now Salpi.] the seaport of the Argyrippini. For not far above the sea (in the plain, at all events) are situated two cities, Canusium^[Now Canosa.] and Argyrippa,^[Now Arpino.] which in earlier times were the largest of the Italiote cities, as is clear from the circuits of their walls. Now, however, Argyrippa is smaller; it was called Argos Hippium at first, then Argyrippa, and then by the present name Arpi. Both are said to have been founded by Diomedes.^[Cp. 5. 1. 9.] And as signs of the dominion of Diomedes in these regions are to be seen the Plain of Diomedes and many other things, among which are the old votive offerings in the temple of Athene at Luceria—a place which likewise was in ancient times a city of the Daunii, but is now reduced—and, in the sea near by, two islands that are called the Islands of Diomedes, of which one is inhabited, while the other, it is said, is desert; on the latter, according to certain narrators of myths, Diomedes was caused to disappear, and his companions were changed to birds, and to this day, in fact, remain tame and live a sort of human life, not only in their orderly ways but also in their tameness towards honorable men and in their flight from wicked and knavish men. But I have already mentioned the stories constantly told among the Heneti about this hero and the rites which are observed in his honor.^[Cp. 5. 1. 9.] It is thought that Sipus^[In Latin, Sipontum; now in ruins, near Santa Maria di Siponto.] also was founded by Diomedes, which is about one hundred and forty stadia distant from Salapia; at any rate it was named "Sepius" in Greek after the "sepia"^[Cuttle-fish.] that are cast ashore by the waves. Between Salapia and Sinus is a navigable river, and also a large lake that opens into the sea; and the merchandise from Sipus, particularly grain, is brought down on both. In Daunia, on a hill by the name of Drium, are to be seen two hero-temples: one, to Calchas, on the very summit, where those who consult the oracle sacrifice to his shade a black ram and sleep in the hide, and the other, to Podaleirius, down near the base of the hill, this temple being about one hundred stadia distant from the sea; and from it flows a stream which is a cure-all for diseases of animals. In front of this gulf is a promontory, Garganum, which extends towards the east for a distance of three hundred stadia into the high sea; doubling the headland, one comes to a small town, Urium, and off the headland are to be seen the Islands of Diomedes. This whole country produces everything in great quantity, and is excellent for horses and sheep; but though the wool is softer than the Tarantine, it is not so glossy. And the country is well sheltered, because the plains lie in hollows. According to some, Diomedes even tried to cut a canal as far as the sea, but left behind both this and the rest of his undertakings only half-finished, because he was summoned home and there ended his life. This is one account of him; but there is also a second, that he stayed here till the end of his life; and a third, the aforesaid mythical account, which tells of his disappearance in the island; and as a fourth one might set down the account of the Heneti, for they too tell a mythical story of how he in some way came to his end in their country, and they call it his apotheosis. Now the above distances are put down in accordance with the data of Artemidorus;^[Artemidorus (flourished about 100 B.C.), of Ephesus, was an extensive traveller and a geographer of great importance. He wrote a geography of the inhabited world in eleven books, a Periplus of the Mediterranean, and Ionian Historical Sketches. But his works, except numerous fragments preserved in other authors, are now lost.] but according to the Chorographer,^[See 5. 2. 7 and footnote.] the distances from Brentesium as far as Garganum^[Monte Gargano.] amount to one hundred and sixty-five miles, whereas according to Artemidorus they amount to more; and thence to Ancona two hundred and fifty-four miles according to the former, whereas according to Artemidorus the distance to the Aesis River, which is near Ancona, is one thousand two hundred and fifty stadia, a much shorter distance. Polybius states that the distance from Iapygia has been marked out by miles, and that the distance to the city of Sena^[Sena Gallica; now Sinigaglia.] is five hundred and sixty-two miles, and thence to Aquileia one hundred and seventy-eight. And they do not agree with the commonly accepted distance along the Illyrian coastline, from the Ceraunian Mountains to the recess of the Adrias,^[The Adriatic.] since they represent this latter coasting voyage as over six thousand stadia,^[Polybius here gives the total length of the coastline on the Italian side as 740 miles, or 6,166 stadia (8 1/3 stadia to the mile; see 7. 7. 4), and elsewhere (2. 4. 3) Strabo quotes him as reckoning the length of the Illyrian coastline from the Ceraunian Mts. only to Iapygia (not including Istria) as 6,150 stadia. Cp. also 7. 5. 3, 4, 10.] thus making it even longer than the former, although it is much shorter. However, every writer does not agree with every other, particularly about the distances, as I often say.^[Cp. 1. 2. 13; 2. 1. 7-8, and 2. 4. 3.] As for myself, where it is possible to reach a decision, I set forth my opinion, but where it is not, I think that I should make known the opinions of others. And when I have no opinion of theirs, there is no occasion for surprise if I too have passed something by, especially when one considers the character of my subject; for I would not pass by anything important, while as for little things, not only do they profit one but slightly if known, but their omission escapes unnoticed, and detracts not at all, or else not much, from the completeness of the work.^[Cp. 1. 1. 23.] The intervening space, immediately after Cape Garganum, is taken up by a deep gulf; the people who live around it are called by the special name of Apuli, although they speak the same language as the Daunii and the Peucetii, and do not differ from them in any other respect either, at the present time at least, although it is reasonable to suppose that in early times they differed and that this is the source of the three diverse names for them that are now prevalent. In earlier times this whole country was prosperous, but it was laid waste by Hannibal and the later wars. And here too occurred the battle of Cannae, in which the Romans and their allies suffered a very great loss of life. On the gulf is a lake; and above the lake, in the interior, is Teanum Apulum,^[Passo di Civita.] which has the same name as Teanum Sidicinum. At this point the breadth of Italy seems to be considerably contracted, since from here to the region of Dicaearcheia^[Puteoli.] an isthmus is left of less than one thousand stadia from sea to sea. After the lake comes the voyage along the coast to the country of the Frentani and to Buca;^[Now Termoli.] and the distance from the lake either to Buca or to Cape Garganum is two hundred stadia. As for the places that come next after Buca, I have already mentioned them.^[5. 4. 2.][^8ee15fb50aef41608d3dc2b0bb7eef8c]

  
## To Iader

From Ancona to Iader is a journey of about 107 miles when travelling by ship down the coast. 

Out of the clouds bursts fire fast upon fire. Dubious days of blind darkness we wander on the deep, nights without a star. Then comes the creak of cables and the cries of seamen. Frequent flashes light the lurid air. All nature, big with instant ruin, frowned destruction. The oars are snapped. Piteous to see, it dashes on shoals and girdles with a sandbank. The helmsman is dashed away and rolled forward headlong.   
  
Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
Within a long recess there lies a bay: an island shades it from the rolling sea and forms a port secure for ships to ride. Two towering crags, twin giants, guard the cove, and threat the skies. Betwixt two rows of rocks a sylvan scene appears above, and groves for ever green. Beneath a precipice that fronts the wave, with limpid springs inside, and many a seat of living marble, lies a sheltered cave. Ships within this happy harbor meet, the thin remainders of the scattered fleet. They lay their weary limbs still dripping on the sand. 

The library at Salona happened to have a copy of _Civil War_, where Virgil encountered it.

## A Story About Salona By Julius Caesar


Caesar having landed his troops, sent the fleet back the same night to Brundusium, to bring over his other legions and cavalry. Fufius Kalenus, lieutenant-general, had the charge of this expedition, with orders to use the utmost despatch. But setting sail too late, he lost the benefit of the wind, which offered fair all night, and fell in with the enemy. For Bibulus hearing at Corcyra of Caesar's arrival, forthwith put to sea, in hopes of intercepting some of the transports; and meeting the fleet as it returned empty, took about thirty ships, which he immediately burned, with all that were on board; partly to satisfy his own vengeance for the disappointment he had received; partly to deter the rest of the troops from attempting the passage. He then stationed his fleet along the coast, from Salona to Oricum, guarded all places with extraordinary care, and even lay himself aboard, notwithstanding the rigour of the winter; declining no danger nor fatigue, and solely intent upon intercepting Caesar's supplies.[^dae3b29eacc7468e8014b017dceec3b0]

\newpage

# Iader To Reate
  
## Travelling By Ship Down The Coast To Titius (River)

Intending to travel by ship down the coast to Titius (river), Virgil left Iader. It was about 48 miles away. 

The breezes woo the sails, and the canvas blows out to the swelling south.   
  
Stormclouds enwrap the day, and rainy gloom blots out the sky. They sweep through the green water.   
  
A fair harbor lies on either side of the city and the entrance is narrow. Curved ships are drawn up along the road. The people of Titius (river) all have stations for their ships, each man one for himself. 

He would later record what Strabo had said about Salona.

## On Salona, According To Strabo


After the mouth of the Silaris one comes to Leucania, and to the temple of the Argoan Hera, built by Jason, and near by, within fifty stadia, to Poseidonia. Thence, sailing out past the gulf, one comes to Leucosia,^[Now Licosa.] an island, from which it is only a short voyage across to the continent. The island is named after one of the Sirens, who was cast ashore here after the Sirens had flung themselves, as the myth has it, into the depths of the sea. In front of the island lies that promontory^[Poseidium, now Punta Della Licosa.] which is opposite the Sirenussae and with them forms the Poseidonian Gulf. On doubling this promontory one comes immediately to another gulf, in which there is a city which was called "Hyele" by the Phocaeans who founded it, and by others "Ele," after a certain spring, but is called by the men of today "Elea." This is the native city of Parmenides and Zeno, the Pythagorean philosophers. It is my opinion that not only through the influence of these men but also in still earlier times the city was well governed; and it was because of this good government that the people not only held their own against the Leucani and the Poseidoniatae, but even returned victorious, although they were inferior to them both in extent of territory and in population. At any rate, they are compelled, on account of the poverty of their soil, to busy themselves mostly with the sea and to establish factories for the salting of fish, and other such industries. According to Antiochus,^[Antiochus Syracusanus, the historian. Cp. Hdt. 1.167] after the capture of Phocaea by Harpagus, the general of Cyrus, all the Phocaeans who could do so embarked with their entire families on their light boats and, under the leadership of Creontiades, sailed first to Cyrnus and Massalia, but when they were beaten off from those places founded Elea. Some, however, say that the city took its name from the River Elees.^[The Latin form is "Hales" (now the Alento).] It is about two hundred stadia distant from Poseidonia. After Elea comes the promontory of Palinurus. Off the territory of Elea are two islands, the Oenotrides, which have anchoring-places. After Palinurus comes Pyxus—a cape, harbor, and river, for all three have the same name. Pyxus was peopled with new settlers by Micythus, the ruler of the Messene in Sicily, but all the settlers except a few sailed away again. After Pyxus comes another gulf, and also Laüs—a river and city; it is the last of the Leucanian cities, lying only a short distance above the sea, is a colony of the Sybaritae, and the distance thither from Ele is four hundred stadia. The whole voyage along the coast of Leucania is six hundred and fifty stadia. Near Laüs is the hero-temple of Draco, one of the companions of Odysseus, in regard to which the following oracle was given out to the Italiotes:^[The Greek inhabitants of Italy were called "Italiotes."] Much people will one day perish about Laïan Draco.^[There is a word-play here which cannot be brought out in translation: the word for "people" in Greek is "laos."] And the oracle came true, for, deceived by it, the peoples^[Literally, "laoi."] who made campaigns against Laüs, that is, the Greek inhabitants of Italy, met disaster at the hands of the Leucani. These, then, are the places on the Tyrrhenian seaboard that belong to the Leucani. As for the other sea,^[The Adriatic.] they could not reach it at first; in fact, the Greeks who held the Gulf of Tarentum were in control there. Before the Greeks came, however, the Leucani were as yet not even in existence, and the regions were occupied by the Chones and the Oenotri. But after the Samnitae had grown considerably in power, and had ejected the Chones and the Oenotri, and had settled a colony of Leucani in this portion of Italy, while at the same time the Greeks were holding possession of both seaboards as far as the Strait, the Greeks and the barbarians carried on war with one another for a long time. Then the tyrants of Sicily, and afterwards the Carthaginians, at one time at war with the Romans for the possession of Sicily and at another for the possession of Italy itself, maltreated all the peoples in this part of the world, but especially the Greeks. Later on, beginning from the time of the Trojan war, the Greeks had taken away from the earlier inhabitants much of the interior country also, and indeed had increased in power to such an extent that they called this part of Italy, together with Sicily, Magna Graecia. But today all parts of it, except Taras,^[The old name of Tarentum.] Rhegium, and Neapolis, have become completely barbarized,^["Barbarized," in the sense of "non-Greek" (cp. 5. 4. 4 and 5. 4. 7).] and some parts have been taken and are held by the Leucani and the Brettii, and others by the Campani—that is, nominally by the Campani but in truth by the Romans, since the Campani themselves have become Romans. However, the man who busies himself with the description of the earth must needs speak, not only of the facts of the present, but also sometimes of the facts of the past, especially when they are notable. As for the Leucani, I have already spoken of those whose territory borders on the Tyrrhenian Sea, while those who hold the interior are the people who live above the Gulf of Tarentum. But the latter, and the Brettii, and the Samnitae themselves (the progenitors of these peoples) have so utterly deteriorated that it is difficult even to distinguish their several settlements; and the reason is that no common organization longer endures in any one of the separate tribes; and their characteristic differences in language, armor, dress, and the like, have completely disappeared; and, besides, their settlements, severally and in detail, are wholly without repute. Accordingly, without making distinctions between them, I shall only tell in a general way what I have learned about the peoples who live in the interior, I mean the Leucani and such of the Samnitae as are their next neighbors. Petelia, then, is regarded as the metropolis of the Chones, and has been rather populous down to the present day. It was founded by Philoctetes after he, as the result of a political quarrel, had fled from Meliboea. It has so strong a position by nature that the Samnitae once fortified it against the Thurii. And the old Crimissa, which is near the same regions, was also founded by Philoctetes. Apollodorus, in his work On Ships,^[That is, his work entitled "On the (Homeric) Catalogue of Ships" (cp. 1. 2. 24).] in mentioning Philoctetes, says that, according to some, when Philoctetes arrived at the territory of Croton, he colonized the promontory Crimissa, and, in the interior above it, the city Chone, from which the Chonians of that district took their name, and that some of his companions whom he had sent forth with Aegestes the Trojan to the region of Eryx in Sicily fortified Aegesta.^[Also spelled Segesta and Egesta.] Moreover, Grumentum and Vertinae are in the interior, and so are Calasarna and some other small settlements, until we arrive at Venusia, a notable city; but I think that this city and those that follow in order after it as one goes towards Campania are Samnite cities. Beyond Thurii lies also the country that is called Tauriana. The Leucani are Samnite in race, but upon mastering the Poseidoniatae and their allies in war they took possession of their cities. At all other times, it is true, their government was democratic, but in times of war they were wont to choose a king from those who held magisterial offices. But now they are Romans. The seaboard that comes next after Leucania, as far as the Sicilian Strait and for a distance of thirteen hundred and fifty stadia, is occupied by the Brettii. According to Antiochus, in his treatise On Italy, this territory (and this is the territory which he says he is describing) was once called Italy, although in earlier times it was called Oenotria. And he designates as its boundaries, first, on the Tyrrhenian Sea, the same boundary that I have assigned to the country of the Brettii—the River Laüs; and secondly, on the Sicilian Sea, Metapontium. But as for the country of the Tarantini, which borders on Metapontium, he names it as outside of Italy, and calls its inhabitants Iapyges. And at a time more remote, according to him, the names "Italians" and "Oenotrians" were applied only to the people who lived this side the isthmus in the country that slopes toward the Sicilian Strait. The isthmus itself, one hundred and sixty stadia in width, lies between two gulfs—the Hipponiate (which Antiochus has called Napetine) and the Scylletic. The coasting-voyage round the country comprised between the isthmus and the Strait is two thousand stadia. But after that, he says, the name of "Italy" and that of the "Oenotrians" was further extended as far as the territory of Metapontium and that of Seiris, for, he adds, the Chones, a well-regulated Oenotrian tribe, had taken up their abode in these regions and had called the land Chone. Now Antiochus had spoken only in a rather simple and antiquated way, without making any distinctions between the Leucani and the Brettii. In the first place, Leucania lies between the Tyrrhenian and Sicilian coastlines,^[Between the coastlines on the Tyrrhenian and Sicilian Seas.] the former coastline from the River Silaris as far as Laüs, and the latter, from Metapontium as far as Thurii; in the second place, on the mainland, from the country of the Samnitae as far as the isthmus which extends from Thurii to Cerilli (a city near Laüs), the isthmus is three hundred stadia in width. But the Brettii are situated beyond the Leucani; they live on a peninsula, but this peninsula includes another peninsula which has the isthmus that extends from Scylletium to the Hipponiate Gulf. The name of the tribe was given to it by the Leucani, for the Leucani call all revolters "brettii." The Brettii revolted, so it is said (at first they merely tended flocks for the Leucani, and then, by reason of the indulgence of their masters, began to act as free men), at the time when Rio made his expedition against Dionysius and aroused all peoples against all others. So much, then, for my general description of the Leucani and the Brettii. The next city after Laüs belongs to Brettium, and is named Temesa, though the men of today call it Tempsa; it was founded by the Ausones, but later on was settled also by the Aetolians under the leadership of Thoas; but the Aetolians were ejected by the Brettii, and then the Brettii were crushed by Hannibal and by the Romans. Near Temesa, and thickly shaded with wild olive trees, is the hero-temple of Polites, one of the companions of Odysseus, who was treacherously slain by the barbarians, and for that reason became so exceedingly wroth against the country that, in accordance with an oracle, the people of the neighborhood collected tribute^[According to Paus. 6.6.2 the oracle bade the people annually to give the hero to wife the fairest maiden in Temesa.] for him; and hence, also, the popular saying applied to those who are merciless,^["Merciless" is an emendation. Some read "disagreeable." According to Aelian Var. Hist. 8.18, the popular saying was applied to those who in pursuit of profit overreached themselves (so Plutarch Prov. 31). But Eustathius (note on Iliad 1.185) quotes "the geographer" (i.e., Strabo; see note 1, p. 320) as making the saying apply to "those who are unduly wroth, or very severe when they should not be."] that they are "beset by the hero of Temesa." But when the Epizephyrian Locrians captured the city, Euthymus, the pugilist, so the story goes, entered the lists against Polites, defeated him in the fight and forced him to release the natives from the tribute. People say that Homer has in mind this Temesa, not the Tamassus in Cyprus (the name is spelled both ways), when he says "to Temesa, in quest of copper."^[Hom. Od. 1.184] And in fact copper mines are to be seen in the neighborhood, although now they have been abandoned. Near Temesa is Terina, which Hannibal destroyed, because he was unable to guard it, at the time when he had taken refuge in Brettium itself. Then comes Consentia, the metropolis of the Brettii; and a little above this city is Pandosia, a strong fortress, near which Alexander the Molossian^[Cp. 6. 3. 4 and footnote.] was killed. He, too, was deceived by the oracle^[The oracle, quoted by Casaubon from some source unknown to subsequent editors was:\rendergreek{Αἰακίδη, προφύλαξο μολεῖν Α᾿χερούσιον ὕδωρ}\rendergreek{Πανδοσίην δ᾽ ὅθι τοι θάνατος πεπρωμένος ἐστί}Source unknown. "Son of Aeacus, beware to go to the Acherusian water and Pandosia, where it is fated you will die."] at Dodona, which bade him be on his guard against Acheron and Pandosia; for places which bore these names were pointed out to him in Thesprotia, but he came to his end here in Brettium. Now the fortress has three summits, and the River Acheron flows past it. And there was another oracle that helped to deceive him: Three-hilled Pandosia, much people shalt thou kill one day; for he thought that the oracle clearly meant the destruction of the enemy, not of his own people. It is said that Pandosia was once the capital of the Oenotrian Kings. After Consentia comes Hipponium, which was founded by the Locrians. Later on, the Brettii were in possession of Hipponium, but the Romans took it away from them and changed its name to Vibo Valentia. And because the country round about Hipponium has luxuriant meadows abounding in flowers, people have believed that Core^[i.e., Persephone.] used to come hither from Sicily to gather flowers; and consequently it has become the custom among the women of Hipponium to gather flowers and to weave them into garlands, so that on festival days it is disgraceful to wear bought garlands. Hipponium has also a naval station, which was built long ago by Agathocles, the tyrant of the Siciliotes,^[The "Siciliotes" were Sicilian Greeks, as distinguished from native Sicilians.] when he made himself master of the city. Thence one sails to the Harbor of Heracles,^[Now Tropea. But in fact the turn towards the west begins immediately after Hipponium.] which is the point where the headlands of Italy near the Strait begin to turn towards the west. And on this voyage one passes Medma, a city of the same Locrians aforementioned, which has the same name as a great fountain there, and possesses a naval station near by, called Emporium. Near it is also the Metaurus River, and a mooring-place bearing the same name. Off this coast lie the islands of the Liparaei, at a distance of two hundred stadia from the Strait. According to some, they are the islands of Aeolus, of whom the Poet makes mention in the Odyssey.^[Hom. Od. 10.2ff] They are seven in number and are all within view both from Sicily and from the continent near Medma. But I shall tell about them when I discuss Sicily. After the Metaurus River comes a second Metaurus.^[Strabo's "Metaurus" and "second Metaurus" are confusing. Kramer, Meineke, and others wish to emend the text so as to make the "second" river refer to Crataeis or some other river. But we should have expected Strabo to mention first the Medma (now the Mesima), which was much closer to Medma than the Metaurus (now the Marro), and to which he does not refer at all. Possibly he thought both rivers were called Metaurus (cp. Müller, Ind. Var. Lectionis, p. 975), in which case "the second Metaurus" is the Metaurus proper. The present translator, however, believes that Strabo, when he says "second Metaurus," alludes to the Umbrian Metaurus (5. 2. 10) as the first, and that the copyist, unaware of this fact, deliberately changed "Medma" to Metaurus" in the two previous instances.] Next after this river comes Scyllaeum, a lofty rock which forms a peninsula, its isthmus being low and affording access to ships on both sides. This isthmus Anaxilaüs, the tyrant of the Rhegini, fortified against the Tyrrheni, building a naval station there, and thus deprived the pirates of their passage through the strait. For Caenys,^[Now Cape Cavallo.] too, is near by, being two hundred and fifty stadia distant from Medma; it is the last cape, and with the cape on the Sicilian side, Pelorias, forms the narrows of the Strait. Cape Pelorias is one of the three capes that make the island triangular, and it bends towards the summer sunrise,^[North-east (cp. 1. 2. 21).] just as Caenys bends towards the west, each one thus turning away from the other in the opposite direction. Now the length of the narrow passage of the Strait from Caenys as far as the Poseidonium,^[Altar or temple of Poseidon.] or the Columna Rheginorum, is about six stadia, while the shortest passage across is slightly more; and the distance is one hundred stadia from the Columna to Rhegium, where the Strait begins to widen out, as one proceeds towards the east, towards the outer sea, the sea which is called the Sicilian Sea. Rhegium was founded by the Chalcidians who, it is said, in accordance with an oracle, were dedicated, one man out of every ten Chalcidians, to Apollo,^[Cp. 6. 1. 9.] because of a dearth of crops, but later on emigrated hither from Delphi, taking with them still others from their home. But according to Antiochus, the Zanclaeans sent for the Chalcidians and appointed Antimnestus their founder-in-chief.^[Zancle was the original name of Messana (now Messina) in Sicily. It was colonized and named Messana by the Peloponnesian Messenians (6. 2. 3).] To this colony also belonged the refugees of the Peloponnesian Messenians who had been defeated by the men of the opposing faction. These men were unwilling to be punished by the Lacedaemonians for the violation of the maidens^[Cp. 6. 3. 3. and 8. 4. 9.] which took place at Limnae, though they were themselves guilty of the outrage done to the maidens, who had been sent there for a religious rite and had also killed those who came to their aid.^[Cp. Paus. 4.4.1] So the refugees, after withdrawing to Macistus, sent a deputation to the oracle of the god to find fault with Apollo and Artemis if such was to be their fate in return for their trying to avenge those gods, and also to enquire how they, now utterly ruined, might be saved. Apollo bade them go forth with the Chalcidians to Rhegium, and to be grateful to his sister; for, he added, they were not ruined, but saved, inasmuch as they were surely not to perish along with their native land, which would be captured a little later by the Spartans. They obeyed; and therefore the rulers of the Rhegini down to Anaxilas^[Anaxilas (also spelled Anaxilaüs) was ruler of Rhegium from 494 to 476 B.C. (Diod. Sic. 11.48).] were always appointed from the stock of the Messenians. According to Antiochus, the Siceli and Morgetes had in early times inhabited the whole of this region, but later on, being ejected by the Oenotrians, had crossed over into Sicily. According to some, Morgantium also took its name from the Morgetes of Rhegium.^[Cp. 6. 2. 4. The Latin name of this Sicilian city was "Murgantia." Livy 10.17 refers to another Murgantia in Samnium.] The city of Rhegium was once very powerful and had many dependencies in the neighborhood; and it was always a fortified outpost threatening the island, not only in earlier times but also recently, in our own times, when Sextus Pompeius caused Sicily to revolt. It was named Rhegium, either, as Aeschylus says, because of the calamity that had befallen this region, for, as both he and others state, Sicily was once "rent"^[Cp. 1. 3. 19 and the footnote on "rent."] from the continent by earthquakes, "and so from this fact," he adds, "it is called Rhegium." They infer from the occurrences about Aetna and in other parts of Sicily, and in Lipara and in the islands about it, and also in the Pithecussae and the whole of the coast of the adjacent continent, that it is not unreasonable to suppose that the rending actually took place. Now at the present time the earth about the Strait, they say, is but seldom shaken by earthquakes, because the orifices there, through which the fire is blown up and the red-hot masses and the waters are ejected, are open. At that time, however, the fire that was smouldering beneath the earth, together with the wind, produced violent earthquakes, because the passages to the surface were all blocked up, and the regions thus heaved up yielded at last to the force of the blasts of wind, were rent asunder, and then received the sea that was on either side, both here^[At the Strait.] and between the other islands in that region.^[Cp. 1. 3. 10 and the footnote.] And, in fact, Prochyte and the Pithecussae are fragments broken off from the continent, as also Capreae, Leucosia, the Sirenes, and the Oenotrides. Again, there are islands which have arisen from the high seas, a thing that even now happens in many places; for it is more plausible that the islands in the high seas were heaved up from the deeps, whereas it is more reasonable to think that those lying off the promontories and separated merely by a strait from the mainland have been rent therefrom. However, the question which of the two explanations is true, whether Rhegium got its name on account of this or on account of its fame (for the Samnitae might have called it by the Latin word for "royal,"^[Regium.] because their progenitors had shared in the government with the Romans and used the Latin language to a considerable extent), is open to investigation. Be this as it may, it was a famous city, and not only founded many cities but also produced many notable men, some notable for their excellence as statesmen and others for their learning; nevertheless, Dionysius^[Dionysius the Elder (b. about 432 B.C., d. 367 B.C.)] demolished it, they say, on the charge that when he asked for a girl in marriage they proffered the daughter of the public executioner;^[Diod. Sic. 14.44 merely says that the Assembly of the Rhegini refused him a wife.] but his son restored a part of the old city and called it Phoebia.^[Apparently in honor of Phoebus (Apollo); for, according to Plut. De Alexandri Virtute, (338) Dionysius the Younger called himself the son of Apollo, "offspring of his mother Doris by Phoebus."] Now in the time of Pyrrhus the garrison of the Campani broke the treaty and destroyed most of the inhabitants, and shortly before the Marsic war much of the settlement was laid in ruins by earthquakes; but Augustus Caesar, after ejecting Pompeius from Sicily, seeing that the city was in want of population, gave it some men from his expeditionary forces as new settlers, and it is now fairly populous. As one sails from Rhegium towards the east, and at a distance of fifty stadia, one comes to Cape Leucopetra^[Literally, "White Rock."] (so called from its color), in which, it is said, the Apennine Mountain terminates. Then comes Heracleium, which is the last cape of Italy and inclines towards the south; for on doubling it one immediately sails with the southwest wind as far as Cape Iapygia, and then veers off, always more and more, towards the northwest in the direction of the Ionian Gulf.^[The "Ionian Gulf" was the southern "part of what is now called the Adriatic Sea" (2. 5. 20); see 7. 5. 8-9.] After Heracleium comes a cape belonging to Locris, which is called Zephyrium; its harbor is exposed to the winds that blow from the west, and hence the name. Then comes the city Locri Epizephyrii,^[Literally, the "western Locrians," both city and inhabitants having the same name.] a colony of the Locri who live on the Crisaean Gulf,^[Now the Gulf of Salona in the Gulf of Corinth.] which was led out by Evanthes only a little while after the founding of Croton and Syracuse.^[Croton and Syracuse were founded, respectively, in 710 and 734 B.C. According to Diod. Sic. 4.24, Heracles had unintentionally killed Croton and had foretold the founding of a famous city on the site, the same to be named after Croton.] Ephorus is wrong in calling it a colony of the Locri Opuntii. However, they lived only three or four years at Zephyrium, and then moved the city to its present site, with the cooperation of Syracusans [for at the same time the latter, among whom . . .]^[The Greek text, here translated as it stands, is corrupt. The emendations thus far offered yield (instead of the nine English words of the above rendering) either (1) "for the latter were living" (or "had taken up their abode") "there at the same time" or (2) "together with the Tarantini." There seems to be no definite corroborative evidence for either interpretation; but according to Pausanias, "colonies were sent to Croton, and to Locri at Cape Zephyrium, by the Lacedaemonians" (3.3); and "Tarentum is a Lacedaemonian colony" (10. 10). Cp. the reference to the Tarantini in Strabo's next paragraph.] And at Zephyrium there is a spring, called Locria, where the Locri first pitched camp. The distance from Rhegium to Locri is six hundred stadia. The city is situated on the brow of a hill called Epopis. The Locri Epizephyrii are believed to have been the first people to use written laws. After they had lived under good laws for a very long time, Dionysius, on being banished from the country of the Syracusans,^[Dionysius the Younger was banished thence in 357 B.C.] abused them most lawlessly of all men. For he would sneak into the bed-chambers of the girls after they had been dressed up for their wedding, and lie with them before their marriage; and he would gather together the girls who were ripe for marriage, let loose doves with cropped wings upon them in the midst of the banquets, and then bid the girls waltz around unclad, and also bid some of them, shod with sandals that were not mates (one high and the other low), chase the doves around—all for the sheer indecency of it. However, he paid the penalty after he went back to Sicily again to resume his government; for the Locri broke up his garrison, set themselves free, and thus became masters of his wife and children. These children were his two daughters, and the younger of his two sons (who was already a lad), for the other, Apollocrates, was helping his father to effect his return to Sicily by force of arms. And although Dionysius—both himself and the Tarantini on his behalf—earnestly begged the Locri to release the prisoners on any terms they wished, they would not give them up; instead, they endured a siege and a devastation of their country. But they poured out most of their wrath upon his daughters, for they first made them prostitutes and then strangled them, and then, after burning their bodies, ground up the bones and sank them in the sea. Now Ephorus, in his mention of the written legislation of the Locri which was drawn up by Zaleucus from the Cretan, the Laconian, and the Areopagite usages, says that Zaleucus was among the first to make the following innovation—that whereas before his time it had been left to the judges to determine the penalties for the several crimes, he defined them in the laws, because he held that the opinions of the judges about the same crimes would not be the same, although they ought to be the same. And Ephorus goes on to commend Zaleucus for drawing up the laws on contracts in simpler language. And he says that the Thurii, who later on wished to excel the Locri in precision, became more famous, to be sure, but morally inferior; for, he adds, it is not those who in their laws guard against all the wiles of false accusers that have good laws, but those who abide by laws that are laid down in simple language. And Plato has said as much—that where there are very many laws, there are also very many lawsuits and corrupt practices, just as where there are many physicians, there are also likely to be many diseases.^[This appears to be an exact quotation, but the translator has been unable to find the reference in extant works. Plato utters a somewhat similar sentiment, however, in the Plat. Rep. 404e-405a] The Halex River, which marks the boundary between the Rhegian and the Locrian territories, passes out through a deep ravine; and a peculiar thing happens there in connection with the grasshoppers, that although those on the Locrian bank sing, the others remain mute. As for the cause of this, it is conjectured that on the latter side the region is so densely shaded that the grasshoppers, being wet with dew, cannot expand their membranes, whereas those on the sunny side have dry and horn-like membranes and therefore can easily produce their song. And people used to show in Locri a statue of Eunomus, the cithara-bard, with a locust seated on the cithara. Timaeus says that Eunomus and Ariston of Rhegium were once contesting with each other at the Pythian games and fell to quarrelling about the casting of the lots;^[Apparently as to which should perform first.] so Ariston begged the Delphians to cooperate with him, for the reason that his ancestors belonged^[Cp. 6. 1. 6.] to the god and that the colony had been sent forth from there;^[From Delphi to Rhegium.] and although Eunomus said that the Rhegini had absolutely no right even to participate in the vocal contests, since in their country even the grasshoppers, the sweetest-voiced of all creatures, were mute, Ariston was none the less held in favor and hoped for the victory; and yet Eunomus gained the victory and set up the aforesaid image in his native land, because during the contest, when one of the chords broke, a grasshopper lit on his cithara and supplied the missing sound. The interior above these cities is held by the Brettii; here is the city Mamertium, and also the forest that produces the best pitch, the Brettian. This forest is called Sila, is both well wooded and well watered, and is seven hundred stadia in length. After Locri comes the Sagra, a river which has a feminine name. On its banks are the altars of the Dioscuri, near which ten thousand Locri, with Rhegini,^[The Greek, as the English, leaves one uncertain whether merely the Locrian or the combined army amounted to 10,000 men. Justin 20.3 gives the number of the Locrian army as 15,000, not mentioning the Rhegini; hence one might infer that there were 5,000 Rhegini, and Strabo might have so written, for the Greek symbol for 5,000 (\rendergreek{,ε}), might have fallen out of the text.] clashed with one hundred and thirty thousand Crotoniates and gained the victory—an occurrence which gave rise, it is said, to the proverb we use with incredulous people, "Truer than the result at Sagra." And some have gone on to add the fable that the news of the result was reported on the same day^[Cicero De Natura Deorum 2.2 refers to this tradition.] to the people at the Olympia when the games were in progress, and that the speed with which the news had come was afterwards verified. This misfortune of the Crotoniates is said to be the reason why their city did not endure much longer, so great was the multitude of men who fell in the battle. After the Sagra comes a city founded by the Achaeans, Caulonia, formerly called Aulonia, because of the glen^["Aulon."] which lies in front of it. It is deserted, however, for those who held it were driven out by the barbarians to Sicily and founded the Caulonia there. After this city comes Scylletium, a colony of the Athenians who were with Menestheus (and now called Scylacium).^[Cp. Vergil Aen. 3.552] Though the Crotoniates held it, Dionysius included it within the boundaries of the Locri. The Scylletic Gulf, which, with the Hipponiate Gulf forms the aforementioned isthmus,^[6. 1. 4.] is named after the city. Dionysius undertook also to build a wall across the isthmus when he made war upon the Leucani, on the pretext, indeed, that it would afford security to the people inside the isthmus from the barbarians outside, but in truth because he wished to break the alliance which the Greeks had with one another, and thus command with impunity the people inside; but the people outside came in and prevented the undertaking. After Scylletium comes the territory of the Crotoniates, and three capes of the Iapyges; and after these, the Lacinium,^[The Lacinium derived its name from Cape Lacinium (now Cape Nao), on which it was situated. According to Diod. Sic. 4.24, Heracles, when in this region, put to death a cattle-thief named Lacinius. Hence the name of the cape.] a temple of Hera, which at one time was rich and full of dedicated offerings. As for the distances by sea, writers give them without satisfactory clearness, except that, in a general way, Polybius gives the distance from the strait to Lacinium as two thousand three hundred stadia,^[Strabo probably wrote "two thousand" and not "one thousand" (see Manner, t. 9. 9, p. 202), and so read Gosselin, Groskurd, Forbiger, Müller-Dübner, and Meineke. Compare Strabo's other quotation (5. 1. 3) from Polybius on this subject. There, as here, unfortunately, the figures ascribed to Polybius cannot be compared with his original statement, which is now lost.] and the distance thence across to Cape Iapygia as seven hundred. This point is called the mouth of the Tarantine Gulf. As for the gulf itself, the distance around it by sea is of considerable length, two hundred and forty miles,^[240 Roman miles=1,920, or 2,000 (see 7. 7. 4), stadia.] as the Chorographer^[See 5. 2. 7, and the footnote.] says, but Artemidorus says three hundred and eighty for a man well-girded, although he falls short of the real breadth of the mouth of the gulf by as much.^[This passage ("although . . . much") is merely an attempt to translate the Greek of the manuscripts. The only variant in the manuscripts is that of "ungirded" for "well-girded." If Strabo wrote either, which is extremely doubtful, we must infer that Artemidorus' figure, whatever it was pertained to the number of days it would take a pedestrian, at the rate, say of 160 stadia (20 Roman miles) per day, to make the journey around the gulf by land. Most of the editors (including Meineke) dismiss the passage as hopeless by merely indicating gaps in the text. Groskurd and C. Müller not only emend words of the text but also fill in the supposed gaps with seventeen and nine words, respectively. Groskurd makes Artemidorus say that a well-girded pedestrian can complete the journey around the gulf in twelve days, that the coasting-voyage around it is 2,000 stadia, and that he leaves for the mouth the same number (700) of stadia assigned by Polybius to the breadth of the mouth of the gulf. But C. Müller writes: "Some make it less, saying 1,380 stadia, whereas Artemidorus makes it as many plus 30 (1,410), in speaking of the breadth of the mouth of the gulf." But the present translator, by making very simple emendations (see critical note 2 on page 38), arrives at the following: Artemidorus says eighty stadia longer (i.e., 2,000) although he falls short of the breadth of the mouth of the gulf by as much (i.e., 700 - 80 = 620). It should be noted that Artemidorus, as quoted by Strabo, always gives distances in terms of stadia, not miles (e.g., 3. 2. 11, 8. 2. 1, 14. 2. 29, et passim), and that his figures at times differ considerably from those of the Chorographer (cp. 6. 3. 10).] The gulf faces the winter-sunrise;^[i.e., south-east.] and it begins at Cape Lacinium, for, on doubling it, one immediately comes to the cities^[As often Strabo refers to sites of perished cities as cities.] of the Achaeans, which, except that of the Tarantini, no longer exist, and yet, because of the fame of some of them, are worthy of rather extended mention. The first city is Croton, within one hundred and fifty stadia from the Lacinium; and then comes the River Aesarus, and a harbor, and another river, the Neaethus. The Neaethus got its name, it is said, from what occurred there: Certain of the Achaeans who had strayed from the Trojan fleet put in there and disembarked for an inspection of the region, and when the Trojan women who were sailing with them learned that the boats were empty of men, they set fire to the boats, for they were weary of the voyage, so that the men remained there of necessity, although they at the same time noticed that the soil was very fertile. And immediately several other groups, on the strength of their racial kinship, came and imitated them, and thus arose many settlements, most of which took their names from the Trojans; and also a river, the Neaethus, took its appellation from the aforementioned occurrence.^[The Greek "Neas aethein" means "to burn ships."] According to Antiochus, when the god told the Achaeans to found Croton, Myscellus departed to inspect the place, but when he saw that Sybaris was already founded—having the same name as the river near by—he judged that Sybaris was better; at all events, he questioned the god again when he returned whether it would be better to found this instead of Croton, and the god replied to him (Myscellus^[Ovid Met. 15.20 spells the name "Myscelus," and perhaps rightly; that is, "Mouse-leg" (?).] was a hunchback as it happened): "Myscellus, short of back, in searching else outside thy track, thou hunt'st for morsels only; 'tis right that what one giveth thee thou do approve;"^[For a fuller account, see Diod. Sic. 8. 17 His version of the oracle is: "Myscellus, short of back, in searching other things apart from god, thou searchest only after tears; what gift god giveth thee, do thou approve."] and Myscellus came back and founded Croton, having as an associate Archias, the founder of Syracuse, who happened to sail up while on his way to found Syracuse.^[The generally accepted dates for the founding of Croton and Syracuse are, respectively, 710 B.C. and 734 B.C. But Strabo's account here seems to mean that Syracuse was founded immediately after Croton (cp. 6. 2. 4). Cp. also Thucydides 6. 3. 2] The Iapyges used to live at Croton in earlier times, as Ephorus says. And the city is reputed to have cultivated warfare and athletics; at any rate, in one Olympian festival the seven men who took the lead over all others in the stadium-race were all Crotoniates, and therefore the saying "The last of the Crotoniates was the first among all other Greeks" seems reasonable. And this, it is said, is what gave rise to the other proverb, "more healthful than Croton," the belief being that the place contains something that tends to health and bodily vigor, to judge by the multitude of its athletes. Accordingly, it had a very large number of Olympic victors, although it did not remain inhabited a long time, on account of the ruinous loss of its citizens who fell in such great numbers^[Cp. 6. 1 10.] at the River Sagra. And its fame was increased by the large number of its Pythagorean philosophers, and by Milo, who was the most illustrious of athletes, and also a companion of Pythagoras, who spent a long time in the city. It is said that once, at the common mess of the philosophers, when a pillar began to give way, Milo slipped in under the burden and saved them all, and then drew himself from under it and escaped. And it is probably because he relied upon this same strength that he brought on himself the end of his life as reported by some writers; at any rate, the story is told that once, when he was travelling through a deep forest, he strayed rather far from the road, and then, on finding a large log cleft with wedges, thrust his hands and feet at the same time into the cleft and strained to split the log completely asunder; but he was only strong enough to make the wedges fall out, whereupon the two parts of the log instantly snapped together; and caught in such a trap as that, he became food for wild beasts. Next in order, at a distance of two hundred stadia, comes Sybaris, founded by the Achaeans; it is between two rivers, the Crathis and the Sybaris. Its founder was Is of Helice.^[The reading, "Is of Helice," is doubtful. On Helice, see 1. 3. 18 and 8. 7. 2.] In early times this city was so superior in its good fortune that it ruled over four tribes in the neighborhood, had twenty- five subject cities, made the campaign against the Crotoniates with three hundred thousand men, and its inhabitants on the Crathis alone completely filled up a circuit of fifty stadia. However, by reason of luxury^[Cp. "Sybarite."] and insolence they were deprived of all their felicity by the Crotoniates within seventy days; for on taking the city these conducted the river over it and submerged it. Later on, the survivors, only a few, came together and were making it their home again, but in time these too were destroyed by Athenians and other Greeks, who, although they came there to live with them, conceived such a contempt for them that they not only slew them but removed the city to another place near by and named it Thurii, after a spring of that name. Now the Sybaris River makes the horses that drink from it timid, and therefore all herds are kept away from it; whereas the Crathis makes the hair of persons who bathe in it yellow or white, and besides it cures many afflictions. Now after the Thurii had prospered for a long time, they were enslaved by the Leucani, and when they were taken away from the Leucani by the Tarantini, they took refuge in Rome, and the Romans sent colonists to supplement them, since their population was reduced, and changed the name of the city to Copiae. After Thurii comes Lagaria, a stronghold, bounded by Epeius and the Phocaeans; thence comes the Lagaritan wine, which is sweet, mild, and extremely well thought of among physicians. That of Thurii, too, is one of the famous wines. Then comes the city Heracleia, a short distance above the sea; and two navigable rivers, the Aciris and the Siris. On the Siris there used to be a Trojan city of the same name, but in time, when Heracleia was colonized thence by the Tarantini, it became the port of the Heracleotes. It is Twenty-four stadia distant from Heracleia and about three hundred and thirty from Thurii. Writers produce as proof of its settlement by the Trojans the wooden image of the Trojan Athene which is set up there—the image that closed its eyes, the fable goes, when the suppliants were dragged away by the Ionians who captured the city; for these Ionians came there as colonists when in flight from the dominion of the Lydians, and by force took the city, which belonged to the Chones,^[Cp. 6. 1. 2.] and called it Polieium; and the image even now can be seen closing its eyes. It is a bold thing, to be sure, to tell such a fable and to say that the image not only closed its eyes (just as they say the image in Troy turned away at the time Cassandra was violated) but can also be seen closing its eyes; and yet it is much bolder to represent as brought from Troy all those images which the historians say were brought from there; for not only in the territory of Siris, but also at Rome, at Lavinium, and at Luceria, Athene is called "Trojan Athena," as though brought from Troy. And further, the daring deed of the Trojan women is current in numerous places, and appears incredible, although it is possible. According to some, however, both Siris and the Sybaris which is on the Teuthras^[The "Teuthras" is otherwise unknown, except that there was a small river of that name, which cannot be identified, near Cumae (see Propertius 1. 11.11 and Silius Italicus 11.288). The river was probably named after Teuthras, king of Teuthrania in Mysia (see 12. 8. 2). But there seems to be no evidence of Sybarites in that region. Meineke and others are probably right in emending to the "Trais" (now the Trionto), on which, according to Diod. Sic. 12.22, certain Sybarites took up their abode in 445 B.C.] were founded by the Rhodians. According to Antiochus, when the Tarantini were at war with the Thurii and their general Cleandridas, an exile from Lacedaemon, for the possession of the territory of Siris, they made a compromise and peopled Siris jointly, although it was adjudged the colony of the Tarantini; but later on it was called Heracleia, its site as well as its name being changed. Next in order comes Metapontium, which is one hundred and forty stadia from the naval station of Heracleia. It is said to have been founded by the Pylians who sailed from Troy with Nestor; and they so prospered from farming, it is said, that they dedicated a golden harvest^[An ear, or sheaf, of grain made of gold, apparently.] at Delphi. And writers produce as a sign of its having been founded by the Pylians the sacrifice to the shades of the sons of Neleus.^[Neleus had twelve sons, including Nestor. All but Nestor were slain by Heracles.] However, the city was wiped out by the Samnitae. According to Antiochus: Certain of the Achaeans were sent for by the Achaeans in Sybaris and resettled the place, then forsaken, but they were summoned only because of a hatred which the Achaeans who had been banished from Laconia had for the Tarantini, in order that the neighboring Tarantini might not pounce upon the place; there were two cities, but since, of the two, Metapontium was nearer^[The other, of course, was Siris.] to Taras,^[The old name of Tarentum.] the newcomers were persuaded by the Sybarites to take Metapontium and hold it, for, if they held this, they would also hold the territory of Siris, whereas, if they turned to the territory of Siris, they would add Metapontium to the territory of the Tarantini, which latter was on the very flank of Metapontium; and when, later on, the Metapontians were at war with the Tarantini and the Oenotrians of the interior, a reconciliation was effected in regard to a portion of the land—that portion, indeed, which marked the boundary between the Italy of that time and Iapygia.^[i.e., the Metapontians gained undisputed control of their city and its territory, which Antiochus speaks of as a "boundary" (cp. 6. 1. 4 and 6. 3. 1).] Here, too, the fabulous accounts place Metapontus,^[The son of Sisyphus. His "barbarian name," according to Stephanus Byzantinus and Eustathius, was Metabus.] and also Melanippe the prisoner and her son Boeotus.^[One of Euripides' tragedies was entitled Melanippe the Prisoner; only fragments are preserved. She was the mother of Boeotus by Poseidon.] In the opinion of Antiochus, the city Metapontium was first called Metabum and later on its name was slightly altered, and further, Melanippe was brought, not to Metabus, but to Dius,^[A Metapontian.] as is proved by a hero-temple of Metabus, and also by Asius the poet, when he says that Boeotus was brought forth "in the halls of Dius by shapely Melanippe,"^[Asius Fr.] meaning that Melanippe was brought to Dius, not to Metabus. But, as Ephorus says, the colonizer of Metapontium was Daulius, the tyrant of the Crisa which is near Delphi. And there is this further account, that the man who was sent by the Achaeans to help colonize it was Leucippus, and that after procuring the use of the place from the Tarantini for only a day and night he would not give it back, replying by day to those who asked it back that he had asked and taken it for the next night also, and by night that he had taken and asked it also for the next day.Next in order comes Taras and Iapygia; but before discussing them I shall, in accordance with my original purpose, give a general description of the islands that lie in front of Italy; for as from time to time I have named also the islands which neighbor upon the several tribes, so now, since I have traversed Oenotria from beginning to end, which alone the people of earlier times called Italy, it is right that I should preserve the same order in traversing Sicily and the islands round about it.[^ab2a6957b5864c6ebe57c39eabc138c4]

  
## To Iader By Ship

From Titius (river) to Iader is a journey of about 48 miles when travelling by ship down the coast. 

The sky all round them and all round them the deep.   
  
They beheld the harbor of Iader with gladness. Here they shape the thin oar-blades. For they care not for bow or quiver, but for masts and oars of ships. 

All of this brought to his mind what Aristotle. 384-322 had said about the countryside near that place:

## A Story About The Countryside Near That Place


The wealthiest inhabitants were selected to provide the choruses, and were informed what they were expected to furnish. Noticing their disinclination, Philoxenus sent to them privately and asked what they would give to be relieved of the duty. They told him they were prepared to pay a much larger sum than they expected to spend  in order to avoid the trouble and the interruption of their business. Philoxenus accepted their offers, and proceeded to enrol a second levy. These also paid; and at last he received what he desired from each company. Euaises the Syrian, when governor of Egypt, received information that the local governors were meditating rebellion. He therefore summoned them to the palace and proceeded to hang them all, sending word to their relations that they were in prison. These accordingly made offers, each on behalf of his own kinsman, seeking by payment to secure their release. Euaises agreed to accept a certain sum for each, and when it had been paid returned to the relations the dead body. While Cleomenes of Alexandria was governor of Egypt,^[Cf. Dem. 56: "Cleomenes . . . from the time that he received the government, has done immense mischief to your state, and still more to the rest of Greece, by buying up corn for resale and keeping it at his own price" ( Kennedy's translation).] at a time when there was some scarcity in the land, but elsewhere a grievous famine, he forbade the export of grain. On the local governors representingthat if there were no export of grain they would be unable to pay in their taxes, he allowed the export, but laid a heavy duty on the corn. By this means he obtained a large amount of duty from a small amount of export, and at the same time deprived the officials of their excuse.When Cleomenes was making a progress by water through the province where the crocodile is worshipped, one of his servants was carried off. Accordingly, summoning the priests, he told them that he intended to retaliate on the crocodiles for this unprovoked aggression; and gave orders for a battue. The priests, to save the credit of their god, collected all the gold they could, and succeeded in putting an end to the pursuit.King Alexander had given Cleomenes command to establish a town near the island of Pharus, and to transfer thither the market hitherto held at Canopus. Sailing therefore to Canopus he informed the priests and the men of property there that he was come to remove them. The priests and residents thereupon contributed money to induce him to leave their market where it was. He took what they offered, and departed; but afterwards returned, when all was ready to build the town,[^f12aa0107c3d41e19828808a5f7c9168]

  
## Departing From Iader

From Iader to Burnum is a journey of about 40 miles when travelling by road. 

There a spring wells up, and around about it is a meadow. A caravan from Burnum passed by. The road narrows here, an orchard wall encroaching on it. He passes another milestone. His shoes are covered in dust from the road. 

While he was visiting Salona, he made a point of copying down what Julius Caesar had written.

## The Story Of Salona


After the departure of the Liburnian his command, sailed from Illyricum, and came before Salona. Having spirited up the Dalmatians, and other barbarous nations in those parts, he drew Issa to revolt from Caesar. But finding that the council of Salona was neither to be moved by promises nor threats, he resolved to invest the town. Salona is built upon a hill, and advantageously situated for defence; but as the fortifications were very inconsiderable, the Roman citizens, residing there, immediately surrounded the place with wooden towers; and finding themselves too few to resist the attacks of the enemy, who soon overwhelmed them with wounds, betook themselves to their last refuge, by granting liberty to all slaves capable of bearing arms, and cutting off the women's hair, to make cords for their engines. Octavius perceiving their obstinacy, formed five different camps round the town, that they might at once suffer all the inconveniences of a siege, and be exposed to frequent attacks. The Salonians, determined to endure any thing, found themselves most pressed for want of corn; and therefore sent deputies to Caesar to solicit a supply, patiently submitting to all the other hardships they laboured under. When the siege had now continued a considerable time, and the Octavians began to be off their guard, the Salonians, finding the opportunity favourable, about noon, when the enemy were dispersed, disposed their wives and children upon the walls, that every thing might have its wonted appearance; and sallying in a body with their enfranchised slaves, attacked the nearest quarters of Octavius. Having soon forced these, they advanced to the next; thence to a third, a fourth, and so on through the rest; till having driven the enemy from every post, and made great slaughter of their men, they at length compelled them, and Octavius their leader, to betake themselves to their ships. Such was the issue of the siege. As winter now approached, and the loss had been very considerable; Octavius, despairing to reduce the place, retired to Dyrrhachium, and joined Pompey.[^5ef1a5880e3444d79887c121fa441f08]

  
## To Salona

Virgil departed from Burnum, intending to travel by road to Salona, at least 50 miles. 

This is a smooth road, by which many wagons were bringing wood to Salona. Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from Salona passed by. He left the city early, before the rising of the sun. 

All of this brought to his mind what Lucan, 39-65 had said about Salona:

## The Story Of Salona


  
Not thus did Fortune upon Caesar smile  
In all the parts of earth;^[The scene is the Dalmatian coast of the Adriatic. Here was Diocletian's palace.] but 'gainst his arms  
Dared somewhat, where Salona's lengthy waste  
Is laved by Hadria, and Iadar warm  
Meets with his waves the breezes of the west.  
There brave Curectae dwell, whose island home  
Is girded by the main; on whom relied  
Antonius, and, beleaguered by the foe,  
Upon the furthest margin of the shore  
(Safe from all ills but famine) placed his camp.  
But for his steeds the earth no forage gave,  
Nor golden Ceres harvest; and his troops  
Gnawed the dry herbage of the scanty turf  
Within their rampart lines. But when they knew  
That Basilus was on th' opposing shore  
With friendly force, by novel mode of flight  
They aim to reach him. Not the accustomed keel  
They lay, nor build the ship, but shapeless rafts  
Of timbers knit together, strong to bear  
All ponderous weight; on empty casks beneath  
By tightened chains made firm, in double rows  
Supported; nor upon the deck were placed  
The oarsmen, to the hostile dart exposed,  
But in a hidden space, by beams concealed.  
And thus the eye amazed beheld the mass  
Move silent on its path across the sea,  
By neither sail nor stalwart arm propelled.  
They watch the main until the refluent waves  
Ebb from the growing sands; then, on the tide  
Receding, launch their vessel; thus she floats  
With comrades twin: and rises over each  
With quivering battlements a lofty tower.  
Octavius, guardian of Illyrian seas,  
Restrained his swifter keels, and left the rafts  
Free from attack, in hope of larger spoil  
From fresh adventures; for the peaceful sea  
Might tempt them, and their goal in safety reached,  
To dare a second voyage. Round the stag  
Thus will the cunning hunter draw a line  
Of tainted feathers poisoning the air;  
Or spread the mesh, and muzzle in his grasp  
The straining jaws of the Molossian hound,  
And leash the Spartan pack; nor is the brake  
Trusted to any dog but such as tracks  
The scent with lowered nostrils, and refrains  
From giving tongue the while; content to mark  
By shaking cord the covert of the prey.  
Ere long they manned the rafts in eager wish  
To quit the island, when the latest glow  
Still parted day from night. But Magnus' troops,  
Cilician once, taught by their ancient art,  
In fraudulent deceit had left the sea  
To view unguarded; but with chains unseen  
Fast to Illyrian shores, and hanging loose,  
They blocked the outlet in the waves beneath.  
The leading rafts passed safely, but the third,  
Caught by the rope, was drawn beneath the rocks.  
These, hollowed by the sea, in ponderous mass  
O'erhanging, seemed upon the point to fall;  
And trees made dark the wave. Here oft the main  
Within the deep recess sweeps broken wrecks  
And bodies of the drowned, till ebbing tides  
Return the spoil. Then from the cavernous arch  
Is belched the ocean forth in such turmoil  
Of swirling billows, as excels the rage  
Of that famed whirlpool on Sicilian shores.  
Here, with Venetian settlers for its load,  
Stood motionless the raft. Octavius' ships  
Gathered around, while foemen on the land  
Filled all the shore. But well the captain knew,  
Volteius, how the secret fraud was planned,  
And tried in vain with sword and steel to burst  
The chains that held them; without hope he fights,  
Uncertain where to avoid or front the foe.  
Caught in the strait they strove as brave men should  
Against opposing hosts; nor long the fight,  
For fallen darkness brought a truce to arms.  
Then to his men disheartened and in fear  
Of coming fate Volteius, great of soul,  
Thus spake in tones commanding: ' Free no more,  
'Save for this little night, consult ye now  
'In this last moment, soldiers, how to face  
'Your final fortunes. No man's life is short  
' Who can take thought for death, nor is your fame  
' Less than a conqueror's, if with breast advanced  
'Ye meet your destined doom. None know how long  
'The life that waits them. Summon your own fate,  
'And equal is your praise, whether the hand  
'Quench the last flicker of departing light,  
' Or shear the hope of years. But choice to die  
'Is thrust not on the mind-we cannot flee;  
'See at our throats, e'en now, our kinsmen's swords.  
' Then choose for death; desire what fate decrees.  
'At least in war's blind cloud we shall not fall;  
' Nor when the flying weapons hide the day,  
'And slaughtered heaps of foemen load the field,  
'And death is common, and the brave man sinks  
'Unknown, inglorious. Us within this ship,  
'Seen of both friends and foes, the gods have placed;  
'Both land and sea and island cliffs shall bear,  
'From either shore, their witness to our death,  
'In which some great and memorable fame  
'Thou, Fortune, dost prepare. What glorious deeds  
' Of warlike heroism, of noble faith,  
'Time's annals show! All these shall we surpass.  
'True, Caesar, that to fall upon our swords  
'For thee is little; yet beleaguered thus,  
'With neither sons nor parents at our sides,  
'Shorn of the glory that we might have earned,  
'We give thee here the only pledge we may.  
'Yet let these hostile thousands fear the souls  
'That rage for battle and that welcome death,  
'And know us for invincible, and joy  
'That no more rafts were stayed. They'll offer terms,  
'And tempt us with a base unhonoured life.  
'Would that, to give that death which shall be ours  
'The greater glory, they may bid us hope  
'For pardon and for life! lest when our swords  
'Are reeking with our hearts'-blood, they may say  
'This was despair of living. Great must be  
'The prowess of our end, if in the hosts  
'That fight his battles, Caesar is to mourn  
'This little handful lost. For me, should fate  
'Grant us retreat-myself would scorn to shun  
'The coming onset. Life I cast away,  
'The frenzy of the death that comes apace  
'Controls my being. Those whose end is near  
'Alone may know the happiness of death;  
'Which pitying heaven from all else conceals  
'That men may bear to live.'^[Quoted in Sir T. Browne's 'Religio Medici,' i., 44. 'There be many excellent strains in that Poet wherewith his stoical genius hath liberally supplied him.'] His stirring words  
Warmed his brave comrades' hearts-they who with fear  
And tearful eyes had looked upon the Wain,  
Turning his nightly course, now hoped for day,  
Such precepts deep within them. Nor delayed  
The sky to dip the stars below the main;  
For Phoebus in the Twins his chariot drave  
At noon near Cancer; and the hours of night^[That is, night was at its shortest.]  
Were shortened by the Archer.  
When day broke,  
Lo! on the rocks the Istrians;^[On this passage see Dean Merivale's remarks, 'History of the Roman Empire,' chapter xvi.] while the sea  
Swarmed with the galleys and their Grecian fleet  
All armed for fight: but first the war was stayed  
And terms proposed: life to the foe they thought  
Would seem the sweeter, by delay of death  
Thus granted. But the band devoted stood,  
Proud of their promised end, life all forsworn,  
And careless of the fight: no jarring note  
Opposed their high resolve. In numbers few  
'Gainst foemen numberless by land and sea,  
They wage the desperate war; then satiate  
Turn from the foe. And first demanding death  
Volteius bared his throat. ' What youth,' he cries,  
' Dares strike me down, and through his captain's wounds  
'Attest his love for death? ' Then through his side  
Plunge blades uncounted on the moment drawn.  
He praises all : but him who struck the first  
Grateful, with dying strength, he does to death.  
They rush together, and without a foe  
Work all the guilt of battle. Thus of yore,  
Rose up the glittering Dircaean band  
From seed by Cadmus sown, and fought and died,  
Dire omen for the brother kings of Thebes.  
And so in Phasis' fields the sons of earth,  
Born of the sleepless dragon, all inflamed  
By magic incantations, with their blood  
Deluged the monstrous furrow, while the Queen  
Feared at the spells she wrought. Devoted thus  
To death, they fall, yet in their death itself  
Less valour show than in the fatal wounds  
They take and give; for e'en the dying hand  
Missed not a blow nor did the stroke alone  
Inflict the wound, but rushing on the sword  
Their throat or breast received it to the hilt;  
And when by fatal chance or sire with son,  
Or brothers met, yet with unfaltering weight  
Down flashed the pitiless sword: this proved their love,  
To give no second blow. Half living now  
They dragged their mangled bodies to the side,  
Whence flowed into the sea a crimson stream  
Of slaughter. 'Twas their pleasure yet to see  
The light they scorned; with haughty looks to scan  
The faces of their victors, and to feel  
The death approaching. But the raft was now  
Piled up with dead; which, when the foemen saw,  
Wondering at such a chief and such a deed,  
They gave them burial. Never through the world  
Of any brave achievement was the fame  
More widely blazed. Yet meaner men, untaught  
By such examples, see not that the hand  
Which frees from slavery needs no valiant mind  
To guide the stroke. But tyranny is feared  
As dealing death; and Freedom's self is galled  
By ruthless arms; and knows not that the sword  
Was given for this, that none need live a slave.  
Ah Death! wouldst thou but let the coward live  
And grant the brave alone the prize to die!  
Nor less were Libyan fields ablaze with war.  
[^88962ea5db354054954ea7c5430f2238]

  
## Travelling By Ship

From Salona to Aternum is about 153 miles away when travelling by ship down the coast. 

They spread their sails and ran over the waste sea in their hollow wood.   
  
The harbor of Aternum came into view over the horizon. The people of Aternum all have stations for their ships, each man one for himself. 

The library at the countryside near that place happened to have a copy of _Histories_, where Virgil encountered it.

## What Polybius Once Said About The Countryside Near That Place


It did not escape the observation of Aratus that the people of Megalopolis would be more ready than others to seek the protection of Antigonus, and the hopes of safety offered by Macedonia; for their neighbourhood to Sparta exposed them to attack before the other states; while they were unable to get the help which they ought to have, because the Achaeans were themselves hard pressed and in great difficulties. Besides they had special reasons for entertaining feelings of affection towards the royal family of Macedonia, founded on the favours received in the time of Philip, son of Amyntas. He therefore imparted his general design under pledge of secrecy to Nicophanes and Cercidas of Megalopolis, who were family friends of his own and of a character suited to the undertaking; and by their means experienced no difficulty in inducing the people of Megalopolis to send envoys to the league, to advise that an application for help should be made to Antigonus. Nicophanes and Cercidas were themselves selected to go on this mission to the league, and thence, if their view was accepted, to Antigonus. The league consented to allow the people of Megalopolis to send the mission; and accordingly Nicophanes lost no time in obtaining an interview with the king. About the interests of his own country he spoke briefly and summarily, confining himself to the most necessary statements; the greater part of his speech was, in accordance with the directions of Aratus, concerned with the national question.[^218461c3301e4ae9adeca61a2b85bd4e]

  
## From Aternum To Castrum Truentinum

Leaving Aternum, Virgil set out for Castrum Truentinum by ship down the coast, at least 38 miles. 

Straightway the winds upturn the main, and great seas rise. Then comes the creak of cables and the cries of seamen. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Round swings the prow, and lets the waters sweep the broadside. Down in a heap comes a broken mountain of water. They are in the wave's huge hollow. Yawning wide, the wave lays bare the ground below. The south wind catches and hurls a ship on hidden rocks. As she lies the billow sends her spinning thrice round with it, and engulfs her in the swift whirl.   
  
Then was land at last seen to rise, discovering distant hills and sending up wreaths of smoke.   
  
Within a long recess there lies a bay: an island shades it from the rolling sea and forms a port secure for ships to ride. Beneath a precipice that fronts the wave, with limpid springs inside, and many a seat of living marble, lies a sheltered cave. Glad at length to greet the welcome earth, the sailors leap to land. They lay their weary limbs still dripping on the sand. 

The library at the countryside near that place happened to have a copy of _For Sextus Roscius of Ameria_, where Virgil encountered it.

## A Story About The Countryside Near That Place


Of such important and such atrocious actions, I am aware that I can neither speak with sufficient propriety, nor complain with sufficient dignity, nor cry out against with sufficient freedom. For my want of capacity is a hindrance to my speaking with propriety; my age, to my speaking with dignity; the times themselves are an obstacle to my speaking with freedom. To this is added great fear, which both nature and my modesty cause me, and your dignity, and the violence of our adversaries, and the danger of Sextus Roscius. On which account, I beg and entreat of you, O judges, to hear what I have to say with attention, and with your favourable construction.[^3eb8faafbb834f38a17da2cc90440190]

  
## From Castrum Truentinum To Asculum

From Castrum Truentinum to Asculum is a journey of about 17 miles when travelling by road. 

Along the road are graves, and a cenotaph. Workers are raising the level of the road. He had set out from Castrum Truentinum amidst a throng travelling the same way. There is a fountain of cold water springing from the rock. He left the city early, before the rising of the sun. A caravan from Asculum passed by. Next to the straight road that leads to Asculum, there is visible a sculpted tomb. His shoes are covered in dust from the road. 

All of this brought to his mind what Suetonius ca. 69-ca. 122 had said about the countryside near that place:

## The Story Of The Countryside Near That Place


THE empire, which had been long thrown into a disturbed and unsettled state, by the rebellion and violent death of its three last rulers, was at length restored to peace and security by the Flavian family, whose descent was indeed obscure, and which boasted no ancestral honours; but the public had no cause to regret its elevation; though it is acknowledged that Domitian met with the just reward of his avarice and cruelty. Titus Flavius Petro, a townsman of Reate,^[Reate, the original seat of the Flavian family, was a city of the Sabines. Its present name is Rieti. ] whether a centurion or an _evocatus_^[It does not very clearly appear what rank in the Roman armies was held by the evocati. They are mentioned on three occasions by Suetonius, without affording us much assistance. Caesar, like our author, joins them with the centurions. See, in particular, De Bell. Civil. I. xvii. 4. ] of Pompey's party in the civil war, is uncertain, fled out of the battle of Pharsalia and went home; where, having at last obtained his pardon and discharge, he became a collector of the money raised by public sales in the way of auction. His son, surnamed Sabinus, was never engaged in the military service, though some say he was a centurion of the first order, and others, that whilst he held that rank, he was discharged on account of his bad state of health: this Sabinus, I say, was a republican, and received the tax of the fortieth penny in Asia. And there were remaining, at the time of the advancement of the family, several statues, which had been erected to him by the cities of that province, with this inscription: "To the honest Tax-farmer."^[The inscription was in Greek, \rendergreek{καλῶς τελωθήσαντι}] He afterwards turned usurer amongst the Helvetii, and there died, leaving behind him his wife, Vespasia Polla, and two sons by her; the elder of whom, Sabinus, came to be prefect of the city, and the younger, Vespasian, to be emperor. Polla, descended of a good family, at Nursia,^[In the ancient Umbria. afterwards the duchy of Spoleto; its modern name being Norcia.] had for her father Vespasius Pollio, thrice appointed military tribune, and at last prefect of the camp; and her brother was a senator of praetorian dignity. There is to this day, about six miles from Nursia, on the road to Spoletum, a place on the summit of a hill, called Vespasize, where are several monuments of the Vespasii, a sufficient proof of the splendour and antiquity of the family. I will not deny that some have pretended to say. that Petro's father was a native of Gallia Transpadana,^[Gaul beyond, north of, the Po, now Lombardy. ] whose employment was to hire work-people who used to emigrate every year from the country of the Umbria into that of the Sabines, to assist them in their husbandry;^[We find the annual migration of labourers in husbandry a very common practice in ancient as well as in modern times. At present, several thousand industrious labourers cross over every summer from the duchies of Parma and Modena, bordering on the district mentioned by Suetonius, to the island of Corsica; returning to the continent when the harvest is got in. ] but who settled at last in the town of Reate, and there married. But of this I have not been able to discover the least proof, upon the strictest inquiry.[^75a6e222274c4482be3df92b07dbfc55]

  
## Departing From Asculum

From Asculum to Reate is at least 59 miles when travelling by road. 

Now the road is quieter. His shoes are covered in dust from the road. By the road is a salt spring. Above the roads are ruins, among which is a cave sacred to Asclepius. There is a fountain of cold water springing from the rock. He had set out from Asculum amidst a throng travelling the same way. He left the city early, before the rising of the sun. An oxcart passes, loaded with grain. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

While he visited his friend at Reate, he was pleased to discover _Commentary on Vergil's Aeneid, Volume 2_, by John Conington. Picking it up, he read:

## On The Subject Of Reate


Sulfurea explains "albus." Virg. doubtless thought of Enn. A. 7. fr. 19, Sulfureas posuit spiramina Naris ad undas. "Fontes Velini" appears to be the lacus Velinus in the hills beyond Reate and close to the Nar, at least seventy miles from the Trojan camp. The limit may be merely poetical, or it may designate loosely the Sabine country as the extremity of the confederacy.[^86c0b69cb98f49659fb1621144dd8b68]

\newpage

# Reate To Formiae
  
## 44 Miles To Roma

Intending to travel by road to Roma, Virgil left Reate. It was a distance of about 44 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A grove of Minerva is hard by the road, a grove of poplar trees. His shoes are covered in dust from the road. A caravan from Roma passed by. The sun beats down. Now the road is quieter. Workers are raising the level of the road. 

All of this brought to his mind what Ovid 43 B.C.-17 or 18 A.D had said about Roma:

## A Story About Roma By Ovid 43 B.C.-17 Or 18 A.D


  
When ended was this piteous plaint, the Earth did hold hir peace.  
She could no lenger dure the heate but was compelde to cease.  
Into hir bosome by and by she shrunke hir cinged heade  
More nearer to the Stygian caves, and ghostes of persones deade.  
The Sire of Heaven protesting all the Gods and him also  
That lent the Chariot to his child, that all of force must go  
To havocke if he helped not, went to the highest part  
And top of all the Heaven from whence his custome was to dart  
His thunder and his lightning downe. But neyther did remaine  
A Cloude wherewith to shade the Earth, nor yet a showre of raine.  
Then with a dreadfull thunderclap up to his eare he bent  
His fist, and at the Wagoner a flash of lightning sent,  
Which strake his bodie from the life and threw it over wheele  
And so with fire he quenched fire. The Steedes did also reele  
Upon their knees, and starting up sprang violently, one here,  
And there another, that they brast in pieces all their gere.  
They threw the Collars from their neckes, and breaking quite asunder  
The Trace and Harnesse flang away: here lay the bridles: yonder  
The Extree plucked from the Naves: and in another place  
The shevered spokes of broken wheeles: and so at every pace  
The pieces of the Chariot torne lay strowed here and there.  
But Phaeton (fire yet blasing stil among his yellow haire)  
Shot headlong downe, and glid along the Region of the Ayre  
Like to a starre in Winter nights (the wether cleare and fayre)  
Which though it doe not fall in deede, yet falleth to our sight,  
Whome almost in another world and from his countrie quite  
The River Padus did receyve, and quencht his burning head.  
The water Nymphes of Italie did take his carkasse dead  
And buried it yet smoking still, with Joves threeforked flame,  
And wrate this Epitaph in the stone that lay upon the same:  
Here lies the lusty Phaeton which tooke in hand to guide  
His fathers Chariot, from the which although he chaunst to slide:  
Yet that he gave a proud attempt it cannot be denide.  
Wyth ruthfull cheere and heavie heart his father made great mone  
And would not shew himselfe abrode, but mournd at home alone.  
And if it be to be beleved, as bruited is by fame  
A day did passe without the Sunne. The brightnesse of the flame  
Gave light: and so unto some kinde of use that mischiefe came.  
But Clymen having spoke, as much as mothers usually  
Are wonted in such wretched case, discomfortablely,  
And halfe beside hir selfe for wo, with torne and scratched brest,  
Sercht through the universall world, from East to furthest West,  
First seeking for hir sonnes dead coarse, and after for his bones.  
She found them by a forren streame, entumbled under stones.  
There fell she groveling on his grave, and reading there his name,  
Shed teares thereon, and layd hir breast all bare upon the same.  
The daughters also of the Sunne no lesse than did their mother,  
Bewaild in vaine with flouds of teares, the fortune of their brother:  
And beating piteously their breasts, incessantly did call  
The buried Phaeton day and night, who heard them not at all,  
About whose tumbe they prostrate lay. Foure times the Moone had filde  
The Circle of hir joyned hornes, and yet the sisters hilde  
Their custome of lamenting still: (for now continuall use  
Had made it custome.) Of the which the eldest, Phaetuse,  
About to kneele upon the ground, complaynde hir feete were nom.  
To whome as fayre Lampetie was rising for to com,  
Hir feete were held with sodaine rootes. The third about to teare  
Hir ruffled lockes, filde both hir handes with leaves in steade of heare.  
One wept to see hir legges made wood: another did repine  
To see hir armes become long boughes. And shortly to define,  
While thus they wondred at themselves, a tender barke began  
To grow about their thighes and loynes, which shortly overran  
Their bellies, brestes, and shoulders eke, and hands successively,  
That nothing (save their mouthes) remainde, aye calling piteously  
Upon the wofull mothers helpe. What could the mother doe  
But runne now here now there, as force of nature drue hir to  
And deale hir kisses while she might? She was not so content:  
But tare their tender braunches downe: and from the slivers went  
Red drops of bloud as from a wound. The daughter that was rent  
Cride: Spare us mother spare I pray, for in the shape of tree  
The bodies and the flesh of us your daughters wounded bee.  
And now farewell. That word once said, the barke grew over all.  
Now from these trees flow gummy teares that Amber men doe call,  
Which hardened with the heate of sunne as from the boughs they fal  
The trickling River doth receyve, and sendes as things of price  
To decke the daintie Dames of Rome and make them fine and nice.  
Now present at this monstruous hap was Cygnus, Stenels son,  
Who being by the mothers side akinne to Phaeton  
Was in condicion more akinne. He leaving up his charge  
(For in the land of Ligurie his Kingdome stretched large)  
Went mourning all along the bankes and pleasant streame of Po  
Among the trees encreased by the sisters late ago.  
Annon his voyce became more small and shrill than for a man.  
Gray fethers muffled in his face: his necke in length began  
Far from his shoulders for to stretche: and furthermore there goes  
A fine red string acrosse the joyntes in knitting of his toes:  
With fethers closed are his sides: and on his mouth there grew  
A brode blunt byll: and finally was Cygnus made a new  
And uncoth fowle that hight a Swan, who neither to the winde,  
The Ayre, nor Jove betakes himselfe, as one that bare in minde  
The wrongfull fire sent late against his cousin Phaeton.  
In Lakes and Rivers is his joy: the fire he aye doth shon,  
And chooseth him the contrary continually to won.  
Forlorne and altogether voyde of that same bodie shene  
Was Phaetons father in that while which erst had in him bene,  
Like as he looketh in Th'eclypse. He hates the yrkesome light,  
He hates him selfe, he hates the day, and settes his whole delight  
In making sorrow for his sonne, and in his griefe doth storme -  
And chaufe denying to the worlde his dutie to performe.  
My lot (quoth he) hath had inough of this unquiet state  
From first beginning of the worlde. It yrkes me (though too late)  
Of restlesse toyles and thankelesse paines. Let who so will for me  
Go drive the Chariot in the which the light should caried be.  
If none dare take the charge in hand, and all the Gods persist  
As insufficient, he himselfe go drive it if he list,  
That at the least by venturing our bridles for to guide  
His lightning making childlesse Sires he once may lay aside.  
By that time that he hath assayde the unappalled force  
That doth remaine and rest within my firiefooted horse,  
I trow he shall by tried proufe be able for to tell  
How that he did not merit death that could not rule them well.  
The Goddes stoode all about the Sunne thus storming in his rage  
Beseching him in humble wise his sorrow to asswage.  
And that he would not on the world continuall darkenesse bring,  
Jove eke excusde him of the fire the which he chaunst to sling,  
And with entreatance mingled threates as did become a King.  
Then Phebus gathered up his steedes that yet for feare did run  
Like flaighted fiendes, and in his moode without respect begun  
To beate his whipstocke on their pates and lash them on the sides.  
It was no neede to bid him chaufe; for ever as he rides  
He still upbraides them with his sonne, and layes them on the hides.  
[^b0c063a26f004f28ba36b3ee4d6fab65]

  
## To Ostia/Portus By River

From Roma to Ostia/Portus is about 17 miles away when travelling on a boat heading downstream. 

A breeze from an unexpected quarter cools the air. The sun beats down. On a pillar was written: Augurin(o) co(n)s(ule). He contemplated it. 

While he was visiting Ostia/Portus, he made a point of copying down what Suetonius ca. 69-ca. 122 had written.

## On Ostia/Portus, According To Suetonius Ca. 69-Ca. 122


In nothing was he more prodigal than in his buildings. He completed his palace by continuing it from the Palatine to the Esquiline hill, calling the building at first only "The Passage," but after it was burnt down and rebuilt, "The Golden House.^[The Palace of the Caesars, on the Palatine hill, was enlarged by Augustus from the dimensions of a private house (see AUGTUSTUS, cc. xxix., lvii.). Tiberius made some additions to it, and Caligula extended it to the forum (CALIGULA, c. xxxi.). Tacitus gives a similar account with that of our author of the extent and splendour of the works of Claudius. Annma xv. c. xlli. Reaching from the Palatine to the Esquiline hill, it covered all the intermediate space, where the Colosseum now stands. We shall find that it was still further enlarged by Domitian, c. xv. of his life in the present work.] Of its dimensions and furniture, it may be sufficient to say thus much: the porch was so high that there stood in it a colossal statue of himself a hundred and twenty feet in height; and the space included in it was so ample, that it had triple porticos a mile in length, and a lake like a sea, surrounded with buildings which had the appearance of a city. Within its area were corn fields, vineyards, pastures, and woods, containing a vast number of animals of various kinds, both wild and tame. In other parts it was entirely over-laid with gold, and adorned with jewels and mother of pearl. The supper rooms were vaulted, and compartments of the ceilings, inlaid with ivory, were made to revolve, and scatter flowers; while they contained pipes which shed unguents upon the guests. The chief banqueting room was circular, and revolved perpetually, night and day, in imitation of the motion of the celestial bodies. The baths were supplied with water from the sea and the Albula. Upon the dedication of this magnificent house after it was finished, all he said in approval of it was, "that he had now a dwelling fit for a man." He commenced making a pond for the reception of all the hot springs from Baiae, which he designed to have continued from Misenum to the Avernian lake, in a conduit, enclosed in galleries: and also a canal from Avernum to Ostia, that ships might pass from one to the other, without a sea voyage. The length of the proposed canal was one hundred and sixty miles; and it was intended to be of breadth sufficient to permit ships with five banks of oars to pass each other. For the execution of these designs, he ordered all prisoners, in every part of the empire, to be brought to Italy; and that even those who were convicted of the most heinous crimes, in lieu of any other sentence, should be condemned to work at them. He was encouraged to all this wild and enormous profu sion, not only by the great revenue of the empire, but by the sudden hopes given him of an immense hidden treasure, which queen Dido, upon her flight from Tyre, had brought with her to Africa. This, a Roman knight pretended to assure him, upon good grounds, was still hid there in some deep caverns, and might with a little labour be recovered.[^8b8fa88085374db6aeeb3edb8a63a234]

  
## Departing From Ostia/Portus

Virgil departed from Ostia/Portus, intending to travel by ship down the coast to Tarracina, a journey of about 77 miles. 

The ship held the high seas, no land yet appearing.   
  
Driven from our course, we go wandering on the blind waves. Dubious days of blind darkness we wander on the deep, nights without a star. Without delay the sailors strongly toss up the foam.   
  
They beheld the harbor of Tarracina with gladness. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. They care for the shapely ships, rejoicing in that which they cross over the grey sea. 

While he was visiting Tarracina, he made a point of copying down what John Conington had written.

## On Tarracina, According To John Conington


Geticis qui praesidet arvis 3. 35. Here the reference seems to be to the position of the temple on a height. For the different views taken of the goddess Feronia see Dict. M. s. v. She appears again 8. 564 as the mother of a king Erulus. More than one grove was called by her name: that meant here was three miles from Tarracina (Hor. 1 S. 5. 24 foll.), on the border of the Pontine marshes (Dict. G. s. v.).[^3992eae6099f4698ae00d4fefdc8c698]

  
## 24 Miles To Formiae

From Tarracina to Formiae is a distance of about 24 miles when travelling by ship down the coast. 

The sky all round them and all round them the deep. A dusky shower drew up overhead carrying night and tempest.   
  
Dubious days of blind darkness we wander on the deep, nights without a star. The sails drop; they swing back to the oars.   
  
The harbor of Formiae came into view over the horizon. Here the men are busied with the tackle of their black ships, with cables and sails. Here they shape the thin oar-blades. 

He would later record what Suetonius ca. 69-ca. 122 had said about Formiae.

## A Story About Formiae


He lived twenty-nine years, and reigned three years, ten months and eight days. His body was carried privately into the Lamian Gardens,^[The Lamian was an ancient family, the founders of Formiae. They had gardens on the Esquiline mount.] where it was half burnt upon a pile hastily raised, and then had some earth carelessly thrown over it. It was afterwards disinterred by his sisters, on their return from banishment, burnt to ashes, and buried. Before this was done, it is well-known that the keepers of the gardens were greatly disturbed by apparitions; and that not a night passed without some terrible alarm or other in the house where he was slain, until it was destroyed by fire. His wife Caesonia was killed with him, being stabbed by a centurion; and his daughter had her brains knocked out against a wall.[^76d321a74fc94d9ba741745dfbb1cee0]

  
## Travelling By Ship

Intending to travel by ship down the coast to Minturnae, Virgil left Formiae. It was at least 18 miles. 

The ship held the high seas, no land yet appearing. A dusky shower drew up overhead carrying night and tempest.   
  
Dubious days of blind darkness we wander on the deep, nights without a star. The sails drop; they swing back to the oars.   
  
They beheld the harbor of Minturnae with gladness. For they care not for bow or quiver, but for masts and oars of ships. 

All of this brought to his mind what John Conington had said about Minturnae:

## Minturnae In _Commentary On Vergil'S Aeneid, Volume 2_


Moveo stir, and so commence. Comp. v. 641 cantusque movete, and Livy 23. 39, movere ac moliri quicquam. For Latinus, the Italian god Faunus and the nymph Marica, who was worshipped at Minturnae, see Dict. Myth. "Arva et urbes" 3. 418.[^de8763598f3d42ed8bc8bb865ccc2260]

  
## Travelling By Ship Down The Coast To Formiae

Leaving Minturnae, Virgil set out for Formiae by ship down the coast, a distance of about 18 miles. 

The ship held the high seas, no land yet appearing.   
  
Out of the clouds bursts fire fast upon fire. The navigator professes he cannot tell day from night on the sky, nor remember the way amid the waters. The sails drop; they swing back to the oars.   
  
They beheld the harbor of Formiae with gladness. For they care not for bow or quiver, but for masts and oars of ships. 

All of this brought to his mind what Horace had said about Formiae:

## Formiae In _Satires_


HAVING^[ Octavius and Antony, both aspiring to the sovereign power, must necessarily have had frequent quarrels and dissensions. Their reconciliations were of short continuance, because they were insincere. Among many negotiations, undertaken by their common friends to reconcile them, history mentions two more particularly. The first in the year 714, the other in 717, which was concluded by the mediation of Octavia, and to which our poet was carried by Maecenas. ] left mighty Rome, Aricia received me in but a middling inn: Heliodorus the rhetorician, most learned in the Greek language, was my fellow-traveler: thence we proceeded to Forum-Appi, stuffed with sailors and surly landlords. This stage, but one for better travelers^[ Praecinctis. Prepared for traveling, i. e. _altius praecincis_, "to those who were better travelers than we were." _Praecinctus_ means having the dress tucked up, that it may not prevent exertion. Hence used for "diligent," "active." Compare Sat. ii. 8, 10. ] than we, being laggard we divided into two; the Appian way is less tiresome to bad travelers. Here I, on account of the water, which was most vile, proclaim war against my belly, waiting not without impatience for my companions while at supper.

Octavius and Antony, both aspiring to the sovereign power, must necessarily have had frequent quarrels and dissensions. Their reconciliations were of short continuance, because they were insincere. Among many negotiations, undertaken by their common friends to reconcile them, history mentions two more particularly. The first in the year 714, the other in 717, which was concluded by the mediation of Octavia, and to which our poet was carried by Maecenas.

Praecinctis. Prepared for traveling, i. e. _altius praecincis_, "to those who were better travelers than we were." _Praecinctus_ means having the dress tucked up, that it may not prevent exertion. Hence used for "diligent," "active." Compare Sat. ii. 8, 10.

Now the night was preparing to spread her shadows upon the earth, and to display the constellations in the heavens. Then our slaves began to be liberal of their abuse to the watermen, and the watermen to our slaves. "Here bring to." "You are stowing in hundreds; hold, now sure there is enough."

Thus while the fare is paid, and the mule fastened, a whole hour is passed away. The cursed gnats, and frogs of the fens, drive off repose. While the waterman and a passenger, well-soaked with plenty of thick wine, vie with one another in singing the praises of their absent mistresses: at length the passenger being fatigued, begins to sleep; and the lazy waterman ties the halter of the mule, turned out a-grazing, to a stone, and snores, lying flat on his back. And now the day approached, when we saw the boat made no way; until a choleric fellow, one of the passengers, leaps out of the boat, and drubs the head and sides of both mule and waterman with a willow cudgel. At last we were scarcely set ashore at the fourth hour.^[ Quarta hora. The Romans during more than four hundred and fifty years never had names for the hours of the day. The twelve tables divided it into three parts; the rising sun, the setting sun, and mid-day. The hours of night and day were equal in number through the year; but from spring to autumn, those of the day were longer than those of the night, and from September to March the hours of night were longest. ] We wash our faces and hands in thy water, O Feronia. Then, having dined, we crawled on three miles; and arrive under Anxur, which is built upon rocks that look white to a great distance. Maecenas was to come here, as was the excellent Cocceius, both sent embassadors on matters of great importance; having been accustomed to reconcile friends at variance.^[ Three particulars demonstrate that this journey was to the second conference at Brundusium. Fonteius is here joined with Maecenas and Cocceius, but was not engaged in the first. The poet says, that Maecenas and Cocceius had been before employed to reconcile Octavius and Antony, _soliti_, which must necessarily suppose the first congress in 714, when Horace had not been introduced to Macenas. ] Here, having got sore eyes, I was obliged to use the black ointment. In the mean time came Macenas and Cocceius, and Fonteius Capito^[ Fonteius Capito. Probably the father of him who was consul two years before the death of Augustus. he was here of the party of Antony, and Maecenas on the side of Augustus. Cocceius was by way of an arbitrator between them, to settle their differences. Homo factus ad unguem, a complete man, every way accomplished. ] along with them, a man of perfect polish,^[ Ad unguem factus homo. This figurative expression is taken from engravers in wood or marble, who used to pass their nail over the work, to know whether it were well polished. ] and intimate with Mark Antony, no man more so.

Quarta hora. The Romans during more than four hundred and fifty years never had names for the hours of the day. The twelve tables divided it into three parts; the rising sun, the setting sun, and mid-day. The hours of night and day were equal in number through the year; but from spring to autumn, those of the day were longer than those of the night, and from September to March the hours of night were longest.

Three particulars demonstrate that this journey was to the second conference at Brundusium. Fonteius is here joined with Maecenas and Cocceius, but was not engaged in the first. The poet says, that Maecenas and Cocceius had been before employed to reconcile Octavius and Antony, _soliti_, which must necessarily suppose the first congress in 714, when Horace had not been introduced to Macenas.

Fonteius Capito. Probably the father of him who was consul two years before the death of Augustus. he was here of the party of Antony, and Maecenas on the side of Augustus. Cocceius was by way of an arbitrator between them, to settle their differences. Homo factus ad unguem, a complete man, every way accomplished.

Ad unguem factus homo. This figurative expression is taken from engravers in wood or marble, who used to pass their nail over the work, to know whether it were well polished.

Without regret we passed Fundi, where Aufidius Luscus was praetor,^[ Praetore. The colonies and municipal towns had the same dignities and magistracies as the city of Rome; senators, praetors, quaestors, and aediles. It is difficult to know whether Fundi had a praetor chosen out of her own citizens, or whether he was sent from Rome. ] laughing at the honors of that crazy scribe,^[ Praemia scribe. Horace calls these robes praemia scribae, because the secretaries in colonies and municipal towns were frequently raised to the dignity of the praetorship. The _toga praetexta_ was a robe bordered with purple. _Tunica clavata_ was a vest with two borders of purple laid like a lace upon the middle or opening of it, down to the bottom; in such a manner as that when the vest was drawn close or buttoned, the two purple borders joined and seemed to be but one. If these borders were large, the vest was called _latus clavus_, or _tunica laticlavia_; if they were narrow, then it was named _angustus clavus, tunica angusticlavia_. These two sorts of tunics were worn to distinguish the magistrates in their employments, and were very different from those worn by the common people, _tunicato popello_, which were closed before, and without any purple border. They were called _tunicae rectae._ ] his praetexta, laticlave, and pan of incense.^[ Prunaeque batillum. A pan for incense, frequently carried before the emperors, of those possessed of the sovereign authority. ] At our next stage, being weary, we tarry in the city of the Mamurrae,^[ The stroke of satire here is of a delicate and almost imperceptible malignity. Formiae, the city which Horace means, belonged to the Lamian family, whose antiquity was a great honor to it. But our poet paraphrases it by the name of a person, who was born there, and who has made his country famous in a very different manner. Mamurra was a Roman knight, who was infamous for his rapine, luxury and debauchcry. Catullus calls him _Decoctor Formianus._ ] Murena complimenting us with his house,^[ Murena was brother of Licymnia, married afterward to Maecenas. He was condemned to death for conspiring against Augustus. Varius and Plotius Tucca were the persons to whom Augustus intrusted the correction of the Aeneid, after Virgil's death, but with an order not to make any additions to it. ] and Capito with his kitchen.

Praetore. The colonies and municipal towns had the same dignities and magistracies as the city of Rome; senators, praetors, quaestors, and aediles. It is difficult to know whether Fundi had a praetor chosen out of her own citizens, or whether he was sent from Rome.

Praemia scribe. Horace calls these robes praemia scribae, because the secretaries in colonies and municipal towns were frequently raised to the dignity of the praetorship. The _toga praetexta_ was a robe bordered with purple. _Tunica clavata_ was a vest with two borders of purple laid like a lace upon the middle or opening of it, down to the bottom; in such a manner as that when the vest was drawn close or buttoned, the two purple borders joined and seemed to be but one. If these borders were large, the vest was called _latus clavus_, or _tunica laticlavia_; if they were narrow, then it was named _angustus clavus, tunica angusticlavia_. These two sorts of tunics were worn to distinguish the magistrates in their employments, and were very different from those worn by the common people, _tunicato popello_, which were closed before, and without any purple border. They were called _tunicae rectae._

Prunaeque batillum. A pan for incense, frequently carried before the emperors, of those possessed of the sovereign authority.

The stroke of satire here is of a delicate and almost imperceptible malignity. Formiae, the city which Horace means, belonged to the Lamian family, whose antiquity was a great honor to it. But our poet paraphrases it by the name of a person, who was born there, and who has made his country famous in a very different manner. Mamurra was a Roman knight, who was infamous for his rapine, luxury and debauchcry. Catullus calls him _Decoctor Formianus._

Murena was brother of Licymnia, married afterward to Maecenas. He was condemned to death for conspiring against Augustus. Varius and Plotius Tucca were the persons to whom Augustus intrusted the correction of the Aeneid, after Virgil's death, but with an order not to make any additions to it.

The next day arises, by much the most agreeable to all: for Plotius, and Varius, and Virgil met us at Sinuessa; souls more candid ones than which the world never produced, nor is there a person in the world more bound to them than myself. 0h what embraces, and what transports were there! While I am in my senses, nothing can I prefer to a pleasant friend. The village, which is next adjoining to the bridge of Campania, accommodated us with lodging [at night]; and the public officers^[ Parochi . Before the consulship of Lucius Posthumius, the magistrates of Rome traveled at the public charge, without being burthensome to the provinces. Afterward commissaries were appointed in all the great roads to defray all expenses of those who were employed in the business of the state. They were obliged, by the _Lex Julia de provinciis_, to provide lodging, fire, salt, hay, straw, etc. ] with such a quantity of fuel and salt as they are obliged to [by law]. From this place the mules deposited their pack-saddles at Capua betimes [in the morning]. Maecenas goes to play [at tennis]; but I and Virgil to our repose: for to play at tennis is hurtful to weak eyes and feeble constitutions.

Parochi . Before the consulship of Lucius Posthumius, the magistrates of Rome traveled at the public charge, without being burthensome to the provinces. Afterward commissaries were appointed in all the great roads to defray all expenses of those who were employed in the business of the state. They were obliged, by the _Lex Julia de provinciis_, to provide lodging, fire, salt, hay, straw, etc.

From this place the villa of Cocceius, situated above the Caudian inns, which abounds with plenty, receives us. Now, my muse, I beg of you briefly to relate the engagement between the buffoon Sarmentus and Messius Cicirrus; and from what ancestry descended each began the contest. The illutrious race of Messius-Oscan:^[ Osci is a nominative case, and we must construe it, _Osci sunt clarum genus Messii_. The Oscans gave to Messius his illustrious birth, a sufficient proof that he was an infamous scoundrel. The people who inhabited this part of Campania were guilty of execrable debaucheries. ] Sarmentus's mistress is still alive. Sprung from such families as these, they came to the combat. First, Sarmentus: "I pronounce thee to have the look of a mad horse." We laugh; and Messius himself [says], "I accept your challenge:" and wags his head. "O!" cries he, "if the horn were not cut off your forehead, what would you not do; since, maimed as you are, you bully at such a rate?" For a foul scar has disgraced the left part of Messius's bristly forehead. Cutting many jokes upon his Campanian disease, and upon his face, he desired him to exhibit Polyphemus's dance:^[ Saltaret uti Cyclopa. The raillery is founded on his gigantic size, and the villainous gash that Messius had on his forehead, which made him look so like a Polyphemus, that he might dance the part without buskins or a mask. To dance a Cyclops, a Glaucus, a Ganymede, a Leda, was an expression for representing their story by dancing. ] that he had no occasion for a mask, or the tragic buskins. Cicirrus [retorted] largely to these: he asked, whether he had consecrated his chain^[ Donasset iamne catenam. Only the vilest slaves, or those who worked in the country, were chained. It appears by an epigram of Martial, that when they were set at liberty, they consecrated their chains to Saturn, because slavery was unknown under his reign. But when Messius asks Sarmentus whether he had dedicated his chain to the Dii Lares, he would reproach him with being a fugitive. These gods were invoked by travelers, because they presided over highways, from whence they were called viales. They themselves were always represented like travelers, as if they were ready to leave the house; succincti. Or Sarmentus was a slave so vile that he knew no other gods, but those who stood on the hearth, and which it was his employment to keep clean. ] to the household gods according to his vow; though he was a scribe, [he told him] his mistress's property in him was not the less. Lastly, he asked, how lie ever came to run away; such a lank meager fellow, for whom a pound of corn [a-day] would be ample.^[ By the laws of the twelve tables, a slave was allowed a pound of corn a day. "Qui eum vinctum habebit, libras farris in dies dato." ] We were so diverted, that we continued that supper to an unusual length.

Osci is a nominative case, and we must construe it, _Osci sunt clarum genus Messii_. The Oscans gave to Messius his illustrious birth, a sufficient proof that he was an infamous scoundrel. The people who inhabited this part of Campania were guilty of execrable debaucheries.

Saltaret uti Cyclopa. The raillery is founded on his gigantic size, and the villainous gash that Messius had on his forehead, which made him look so like a Polyphemus, that he might dance the part without buskins or a mask. To dance a Cyclops, a Glaucus, a Ganymede, a Leda, was an expression for representing their story by dancing.

Donasset iamne catenam. Only the vilest slaves, or those who worked in the country, were chained. It appears by an epigram of Martial, that when they were set at liberty, they consecrated their chains to Saturn, because slavery was unknown under his reign. But when Messius asks Sarmentus whether he had dedicated his chain to the Dii Lares, he would reproach him with being a fugitive. These gods were invoked by travelers, because they presided over highways, from whence they were called viales. They themselves were always represented like travelers, as if they were ready to leave the house; succincti. Or Sarmentus was a slave so vile that he knew no other gods, but those who stood on the hearth, and which it was his employment to keep clean.

By the laws of the twelve tables, a slave was allowed a pound of corn a day. "Qui eum vinctum habebit, libras farris in dies dato."

Hence we proceed straight on for Beneventum; where the bustling landlord almost burned himself, in roasting some lean thrushes: for, the fire falling through the old kitchen [floor], the spreading flame made a great progress toward the highest part of the roof. Then you might have seen the hungry guests and frightened slaves snatching their supper out [of the flames], and every body endeavoring to extinguish the fire.

After this Apulia began to discover to me her well-known mountains, which the Atabulus scorches [with his blasts]: and through which we should never have crept, unless the neighboring village of Trivicus had received us, not without a smoke that brought tears into our eyes; occasioned by a hearth's burning some green boughs with the leaves upon them. Here, like a great fool as I was, I wait till midnight for a deceitful mistress: sleep, however, overcomes me, while meditating love; and disagreeable dreams make me ashamed of myself and every thing about me.

Hence we were bowled away in chaises twenty-four miles, intending to stop at a little town, which one can not name in a verse, but it is easily enough known by description.^[ This (as the Schol. informs us) was Equotuticum. The reason that it can not occur in dactylics is, that the first is short, and the next two syllables long, while the penultimate is short. Were the first long, thero could be no difficulty about introducing it. MCCAUL. ] For water is sold here, though the worst in the world; but their bread is exceeding fine, inasmuch that the weary traveler is used to carry it willingly on his shoulders; for [the bread] at Canusium is gritty; a pitcher of water is worth no more [than it is here]: which place was formerly built by the valiant Diomedes. Here Varius departs dejected from his weeping friends.

This (as the Schol. informs us) was Equotuticum. The reason that it can not occur in dactylics is, that the first is short, and the next two syllables long, while the penultimate is short. Were the first long, thero could be no difficulty about introducing it. MCCAUL.

Hence we came to Rabi, fatigued: because we made a long journey, and it was rendered still more troublesome by the rains. Next day the weather was better, the road worse, even to the very walls of Barium that abounds in fish. In the next place Egnatia, which [seems to have] been built on troubled waters, gave us occasion for jests and laughter; for they wanted to persuade us, that at this sacred portal the incense melted without fire. The Jew Apella may believe this, not I. For I have learned [from Epicurus], that the gods dwell in a state of tranquillity; nor, if nature effect any wonder, that the anxious gods send it from the high canopy of the heavens.

Brundusium ends both my long journey, and my paper.[^baff5834469c4f91bc9d079eb3919198]

  
## To Minturnae By Ship

Intending to travel by ship down the coast to Minturnae, Virgil left Formiae. It was about 18 miles away. 

The breezes woo the sails, and the canvas blows out to the swelling south.   
  
Driven from our course, we go wandering on the blind waves. The sails drop; they swing back to the oars.   
  
The harbor of Minturnae came into view over the horizon. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. 

While he visited his friend at Minturnae, he was pleased to discover _On the Agrarian Law_, by Cicero, Marcus Tullius. Picking it up, he read:

## A Story By Cicero, Marcus Tullius About Minturnae From _On The Agrarian Law_


I assure you with the most real sincerity, O Romans, that I applied myself to the reading and understanding of this law with these feelings, that if I had thought it well adapted to your interests, and advantageous to them, I would have been a chief mover in and promoter of it. For the consulship has not, either by nature, or by any inherent difference of object, or by any instinctive hatred, any enmity against the tribuneship, though good and fearless consuls have often opposed seditious and worthless tribunes of the people, and though the power of the tribunes has sometimes opposed the capricious licentiousness of the consuls. It is not the dissimilarity of their powers, but the disunion of their minds, that creates dissension between them.[^99afe678f22d4e83b05ab27cd64e6e7c]

  
## From Minturnae To Formiae

Leaving Minturnae, Virgil set out for Formiae by ship down the coast, at least 18 miles. 

They spread their sails and ran over the waste sea in their hollow wood. The wave shuddered and gloomed.   
  
A fair harbor lies on either side of the city and the entrance is narrow. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. 

While he was visiting Formiae, he made a point of copying down what Horace had written.

## On Formiae, According To Horace


Aelius, of Lamus' ancient name  
(For since from that high parentage  
The prehistoric Lamias came  
And all who fill the storied page,  
No doubt you trace your line from him,  
Who stretch'd his sway o'er Formiae,  
And Liris, whose still waters swim  
Whore green Marica skirts the sea,  
Lord of broad realms), an eastern gale  
Will blow to-morrow, and bestrew  
The shore with weeds, with leaves the vale,  
If rain's old prophet tell me true,  
The raven. Gather, while 'tis fine,  
Your wood; tomorrow shall be gay  
With smoking pig and streaming wine,  
And lord and slave keep holyday.  
[^f47d2ae39ebb42218adf3ff0981edae9]

\newpage

# Formiae To Ocriculum
  
## Travelling By Ship

From Formiae to Tarracina is at least 24 miles when travelling by ship down the coast. 

They spread their sails and ran over the waste sea in their hollow wood. A dusky shower drew up overhead carrying night and tempest.   
  
Driven from our course, we go wandering on the blind waves. They sweep through the green water.   
  
A fair harbor lies on either side of the city and the entrance is narrow. The people of Tarracina all have stations for their ships, each man one for himself. There, too, is their place of assembly about the fair temple of Poseidon, fitted with huge stones set deep in the earth. 

The library at Tarracina happened to have a copy of _Historiae_, where Virgil encountered it.

## The Story Of Tarracina


Meanwhile Lucius Vitellius, who was encamped near Feronia, was threatening Tarracina with destruction. There were shut up in the place a few gladiators and seamen, who dared not leave the walls and risk an engagement in the plain. I have mentioned before that Julianus was in command of the gladiators, Apollinaris of the seamen, two men whose profligacy and indolence made them resemble gladiators rather than generals. They kept no watch; they did not strengthen the weak points of the fortifications; but, making each pleasant spot ring with the noise of their daily and nightly dissipation, they dispersed their soldiers on errands which were to minister to their luxury, and never spoke of war, except at their banquets. Apinius Tiro had quitted the place a few days before, and was now, by the harsh exaction of presents and contributions from the towns, adding to the unpopularity rather than to the resources of his party.[^431993fc03c74a87aa9650a70e768943]

  
## To Forum Appii

From Tarracina to Forum Appii is at least 14 miles when travelling on a boat heading upstream. 

There was written there these words: [I]mp(eratore) T(ito) C(aesare) A(ugusto) VIII / Domitiano Cae(sare) VI co(n)s(ulibus). The sun beats down. The countryside is quieter than the city. 

  
## From Forum Appii To Tarracina

From Forum Appii to Tarracina is a journey of about 14 miles when travelling on a boat heading downstream. 

No backward glances for the city left behind. 

The library at Tarracina happened to have a copy of _Histories_, where Virgil encountered it.

## A Story About Tarracina By Polybius


After this treaty there was a second, in which we find that the Carthaginians have included the Tyrians and the township of Utica in addition to their former territory; and to the Fair Promontory Mastia and Tarseium are added, as the points east of which the Romans are not to make marauding expeditions or found a city. The treaty is as follows: "There shall be friendship between the Romans and their allies, and the Carthaginians, Tyrians, and township of Utica, on these terms: The Romans shall not maraud, nor traffic, nor found a city east of the Fair Promontory, Mastia, Tarseium. If the Carthaginians take any city in Latium which is not subject to Rome, they may keep the prisoners and the goods, but shall deliver up the town. If the Carthaginians take any folk, between whom and Rome a peace has been made in writing, though they be not subject to them, they shall not bring them into any harbours of the Romans; if such an one be so brought ashore, and any Roman lay claim to him,^[\rendergreek{ἐπιλάβηται} _injecerit manum,_ the legal form of claiming a slave.] he shall be released. In like manner shall the Romans be bound towards the Carthaginians.

"If a Roman take water or provisions from any district within the jurisdiction of Carthage, he shall not injure, while so doing, any between whom and Carthage there is peace and friendship. Neither shall a Carthaginian in like case. If any one shall do so, he shall not be punished by private vengeance, but such action shall be a public misdemeanour.

"In Sardinia and Libya no Roman shall traffic nor found a city; he shall do no more than take in provisions and refit his ship. If a storm drive him upon-those coasts, he shall depart within five days.

"In the Carthaginian province of Sicily and in Carthage he may transact business and sell whatsoever it is lawful for a citizen to do. In like manner also may a Carthaginian at Rome."

Once more in this treaty we may notice that the Carthaginians emphasise the fact of their entire possession of Libya and Sardinia, and prohibit any attempt of the Romans to land in them at all; and on the other hand, in the case of Sicily, they clearly distinguish their own province in it. So, too, the Romans, in regard to Latium, stipulate that the Carthaginians shall do no wrong to Ardea, Antium, Circeii, Tarracina, all of which are on the seaboard of Latium, to which alone the treaty refers.[^2c3f72703e6c403a847d63cfd90c75e6]

  
## 14 Miles To Forum Appii

Virgil departed from Tarracina, intending to travel on a boat heading upstream to Forum Appii, a journey of about 14 miles. 

A breeze from an unexpected quarter cools the air. 

  
## After Forum Appii

Leaving Forum Appii, Virgil set out for Roma by road, a journey of about 42 miles. 

On the road from Forum Appii to Roma there is a village, in which there is a temple and grove. He had set out from Forum Appii amidst a throng travelling the same way. A cloud passes in front of the sun. He left the city early, before the rising of the sun. By the road is a salt spring. Workers are raising the level of the road. 

While he was visiting Roma, he made a point of copying down what Horace had written.

## A Story About Roma By Horace


Of battles fought I fain had told,  
And conquer'd towns, when Phoebus smote  
His harp-string: "Sooth, 'twere over-bold.  
To tempt wide seas in that frail boat."  
Thy age, great Caesar, has restored  
To squalid fields the plenteous grain,  
Given back to Rome's almighty Lord  
Our standards, torn from Parthian fane,  
Has closed Quirinian Janus' gate,  
Wild passion's erring walk controll'd,  
Heal'd the foul plague-spot of the state,  
And brought again the life of old,  
Life, by whose healthful power increased  
The glorious name of Latium spread  
To where the sun illumes the east  
From where he seeks his western bed.  
While Caesar rules, no civil strife  
Shall break our rest, nor violence rude,  
Nor rage, that whets the slaughtering knife  
And plunges wretched towns in feud.  
The sons of Danube shall not scorn  
The Julian edicts; no, nor they  
By Tanais' distant river horn,  
Nor Persia, Scythia, or Cathay.  
And we on feast and working-tide,  
While Bacchus' bounties freely flow,  
Our wives and children at our side,  
First paying Heaven the prayers we owe,  
Shall sing of chiefs whose deeds are done,  
As wont our sires, to flute or shell,  
And Troy, Anchises, and the son  
Of Venus on our tongues shall dwell.  
[^2ee18131884e46abb67b71b4500714f1]

  
## Roma To Ocriculum By River, Upstream

Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, at least 64 miles. 

A breeze from an unexpected quarter cools the air. No backward glances for the city left behind. Birds sing their greetings. 

While he was visiting Tibur, he made a point of copying down what John Conington had written.

## On The Subject Of Tibur


"Two brothers, Catillus and Coras, come from Tibur."[^59ae4583f7ac48c0ad7169bdb776b074]

  
## From Ocriculum To Narnia

Virgil departed from Ocriculum, intending to travel by road to Narnia, a journey of about 8 miles. 

Next to the straight road that leads to Narnia, there is visible a sculpted tomb. He left the city early, before the rising of the sun. There a spring wells up, and around about it is a meadow. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Above the roads are ruins, among which is a cave sacred to Asclepius. There is a fountain of cold water springing from the rock. A grove of Minerva is hard by the road, a grove of poplar trees. 

The library at Narnia happened to have a copy of _Historiae_, where Virgil encountered it.

## The Story Of Narnia


Vitellius, when informed of these events, left a portion of his army at Narnia under the command of the prefect of the Prætorian Guard, and deputed his brother Lucius with six cohorts of infantry and 500 cavalry to encounter the danger that now threatened him on the side of Campania. Sick at heart, he found relief in the zeal of the soldiers and in the shouts with which the people clamoured for arms, while he gave the delusive name of an army and of Roman legions to a cowardly mob, that would not venture on any thing beyond words. At the instance of his freedmen (for his friends were the less faithful the more distinguished their rank) he ordered the tribes to be convoked, and to those who gave in their names administered the oath of service. As the numbers were excessive, he divided the business of enrolment between the consuls. He required the Senators to furnish a prescribed number of slaves and a certain weight of silver. The Roman Knights offered their services and money, and even the freedmen voluntarily sought the privilege of doing the same. This pretence of loyalty, dictated at first by fear, passed into enthusiasm, and many expressed compassion, not so much for Vitellius, as for the fallen condition of the Imperial power. Vitellius himself failed not to draw out their sympathies by his pitiable looks, his voice, and his tears; he was liberal in his promises and even extravagant, as men in their alarm naturally are. He even expressed a wish to be saluted as Cæsar, a title which he had formerly rejected. But now he had a superstitious feeling about the name; and it is a fact that in the moment of terror the counsels of the wise and the voice of the rabble are listened to with equal respect. But as all movements that originate in thoughtless impulse, however vigorous in their beginnings, become feeble after a time, the throng of Senators and Knights gradually melted away, dispersing at first tardily and during the absence of the Emperor, but before long with a contemptuous indifference to his presence, till, ashamed of the failure of his efforts, Vitellius waived his claims to services which were not offered.[^db3ebbb2bbb549f9aab373b883346d54]

  
## Leaving Narnia By Road

Intending to travel by road to Ocriculum, Virgil left Narnia. It was at least 8 miles. 

As they go up from Narnia, they see the ruined walls. There a spring wells up, and around about it is a meadow. He passes another milestone. He left the city early, before the rising of the sun. A caravan from Ocriculum passed by. His shoes are covered in dust from the road. There is a fountain of cold water springing from the rock. He had set out from Narnia amidst a throng travelling the same way. 

He would later record what Cicero, Marcus Tullius had said about the countryside near that place.

## A Story By Cicero, Marcus Tullius About The Countryside Near That Place From _On The Agrarian Law_


But remark how carefully he preserves the rights of the tribunitian power. The consuls are often interrupted in proposing a _lex curiata_, by the intercession of the tribunes of the people. Not that we complain that the tribunes should have this power; only, if any one uses it in a random and inconsiderate manner, we form our own opinion. But this tribune of the people, by his _lex curiata_, which the praetor is to bring forward, takes away the power of intercession. And while he is made to be blamed for causing the tribunitian power to be diminished by his instrumentality, he is also to be laughed at, because a consul, if he be not invested with the authority by a _lex curiata_, has no power to interfere in military affairs; and yet he gives this man whom he prohibits from interceding, the very same power, even if the veto be interposed, as if a _lex curiata_ had been passed. So that I am at a loss to understand either why he prohibits the intercession, or why he thinks that any one will intercede; as the intercession will only prove the folly of the intercessor, and will not hinder the business.[^2f6d12b0dad9459d9eafb75408b11b8f]

\newpage

# Ocriculum To Placentia
  
## Travelling By Road

Virgil departed from Ocriculum, intending to travel by road to Narnia, a journey of about 8 miles. 

Virgil saw this on a roadside tomb: [C(aius) Iu]lius Rammius Eutychus / [se]vir Aug(ustalis) fecit sibi et / [C(aio) Iu]lio Rammio Hi[l]aro / patrono b(ene) m(erenti) et / Iuliae Euvenniae(!) lib(ertae) [b(ene)] m(erenti) coniugi / et Iuliae C(ai) f(iliae) In[genuae e]t Iuliae / C(ai) f(iliae) Felicitati et Iu[liae - - -]leni lib(ertae) et / libert(is) libertabus p[osteri]sq(ue) eorum / in fro(nte) p(edes) XV in agro p(edes) XXX h(oc) m(onumentum) h(eredem) f(amiliae) e(xterae) n(on) s(equetur). Above the roads are ruins, among which is a cave sacred to Asclepius. A grove of Minerva is hard by the road, a grove of poplar trees. Next to the straight road that leads to Narnia, there is visible a sculpted tomb. Along the road are graves, and a cenotaph. He left the city early, before the rising of the sun. 

While he was visiting Narnia, he made a point of copying down what Cornelius Tacitus had written.

## A Story By Cornelius Tacitus About Narnia From _Historiae_


Antonius marched by the Via Flaminia, and arrived at Saxa Rubra, when the night was far spent, too late to give any help. There he received nothing but gloomy intelligence, that Sabinus was dead, that the Capitol had been burnt to the ground, that Rome was in consternation, and also that the populace and the slaves were arming themselves for Vitellius. And Petilius Cerialis had been defeated in a cavalry skirmish. While he was hurrying on without caution, as against a vanquished enemy, the Vitellianists, who had disposed some infantry among their cavalry, met him. The conflict took place not far from the city among buildings, gardens, and winding lanes, which were well known to the Vitellianists, but disconcerting to their opponents, to whom they were strange. Nor indeed were all the cavalry one in heart, for there were with them some who had lately capitulated at Narnia, and who were anxiously watching the fortunes of the rival parties. Tullius Flavianus, commanding a squadron, was taken prisoner; the rest fled in disgraceful confusion, but the victors did not continue the pursuit beyond Fidenæ.[^9db735a74d2549dd8c176b2655cf5281]

  
## Departing From Narnia

Intending to travel by road to Spoletium, Virgil left Narnia. It was about 22 miles away. 

This is a smooth road, by which many wagons were bringing wood to Spoletium. He had set out from Narnia amidst a throng travelling the same way. The road narrows here, an orchard wall encroaching on it. $] aid(ilis) lust(ralis) / ISIIS RVI(?) / [&: he pondered the sight of this inscription. On the road from Narnia to Spoletium there is a village, in which there is a temple and grove. The sun beats down. He left the city early, before the rising of the sun. A caravan from Spoletium passed by. A cloud passes in front of the sun. 

He would later record what Titus Livius (Livy) had said about the countryside near that place.

## On The Countryside Near That Place, According To Titus Livius (Livy)


By the unanimous vote of the states, the conduct of the war was entrusted to Attius Tullius and Cn. Marcius, the Roman exile, on whom their hopes chiefly rested. He fully justified their expectations, so that it became quite evident that the strength of Rome lay in her generals rather than in her army.

He first marched against Cerceii, expelled the Roman colony and handed it over to the Volscians as a free city. Then he took: Satricum, Longula, Polusca, and Corioli, towns which the Romans had recently acquired. Marching across country into the Latin road, he recovered Lavinium, and then, in succession, Corbio, Vetellia, Trebium Labici, and Pedum. Finally, he advanced from Pedum against the City. He entrenched his camp at the Cluilian Dykes, about five miles distant, and from there he ravaged the Roman territory. The raiding parties were accompanied by men whose business it was to see that the lands of the patricians were not touched; a measure due either to his rage being especially directed against the plebeians, or to his hope that dissensions might arise between them and the patricians. These certainly would have arisen —to such a pitch were the tribunes exciting the plebs by their attacks on the chief men of the State —had not the fear of the enemy outside —the strongest bond of union —brought men together in spite of their mutual suspicions and aversion. On one point they disagreed; the senate and the consuls placed their hopes solely in arms, the plebeians preferred anything to war.

Sp. Nautius and Sex. Furius were now consul. Whilst they were reviewing the legions and manning the walls and stationing troops in various places, an enormous crowd gathered together. At first they alarmed the consuls by seditious shouts, and at last they compelled them to convene the senate and submit a motion for sending ambassadors to Cn. Marcius. As the courage of the plebeians was evidently giving way, the senate accepted the motion, and a deputation was sent to Marcius with proposals for peace. They brought back the stern reply: If the territory were restored to the Volscians, the question of peace could be discussed; but if they wished to enjoy the spoils of war at their ease, he had not forgotten the wrongs inflicted by his country-men nor the kindness shown by those who were now his hosts, and would strive to make it clear that his spirit had been roused, not broken, by his exile. The same envoys were sent on a second mission, but were not admitted into the camp. According to the tradition, the priests also in their robes went as suppliants to the enemies' camp, but they had no more influence with him than the previous deputation.[^27018263a3964e74a99f6952d33a2bd2]

  
## Departing From Spoletium

From Spoletium to Fanum Fortunae is a distance of about 90 miles when travelling by road. 

There is a fountain of cold water springing from the rock. There a spring wells up, and around about it is a meadow. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. They pass a pillar on the right surmounted by a stone urn. He left the city early, before the rising of the sun. A caravan from Fanum Fortunae passed by. 

All of this brought to his mind what Vitruvius Pollio had said about Fanum Fortunae:

## On The Subject Of Fanum Fortunae


1\. THE Greeks lay out their forums in the form of a square surrounded by very spacious double colonnades, adorn them with columns set rather closely together, and with entablatures of stone or marble, and construct walks above in the upper story. But in the cities of Italy the same method cannot be followed, for the reason that it is a custom handed down from our ancestors that gladiatorial shows should be given in the forum.

2\. Therefore let the intercolumniations round the show place be pretty wide; round about in the colonnades put the bankers' offices; and have balconies on the upper floor properly arranged so as to be convenient, and to bring in some public revenue.

The size of a forum should be proportionate to the number of inhabitants, so that it may not be too small a space to be useful, nor look like a desert waste for lack of population. To determine its breadth, divide its length into three parts and assign two of them to the breadth. Its shape will then be oblong, and its ground plan conveniently suited to the conditions of shows.

3\. The columns of the upper tier should be one fourth smaller than those of the lower, because, for the purpose of bearing the load, what is below ought to be stronger than what is above, and also, because we ought to imitate nature as seen in the case of things growing; for example, in round smooth-stemmed trees, like the fir, cypress, and pine, every one of which is rather thick just above the roots and then, as it goes on increasing in height, tapers off naturally and symmetrically in growing up to the top. Hence, if nature requires this in things growing, it is the right arrangement that what is above should be less in height and thickness than what is below.

4\. Basilicas should be constructed on a site adjoining the forum and in the warmest possible quarter, so that in winter business men may gather in them without being troubled by the weather. In breadth they should be not less than one third nor more than one half of their length, unless the site is naturally such as to prevent this and to oblige an alteration in these proportions. If the length of the site is greater than necessary, Chalcidian porches may be constructed at the ends, as in the Julia Aquiliana.

5\. It is thought that the columns of basilicas ought to be as high as the side-aisles are broad; an aisle should be limited to one third of the breadth which the open space in the middle is to have. Let the columns of the upper tier be smaller than those of the lower, as written above. The screen, to be placed between the upper and the lower tiers of columns, ought to be, it is thought, one fourth lower than the columns of the upper tier, so that people walking in the upper story of the basilica may not be seen by the business men. The architraves, friezes, and cornices should be adjusted to the proportions of the columns, as we have stated in the third book.

6\. But basilicas of the greatest dignity and beauty may also be constructed in the style of that one which I erected, and the building of which I superintended at Fano. Its proportions and symmetrical relations were established as follows. In the middle, the main roof between the columns is 120 feet long and sixty feet wide. Its aisle round the space beneath the main roof and between the walls and the columns is twenty feet broad. The columns, of unbroken height, measuring with their capitals fifty feet, and being each five feet thick, have behind them pilasters, twenty feet high, two and one half feet broad, and one and one half feet thick, which support the beams on which is carried the upper flooring of the aisles. Above them are other pilasters, eighteen feet high, two feet broad, and a foot thick, which carry the beams supporting the principal raftering and the roof of the aisles, which is brought down lower than the main roof.

7\. The spaces remaining between the beams supported by the pilasters and the columns, are left for windows between the intercolumniations. The columns are: on the breadth of the main roof at each end, four, including the corner columns at right and left; on the long side which is next to the forum, eight, including the same corner columns; on the other side, six, including the corner columns. This is because the two middle columns on that side are omitted, in order not to obstruct the view of the pronaos of the temple of Augustus (which is built at the middle of the side wall of the basilica, facing the middle of the forum and the temple of Jupiter) and also the tribunal which is in the former temple, shaped as a hemicycle whose curvature is less than a semicircle.

8\. The open side of this hemicycle is forty-six feet along the front, and its curvature inwards is fifteen feet, so that those who are standing before the magistrates may not be in the way of the business men in the basilica. Round about, above the columns, are placed the architraves, consisting of three two-foot timbers fastened together. These return from the columns which stand third on the inner side to the antae which project from the pronaos, and which touch the edges of the hemicycle at right and left.

9\. Above the architraves and regularly dispersed on supports directly over the capitals, piers are placed, three feet high and four feet broad each way. Above them is placed the projecting cornice round about, made of two two-foot timbers. The tiebeams and struts, being placed above them, and directly over the shafts of the columns and the antae and walls of the pronaos, hold up one gable roof along the entire basilica, and another from the middle of it, over the pronaos of the temple.

10\. Thus the gable tops run in two directions, like the letter T, and give a beautiful effect to the outside and inside of the main roof. Further, by the omission of an ornamental entablature and of a line of screens and a second tier of columns, troublesome labour is saved and the total cost greatly diminished. On the other hand, the carrying of the columns themselves in unbroken height directly up to the beams that support the main roof, seems to add an air of sumptuousness and dignity to the work.[^95f2851bdf30454880fb872c6007a6e7]

  
## Departing From Fanum Fortunae

Leaving Fanum Fortunae, Virgil set out for Ariminum by ship down the coast, a journey of about 38 miles. 

Stormclouds enwrap the day, and rainy gloom blots out the sky. Out of the clouds bursts fire fast upon fire. Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. The oars are snapped. The prow swings away and gives her side to the waves. Rocks amid the waves, a vast reef banking the sea. The helmsman is dashed away and rolled forward headlong.   
  
They sweep through the green water.   
  
In a far retreat there lies a haven. Towards the deep doth stand an island, on whose jutting headlands beat the broken billows, shivered into sleet. Beneath a precipice that fronts the wave, with limpid springs inside, and many a seat of living marble, lies a sheltered cave. Ships within this happy harbor meet, the thin remainders of the scattered fleet. They lay their weary limbs still dripping on the sand. 

While he was visiting Ariminum, he made a point of copying down what Cicero, Marcus Tullius had written.

## A Story About Ariminum


Since you make this statement, and lay down this principle, "that, if Caecina, when he was actually in his farm, had been driven from it, then it would have been right for him to be restored by means of this interdict; but now he can by no means be said to have been from a place where he has not been; and, therefore, we have gained nothing by this interdict;" I ask you, if, this day, when you are returning home, men collected in a body, and armed, not only prevent you from crossing the threshold and from coming under the roof of your own house, but keep you off from approaching it— from even entering the court yard,—what will you do? My friend Lucius Calpurnius reminds you to say the same thing that he said before, namely that you would bring an action for the injury. But what has this to do with possession? What has this to do with restoring a man who ought to be restored? or with the civil law? I will grant you even more. I will allow you not only to bring your action, but also to succeed in it. Will you be any the more in possession of your property for that? For an action for injury done does not carry with it, even if successful, any right of possession; but merely makes up to a man for the loss he sustains through the diminution of his liberty, by the trial and penalty imposed upon the offender.[^8edd19034673482b9e3a0bde03101a47]

  
## From Ariminum To Faventia

Leaving Ariminum, Virgil set out for Faventia by road, about 38 miles away. 

He passes another milestone. There a spring wells up, and around about it is a meadow. He left the city early, before the rising of the sun. A caravan from Faventia passed by. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Now the road is quieter. As they go up from Ariminum, they see the ruined walls. Water has washed out the road, making for slow going. The sun beats down. 

All of this brought to his mind what Lucan, 39-65 had said about the countryside near that place:

## A Story About The Countryside Near That Place By Lucan, 39-65


  
For Nero's coming, nor the gods with ease  
Gain thrones in heaven; and if the Thunderer  
Prevailed not till the giants' war was done,  
We plain no more, ye gods! for such a boon  
All wickedness be welcome and all crime;  
Thronged with our dead be dire Pharsalia's fields,  
Be Punic ghosts avenged by Roman blood;  
Add, Caesar, to these ills the Mutin toils;  
Perusia's dearth; on Munda's final field  
The shock of battle joined; let Leucas' Cape  
Shatter the routed navies; servile hands  
Unsheath the sword on fiery Etna's slopes:  
Still Rome is gainer by the civil war.  
Thou, Caesar, art her prize. When thou shalt choose,  
Thy watch relieved, to seek at length the stars,  
All heaven rejoicing; and shalt hold a throne,  
Or else elect to govern Phoebus' car  
And light a subject world that shall not dread  
To owe her brightness to a different Sun;  
All shall concede thy right: do what thou wilt,  
Select thy Godhead, and the central clime  
Whence thou shalt rule the world with power divine.  
And yet the Northern or the Southern Pole  
We pray thee, choose not; but in rays direct  
Vouchsafe thy radiance to thy city Rome.  
Press thou on either side, the universe  
Should lose its equipoise: take thou the midst,  
And weight the scales, and let that part of heaven  
Where Caesar sits be evermore serene  
And smile upon us with unclouded blue.  
Then may all men lay down their arms, and peace  
Through all the nations reign, and shut the gates  
That close the temple of the God of War.  
Be thou my help, to me e'en now divine!  
Let Delphi's steep her own Apollo guard,  
And Nysa keep her Bacchus, uninvoked.  
Rome is my subject and my muse art thou!  
First of such deeds I purpose to unfold  
The causes task immense what drove to arms  
A maddened nation and from all the world  
Struck peace away.  
By envious fate's decrees  
Abide not long the mightiest lords of earth;  
Too great the burden, great shall be the fall.  
Thus Rome o'ergrew her strength. So when that hour,  
The last in all the centuries, shall sound  
The world's disruption, all things shall revert  
To that primaeval chaos, stars on stars  
Shall crash; and fiery meteors from the sky  
Plunge in the ocean. Earth shall then no more  
Front with her bulwark the encroaching sea:  
The moon, indignant at her path oblique,  
Shall drive her chariot 'gainst her brother Sun  
And claim the day for hers; and discord huge  
Shall rend the spheres asunder. On themselves  
The great are dashed: such end the gods have set  
To height of power: nor ever Fortune shares  
With other lands the weapons of her spite  
Against a nation lord of land and sea.  
Thou, Rome, degraded, sold, the common prey  
Of triple despots, of a tyrant rule  
Partnered as ne'er before-thyself art cause  
Of all the ills. Ye chiefs, with greed of power  
Blind, leagued for evil, is your force conjoined  
To hold the world in common as your prize?  
So long as Sea on Earth and Earth on Air  
Lean for support while Titan runs his course,  
And night with day divides an equal sphere,  
No king shall brook his fellow, nor shall rule  
Endure a rival. Search no foreign lands:  
These walls are proof that in their infant days  
A hamlet, not the world, was prize enough  
To cause the shedding of a brothers blood.  
Concord, on discord based, brief time endured,  
Unwelcome to the rivals; and alone  
Crassus delayed the advent of the war.  
Like to the slender neck that separates  
The seas of Graecia: should it be engulfed  
Then would th' Ionian and Aegean mains  
Break each on other^[See a similar passage in the final scene of Ben Jonson's ' Catiline.' The cutting of the Isthmus of Corinth was proposed in Nero's reign, and actually commenced in his presence; but abandoned because it was asserted that the level of the water in the Corinthian Gulf was higher than that in the Saronic Gulf, so that, if the canal were cut, the island of AEgina would be submerged. Merivale's 'Roman Empire,' chapter lv.]: thus when Crassus fell,  
Who held apart the chiefs, in piteous death,  
And stained Assyria's plains with Latian blood,  
Defeat in Parthia loosed the war in Rome.  
More in that victory than ye thought was won,  
Ye sons of Arsaces; your conquered foes  
Took at your hands the rage of civil strife.  
By sword the realm is parted; and the state  
Supreme o'er earth and sea, wide as the world,  
Could not find space for two.^[Compare: 'Two stars keep not their motion in one sphere Nor can one England brook a double reign Of Harry Percy and the Prince of Wales.'] For Julia bore,  
'Two stars keep not their motion in one sphere  
Nor can one England brook a double reign  
Of Harry Percy and the Prince of Wales.'  
Cut off by fate unpitying,^[This had taken place in B.C. 54, about five years before the action of the poem opens.] the bond  
Of that ill-omened marriage and the pledge  
Of blood united, to the shades below.  
Hadst thou but longer stayed, it had been thine  
To keep the parent and the spouse apart,  
Strike sword from grasp and join the threatening hands;  
As Sabine matrons in the days of old  
Joined in the midst the bridegroom and the sire.  
With thee all trust was buried, and the chiefs  
Could give their courage vent, and rushed to war.  
Lest newer glories triumphs past obscure,  
Late conquered Gaul the bays from pirates won,  
This, Magnus, is thy fear; thy roll of fame,  
Of glorious deeds accomplished for the state  
Allows no equal; nor will Caesar's pride  
A prior rival in his triumphs brook;  
Which had the right 'twere impious to enquire;  
Each for his cause can vouch a judge supreme;  
The victor, heaven: the vanquished, Cato, thee.^[This famous line was quoted by Lamartine when addressing the French Assembly in 1848. He was advocating, against the interests of his own party (which in the Assembly was all-powerful), that the President of the Republic should be chosen by the nation, and not by the Assembly; and he ended by saying that if the course he advocated was disastrous to himself, 'Victrix causa Diis placuit, sed victa Catoni.']  
Nor were they like to like: the one in years  
Now verging towards decay, in times of peace  
Had unlearned war; but thirsting for applause  
Gave to the people much, and proud of fame  
His former glory cared not to renew,  
But joyed in plaudits of the theatre,^['Plausuque sui gaudere theatri.' Quoted by Mr. Pitt, in his speech on the address in 1783, on the occasion of peace being made with France, Spain, and America; in allusion to Mr. Sheridan. The latter replied, 'If ever I again engage in the compositions he alludes to, I may be tempted to an act of presumption-to attempt an improvement on one of Ben Jonson's best characters-the character of the Angry Boy in the "Alchymist."']  
His gift to Rome: his triumphs in the past,  
Himself the shadow of a mighty name.  
As when some oak, in fruitful field sublime,^[Mr. Canning, in his speech on the vote for the Windsor Establishment, said of King George III., 'Scathed by Heaven's lightning, but consecrated as much as blasted by the blow, he yet exhibited to the awe and veneration of mankind a mighty monument of strength and majesty in decay. He stood like the oak of the poet stripped of that luxuriant foliage and spreading those denuded arms which had afforded shelter to successive generations: et trunco non frondibus efficit umbram.']  
Adorned with venerable spoils, and gifts  
Of bygone leaders, by its weight to earth  
With feeble roots still clings; its naked arms  
And hollow trunk, though leafless, give a shade;  
And though condemned beneath the tempest's shock  
To speedy fall, amid the sturdier trees  
In sacred grandeur rules the forest still.  
No such repute had Caesar won, nor fame;  
But energy was his that could not rest-  
The only shame he knew was not to win.  
Keen and unvanquished,^[Cicero wrote thus of Caesar: 'Have you ever read or heard of a man more vigorous in action or more moderate in the use of victory than our Caesar' - Epp. ad Diversos, viii. 15.] where revenge or hope  
Might call, resistless would he strike the blow  
With sword unpitying: every victory won  
Reaped to the full; the favour of the gods  
Pressed to the utmost; all that stayed his course  
Aimed at the summit of power, was thrust aside:  
Triumph his joy, though ruin marked his track.  
As parts the clouds a bolt by winds compelled,  
With crack of riven air and crash of worlds,  
And veils the light of day, and on mankind,  
Blasting their vision with its flames oblique,  
Sheds deadly fright; then turning to its home,  
Nought but the air opposing, through its path  
Spreads havoc, and collects its scattered fires.  
[^554de7e5295a466ba0f0373398ef0a84]

  
## Leaving Faventia By Road

From Faventia to Bononia is a journey of about 30 miles when travelling by road. 

He had set out from Faventia amidst a throng travelling the same way. Workers are raising the level of the road. By the road is a salt spring. They pass a pillar on the right surmounted by a stone urn. Water has washed out the road, making for slow going. A grove of Minerva is hard by the road, a grove of poplar trees. Next to the straight road that leads to Bononia, there is visible a sculpted tomb. 

He would later record what Catullus, Gaius Valerius had said about Bononia.

## The Story Of Bononia


Rufa of Bononia blows Rufulus, she the wife of Menenius. Often you have seen her among the tombs, snatching her meal from the funeral pyre. When she chases after the bread which has rolled from the fire, she is buffeted by the half-shaven cremator.[^c931b563038f46bda97774cbb3fd5670]

  
## Travelling By River

Leaving Bononia, Virgil set out for a village on a military boat floating downstream, a distance of about 39 miles. 

The journey is more tiring than you might expect. They passed by an inscription that read: Caeselliae [- -] / Gazzae / Q(uintus) Sulfius Apella / vir fecit. 

  
## To Placentia By River, Upstream

Leaving a village, Virgil set out for Placentia on a military boat headed upstream, a distance of about 140 miles. 

The sun beats down. Birds sing their greetings. 

He would later record what Polybius had said about Placentia.

## An Account Of Placentia


But the Celtic contingent of the Roman army, seeing that Hannibal's prospects looked the brighter of the two, concerted their plans for a fixed time, and waited in their several tents for the moment of carrying them out. When the men within the rampart of the camp had taken their supper and were gone to bed, the Celts let more than half the night pass, and just about the time of the morning watch armed themselves and fell upon the Romans who were quartered nearest to them; killed a considerable number, and wounded not a few; and, finally, cutting off the heads of the slain, departed with them to join the Carthaginians, to the number of two thousand infantry and nearly two hundred cavalry. They were received with great satisfaction by Hannibal; who, after addressing them encouragingly, and promising them all suitable rewards, sent them to their several cities, to declare to their compatriots what they had done, and to urge them to make alliance with him: for he knew that they would now all feel compelled to take part with him, when they learnt the treachery of which their fellow-countrymen had been guilty to the Romans. Just at the same time the Boii came in, and handed over to him the three Agrarian Commissioners, sent from Rome to divide the lands; whom, as I have already related, they had seized by a sudden act of treachery at the beginning of the war. Hannibal gratefully acknowledged their good intention, and made a formal alliance with those who came: but he handed them back their prisoners, bidding them keep them safe, in order to get back their own hostages from Rome, as they intended at first.

Publius regarded this treachery as of most serious importance; and feeling sure that the Celts in the neighbourhood had long been ill-disposed, and would, after this event, all incline to the Carthaginians, he made up his mind that some precaution for the future was necessary. The next night, therefore, just before the morning watch, he broke up his camp and marched for the river Trebia, and the high ground near it, feeling confidence in the protection which the strength of the position and the neighbourhood of his allies would give him.[^cc4a81cf5b174bac9357f7ff26d9f32e]

\newpage

# Placentia To Altinum
  
## Departing From Placentia

Intending to travel by road to a village, Virgil left Placentia. It was a journey of about 11 miles. 

There is a fountain of cold water springing from the rock. Now the road is quieter. Next to the straight road that leads to a village, there is visible a sculpted tomb. By the road is a salt spring. His shoes are covered in dust from the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A caravan from a village passed by. 

  
## Travelling By Road To Mediolanum

Leaving a village, Virgil set out for Mediolanum by road, at least 27 miles. 

On the road from a village to Mediolanum there is a village, in which there is a temple and grove. Virgil saw this on a roadside tomb: Lucius Pinxit. An oxcart passes, loaded with grain. This is a smooth road, by which many wagons were bringing wood to Mediolanum. The sun beats down. Workers are raising the level of the road. Along the road are graves, and a cenotaph. 

While he was visiting Mediolanum, he made a point of copying down what Cornelius Tacitus had written.

## A Story By Cornelius Tacitus About Mediolanum From _Historiae_


Cæcina while halting for a few days in the Helvetian territory, till he could learn the decision of Vitellius, and at the same time making preparations for the passage of the Alps, received from Italy the good news, that Silius' Horse, which was quartered in the neighbourhood of Padus, had sworn allegiance to Vitellius. They had served under him when he was Proconsul in Africa, from which place Nero had soon afterwards brought them, intending to send them on before himself into Egypt, but had recalled them in consequence of the rebellion of Vindex. They were still in Italy, and now at the instigation of their decurions, who knew nothing of Otho, but were bound to Vitellius, and who magnified the strength of the advancing legions and the fame of the German army, they joined the Vitellianists, and by way of a present to their new Prince they secured for him the strongest towns of the country north of the Padus, Mediolanum, Novaria, Eporedia, and Vercellæ. This Cæcina had learnt from themselves. Aware that the widest part of Italy could not be held by such a force as a single squadron of cavalry, he sent on in advance the auxiliary infantry from Gaul, Lusitania, and Rhætia, with the veteran troops from Germany, and Petra's Horse, while he made a brief halt to consider whether he should pass over the Rhætian range into Noricum, to attack Petronius, the procurator, who had collected some auxiliaries, and broken down the bridges over the rivers, and was thought to be faithful to Otho. Fearing however that he might lose the infantry and cavalry which he had sent on in advance, and at the same time reflecting that more honour was to be gained by holding possession of Italy, and that, wherever the decisive conflict might take place, Noricum would be included among the other prizes of victory, he marched the reserves and the heavy infantry through the Penine passes while the Alps were still covered with the snows of winter.[^dc31ad3fdf1249e0bbc7c0c27178b805]

  
## From Mediolanum To Verona

Virgil departed from Mediolanum, intending to travel by road to Verona, a journey of about 101 miles. 

He passes another milestone. There a spring wells up, and around about it is a meadow. The sun beats down. Now the road is quieter. A grove of Minerva is hard by the road, a grove of poplar trees. He left the city early, before the rising of the sun. An oxcart passes, loaded with grain. The road narrows here, an orchard wall encroaching on it. Along the road are graves, and a cenotaph. 

All of this brought to his mind what E. T. Merrill had said about Verona:

## A Story By E. T. Merrill About Verona From _Commentary On Catullus_


37\. But even Sirmio could not long detain him from his loved Rome. His reappearance among his old friends is marked by a single poem (c. 10), whose gay and charming humor shows that even the vicinity of Lesbia had lost its power constantly to embitter his thoughts. And to the passion for Lesbia now appears to have succeeded that for a boy, Juventius, with the charms of whose company Catullus perhaps attempted to drive out the thoughts of his former love. How the intimacy began we cannot tell. The Juventian _gens_ sprang from Tusculum, but inscriptions (C. I. L. vol. V. passim) show that people of that name also lived in the neighborhood of Verona. It may be, therefore, that the boy came to Rome under the guardianship of Catullus, as perhaps Catullus, years before, under that of Nepos But nothing further is known of him beyond what may be inferred from the poems of Catullus that concern him (cf. introductory note to c. 15). His history is interwoven with that of a pair of friends, Aurelius and Furius, both at first friends of Catullus, to the former of whom the poet at one time was led to entrust temporarily the care of his ward (c. 15). The result might have been anticipated. Juventius learned to prefer them to Catullus, and in consequence Catullus vented his wrath upon them in a group of bitter poems (cc. 16, 21, 23, 26), though for Juventius he had only sorrowful remonstrance (cc. 24, 81).

38\. Yet all this experience appears to have touched him in no wise deeply. It was but a passing diversion, and his jealousy not the bitter passion felt against his rivals with Lesbia. With far more earnestness did he throw himself into the political quarrel of his time. The year of his return from Bithynia (56 B.C.) had witnessed the so-called renewal of the triumvirate at Luca, and Caesar appeared to have won everything. In accordance with the agreement made at the Luca conference, Pompey and Crassus were consuls a second time for the year 55, and the senatorial party was at its wits' end. Catullus was apparently not an active political worker, but he did not hesitate to join his political friends in personal attacks upon the foe. Perhaps his earlier shafts were those aimed against Mamurra (cf. § 73), Caesar's notorious favorite (cc. 29, 41, 43, 57), whom Catullus sometimes celebrates under the nickname of Mentula (cc. 94, 105, 114, 115), and these opened the way for the direct attack upon Caesar himself (cc. 54, 93). But whatever the order of attack, that Caesar was piqued by it we know from Suetonius (Iul. 73). That he made a successful effort to win over Catullus, as he did Calvus, we are also assured from the same source. Caesar understood better than most Romans that political power in that city and that day must rest largely upon personal popularity, and he was not above exerting himself to win the good will of individuals of high or low degree. And aside from the fascination due to his great political and military success, he had personal traits that gave him a power over young men. It was the mysterious influence of a natural leader of men; and in many more than these two instances the number of his friends was recruited from the ranks of the younger of his fiercest foes. There was another element also that must have tended to promote the reconciliation between Caesar and Catullus. The father of Catullus was resident at Verona within the limits of Caesar's Cisalpine province. He may not have taken an active part in politics, but at any rate he was a personal friend of Caesar, and often his host (Suet. l.c.). This intimacy may well have led him to see clearly what the result of the approaching struggle for supremacy in Rome was likely to be, and to desire the more eagerly to see his son arrayed for Caesar and not against him.

39\. At all events, the reconciliation was brought about, and the lively pen of Catullus ceased to lampoon the great commander. Some have thought, however, that Mamurra was not included in the peace, and that the utmost Caesar could effect in his favorite's behalf was that his personality should be thereafter thinly veiled under the pseudonym Mentula.

40\. But Caesar was not to profit greatly from his new ally. Up to the end of the year 55 B.C. Catullus displays only hostility to Caesar and the Caesarians. The reconciliation apparently took place at the house of the father of Catullus at Verona during the winter visit of the governor to the nearer province in the early part of the year 54 (Caes. B. G. 5.1). The only poem that shows the change of feeling toward Caesar is c. 11, and this is connected with another marked incident in the life of the poet.

41\. Catullus was now the friend of Caesar. The great commander was entertained at his father's house, and perhaps even there was making his plans for future campaigns. The fortunes of the poet were rising. What might he not hope for from his great patron, and why should others not share in his success? Furius and Aurelius, scorned by him since their faithlessness in the matter of Juventius, were eager to crawl back into his favor. And they fancied they could bring him a message that would be joyfully greeted, and would secure them the favorable reception they sought for their own advances: Lesbia was willing to recall her recalcitrant lover. She had once before been successful when making the first advances herself (cf. § 19). Why should she fear defeat now? But both she and her ill-chosen emissaries were speedily undeceived. The broken chain of the old love could never be welded again. Catullus had won by absence, by self-discipline, and most of all, perhaps, by real knowledge of facts in the case, the freedom from his passion for which he had prayed (c. 76). He could once more believe in the friendship of Caelius Rufus, and to him acknowledge, with pain, indeed, but no longer with unavailing torture his true view of Lesbia's character (c. 58). And these proffers now made to him through, and by, Furius and Aurelius were definitely and disdainfully rejected (c. 11), -with a manly, not a petulant disdain, for Catullus could not even then forget that he had loved Lesbia>.

42\. This manly utterance was almost the last of the poet's life. A few scattered verses there may have been, closing perhaps with the touching appeal written from Verona (cf. § 56) to his brother-poet, Cornificius, for a word of consolation, but that was all; and sometime in the year 54 B.C., in his beloved Rome, so says the chronicler, the swiftly burning candle of his life burned itself out.

43\. With him died the clearest, if not the richest, poet-voice ever lifted in Rome. He lacked the lofty grandeur of Lucretius, the polished stateliness of Vergil, the broad sympathies of Horace. For on the one hand, he was no recluse to be filled with heavenly visions, and on the other, his personality was too intense to allow him to cultivate a tolerant spirit. He delighted in life with a vigorous animal passion. Not without charm to him was nature in her sylvan aspect (cf. _e.g._ 34.9 ff.) yet his highest enjoyment was in the life of men. And this life he did not study, as did Horace, from the standpoint of a philosopher. Indeed, he did not study it at all, but simply felt it. For he was not outside of it, but a part of it to the fullest degree, swayed by its ever-changing emotions. Such a nature must of necessity ever remain in many essential aspects the nature of a child. And such was the nature of Catullus throughout his brief life,--warm in quick affections, hot in swift hatreds, pulsing with most active red blood.[^76f5b5ac6dd646f79e431c1f0d06a57a]

  
## From Verona To Patavium

Virgil departed from Verona, intending to travel by road to Patavium, about 50 miles away. 

There a spring wells up, and around about it is a meadow. By the road is a salt spring. A caravan from Patavium passed by. Now the road is quieter. On the road from Verona to Patavium there is a village, in which there is a temple and grove. His shoes are covered in dust from the road. Above the roads are ruins, among which is a cave sacred to Asclepius. He passes another milestone. They pass a pillar on the right surmounted by a stone urn. 

While he was visiting Patavium, he made a point of copying down what Cornelius Tacitus had written.

## A Story By Cornelius Tacitus About Patavium From _Historiae_


Antonius, as he hurried with the veteran soldiers of the cohorts and part of the cavalry to invade Italy, was accompanied by Arrius Varus, an energetic soldier. Service under Corbulo, and successes in Armenia, had gained for him this reputation; yet it was generally said, that in secret conversations with Nero he had calumniated Corbulo's high qualities. The favour thus infamously acquired made him a centurion of the first rank, yet the ill-gotten prosperity of the moment afterwards turned to his destruction. Primus and Varus, having occupied Aquileia, were joyfully welcomed in the neighbourhood, and in the towns of Opitergium and Altinum. At Altinum a force was left to oppose the Ravenna fleet, the defection of which from Vitellius was not yet known. They next attached to their party Patavium and Ateste. There they learnt that three cohorts, belonging to Vitellius, and the Sebonian Horse had taken up a position at the Forum Alieni, where they had thrown a bridge across the river. It was determined to seize the opportunity of attacking this force, unprepared as it was; for this fact had likewise been communicated. Coming upon them at dawn, they killed many before they could arm. Orders had been given to slay but few, and to constrain the rest by fear to transfer their allegiance. Some indeed at once surrendered, but the greater part broke down the bridge, and thus cut off the advance of the pursuing enemy.[^74c23d1d04f640afa8cc559f4b423313]

  
## Travelling By Road

Intending to travel by road to a village, Virgil left Patavium. It was at least 13 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He left the city early, before the rising of the sun. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. As they go up from Patavium, they see the ruined walls. There is a fountain of cold water springing from the rock. Now the road is quieter. 

  
## The Journey To Altinum

Intending to travel by road to Altinum, Virgil left a village. It was at least 14 miles. 

An oxcart passes, loaded with grain. Workers are raising the level of the road. Along the road are graves, and a cenotaph. A cloud passes in front of the sun. 

While he visited his friend at the countryside near that place, he was pleased to discover _Histories_, by Herodotus. Picking it up, he read:

## What Herodotus Once Said About The Countryside Near That Place


After the loss of his son, Croesus remained in deep sorrow for two years. After this time, the destruction by Cyrus son of Cambyses of the sovereignty of Astyages son of Cyaxares, and the growth of the power of the Persians, distracted Croesus from his mourning; and he determined, if he could, to forestall the increase of the Persian power before they became great. Having thus determined, he at once made inquiries of the Greek and Libyan oracles, sending messengers separately to Delphi, to Abae in Phocia, and to Dodona, while others were despatched to Amphiaraus and Trophonius,^[That is, to the oracular shrines of these legendary heroes.] and others to Branchidae in the Milesian country. These are the Greek oracles to which Croesus sent for divination: and he told others to go inquire of Ammon in Libya. His intent in sending was to test the knowledge of the oracles, so that, if they were found to know the truth, he might send again and ask if he should undertake an expedition against the Persians.[^cac6180032734088a65f964017b051ff]

  
## The Journey To Brundulum

Intending to travel by ship down the coast to Brundulum, Virgil left Altinum. It was about 27 miles away. 

Out of the clouds bursts fire fast upon fire. Clouds the darkened heavens have drowned, and snatched the daylight from their eyes. Black night broods on the waters. A gust of the shrill north strikes full on the sail and raises the waves up to heaven. Down in a heap comes a broken mountain of water. They are horsed astride a surge's crest, rocking pendent over the deep. Rocks amid the waves, a vast reef banking the sea.   
  
The sails drop; they swing back to the oars.   
  
Down through the crannies of the living walls the crystal streams descend in murmuring falls. Ships within this happy harbor meet, the thin remainders of the scattered fleet. They lay their weary limbs still dripping on the sand. 

While he was visiting Ravenna, he made a point of copying down what Julius Caesar had written.

## A Story By Julius Caesar About Ravenna From _Civil War_


Thus nothing but tumult and violence was to be seen in the public debates. Caesar's friends had no time given them to inform him of what passed. Even the tribunes themselves were not exempt from danger, nor durst they have recourse to that right of intercession, which Sylla had left them, as the last bulwark of liberty; insomuch that the seventh day after entering upon their office, they saw themselves obliged to provide for their safety; whereas in former times, the most turbulent and seditious tribunes never began to apprehend themselves in danger, till towards the eighth month of their administration. Recourse was had to that rigid and ultimate decree which was never used but in the greatest extremities, when the city was threatened with ruin and conflagration: "That the consuls, the pretors, the tribunes of the people, and the proconsuls that were near Rome, should take care that the commonwealth received no detriment." This decree passed the seventh of January; so that during the first five days in which it was permitted the senate to assemble, after Lentulus's entrance upon the consulship, (for two days are always appropriated to the holding of the comitia,) the most severe and rigorous resolutions were taken, both in relation to Caesar's government, and the tribunes of the people, men of eminent worth and dignity. The tribunes immediately quitted the city, and fled to Caesar, who was then at Ravenna, waiting an answer to his late demands, whose equity he hoped would dispose all parties to entertain thoughts of peace.[^45f0ee7d275f448fa521a172af5d7432]

  
## Departing From Brundulum

Virgil departed from Brundulum, intending to travel by ship down the coast to Altinum, about 27 miles away. 

They spread their sails and ran over the waste sea in their hollow wood. The ship held the high seas, no land yet appearing.   
  
They beheld the harbor of Altinum with gladness. Curved ships are drawn up along the road. 

All of this brought to his mind what Flavius Josephus had said about the countryside near that place:

## A Story About The Countryside Near That Place


However, these robbers and other authors of this tumult, who were afraid, on their own account, lest I should punish them for what they had done, took six hundred armed men, and came to the house where I abode, in order to set it on fire. When this their insult was told me, I thought it indecent for me to run away, and I resolved to expose myself to danger, and to act with some boldness; so I gave order to shut the doors, and went up into an upper room, and desired that they would send in some of their men to receive the money [from the spoils] for I told them they would then have no occasion to be angry with me; and when they had sent in one of the boldest of them all, I had him whipped severely, and I commanded that one of his hands should be cut off, and hung about his neck; and in this case was he put out to those that sent him. At which procedure of mine they were greatly affrighted, and in no small consternation, and were afraid that they should themselves be served in like manner, if they staid there; for they supposed that I had in the house more armed men than they had themselves; so they ran away immediately, while I, by the use of this stratagem, escaped this their second treacherous design against me.[^5934e4f43ff44fd69d01cc0190aa2577]

\newpage

# Altinum To Pons Drusi
  
## Leaving Altinum By Road

Virgil departed from Altinum, intending to travel by road to Iulia Concordia, at least 26 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Above the roads are ruins, among which is a cave sacred to Asclepius. A cloud passes in front of the sun. His shoes are covered in dust from the road. They pass a pillar on the right surmounted by a stone urn. Along the road are graves, and a cenotaph. 

While he visited his friend at the countryside near that place, he was pleased to discover _Description of Greece_, by Pausanias, fl. ca. 150-175. Picking it up, he read:

## The Countryside Near That Place In _Description Of Greece_


Not far from the gate is a common tomb, where lie all those who met their death when fighting against Alexander and the Macedonians. Hard by they show a place where, it is said, Cadmus (he may believe the story who likes) sowed the teeth of the dragon, which he slew at the fountain, from which teeth men came up out of the earth.

On the right of the gate is a hill sacred to Apollo. Both the hill and the god are called Ismenian, as the river Ismenus Rows by the place. First at the entrance are Athena and Hermes, stone figures and named Pronai (Of the fore-temple). The Hermes is said to have been made by Pheidias, the Athena by Scopas. The temple is built behind. The image is in size equal to that at Branchidae; and does not differ from it at all in shape. Whoever has seen one of these two images, and learnt who was the artist, does not need much skill to discern, when he looks at the other, that it is a work of Canachus. The only difference is that the image at Branchidae is of bronze, while the Ismenian is of cedar-wood.

Here there is a stone, on which, they say, used to sit Manto, the daughter of Teiresias. This stone lies before the entrance, and they still call it Manto's chair. On the right of the temple are statues of women made of stone, said to be portraits of Henioche and Pyrrha, daughters of Creon, who reigned as guardian of Laodamas, the son of Eteocles.

The following custom is, to my knowledge, still carried out in Thebes. A boy of noble family, who is himself both handsome and strong, is chosen priest of Ismenian Apollo for a year. He is called Laurel-bearer, for the boys wear wreaths of laurel leaves. I cannot say for certain whether all alike who have worn the laurel dedicate by custom a bronze tripod to the god; but I do not think that it is the rule for all, because I did not see many votive tripods there. But the wealthier of the boys do certainly dedicate them. Most remarkable both for its age and for the fame of him who dedicated it is a tripod dedicated by Amphitryon for Heracles after he had worn the laurel.

Higher up than the Ismenian sanctuary you may see the fountain which they say is sacred to Ares, and they add that a dragon was posted by Ares as a sentry over the spring. By this fountain is the grave of Caanthus. They say that he was brother to Melia and son to Ocean, and that he was commissioned by his father to seek his sister, who had been carried away. Finding that Apollo had Melia, and being unable to get her from him, he dared to set fire to the precinct of Apollo that is now called the Ismenian sanctuary. The god, according to the Thebans, shot him.

Here then is the tomb of Caanthus. They say that Apollo had sons by Melia, to wit, Tenerus and Ismenus. To Tenerus Apollo gave the art of divination, and from Ismenus the river got its name. Not that the river was nameless before, if indeed it was called Ladon before Ismenus was born to Apollo.[^2c0d53cad4e44f96900adac123d3c27f]

  
## Iulia Concordia To Aquileia By Road

Virgil departed from Iulia Concordia, intending to travel by road to Aquileia, a journey of about 26 miles. 

Workers are raising the level of the road. Now the road is quieter. There is a fountain of cold water springing from the rock. They pass a pillar on the right surmounted by a stone urn. 

All of this brought to his mind what Julius Caesar had said about Aquileia:

## A Story About Aquileia By Julius Caesar


It is again told Caesar, that the Helvetii intended to march through the country of the Sequani and the Aedui into the territories of the Santones, which are not far distant from those boundaries of the Tolosates, which [viz. Tolosa , Toulouse] is a state in the Province. If this took place, he saw that it would be attended with great danger to the Province to have warlike men, enemies of the Roman people, bordering upon an open and very fertile tract of country. For these reasons he appointed Titus Labienus, his lieutenant, to the command of the fortification which he had made. He himself proceeds to Italy by forced marches, and there levies two legions, and leads out from winter-quarters three which were wintering around Aquileia , and with these five legions marches rapidly by the nearest route across the Alps into Further Gaul. Here the Centrones and the Graioceli and the Caturiges, having taken possession of the higher parts, attempt to obstruct the army in their march. After having routed these in several battles, he arrives in the territories of the Vocontii in the Further Province on the seventh day from Ocelum, which is the most remote town of the Hither Province; thence he leads his army into the country of the Allobroges, and from the Allobroges to the Segusiani. These people are the first beyond the Province on the opposite side of the Rhone .[^bf732909d26440f2a4ba7c8382ec66ef]

  
## 28 Miles To Ad Tricesimum

Leaving Aquileia, Virgil set out for Ad Tricesimum by road, a journey of about 28 miles. 

Along the road are graves, and a cenotaph. Above the roads are ruins, among which is a cave sacred to Asclepius. The road narrows here, an orchard wall encroaching on it. Workers are raising the level of the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He had set out from Aquileia amidst a throng travelling the same way. Water has washed out the road, making for slow going. On the road from Aquileia to Ad Tricesimum there is a village, in which there is a temple and grove. There is a fountain of cold water springing from the rock. 

The library at the countryside near that place happened to have a copy of _Odes_, where Virgil encountered it.

## The Countryside Near That Place In _Odes_


While I had power to bless you,  
Nor any round that neck his arms did fling  
More privileged to caress you,  
Happier was Horace than the Persian king.  
While you for none were pining  
Sorer, nor Lydia after Chloe came,  
Lydia, her peers outshining,  
Might match her own with Ilia's Roman fame.  
Now Chloe is my treasure,  
Whose voice, whose touch, can make sweet music flow:  
For her I'd die with pleasure,  
Would Fate but spare the dear survivor so.  
I love my own fond lover,  
Young Calais, son of Thurian Ornytus:  
For him I'd die twice over,  
Would Fate but spare the sweet survivor thus.  
What now, if Love returning  
Should pair us 'neath his brazen yoke once more,  
And, bright-hair'd Chloe spurning,  
Horace to off-cast Lydia ope his door?  
Though he is fairer, milder,  
Than starlight, you lighter than bark of tree,  
Than stormy Hadria wilder,  
With you to live, to die, were bliss for me.  
[^da512b1fdacf4be68172ed946f994959]

  
## Travelling By Road To Aquileia

Leaving Ad Tricesimum, Virgil set out for Aquileia by road, about 28 miles away. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. There is a fountain of cold water springing from the rock. His shoes are covered in dust from the road. Above the roads are ruins, among which is a cave sacred to Asclepius. Water has washed out the road, making for slow going. A cloud passes in front of the sun. 

He would later record what Cornelius Tacitus had said about Aquileia.

## The Story Of Aquileia


The next question was, what place should be selected as the seat of war. Verona seemed the most eligible, surrounded as it was with open plains, suitable for the action of cavalry, in which they were very strong. At the same time it was thought that in wresting from Vitellius a colony so rich in resources there would be both profit and glory. They secured Vicetia by simply passing through it. Though in itself a small gain, for the town is but of moderate strength, it was considered an important advantage when they reflected that in this town Cæcina was born, and that, the general of the enemy had lost his native place. The people of Verona were a valuable aid; they served the cause by the example of their zeal and by their wealth, and the army thus occupied a position between Rhætia and the Julian Alps. It was to cut off all passage at this point from the armies of Germany that they had barred this route. All this was done either without the knowledge, or against the commands of Vespasian. He gave orders that the army should halt at Aquileia and there await Mucianus; and these orders he supported by the argument, that as Ægypt, which commanded the corn supplies, and the revenues of the wealthiest provinces were in his hands, the army of Vitellius would be compelled to capitulate from the want of pay and provisions. Mucianus in frequent letters advised the same policy; a victory that should cost neither blood nor tears, and other objects of the kind, were his pretexts; but in truth he was greedy of glory, and anxious to keep the whole credit of the war to himself. Owing, however, to the vast distances, the advice came only after the matter was decided.[^3e42876587ac478fb78038e070a8174d]

  
## To Iulia Concordia By Road

Intending to travel by road to Iulia Concordia, Virgil left Aquileia. It was about 26 miles away. 

He had set out from Aquileia amidst a throng travelling the same way. A caravan from Iulia Concordia passed by. Now the road is quieter. An oxcart passes, loaded with grain. Above the roads are ruins, among which is a cave sacred to Asclepius. Water has washed out the road, making for slow going. The sun beats down. Workers are raising the level of the road. This is a smooth road, by which many wagons were bringing wood to Iulia Concordia. 

All of this brought to his mind what Herodotus had said about the countryside near that place:

## An Extract From _Histories_ By Herodotus


When the Argives inquired at Delphi about the safety of their city, a common response was given, one part regarding the Argives themselves, but there was an additional response for the Milesians. I will mention the part concerning the Argives when I come to that part of my history; this was the prophecy given to the Milesians in their absence: Then, Miletus, contriver of evil deeds, For many will you become a banquet and glorious gifts; Your wives will wash the feet of many long-haired men; Other ministers will tend my Didyman^[Didyma (oftener called Branchidae), was near Miletus; the temple was of Apollo \rendergreek{Διδυμέυς}. Cp. Hdt. 1.46.] shrine! All this now came upon the Milesians, since most of their men were slain by the Persians, who wore long hair, and their women and children were accounted as slaves, and the temple at Didyma with its shrine and place of divination was plundered and burnt. Of the wealth that was in this temple I have often spoken elsewhere in my history.[^07ad232c4c234e9fad55509b24f7878e]

  
## From Iulia Concordia To Tridentum

Virgil departed from Iulia Concordia, intending to travel by road to Tridentum, about 103 miles away. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. An oxcart passes, loaded with grain. There a spring wells up, and around about it is a meadow. He passes another milestone. 

The library at the countryside near that place happened to have a copy of _Historiae_, where Virgil encountered it.

## A Story About The Countryside Near That Place By Cornelius Tacitus


Antonius did not press forward, for he thought of the fatigue and the wounds with which a battle so hard fought, notwithstanding its successful termination, must have disabled his cavalry and their horses. As the shadows of evening deepened the whole strength of the Flavianist army came up. They advanced amid heaps of dead and the traces of recent slaughter, and, as if the war was over, demanded that they should advance to Cremona, and receive the capitulation of the vanquished party, or take the place by storm. This was the motive alleged, and it sounded well, but what every one said to himself was this: "The colony, situated as it is on level ground, may be taken by assault. If we attack under cover of darkness, we shall be at least as bold, and shall enjoy more licence in plunder. If we wait for the light, we shall be met with entreaties for peace, and in return for our toil and our wounds shall receive only the empty satisfaction of clemency and praise, but the wealth of Cremona will go into the purses of the legates and the prefects. The soldiers have the plunder of a city that is stormed, the generals of one which capitulates." The centurions and tribunes were spurned away; that no man's voice might be heard, the troops clashed their weapons together, ready to break through all discipline, unless they were led as they wished.[^d214c7458e45479a9e3ae89cde96822f]

  
## Tridentum To Endidae By Road

Leaving Tridentum, Virgil set out for Endidae by road, a distance of about 20 miles. 

There a spring wells up, and around about it is a meadow. He left the city early, before the rising of the sun. He passes another milestone. A cloud passes in front of the sun. The sun beats down. This is a smooth road, by which many wagons were bringing wood to Endidae. Along the road are graves, and a cenotaph. By the road is a salt spring. There is a fountain of cold water springing from the rock. 

While he was visiting Verona, he made a point of copying down what E. T. Merrill had written.

## On Verona, According To E. T. Merrill


3\. Of this new school of poets the most prominent and interesting figure is Catullus. It is possible to know him personally as only now and then an ancient writer can be known to us, and yet he gives us but few definite biographical facts concerning himself, while still fewer are given by other authors of his own and later ages. But the little body of poems that constitute his extant works is so replete with his intense personality, and shows forth so unreservedly his every emotion, that the man stands out before us as does no other man of the age with the exception of two or three of its political leaders. And all this is true, even though we acknowledge, as we are bound to do, that in many questions of importance concerning his life we must be content with a working hypothesis instead of a series of established facts, and that the biographer, as the interpreter of the poems of Catullus, must be understood to be presenting probabilities and not certainties.

4\. With regard to his full name we are left in some doubt. He refers to himself by name in his poems twenty-five times, but in each case only by the cognomen, Catullus, while the better manuscripts of his writings are inscribed simply _Catulli Veronensis Liber_ . Yet there is no difficulty in ascertaining his gentile name from other writers. Varro (L. L. VII. 50), Suetonius (Iul.73), Porphyrio (on Hor. Sat. 1.10.19), Charisius (1.97), Jerome (T Chron. a. Abr.1930), all give it as Valerius. There are fewer references to his praenomen. Four of the later and interpolated manuscripts give it in their titles as Quintus, and until lately it was supposed that to this indication might be added the testimony of the elder Pliny (N H. XXXVII. 81) - Relying upon such authority Scaliger went so far as to emend c. 67.12 so as to bring in for the unintelligible words qui te the praenomen of the poet in the vocative, Quinte; and his suggestion won the approval of even so keen a critic as Lachmann. But it is now universally conceded that the initial Q. prefixed to the word Catullus in the passage specified from Pliny is an interpolation, the best MS., the _codex Bambergensis_, containing only the cognomen without prefix. There is, moreover, positive evidence in favor of a different praenomen. Jerome (l.c.), in speaking of the birth of the poet, calls him in full C. Valerius Catullus, and Apuleius (Apol. 10), whose accuracy, however, in the matter of names is not above suspicion, calls him C. Catullus. In the face, then, of the testimony of interpolated manuscripts only, his praenomen must stand established as Gaius.

5\. Concerning the birthplace of Gaius Valerius Catullus there is abundant testimony. The titles of the best MSS. of his works call him Veronensis, and Jerome (l.c.) declares him born at Verona. In this testimony concur his admirers among the poets of the centuries immediately following (_e.g._ Ov. Am. 3.15.7; Mart. I.61.1; X. 103.5; XIV. 195; Auson. Op. 23. 1); and his own writings furnish confirmatory evidence of the same fact. He calls himself (c. 39.13) Transpadanus; he possessed a villa at Sirnaio on the shore of Lacus Benacus near Verona (c. 31); he was acquainted with Veronese society (cc. 67, 100); and he spent part of his time at Verona (cc. 35, 68a).[^f18766d4d75b40b8adaebdf883237460]

  
## Leaving Endidae By Road

From Endidae to Pons Drusi is about 13 miles away when travelling by road. 

As they go up from Endidae, they see the ruined walls. He had set out from Endidae amidst a throng travelling the same way. He passes another milestone. He left the city early, before the rising of the sun. This is a smooth road, by which many wagons were bringing wood to Pons Drusi. L(uci) Arre(ni) Maur(i) Anau(nia) was carved into the stone. A grove of Minerva is hard by the road, a grove of poplar trees. 

He would later record what Cornelius Tacitus had said about Patavium.

## A Story By Cornelius Tacitus About Patavium From _Historiae_


When this success became known, two legions, the seventh (Galba's) and the eighteenth (the Gemina), finding the campaign opening in favour of the Flavianists, repaired with alacrity to Patavium under the command of Vedius Aquila the legate. A few days were there taken for rest, and Minucius Justus, prefect of the camp in the 7th legion, who ruled with more strictness than a civil war will permit, was withdrawn from the exasperated soldiery, and sent to Ves- pasian. An act that had been long desired was taken by a flattering construction for more than it was worth, when Antonius gave orders that the statues of Galba, which had been thrown down during the troubles of the times, should be restored in all the towns. It would, he supposed, reflect honour on the cause, if it were thought that they had been friendly to Galba's rule, and that his party was again rising into strength.[^58f9f43c8ffd49ffb60b1994fbde155e]

\newpage

# Pons Drusi To Brigantium
  
## Leaving Pons Drusi By Road

Virgil departed from Pons Drusi, intending to travel by road to a village, at least 28 miles. 

He passes another milestone. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Along the road are graves, and a cenotaph. As they go up from Pons Drusi, they see the ruined walls. This is a smooth road, by which many wagons were bringing wood to a village. The sun beats down. There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. 

  
## 41 Miles To Veldidena

Virgil departed from a village, intending to travel by road to Veldidena, a distance of about 41 miles. 

The road narrows here, an orchard wall encroaching on it. Along the road are graves, and a cenotaph. They pass a pillar on the right surmounted by a stone urn. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. He left the city early, before the rising of the sun. A cloud passes in front of the sun. Workers are raising the level of the road. Above the roads are ruins, among which is a cave sacred to Asclepius. He passes another milestone. 

All of this brought to his mind what E. T. Merrill had said about the countryside near that place:

## The Story Of The Countryside Near That Place


53\. The popularity enjoyed by Catullus among the Augustan elegiasts did not preserve his memory alive through the declining centuries of the Roman empire. The scholars and poets of the latter half of the first millennium after Christ had forgotten even his name. Only Rather, bishop of Verona, in a sermon delivered there in 965 A.D., confesses that he had just become acquainted with his writings; and an anthology of Latin poets written at about the same time (now _cod. Thuaneus, Parisinus 8071_) contains a single poem of Catullus (c. 62). Then he drops cut of ken once more till the opening of the 14th century when a writer of Vicenza, Benvenuto Campesani (who died before 1330), celebrated in a few enigmatic verses (cf. Critical Appendix _ad fin._) the rediscovery of the text of Catullus 'under a bushel,' apparently at Verona. From this MS., or from copies of it, numerous Italian scholars, among them Petrarch, early learned to know the poet. The original MS. soon disappeared, and has never been found; but two descendants of it, apparently not more than one generation removed, are preserved to us, and form the basis of the present text of Catullus. One of these copies, ordinarily called G (now No. 14,137 in the National Library at Paris) was made in the year 1375, and the other, O (No.30 of the Canonici Latin MSS. in the Bodleian Library) at about the same time. (Cf. also introductory note to Critical Appendix.)

54\. The earlier editions of Catullus, however, were based upon interpolated MSS., and though displaying great erudition and classical taste left much to be desired in the way of true principles of textual criticism. The edition of Karl Lachmann (Berlin, 1829) first established the text of Catullus upon a scientific basis, though the two MSS. on which he mainly depended, D and L (in the Royal Library at Berlin), are far inferior to G and O. These became first known to the world, G in 1830 through I. Sillig (Jahrb. für Philol. xiii. p.262 ff.), and O through Robinson Ellis in his first edition of Catullus (Oxford, 1867). During the last quarter of a century, then, the constitution as well as the elucidation of the text of Catullus has made its most marked advances.[^6b1e445bdf524a0dafd17422e7a68b85]

  
## After Veldidena

From Veldidena to a village is at least 41 miles when travelling by road. 

A caravan from a village passed by. By the road is a salt spring. The road narrows here, an orchard wall encroaching on it. An oxcart passes, loaded with grain. Along the road are graves, and a cenotaph. As they go up from Veldidena, they see the ruined walls. He left the city early, before the rising of the sun. The sun beats down. Workers are raising the level of the road. 

  
## A Village To Pons Drusi By Road

From a village to Pons Drusi is at least 28 miles when travelling by road. 

As they go up from a village, they see the ruined walls. Along the road are graves, and a cenotaph. An oxcart passes, loaded with grain. They pass a pillar on the right surmounted by a stone urn. On the road from a village to Pons Drusi there is a village, in which there is a temple and grove. Lucius Pinxit was carved into the stone. Now the road is quieter. Next to the straight road that leads to Pons Drusi, there is visible a sculpted tomb. 

The library at the countryside near that place happened to have a copy of _Commentary on Catullus_, where Virgil encountered it.

## A Story By E. T. Merrill About The Countryside Near That Place From _Commentary On Catullus_


9\. The only relative mentioned by Catullus is his brother, whose death was the occasion to him of such intense and lasting grief (cc. 65, 68, 101). But Suetonius (l.c.) speaks of the father as a host of Julius Caesar even so late, apparently, as the close of the poet's life. Why he (to say nothing of the mother) is never mentioned by the poet, we cannot tell. Not improbably, however, he did not have the same active sympathy with the tastes and inclinations of Catullus as the father of Horace had with those of his son. Catullus, moreover, was not the only son, and was probably younger than the one whose untimely death in the Troad he records.

10\. Yet there was apparently wealth enough in the family to enable even the younger brother to enjoy the advantages that wealth brought to the young Italian of that day. He was able early in his young manhood to go to Rome, and to make that city thenceforth his abiding-place (c. 68.34 ff.). He owned a villa at Sirmio (c. 31), and another on the edge of the Sabine hills (c. 44). And there is no indication that while at Rome he was busy with any pursuit that could fill his purse, although, like many another young Roman, he later obtained a provincial appointment, and went to Bithynia on the staff of the governor Memmius in the hope of wealth (cf. § 29 ff.). The hope, he tells us (cc. 10, 28), proved abortive, but Catullus had yet money enough -- perhaps even to purchase a yacht for his homeward journey like any millionaire (cf. § 35 and introductory note to c. 4) - at any rate to continue his merry life at Rome, apparently without great pecuniary embarrassment. All these indications point to no financial inability or niggardliness on the part of his father. Possibly the villas, and an increase of income, came to him upon the death of his brother.

11\. Whether Catullus, like Horace, was accompanied to Rome by his father is doubtful. On the whole, it seems hardly probable that he was. To say nothing of the considerations possibly connected with the interests of the elder son, the father was apparently resident in Verona at the time when Julius Caesar was governor of Gaul (Suet. Iul. 73), and this fact may indicate that at no time was the family home at Verona broken up in favor of a new one at Rome.[^3095733f96bc4d469f1704ee22c85c5a]

  
## To Maiensis Statio By Road

Virgil departed from Pons Drusi, intending to travel by road to Maiensis Statio, at least 15 miles. 

There is a fountain of cold water springing from the rock. There a spring wells up, and around about it is a meadow. This is a smooth road, by which many wagons were bringing wood to Maiensis Statio. He left the city early, before the rising of the sun. He passes another milestone. The road narrows here, an orchard wall encroaching on it. His shoes are covered in dust from the road. By the gate of Maiensis Statio, these words were carved: [- - -] et Aug(usto) / [- - -] max(imo) / [- - -] co(n)s(uli) / [ordo Triden]tinor(um). 

  
## The Journey To Abodiacum

From Maiensis Statio to Abodiacum is at least 140 miles when travelling by road. 

He left the city early, before the rising of the sun. On the road from Maiensis Statio to Abodiacum there is a village, in which there is a temple and grove. An oxcart passes, loaded with grain. They pass a pillar on the right surmounted by a stone urn. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A grove of Minerva is hard by the road, a grove of poplar trees. This is a smooth road, by which many wagons were bringing wood to Abodiacum. There is a fountain of cold water springing from the rock. Workers are raising the level of the road. 

The library at the countryside near that place happened to have a copy of _Divus Augustus_, where Virgil encountered it.

## The Countryside Near That Place In _Divus Augustus_


He conquered, however, partly in person, and partly by his lieutenants, Cantabria,^[Cantabria, in the north of Spain, now the Basque province.] Aquitania and Pannonia,^[The ancient Pannonia includes Hungary and part of Austria, Styria and Carniola.] Dalmatia, with all Illyricum and Rhaetia,^[The Rhaetian Alps are that part of the chain bordering on the Tyrol.] besides the two Alpine nations, the Vindelici and the Salassii.^[The Vindelici principally occupied the country which is now the kingdom of Bavaria; and the Salassii, that part of Piedmont which includes the valley of Aost.] He also checked the incursions of the Dacians, by cutting off three of their generals with vast armies, and drove the Germans beyond the river Elbe; removing two other tribes who submitted, the Ubii and Sicambri, into Gaul, and settling them in the country bordering on the Rhine. Other nations also, which broke into revolt, he reduced to submission. But he never made war upon any nation without just and necessary cause; and was so far from being ambitious either to extend the empire, or advance his own military glory, that he obliged the chiefs of some barbarous tribes to swear in the temple of Mars the Avenger,^[The temple of Mars Ultor was erected by Augustus in fulfilment of a vow made by him at the battle of Philippi. It stood in the Forum which he built, mentioned in chap. xxix. There are no remains of either.] that they would faithfully observe their engagements, and not violate the peace which they had implored. Of some he demanded a new description of hostages, their women, having found from experience that they cared little for their men when given as hostages; but he always afforded them the means of getting back their hostages whenever they wished it. Even those who engaged most frequently and with the greatest perfidy in their rebellion, he never punished more severely than by selling their captives, on the terms of their not serving in any neighbouring country, nor being released from their slavery before the expiration of thirty years. By the character which he thus acquired, for virtue and moderation, he induced even the Indians and Scythians, nations before known to the Romans by report only, to solicit his friendship, and that of the Roman people, by ambassadors. The Parthians readily allowed his claim to Armenia; restoring, at his demand, the standards which they had taken from Marcus Crassus and Mark Antony, and offering him hostages besides. Afterwards, when a contest arose between several pretenders to the crown of that kingdom, they refused to acknowledge any one who was not chosen by him.[^93f72077f7c344e79713cf54eee1b77f]

  
## After Abodiacum

Virgil departed from Abodiacum, intending to travel by road to Cambodunum, a distance of about 31 miles. 

Next to the straight road that leads to Cambodunum, there is visible a sculpted tomb. By the road is a salt spring. He passes another milestone. Above the roads are ruins, among which is a cave sacred to Asclepius. He left the city early, before the rising of the sun. A caravan from Cambodunum passed by. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Wondering if it was related to his journey, he read the words that were carved there: Iuvenniae Prisc[ae] / uxori carissim[ae] / [- - - - - -] / [- - - bene] / de se merit[ae] / M(arcus) Albinius(?) Fe[lix?] / dec(urio) mun(icipii) qu[i et] / sacerdotalis [omni]/[bus h]onorib(us) in [re p(ublica)] / sua func[tus]. This is a smooth road, by which many wagons were bringing wood to Cambodunum. 

While he visited his friend at the countryside near that place, he was pleased to discover _Galba_, by Suetonius ca. 69-ca. 122. Picking it up, he read:

## A Story About The Countryside Near That Place


He governed the province during eight years, his administration being of an uncertain and capricious character. At first he was active, vigorous, and indeed excessively severe, in the punishment of offenders. For, a money-dealer having committed some fraud in the way of his business, he cut off his hands, and nailed them to his counter. Another, who had poisoned an orphan, to whom he was guardian, and next heir to the estate, he crucified. On this delinquent imploring the protection of the law, and crying out that he was a Roman citizen, he affected to afford him some alleviation, and to mitigate his punishment, by a mark of honour, ordered a cross, higher than usual, and painted white, to be erected for him But by degrees he gave himself up to a life of indolence and inactivity, from the fear of giving Nero any occasion of jealousy, and because, as he used to say, " Nobody was obliged to render an account of their leisure hours." He was holding a court of justice on the circuit at New Carthage,^[Now Carthagena.] when he received intelligence of the insurrection in Gaul;^[A.U.C. 821] and while the lieutenant of Aquitania was soliciting his assistance, letters were brought from Vindex, requesting him " to assert the rights of mankind, and put himself at their head to relieve them from the tyranny of Nero." Without any long demur, he accepted the invitation, from a mixture of fear and hope. For he had discovered that private orders had been sent by Nero to his procurators in the province to get him dispatched; and he was encouraged to the enterprise, as well by several auspices and omens, as by the prophecy of a young woman of good family. The more so, because the priest of Jupiter at Clunia,^[Now Corunna. ] admonished by a dream, had discovered in the recesses of the temple some verses similar to those in which she had delivered her prophecy. These had also been uttered by a girl under divine inspiration, about two hundred years before. The import of the verses was, "That in time, Spain should give the world a lord and master."[^a6a42fbc857e4dfc9fdd1f25334b71e1]

  
## Travelling By Road To Brigantium

Intending to travel by road to Brigantium, Virgil left Cambodunum. It was about 36 miles away. 

He left the city early, before the rising of the sun. Workers are raising the level of the road. They pass a pillar on the right surmounted by a stone urn. On the road from Cambodunum to Brigantium there is a village, in which there is a temple and grove. The sun beats down. A cloud passes in front of the sun. 

He would later record what Cornelius Tacitus had said about the countryside near that place.

## What Cornelius Tacitus Once Said About The Countryside Near That Place


Then Civilis fulfilled a vow often made by barbarians; his hair, which he had let grow long and coloured with a red dye from the day of taking up arms against Rome, he now cut short, when the destruction of the legions had been accomplished. It was also said that he set up some of the prisoners as marks for his little son to shoot at with a child's arrows and javelins. He neither took the oath of allegiance to Gaul himself, nor obliged any Batavian to do so, for he relied on the resources of Germany, and felt that, should it be necessary to fight for empire with the Gauls, he should have on his side a great name and superior strength. Munius Lupercus, legate of one of the legions, was sent along with other gifts to Veleda, a maiden of the tribe of the Bructeri, who possessed extensive dominion; for by ancient usage the Germans attributed to many of their women prophetic powers and, as the superstition grew in strength, even actual divinity. The authority of Veleda was then at its height, because she had foretold the success of the Germans and the destruction of the legions. Lupercus, however, was murdered on the road. A few of the centurions and tribunes, who were natives of Gaul, were reserved as hostages for the maintenance of the alliance. The winter encampments of the auxiliary infantry and cavalry and of the legions, with the sole exception of those at Mogontiacum and Vindonissa, were pulled down and burnt.[^54d08dc974f042a890af72984ca14af8]

\newpage

# Brigantium To Aventicum
  
## Brigantium To Curia By Road

Virgil departed from Brigantium, intending to travel by road to Curia, a distance of about 50 miles. 

As they go up from Brigantium, they see the ruined walls. He left the city early, before the rising of the sun. The sun beats down. There is a fountain of cold water springing from the rock. 

While he was visiting Comum, he made a point of copying down what E. T. Merrill had written.

## An Extract From _Commentary On Catullus_ By E. T. Merrill


An invitation to an otherwise unknown poet, Caecilius of Como, to visit Catullus at Verona, with incidentally a little pleasantry about a love-affair of Caecilius, and a neat compliment about his forthcoming poem. This address could not have been written before 59 B.C. (cf. v. 4 n.), and was written while Catullus was at Verona. Two occasions only are surely known on which he was at his ancestral home after 59, once immediately on his return from Bithynia in the summer of 56, and again somewhat more than a year later, a few months before his death. The poem may well date from one or the other of these periods.—Meter, Phalaecean.

tenero: as a writer of love-poetry; cf. Ovid (with whom it is a favorite word) Ov. Ars Am. 3.333 teneri carmen Properti ; Ov. Rem. Am. 757 teneros ne tange poetas ; Mart. 4.14.13 tener Catullus ; Mart. 7.14.3 teneri amica Catulli.

sodali: implying warm intimacy; cf. Catul. 10.29; Catul. 12.13; Catul. 30.1; Catul. 47.6.

Caecilio: possibly an ancestor of C. Plinius Caecilius Secundus (circ. 62-113 A.D.), whose home was in Novum Comum, where inscriptions show that the Caecilii flourished.

papyre: apostrophe to his book by the author is not uncommon, especially in Ovid (e.g. Ov. Trist. 1.1) and Martial (e.g. Mart. 7.84, also sent to a Caecilius).

relinquens: cf. Catul. 31.6 liquisse .

Comi: in the year 59 B.C., in accordance with the Vatinian law, Julius Caesar settled 5O0O colonists at Comum, a town already established under Cn. Pompeius Strabo, and called the place _Novum Comum_. Como, the modern town, lies at the southern end of the westem arm of Lacus Larius (Lago di Como), about thirty miles north of Mediolanum (Milan).

cogitationes: Catullus desires to entice his friend to visit him, and so speaks with playful vagueness of certain weighty matters that can be communicated only by word of mouth. The whole tone of the poem is opposed to any serious interpretation of the phrase.

amici sui meique: the same playful mysteriousness of expression is kept up here, but Caecilius undoubtedly interpreted it correctly to mean that the friend was the writer himself. So Catullus speaks of himself to Alfenus in Catul. 30.2 as _tui amiculi_.

viam vorabit: an unusual, but perfectly intelligible phrase, perhaps favored by the alliteration, and augmenting by its exaggerated character the playfulness of the urgency.

candida: cf. Catul. 13.4.

roget morari: for the more usual construction of _rogare_ with _ut_ see Catul. 13.14.

illum deperit: is dying for him; cf. Catul. 100.2; Pl. Cas. 449 hic ipsus Casinam deperit ; Nem. Bucol. 2.70 rusticus Alcon te peream ; and in Catul. 45.5 perire used absolutely.

impotente: violent; cf. Catul. 4.18n.

quo tempore: denoting the starting-point of a continued action, as indicated by v. 14 _ex eo;_ cf. Catul. 68.15 tempore quo with Catul. 68.20, where the continuance of activity from the initial period is clearly indicated.

legit: sc. _illa_; she read the opening verses lent her by the author; cf. Catul. 42.1ff., where Catullus was unable to recover his tablets lent, perhaps, under similar circumstances. The custom of public recitation by the author himself was introduced later by Asinius Pollio (cf. Catul. 12.6).

Dindymi dominam: i.e. a poem, or play, based on the story of Cybele; cf. Catul. 63.13, Catul. 63.95, and introductory note to that poem.

misellae: she is pitied only as suffering love's pleasing pain; cf. Catul. 45.21; Catul. 50.9; Catul. 55.5.

ignes: of the flames of love; cf. Catul. 2.8n. _ardor_; Verg. A. 4.66 est mollis flamma medullas ; Ov. Am. 3.10.27 tenerae flammam rapuere medullae.

interiorem: cf. Catul. 64.93 imis medullis ; Catul. 64.196 extremis medullis ; Catul. 66.23 penitus exedit medullas.

medullam: the word occurs only here in Catullus in the singular, but seven times in the plural in the same sense; cf. Catul. 25.2 medullula .

ignosco tibi: sc. for falling deeply in love with Caecilius, and therefore seeking to detain him.

Sapphica musa: i.e. than the inspired Sappho herself; perhaps with a reminiscence of the frequency with which, in the Palatine Anthology, Sappho is ranked among the Muses.

doctior: an epithet commonly applied to poets, especially of this school, which disdained the rude simplicity of its predecessors, and sought inspiration among the polished Alexandrians (Catullus is styled _doctus_ by Ovid in Ov. Am. 3.9.62, by Lygdamus in Tib. 3.6.41, and by Martial in Mart. 7.99.7 and Mart. 14.152.1); Catullus means that a girl so appreciative of the best poetry must have within herself the attributes of a poet: so Propertius calls Cynthia _docta_ (Prop. 3.13.11), and in Catullus Catul. 65.2 the Muses are _doctae virgines._

magna Mater: i.e. Cybele; cf. Catul. 63.9n.

incohata: there is no reason to suppose, as some have done, any playful implication that Caecilius had been unwarrantably long in getting beyond the beginning of his work.[^c36aafa457aa406780bb819d292fef06]

  
## To Comum

From Curia to Comum is at least 92 miles when travelling by road. 

He had set out from Curia amidst a throng travelling the same way. The sun beats down. Workers are raising the level of the road. There is a fountain of cold water springing from the rock. Above the roads are ruins, among which is a cave sacred to Asclepius. $] // pro se et suis v(otum) s(olvit) l(ibens) l(aetus) m(erito) was carved into the stone. A cloud passes in front of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. His shoes are covered in dust from the road. 

He would later record what Suetonius ca. 69-ca. 122 had said about Comum.

## Comum In _Divus Julius_


He endeavoured with equal assiduity to engage in his interest princes and provinces in every part of the world: presenting some with thousands of captives, and sending to others the assistance of troops, at whatever time and place they desired, without any authority from either the senate or people of Rome. He likewise embellished with magnificent public buildings the most powerful cities not only of Italy, Gaul, and Spain, but of Greece and Asia; until all people being now astonished, and speculating on the obvious tendency of these proceedings, Claudius Marcellus, the consul, declaring first by proclamation, that he intended to propose a measure of the utmost importance to the state, made a motion in the senate that some person should be appointed to succeed Caesar in his province, before the term of his command was expired; because the war being brought to a conclusion, peace was restored, and the victorious army ought to be disbanded. He further moved, that Caesar being absent, his claims to be a candidate at the next election of consuls, should not be admitted, as Pompey himself had afterwards abrogated that privilege by a decree of the people. The fact was, that Pompey, in his law relating to the choice of chief magistrates, had forgot to except Caesar, in the article in which he declared all such as were not present incapable of being candidates for any office; but soon afterwards, when the law was inscribed on brass, and deposited in the treasury, he corrected his mistake. Marcellus, not content with depriving Caesar of his provinces, and the privilege intended him by Pompey, likewise moved the senate, that the freedom of the city should be taken from those colonists whom, by the Vatinian law, he had settled at New Como;^[Comum was a town of the Orobii, of ancient standing, and formerly powerful. Julius Csesar added to it five thousand new colonists; whence it was generally called Novocomum. But in time it recovered its ancient name, Comum; Pliny the younger, who was a native of this place, calling it by no other name. ] because it had been conferred upon them with ambitious views, and by a stretch of the laws.[^5d53476bb7844371ae3bc80612de59ee]

  
## Leaving Comum By Road

Virgil departed from Comum, intending to travel by road to Curia, at least 92 miles. 

He passes another milestone. There a spring wells up, and around about it is a meadow. He had set out from Comum amidst a throng travelling the same way. A grove of Minerva is hard by the road, a grove of poplar trees. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

He would later record what E. T. Merrill had said about Comum.

## On Comum, According To E. T. Merrill


The self-mutilation and subsequent lament of Attis, a priest of Cybele. The centre of the worship of the Phrygian \rendergreek{Κυβέλη} or \rendergreek{Κυβήβη}, was in very ancient times the town of Pessinus in Galatian Phrygia, at the foot of Mt. Dindymus, from which the goddess received the name Dindymene. Cybele had early become identified with the Cretan divinity Rhea, the Mother of the Gods, and to some extent with Demeter, the search of Cyhele for Attis being compared with that of Demeter for Persephone. The especial worship of Cybele was conducted by emasculated priests called Galli (or, as in vv. 12 and 34, with reference to their physical condition, Gallae). Their name was derived by the ancients from that of the river Gallus, a tributary of the Sangarius, by drinking from which men became inspired with frenzy (cf. Ov. Fast. 4.361ff.). The worship was orgiastic in the extreme, and was accompanied by the sound of such frenzy-producing instruments as the _tympana, cymbala, tibiae_, and _cornu_, and culminated in scourging, self-mutilation, syncope from excitement. and even death from hemorrhage or heart-failure (cf. Lucr. 2.598ff.; Varr. Sat. Men. 131 Büch.ff.; Ov. Fast. 4.179ff.). The worship of the Magna Mater, or Mater Idaea, as she was often called (perhaps from identification with Rhea of the Cretan Mt. Ida rather than from the Trojan Mt. Ida), was introduced into Rome in 205 B.C. in accordance with a Sibylline oracle which foretold that only so could 'a foreign enemy' (i.e. Hannibal) be driven from Italy. Livy 29.10, Livy 29.14) gives an interesting account of the solemnities that accompanied the transfer from Pessinus to Rome of the black stone that represented the divinity, and of the establishment of the Megalensia; cf. also Ov. Fast. 4.247ff. The stone itself was perhaps a meteorite, and is thus described by Arnobius Adu. Gent. 7.46: lapis quidam non magnus, ferri manu hominis sine ulla impressione qui posset; coloris furvi atque atri, angellis prominentibus inaequalis, et quem omnes hodie … videmus … indolatum et asperum. Servius (Aen. 7.188) speaks of it as _acus Matris Deum_, and as one of the seven objects on which depended the safety of Rome.

The early connection of Attis with the Mother of the Gods seems to point to the association of an original male element with an original female element as the parents of all things. But in the age of tradition Attis appears as a servant instead of an equal, and the subordination of the male to the female element is further emphasized by the representation of Attis, like the Galli of historic times, as an emasculated priest. Greek imagination pictured him as a beautiful youth who was beloved by the goddess, but wandered away from her and became untrue; but being sought and recalled to allegiance by her, in a passion of remorse he not only spent his life in her service, but by his own act made impossible for the future such infidelity on his part, thus setting the example followed by all the Galli after him (cf. Ovid Fast. l. c.). Catullus departs from this form of the Attis myth, and makes Attis a beautiful Greek youth who in a moment of religious frenzy sails across seas at the head of a band of companions to devote himself to the already long-established service of the goddess (vv. 1-3). On reaching the shores of Trojan Ida he consummates the irrevocable act of dedication (vv. 4-5), and with his companions rushes up the mountain to the sanctuary of the goddess (vv. 6-38). But on awaking next morning he feels the full awfulness of his act (vv. 39-47), and gazing out over the sea toward his lost home, bewails his fate (vv. 48-73), till the jealous goddess unyokes a lion from her car and sends him to drive her wavering votary back to his allegiance (vv. 74-fin.). The story is told with a nervous vigor and swing of feeling that are unequalled in Latin literature, and to it the galliambic meter (Intr. 85), the one traditionally appropriated to such themes, lends great effect. The date of composition is uncertain, but Catullus may have found his immediate inspiration in his contact with the Cybelian worship in its original home during his residence in Bithynia in 57-56 B.C. (see Intr. 29ff.). Or it may have been found in his studies in the Alexandrian poets; for Callimachus certainly used the galliambic meter, though no distinct title of a poem by him on this theme is extant. Caecilius of Comum was also engaged on a poem based on the worship of Cybele (cf. Catul. 35.13ff.), and Varro and Maecenas both exercised their talents in the same direction (cf. Varr. Sat. Men. l. c.; Maec. in Baehr. Bragm. Poet. Rom. p. 339).

The poem abounds in rhetorical devices to add to its effect; such are the frequent employment of alliteration (vv. 2, 6, 7, 8, 9, 10, 13, etc.), of strange and harsh compounds (vv. 23 _hederigerae_, 34 _properipedem_, 45 sonipedibus, 51 _erifugae_, 72 _nemorivagus_), and the repetition of words of agitated movement and feeling (eg. _rapidus_ three times, _citatus_ four times, _citus_ twice, _rabidus_ three times, _rabies_ once).

celeri: indicating his eagerness for arrival.

Phrygium nemus: that clothing the slopes not of Dindymus but of Ida (cf. vv. 30, 52).

citato cupide pede: emphazing the eager haste of the traveller, rather than indicating a land journey after reaching the shores of Asia (cf. vv. 47, 89), the poet is not writing as a geographer. Cf. v. 30 _properante pede_.

opaca: cf. v. 32. The mad rush of the new devotees is contrasted with the silent mysteries of the abode of the goddess.

ibi: thereupon; cf. vv. 42, 48, 76; and Catul. 66.33; Catul. 8.6n.

furenti rabie: cf. v. 38 _rabidus furor_.

vagus animis: the plural to indicate his divided, distorted emotions; cf. Verg. A. 8.228 ecce furens animis aderat Tirynthius .

ili: genitive from the stem _ilio-_, a rare but legitimate variant for the more frequent _ili-_; cf. Cels. 4.1 iliis (dat. plur.); Gloss. Labb. ilium \rendergreek{λαγών} ; Marc. Emp. 36 [ilium] .

sine viro: i.e. _sine virilitate_.

terrae sola: (plural, as in v. 40 _sola dura_): cf. Lucr. 2.592 nam multis succensa locis ardent sola terrae.

niveis manibus: cf. v. 10 n. _teneris digitis_. Adjectives descriptive of feminine beauty are employed to accord with the change of gender under which Attis is now spoken of, and himself speaks of his companions (vv. 12 _Gallae_, 15 _exsecutae_, 34 _rapidae Gallae_); cf. Hor. Carm. 2.4.3 niveo colore (of Briseis); Hor. Carm. 3.27.25 niveum latus (of Europe); Verg. A. 8.387 niveis lacertis (of Venus).

citata: Attis is from henceforth a _notha mulier_ (v. 27), and is described by feminine adjectives; cf. vv. 11 _adorta, tremebunda_, 31 _furibunda_, 32 _comitata_, etc.; but when he returns to himself and thinks with sorrow and loathing upon his condition, the masculine adjective is resumed; cf. vv. 51 _miser_, 78 _hunc_, 88 _tenerum_, 89 _ille_. The emendations by which all these later masculines (except v. 78 _hunc_) have been transformed to feminines are based on incorrect feeling.

lene: the tympanum is probably called _leve_ because it is _cavum_ (v. 10).

typanum: Gr. poet. form \rendergreek{τύπανον} _metri gratia_ (cf. v. 21, etc. _tympanum_, Gr. \rendergreek{τύμπανον}); from representations in vase- and wall-paintings, an instrument like the modern tambourine, but with the rattling disks of metal suspended at intervals from its edge by short cords.

tubam Cybelles: as the blare of the _tuba_ is the summons and incitement to warriors, so is the beat of the _tympanum_ to the votaries of Cybele; the phrase is further explained by _tua initia_. The famous norm of Bentley (on Lucan 1.600) that when the penult is short, the form _Cybele_ should be written, but when it is long the form _Cybebe, Cybelle_ being discarded altogether, is not well supported by either Greek or Latin usage. _Cybelle_ (Gr. _*ku/bella_) is found in many good MSS.

mater: Cybele was the _Magna Mater Idaea_ of the Romans, as well as _mater deorum_; cf. intr. note; Hymn. Cyb. μήτερα μοι πάντων τε θεῶν, πάντων τ᾽ ἀνθρώπων .

initia: technically used only of the mysteries of Demeter (cf. Varr. RR 3.I.5 initia vocantur potissimum ea quae Cereri fiunt sacra ), but here of the symbol of the secret worship of Cybele, perhaps by reason of the popular confusion of Cybele with Demeter.

teneris digitis: cf. v. 8 n. _niveis manibus_; Ov. Ib. 456 [ut Attis] quatias molli tympana rauca manu ; Ov. Fast. 4.342 feriunt molles taurea terga manus.

cava: the word _tympanum_ also denoted a kettle-drum with a hemispherical resounding cavity and a single head of hide, and so _cava_, which would properly characterize it, is here used of its cognate instrument, the tambourine; cf. Ov. Fast. 4.183 inania tympana tundent ; Aus. Epist. 29.21 cava tympana.

tremebunda: in the quivermg of nervous excitement.

agite: cf. Catul. 61.38n.

Gallae: cf. v. 34, and intr. note.

Cybeles: Gr. \rendergreek{Κυβέλη}; cf. v. 9 n. _Cybelles_.

Dindymenae dominae: cf. v. 91; Catul. 35.14.

vaga: of the purposeless wanderings of the crazed devotees; cf. vv. 18 _erroribus_; 25 _vaga cohors_; 31 _vaga vadit_.

pecora: cf. Ov. Ib. 457 pecus Magnae Parentis (of the Galli)

sectam meam exsecutae: under my rule; Attis acts as recruiting officer, and then (_duce me_) guides the new devotees to their place of service. _comites_ implies here a certain subordination as in the case of the _comites_ of a provincial governor; cf. Catul. 28.1 Catul. 11.1. Apparently _exsequi_ is used with _sectam_ only here, though Cicero uses _sectam persequi_ (Cic. Verr. 2.5.70.181), and _sectam sequi_ is frequently found (cf. Livy 29.27.2 qui meam sectam secuntur , a formal expression in an invocation).

rapidum: of the rushing waves of the sea, as explained in _truculenta pelagi_; cf. Catul. 64.358 rapido Hellesponto .

truculenta pelagi: with the construction cf. Verg. A. 9.81 pelagi alta ; Hor. Carm. 4.4.76 acuta belli ; with the sentiment, Hor. Carm. 1.3.10 truci pelago .

hilarate, etc.: i.e. haste to gladden the heart of the goddess by the presence of this new accession of enthusiastic votaries.

erroribus: the _rabidus furor animi_ (v. 38) would lead the band, not directly to the temple, but in Maenad-like tortuousness of course.

cymbalum: _cymbala_ were hollow hemispheres of metal a few inches in diameter, held one in each hand by the aid of small rings or thongs attached to the center of their convex surfaces. Struck together, they gave a sharp, clanging sound that fitted well with that of the _tympana_ and _tibiae_; cf. Catul. 64.262 tereti tenuis tinnitus aere ciebant ; Ov. Fast. 4.184 aera tinnitus aere repulsa dabunt ; Ov. Fast. 4.189 sonus aeris acuti ; Aus. Epist. 24.23 tinnitus atinnitus aëni.eumlaut;ni.

reboant: cf. Aus. Epist. 24.21 tentis reboant cava tympana tergis .

Phryx: the _tibiae_ were said to be a Phrygian invention; cf. Catul. 64.264; Lucr. 2.620 Phrygio stimulat numero cava tibia mentis ; Tib. 2.1.86 obstrepit et Phrygio tibia curva sono ; Ov. Fast. 4.181 inflexo Berecyntia tibia cornu .

curvo calamo: the _tibia_ was originally made of a reed. The curved variety appears from bas-reliefs to have been shaped sometimes like the _lituus_, straight and of uniform diameter from the mouth-piece till near the bell, where it curved sharply back upon itself, but sometimes to have had a gentle double curve and an increasing diameter from mouthniece to bell, like a cow-horn. The straight varieties, more commonly used, were generally played in pairs, one with each hand, being often supported in position at the player's mouth by a band admitting the two mouth-pieces and fastened at the back of the head.

graue: cf. Stat. Theb. 6.113 signum luctus cornu grave mugit adunco tibia .

maenades: the poet borrows for the priests of Cybele the name appropriate to the frenzied maidens that attended upon the similar rites of Dionysus.

capita vi iaciunt: frequent wall-paintings and engraved gems show the bacchanals beating the tympana and swaying the head violently back and forth; cf. Catul. 64.255 capita inflectentes ; Maec. frag. 4 Baehr. sonante typano quate flexibile caput ; Varr. Sat. Men. 132 Buech. semiviri teretem comam volantem iactant ; Ov. Met. 3.726 ululavit Agave, collaque iactavit, movitque per aera crinem .

hederigerae: \rendergreek{ἅπαξ λεγόμενον}.

acutis ululatibus cf. v. 28 Maec. frag. 5 Baehr. comitum chorus ululet Ov. Fast. 4.341 exululant comites , Met. l. c.

illa: the demonstrative characterizes as well known the whole statement; in this use _ille_ corresponds closely to our definite article.

volitare vaga: so of Bacchus in Catul. 64.251, Catul. 64.390.

cohors: i.e. _comites_; cf. v. 11 and 28.1 _Pisonis comites, cohors inanis_.

tripudiis: of the wild, rhythmic dance connected with the worship.

simul: sc. _atque_; cf. v. 45 and Catul. 22.15n.

notha mulier: cf. Ov. Fast. 4.183 semimares (of the Galli); Ov. Ib. 453 nec femina nec vir (of Attis); Varro Sat. Men. 132 Buech. semiviri (of the Galli).

thiasus: of a band of raving devotees, as in 64.252, and often, of the attendants of Iacchus.

trepidantibus: as v. 11 _tremebunda_, of the quivering of nervous excitement; cf. Verg. A. 7.395 aliae tremulis ululatibus aethera complent (of the Bacchic worshippers).

ululat: cf. v. 24 n. ululatibus.

leve tympanum: cf. v. 8 _leve tympanum_.

recrepant: the word apparently occurs only here and in Ciris 108 lapis recrepat Cyllenia murmura pulsus .

viridem Idam: cf. v. 70; Culex 311 iugis Ida patens frondentibus ; Ov. AA 1.289 sub umbrosis nemorosae vallibus Idae ; Ov. Fast. 6.327 in opacae vallibus Idae ; Ov. Met. 11.762 umbrosa sub Ida ; Stat. Silv. 3.4.12 pinifera Ida .

properante pede: cf. v. 34 _properipedem_.

animam agens: to be explained from _anhelans_ of the almost fainting condition resulting from haste, excitement, and exhaustion, gasping. It usually means 'to give up the ghost'; cf. Cic. Fam. 8.13.2 Q. Hortensius, cum has litteras scripsi, animam agebat.

comitata: usually with an ablative of person instead of thing when, as here, it has a personal subject.

veluti iuvenca: etc. the comparison is usually employed by the poets of the yoke of love; cf. Catul. 68.118n.

domum Cybelles: apparently the shrine of the goddess on the mountain-top.

Cerere: cf. Cic. ND 2.23.60 fruges Cererem appellamus, vinum autem Liberum; ex quo illud Terenti 'sine Cerere et, Libero friget Venus' (from Ter. Eun. 732).—The fasting in this case was probably not due to a requirement of ritual, but simply to the utterly exhausted condition of the new Galli.

quiete molli: etc. cf. v. 44.

rabidus furor: cf. v. 4 _furenti rabie_.

oris aurei: doubtless to be construed with _Sol_ rather than with _oculis_; cf. Lucr. 5.461 aurea … matutina rubent radiati lumina solis ; Verg. G. 1.232 sol aureus ; Ov. Met. 7.663 iubar aureus extulerat sol .

radiantibus oculis: cf. Ov. Trist. 2.325 radiantia lumina solis ; and with the figure in _oculis_, F. W. Bonrdillon, "the night has a thousand eyes and the day but one."

lustravit: surveyed, rather than 'illumined,' as the figure in _oculis_ shows.

aethera album: etc. the adjectives _album, dura, ferum_ describe permanent characteristics and not those peculiar to the morning, and hence _album_ must be understood not merely of the sky brightened by dawn, but of the bright, fiery aether; cf. Cic. ND 1.13.33 caeli ardorem ; Cic. ND 2.15.41 in ardore caelesti qui aether vel caelum nominatur .

sola: plural, since the sun views every region of earth.

dura: solid, to distinguish the earth from the fluid aether and sea.

feram: a traditional epithet of the sea; cf. v. 16 n.

sonipedibus: first in Lucil. 15.15. Muel. Campanus sonipes ; also in Cic. De Or. 3.47.183 paeon … sicut … sonipedes ; and frequently in later poets.

ibi: temporal, as in v. 4 (see note).

Somnus: etc. the morn having come, Somnus is released from duty and flies eagerly (_citus_) back to Pasithea, whose reciprocal eagerness of longing is indicated by v. 43 _trepidante sinu_. Pasithea was one of the lesser Graces, and was promised to Sleep as a wife by Hera in Hom. Il. 14.267ff.

simul: cf. v. 27 n. simul.

liquida mente: of passionless calm; cf. Pl. Epid. 643 animo liquido et tranquillo's: tace! Pl. Ps. 232 nihil curassis: liquido's animo: ego pro me et pro te curabo .

sine quis: cf. v. 5.

ubique: the quantity of the penult shows the equivalence to _et ubi_.

animo aestuante: contrasted with _liquida mente_; there was but a moment of clear and calm mental vision succeeded by the torture of recollection.

rasum: so sometimes in earlier Latin (including Lucretius) for later _rursus_.

reditum tetulit: cf. v. 79 _uti reditum ferat_; Catul. 61.26 aditum ferens ; Catul. 61.43 aditum ferat. On the archaic form of the verb cf. v. 52; Catul. 34.8n.

maria vasta: cf. Catul. 31.3 mari vasto ; Catul. 64.127 pelagi vastos aestus .

miseriter: for _misere_, as _puriter_ for _pure_ in Catul. 39.14; Catul. 76.19.

miser: while under the influence of his mad enthusiasm, Attis gloried in his emasculation, but now, in his recovered senses, he speaks of his condition only with loathing, using feminines (v. 68) to point this feeling, but of course not using a feminine adjective in this expression of passionate longing for his home.

tetuli: see 34.8 n.

ferarum gelida stabula: cf. Verg. A. 6.179 itur in antiquam silvam, stabula alta ferarum . On the lengthening of the final syllable before initial _st_ see Intr. 86g.

reor: indicative present with future meaning; cf Catul. 1.1n. _dono_.

pupula: cf. Cic. ND 2.57.142 acies ipsa, qua cernimus, quae pupula vocatur.

derigere: so, rather than _dirigere_, of the fixed gaze in a single direction; cf. Catul. 22.8 derecta plumbo .

carens est: for _caret_; cf. Catul. 64.317n. _fuerant exstantia_.

genitoribus: i.e. _parentibus_; cf. Lucr. 2.615 ingrati genitoribus (of the Galli).

foro: the poet here employs the corresponding Latin word for the Greek \rendergreek{ἀγορά}.

miser ah miser: cf. Catul. 61.139.

etiam atque etiam: cf. Pl. Trin. 674 te moneo hoc etiam atque etiam ; Ter. Eun. 56 etiam atque etiam cogita ; and often in later writers.

figurae: under the word is the Greek feeling for the beauty of the human form that had made Attis the object of so much adoration; cf. Cic. ND 1.18.47ff.

mulier: starting with the torturing thought of his present hateful condition, he retraces the steps of his former career as the passionate admiration of a whole city.

adulescens: cf. Catul. 12.9n. _puer_; Censor. Die Nat. 14.2 [Varro putat] usque annum XV. pueros dictos … ad tricensimum annum adulescentes … usque quinque et quadraginta annos iuvenis … adusque sexagensimum annum seniores … inde usque finem vitae senes .

ephebus: cf. Censor. Die Nat. 14.8 de tertia autem aetate adulescentulorum tres gradus esse factos in Graecia prius quam ad viros perveniatur, quod vocent annorum xiiii. \rendergreek{παῖδα, μελλέφηβον} autem xv., dein sedecim \rendergreek{ἔφηβον},tunc septemdecim \rendergreek{ἐξέφηβον}.

gymnasi flos: with the figure cf. Catul. 17.14n.

olei: i.e. _palaestrae_, as the contestants were well rubbed with oil before the sports; cf. Cic. De Or. 1.18.81 nitidum … genus verborum … sed palaestrae … et olei.

ianuae frequentes: devoted admirers flocked to his doors by day.

limina tepida: finding no entrance, his lovers spent the night in complaints on his door-stone; cf. Plat. Symp. 183a οἱ ἐρασται … ποιούμενοι … κοιμήσεις ἐπι θύραις ; Aristaenetus 2.20 ὅτε μὲν γὰρ αὐτοὶ ποθεῖτε, ἀστρώτους καὶ χαμαιπετεῖς κοιμήσεις ἐπὶ θύραις ποιεῖσθε ; Hor. Carm. 3.10.20 non hoc semper erit liminis patiens latus , Prop. 1.16.22 tristis et in tepido limine somnus erit ; Ov. Met. 14.709 posuit in limine duro molle latus .

corollis: the door-posts and threshold were decorated with garlands by the lovers in token of their devotion; cf. Lucr. 4.1177 at lacrimans exclusus amator limina saepe floribus et sertis operit ; Ov. Met. 14.708 interdum madidas lacrimarum rore coronas postibus intendit ; Prop. 1.16.7 mihi non desunt turpes pendere corollae .

linquendum ubi: etc. the proudly careless boy affected so completely to disregard the attentions of his lovers as to be aware of them only as he left the house in the morning for the stadium and palaestra.

esset: only one earlier instance of the subjunctive of repetition with _ubi_ can be cited (Pl. Bacch. 431). In the silver age the construction becomes more frequent; cf. Hor. Carm. 3.6.41 sol ubi montium mutaret umbras.

deum ministra: not specifically a servant of the general pantheon, but simply a temple servant, an unknown priest instead of the beloved of a city: the needful specification follows in _Cybeles famula_; cf. Tac. Ann. 1.10.5; Tac. Ann. 4.37.5 effigie numinum .

ministra, famula: not content with the contrast between the lord of a cityful of lovers and the slave of a mysterious divinity, Attis brands his present disgrace by using the feminine form.

maenas: cf. v. 23 n. _maenades_.

viridis Idae: cf. v. 30 n.

altis Phrygiae columinibus: the following verse makes it clear that mountain-summits are meant, though the form appears to be used only here in that sense; but the form _culmen_ is so used by Caes. BG 3.2 and by Suet. Dom. 23, and perhaps _columinibus_ is here used _metri gratia_.

silvicultrix, nemorivagus: each adjective is \rendergreek{ἅπαξ λεγόμενον}, though Verg. A. 10.551 uses _silvicola_, and Lucr. 2.597 montivagum .

iam iam: with the repetition cf. Cic. Phil. 2 34.87 iam iam minime miror te otium perturbare ; Verg. A. 12.875 iam iam linquo acies .

iam iamque: not = _et iam iam_, for the passionate exclamation of sorrow demands an asyndeton; the phrase rather = _iam et iam_; cf. Cic. Att. 7.20.1 at illum ruere nuntiant et iam iamque adesee ; Cic. Att. 16.9 iam iamque video bellum : and in Catullus himself Catul. 38.3 and Catul. 64.274 magis magis beside Catul. 68.48 magis atque magis .

roseis labellis: the youthful beauty of Attis is thus contrasted with the intensity of his suffering and the bitterness of his plaint; cf. Catul. 45.12n. _purpureo ore_.

geminas: cf. Catul. 51.11 gemina teguntur lumina nocte (where, however, there is a transfer of epithet); Culex 150 geminas aures ; Verg. A. 5.416 temporibus geminis ; Ov. Fast. 2.154 geminos pedes ; Stat. Silv. 4.4.26 geminas aures ; Mart. 10.10.10 geminas manus .

deorum aures: somewhat loosely said, as if Cybele were not alone on the summit of Ida, but in the company of the other gods.

nuntia: the neuter singular in the sense of 'news' is very unusual, and the neuter plural in the same sense is still more rare; cf. however Sedul. 2.474 grandia nuntia .

iuga resolvens: while unfastening the lion from the yoke she addresses him. Cybele is often depicted by the poets as riding in a chariot drawn by yoked lions; cf. Lucr. 2.600 hanc veteres Graium docti cecinere poetae sedibus in curru biiugos agitare Ieones ; Verg. A. 3.113 et iuncti currum dominae subiere Ieones ; Verg. A. 10.253 biiugi ad frena leones.

laevum: the 'nigh' lion; the specification is doubtless introduced for the sake of increasing the realistic effect of the lion's attack by details of word painting.

pecoris hostem: probably with reference to the Greek descriptions of the lion as \rendergreek{ταυροβόρος} (Anth. Plan. 94), \rendergreek{ταυροκτόνος} (Soph. Phil. 400), \rendergreek{ταυρολέτωρ} (Man. Chron. 252), \rendergreek{ταυροσφάγος} (Lyc. 47), \rendergreek{ταυροφόνος} (Orph. Hym. 14.2); for _pecus_ indicates neat cattle as well as sheep; cf. Varro RR 2.1.12 de pecore maiore, in quo sunt … boues, asini, equi .

stimulans: probably not with a goad, but with her words.

agedum, age: with the repetition cf. Ter. And. 310 age age .

fac ut: with the construction cf. v. 79 Catul. 64.231; Catul. 109.3; but for _fac_ and subjunctive without _ut_, v. 82; Catul. 68.46.

reditum ferat: cf. v. 47 _reditum tetulit_.

caede terga cauda: this habit of the lion in rage is noted by Plin. NH 8.16.49, and by Luc. Phar. 1.208 mox ubi se saevae stimulavit verbere caudae erexitque iubam et vasto grave murmur hiatu infremuit .

fac retonent: with the construction cf. Catul. 68.46 and v. 78 n. _retonent_ is \rendergreek{ἅπαξ λεγόμενον}.

minax: of Cybele's attitude toward Attis.

religat iuga: frees the lion from the yoke, completing the action begun in v. 76 _iuncta iaga resolvens_; with this conjunction of resolvere and _religare_ in the same meaning cf. Pallad. Rut. 3.13 providendum est omnibus annis vitem resolvi ac religari . For _religare_ in the other sense cf. Catul. 64.174.

rabidum: Cybele's exhortation was to arouse the lion to fury rather than to haste, and that is the characteristic passion of his subsequent action; hence _rapidum_, the reading of V, must be an error for _rabidum_, as _rapidos_ for _rabidos_ in v. 93, where a similar collocation occurs, _incitatos rabidos_ being like _rabidum incitat_.

pede vago: the lion rushes now here, now there, in search of his prey; otherwise in Catul. 64.277.

albicantis: not of the general color of sea-sand, but of the whiteness and sparkle of a foamwet beach, as the position and use of _umida_ indicate.

loca litoris: cf. v. 70 _Idae loca_.

tenerum: not of the beauty, but of the present effeminate condition of Attis; cf. Juv. 1.22 tener spado .

marmora pelagi: cf. Hom. Il. 14.273 ἅλα μαρμαρέην . The word seems to describe the sparkling of the sea that occurs when it is covered with ripples only, and hence to convey the idea of a calm expanse (_nitens aequor_).

demens: sc. with present fear, not with past recollections.

famula: repeating the feminine used by Attis himself in v. 68, and leaving with the reader, as the final thought, the irrevocable character of the awful self-consecration with which the poem opened.

The epilogue is a brief hymn to the dread goddess herself.

dea magna: cf. Prop. 4.17.35 dea magna Cybelle .

domina Dindymi: cf. v. 13; Catul. 35.14.

procul: etc. cf. Ov. Fast. 4.116 a nobis sit furor iste procul .

age: with the verb in this sense with an adjective expressing, as it were, the result of the action, cf. Ov. Met. 5.13 quae te, germane, furentem mens agit in facinus? Tac. Agr. 41 sic Agricola … in ipsam gloriam praeceps agebatur.

incitatos … rabidos; cf. the same collocation in v. 85 _rabidum incitat_.[^5a251c747dae49c0968e4a270e7b0e24]

  
## Leaving Curia By Road

Intending to travel by road to Brigantium, Virgil left Curia. It was a journey of about 50 miles. 

Water has washed out the road, making for slow going. Workers are raising the level of the road. Next to the straight road that leads to Brigantium, there is visible a sculpted tomb. The road narrows here, an orchard wall encroaching on it. Above the roads are ruins, among which is a cave sacred to Asclepius. He had set out from Curia amidst a throng travelling the same way. His shoes are covered in dust from the road. A grove of Minerva is hard by the road, a grove of poplar trees. 

While he visited his friend at the countryside near that place, he was pleased to discover _Historiae_, by Cornelius Tacitus. Picking it up, he read:

## On The Subject Of The Countryside Near That Place


Accordingly neither the Treveri, the Lingones, nor the other revolted States, took measures at all proportioned to the magnitude of the peril they had incurred. Even their generals did not act in concert. Civilis was traversing the pathless wilds of the Belgæ in attempting to capture Claudius Labeo, or to drive him out of the country. Classicus for the most part wasted his time in indolent repose, as if he had only to enjoy an empire already won. Even Tutor made no haste to occupy with troops the upper bank of the Rhine and the passes of the Alps. Meanwhile the 21st legion, by way of Vindonissa, and Sextilius Felix with the auxiliary infantry, by way of Rhætia, penetrated into the province. They were joined by the Singularian Horse, which had been raised some time before by Vitellius, and had afterwards gone over to the side of Vespasian. Their commanding officer was Julius Briganticus. He was sister's son to Civilis, and he was hated by his uncle and hated him in return with all the extreme bitterness of a family feud. Tutor, having augmented the army of the Treveri with fresh levies from the Vangiones, the Cæracates, and the Triboci, strengthened it with a force of veteran infantry and cavalry, men from the legions whom he had either corrupted by promises or overborne by intimidation. Their first act was to cut to pieces a cohort, which had been sent on in advance by Sextilius Felix; soon afterwards, however, on the approach of the Roman generals at the head of their army, they returned to their duty by an act of honourable desertion, and the Triboci, Vangiones, and Cæracates, followed their example. Avoiding Mogontiacum, Tutor retired with the Treveri to Bingium, trusting to the strength of the position, as he had broken down the bridge over the river Nava. A sudden attack, however, was made by the infantry under the command of Sextilius; a ford was discovered, and he found himself betrayed and routed. The Treveri were panic-stricken by this disaster, and the common people threw down their arms, and dispersed themselves through the country. Some of the chiefs, anxious to seem the first to cease from hostilities, fled to those States which had not renounced the Roman alliance. The legions, which had been removed, as I have before related, from Novesium and Bonna to the ter- ritory of the Treveri, voluntarily swore allegiance to Vespasian. These proceedings took place in the absence of Valentinus. When he returned, full of fury and bent on again throwing everything into confusion and ruin, the legions withdrew to the Mediomatrici, a people in alliance with Rome. Valentinus and Tutor again involved the Treveri in war, and murdered the two legates, Herennius and Numisius, that by diminishing the hope of pardon they might strengthen the bond of crime.[^20cecc1e1c654086baa40dc4bc458db7]

  
## After Brigantium

Intending to travel by road to Cambodunum, Virgil left Brigantium. It was a distance of about 36 miles. 

Next to the straight road that leads to Cambodunum, there is visible a sculpted tomb. Along the road are graves, and a cenotaph. This is a smooth road, by which many wagons were bringing wood to Cambodunum. He passes another milestone. They passed by an inscription that read: $] / [- - -]S[- - -] / [- - -]ATRV[- - -] / [- - -]PATRVE[- - -] / [&. Water has washed out the road, making for slow going. He had set out from Brigantium amidst a throng travelling the same way. 

While he visited his friend at the countryside near that place, he was pleased to discover _Histories_, by Polybius. Picking it up, he read:

## A Story About The Countryside Near That Place By Polybius


The Consuls of the next year, however, Publius Furius Philus and Caius Flaminius, once more invaded the Celtic lands, marching through the territory of the Anamares, who live not far from Placentia.^[Others read Ananes and Marseilles [\rendergreek{Ἀνάνων . . . Μασσαλίας}]; but it seems impossible that the Roman march should have extended so far.] Having secured the friendship of this tribe, they crossed into the country of the Insubres, near the confluence of the Adua and Padus. They suffered some annoyance from the enemy, as they were crossing the river, and as they were pitching their camp; and after remaining for a short time, they made terms with the Insubres and left their country. After a circuitous march of several days, they crossed the River Clusius, and came into the territory of the Cenomani. As these people were allies of Rome, they reinforced the army with some of their men, which then descended once more from the Alpine regions into the plains belonging to the Insubres, and began laying waste their land and plundering their houses. The Insubrian chiefs, seeing that nothing could change the determination of the Romans to destroy them, determined that they had better try their fortune by a great and decisive battle. They therefore mustered all their forces, took down from the temple of Minerva the golden standards, which are called "the immovables," and having made other necessary preparations, in high spirits and formidable array, encamped opposite to their enemies to the number of fifty thousand. Seeing themselves thus outnumbered, the Romans at first determined to avail themselves of the forces of the allied Celtic tribes; but when they reflected on the fickle character of the Gauls, and that they were about to fight with an enemy of the same race as these auxiliary troops, they hesitated to associate such men with themselves, at a crisis of such danger, and in an action of such importance. However, they finally decided to do this. They themselves stayed on the side of the river next the enemy: and sending the Celtic contingent to the other side, they pulled up the bridges; which at once precluded any fear of danger from them, and left themselves no hope of safety except in victory; the impassable river being thus in their rear. These dispositions made, they were ready to engage.[^934cbc67ca064be0b16287e9b1697d16]

  
## The Journey To Brigantium

From Cambodunum to Brigantium is about 36 miles away when travelling by road. 

He passes another milestone. Workers are raising the level of the road. A cloud passes in front of the sun. On the road from Cambodunum to Brigantium there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. The sun beats down. The road narrows here, an orchard wall encroaching on it. As they go up from Cambodunum, they see the ruined walls. They pass a pillar on the right surmounted by a stone urn. 

He would later record what Catullus, Gaius Valerius had said about Comum.

## A Story By Catullus, Gaius Valerius About Comum From _Carmina_


Now to that tender bard, my Comrade fair,  
(Cecilius) say I, " Paper go, declare,  
Verona must we make and bid to New  
Comum's town-walls and Larian Shores adieu;"  
For I determined certain fancies he  
Accept from mutual friend to him and me.  
Wherefore he will, if wise, devour the way,  
Though the blonde damsel thousand times essay  
Recall his going and with arms a-neck  
A-winding would e'er seek his course to check;  
A girl who (if the truth be truly told)  
Dies of a hopeless passion uncontroul'd;  
For since the doings of the Díndymus-dame,  
By himself storied, she hath read, a flame  
Wasting her inmost marrow-core hath burned.  
I pardon thee, than Sapphic Muse more learn'd,  
Damsel : for truly sung in sweetest lays  
Was by Cecilius Magna Mater's praise.  
[^d8d8fdbb6738483c8f8274eefe4c31cf]

  
## From Brigantium To Augusta Raurica

Intending to travel on a military boat headed upstream to Augusta Raurica, Virgil left Brigantium. It was a distance of about 119 miles. 

He presses onward. The journey is more tiring than you might expect. A cloud passes in front of the sun. 

The library at Mediolanum happened to have a copy of _Divus Augustus_, where Virgil encountered it.

## On Mediolanum, According To Suetonius Ca. 69-Ca. 122


He conducted in person only two foreign wars; the Dalmatian, whilst he was yet but a youth; and, after Antony's final defeat, the Cantabrian. He was wounded in the former of these wars; in one battle he received a contusion in the right knee from a stone, and in another, he was much hurt in one leg and both arms, by the fall of a bridge.^[Not a bridge over a river, but a military engine used for gaining admittance into a fortress.] His other wars he carried on by his lieutenants; but occasionally visited the army, in some of the wars of Pannonia and Germany, or remained at no great distance, proceeding from Rome as far as Ravenna, Milan, or Aquileia.[^8f3b8bbe64ca4a02867b163dec933325]

  
## The Journey To Aventicum

Virgil departed from Augusta Raurica, intending to travel by road to Aventicum, a journey of about 58 miles. 

He left the city early, before the rising of the sun. The sun beats down. As they go up from Augusta Raurica, they see the ruined walls. By the road is a salt spring. 

While he was visiting the countryside near that place, he made a point of copying down what Polybius had written.

## On The Countryside Near That Place, According To Polybius


Just then intelligence reached him that Attalus had crossed the sea and, dropping anchor at Peparethos, had occupied the island. He therefore despatched a body of men to the islanders to garrison their city; and at the same time despatched Polyphontes with an adequate force into Phocis and Boeotia; and Menippus, with a thousand peltasts and five hundred Agrianes to Chalcis and the rest of Euboea; while he himself advanced to Scotusa, and sent word at the same time to the Macedonians to meet him at that town. But when he learnt that Attalus had sailed into the port of Nicaea, and that the leaders of the Aetolians were collecting at Heraclea, with the purpose of holding a conference together on the immediate steps to be taken, he started with his army from Scotusa, eager to hurry thither and break up their meeting. He arrived too late to interrupt the conference: but he destroyed or carried off the corn belonging to the people along the Aenianian gulf, and then returned. After this he left his army in Scotusa once more; and, with the light-armed troops and the royal guard, went to Demetrias, and there remained, waiting to see what the enemy would attempt. To secure that he should be kept perfectly acquainted with all their movements, he sent messengers to the Peparethii, and to his troops in Phocis and Euboea, and ordered them to telegraph to him everything which happened, by means of fire signals directed to Mount Tisaeum, which is a mountain of Thessaly conveniently situated for commanding a view of those places.[^4420d57f0ae24c9cb38862b9a9fe9304]

\newpage

# Aventicum To Veldidena
  
## 58 Miles To Augusta Raurica

From Aventicum to Augusta Raurica is a distance of about 58 miles when travelling by road. 

As they go up from Aventicum, they see the ruined walls. An oxcart passes, loaded with grain. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Virgil saw this on a roadside tomb: [In h]onor(em) d(omus) d(ivinae) // Genio sta/[t]ionis Viri/[u]s Probus / miles leg(ionis) XXII / [P(rimigeniae)] [[Alexandr]]/[[[ia]n(a)e]] p(iae) f(idelis) Imp(eratore) d(omino) n(ostro) / [[[Al]exandro]] / [- - - co(n)s(ulibus)] / [&. 

This was the event that influenced him later when he wrote about the countryside near that place in _Georgics_:

## The Countryside Near That Place In Virgil'S _Georgics_


Now, seeing that life doth even to bee-folk bring  
Our human chances, if in dire disease  
Their bodies' strength should languish—which anon  
By no uncertain tokens may be told—  
Forthwith the sick change hue; grim leanness mars  
Their visage; then from out the cells they bear  
Forms reft of light, and lead the mournful pomp;  
Or foot to foot about the porch they hang,  
Or within closed doors loiter, listless all  
From famine, and benumbed with shrivelling cold.  
Then is a deep note heard, a long-drawn hum,  
As when the chill South through the forests sighs,  
As when the troubled ocean hoarsely booms  
With back-swung billow, as ravening tide of fire  
Surges, shut fast within the furnace-walls.  
Then do I bid burn scented galbanum,  
And, honey-streams through reeden troughs instilled,  
Challenge and cheer their flagging appetite  
To taste the well-known food; and it shall boot  
To mix therewith the savour bruised from gall,  
And rose-leaves dried, or must to thickness boiled  
By a fierce fire, or juice of raisin-grapes  
From Psithian vine, and with its bitter smell  
Centaury, and the famed Cecropian thyme.  
There is a meadow-flower by country folk  
Hight star-wort; 'tis a plant not far to seek;  
For from one sod an ample growth it rears,  
Itself all golden, but girt with plenteous leaves,  
Where glory of purple shines through violet gloom.  
With chaplets woven hereof full oft are decked  
Heaven's altars: harsh its taste upon the tongue;  
Shepherds in vales smooth-shorn of nibbling flocks  
By Mella's winding waters gather it.  
The roots of this, well seethed in fragrant wine,  
Set in brimmed baskets at their doors for food.  
  
[^577270aac2184be59b3772e9f7d39a67]

  
## Leaving Augusta Raurica By River

Leaving Augusta Raurica, Virgil set out for Brigantium on a military boat floating downstream, about 119 miles away. 

The sun beats down. 

While he visited his friend at the countryside near that place, he was pleased to discover _Historiae_, by Cornelius Tacitus. Picking it up, he read:

## A Story By Cornelius Tacitus About The Countryside Near That Place From _Historiae_


Forty thousand armed men burst into Cremona, and with them a body of sutlers and camp-followers, yet more numerous and yet more abandoned to lust and cruelty. Neither age nor rank were any protection from indiscriminate slaughter and violation. Aged men and women past their prime, worthless as booty, were dragged about in wanton insult. Did a grown up maiden or youth of marked beauty fall in their way, they were torn in pieces by the violent hands of ravishers; and in the end the destroyers themselves were provoked into mutual slaughter. Men, as they carried off for themselves coin or temple-offerings of massive gold, were cut down by others of superior strength. Some, scorning what met the eye, searched for hidden wealth, and dug up buried treasures, applying the scourge and the torture to the owners. In their hands were flaming torches, which, as soon as they had carried out the spoil, they wantonly hurled into the gutted houses and plundered temples. In an army which included such varieties of language and character, an army comprising Roman citizens, allies, and foreigners, there was every kind of lust, each man had a law of his own, and nothing was forbidden. For four days Cremona satisfied the plunderers. When all things else, sacred and profane, were settling down into the flames, the temple of Mephitis outside the walls alone remained standing, saved by its situation or by divine interposition.[^d3433e3491264951ab51ae691d070d14]

  
## To Cambodunum By Road

Intending to travel by road to Cambodunum, Virgil left Brigantium. It was at least 36 miles. 

Above the roads are ruins, among which is a cave sacred to Asclepius. Next to the straight road that leads to Cambodunum, there is visible a sculpted tomb. There was written there these words: Lagon[- - -]. A caravan from Cambodunum passed by. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There is a fountain of cold water springing from the rock. 

The library at Ticinum happened to have a copy of _Historiae_, where Virgil encountered it.

## The Story Of Ticinum


There were many sanguinary encounters between the soldiers; for ever since the mutiny which broke out at Ticinum there had lingered a spirit of dissension between the legions and the auxiliary troops, though they could unite whenever they had to fight with the rustic population. The most terrible massacre took place at the 7th milestone from Rome. Vitellius was distributing to each soldier provisions ready dressed on the same abundant scale as the gladiators' rations, and the populace had poured forth, and spread themselves throughout the entire camp. Some with the frolicsome humour of slaves robbed the careless soldiers by slily cutting their belts, and then asked them whether they were armed. Unused to insult, the spirit of the soldiers resented the jest. Sword in hand they fell upon the unarmed people. Among the slain was the father of a soldier, who was with his son. He was afterwards recognised, and his murder becoming generally known, they spared the innocent crowd. Yet there was a panic at Rome, as the soldiers pressed on in all directions. It was to the forum that they chiefly directed their steps, anxious to behold the spot where Galba had fallen. Nor were the men themselves a less frightful spectacle, bristling as they were with the skins of wild beasts, and armed with huge lances, while in their strangeness to the place they were embarrassed by the crowds of people, or tumbling down in the slippery streets or from the shock of some casual encounter, they fell to quarrelling, and then had recourse to blows and the use of their swords. Besides, the tribunes and prefects were hurrying to and fro with formidable bodies of armed men.[^f60a6248c51245699e2f012ce022f71c]

  
## After Cambodunum

Leaving Cambodunum, Virgil set out for Abodiacum by road, a journey of about 31 miles. 

A caravan from Abodiacum passed by. The sun beats down. A grove of Minerva is hard by the road, a grove of poplar trees. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Now the road is quieter. He left the city early, before the rising of the sun. 

While he was visiting Mutina, he made a point of copying down what Cicero, Marcus Tullius had written.

## A Story By Cicero, Marcus Tullius About Mutina From _Philippics_


Therefore, this opinion of mine, O Romans, prevailed so much for three days, that although no division was come to, still all, except a very few, appeared inclined to agree with me. But today—I know not, owing to what circumstance—the senate was more indulgent. For the majority decided on our making experiment, by means of ambassadors, how much influence the authority of the senate and your unanimity will have upon Antonius.[^d4c5b2952791418f9682b8eef40086d1]

  
## Abodiacum To Cambodunum By Road

Leaving Abodiacum, Virgil set out for Cambodunum by road, a journey of about 31 miles. 

By the gate of Cambodunum, these words were carved: [Inv]ic[to] / Mi[t]hr[ae] / [F]ructus Q(uinti) / [Sa]bini Verani / [con]d(uctoris) p(ublici) [p(ortorii) ser(vus) vil(icus?) st?]a[t(ionis)?] / [- - - templ(um)? de]di[c]/[avit a]ramq(ue) m[armoream? - - -?]. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A caravan from Cambodunum passed by. The road narrows here, an orchard wall encroaching on it. 

He would later record what Cornelius Tacitus had said about Verona.

## What Cornelius Tacitus Once Said About Verona


Spurinna, on discovering the enemy's route, informed Annius Gallus by letter of the successful defence of Placentia, of what had happened, and of what Cæcina intended to do. Gallus was then bringing up the first legion to the relief of Placentia; he hardly dared trust so few cohorts, fearing that they could not sustain a prolonged siege or the formidable attack of the German army. On hearing that Cæcina had been repulsed, and was making his way to Cremona, though the legion could hardly be restrained, and in its eagerness for action, even went to the length of open mutiny, he halted at Bedriacum. This is a village situated between Verona and Cremona, and has now acquired an ill-omened celebrity by two great days of disaster to Rome. About the same time Martius Macer fought a successful battle not far from Cremona. Martius, who was a man of energy, conveyed his gladiators in boats across the Padus, and suddenly threw them upon the opposite bank. The Vitellianist auxiliaries on the spot were routed; those who made a stand were cut to pieces, the rest directing their flight to Cremona. But the impetuosity of the victors was checked; for it was feared that the enemy might be strengthened by reinforcements, and change the fortune of the day. This policy excited the suspicions of the Othonianists, who put a sinister construction on all the acts of their generals. Vying with each other in an insolence of language proportioned to their cowardice of heart, they assailed with various accusations Annius Gallus, Suetonius Paullinus, and Marius Celsus. The murderers of Galba were the most ardent promoters of mutiny and discord. Frenzied with fear and guilt, they sought to plunge everything into confusion, resorting, now to openly seditious language, now to secret letters to Otho; and he, ever ready to believe the meanest of men and suspicious of the good, irresolute in prosperity, but rising higher under reverses, was in perpetual alarm. The end of it was that he sent for his brother Titianus, and intrusted him with the direction of the campaign.[^4ab38884283243c382cf9dfa23b0cdb7]

  
## Cambodunum To Abodiacum By Road

Virgil departed from Cambodunum, intending to travel by road to Abodiacum, about 31 miles away. 

As they go up from Cambodunum, they see the ruined walls. By the road is a salt spring. A grove of Minerva is hard by the road, a grove of poplar trees. Next to the straight road that leads to Abodiacum, there is visible a sculpted tomb. Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from Abodiacum passed by. 

All of this brought to his mind what E. T. Merrill had said about Verona:

## On Verona, According To E. T. Merrill


Egnatius, who was singled out for especial attack in Catul. 37.17ff., is again satirized in the vein there indicated. Cf. also Martial's satire on the continual grin of Canius Rufus (Catul. 111.20). The poem was doubtless written at about the same time as 37, and the meters are identical.

candidos habet dentes: cf. Catul. 37.19ff.

rei subsellium: the defendant's bench; cf. Cael. ap. Cic. Fam. 8.8.1 invocatus ad subsellia rei occurro. Egnatius was one of the friends gathered (_advocati_) to lend the defendant their support at the trial, and ought to have assumed the expression of countenance that would have accorded with the pathetic character of the counsel's speech and have aided in influencing the judges,—but he grins.

lugetur: he is one of the friends attending the funeral, and should of all men show in his face his sympathy with the bereaved mother,—but he only grins.

quidquid est: whatever is going on.

morbum: cf. Catul. 76.25; Sen. Clem. 2.6.4 morbum esse, non hilaritatem, semper adridere ridentibus et ad omnium oscitationem ipsum quoque os diducere.

neque elegantem: etc. i.e. it isn't a nice habit at all.

monendum est te: this impersonal construction of the neuter gerundive of a transitive verb with a direct object occurs only once in comedy ( Pl. Trin. 869 mi agitandumst vigilias ), but is fairly common in Lucretius and Varro, though nowhere found in Caesar. It rarely occurs in Cicero and in the Augustan and later writers.

bone: this vocative is generally used ironically, in more or less mild disparagement; cf. Ter. Andr. 616 eho dum bone vir, quid ais? viden me consiliis tuis miserum impeditum esse? So also Plato's \rendergreek{ὦ 'γαθέ}.

The meaning is: if you were, not to say a native of Rome, but even anything else than what you are, your grinning would be more decent, though yet objectionable enough; but from a Spaniard it is utterly nauseating. The instances cited are not chosen because of any especial qualities, but as types of Italian provincials from near and far, and the descriptive adjectives are therefore but formal epithets.

parcus: frugal.

obesus: the monuments of the Etruscans show them to have been a short and thick-set people.

ater: dark-complexioned; cf. Catul. 93.2.

dentatus: i.e. having fine teeth; cf. Mart. 1.72.3 dentata sibi videtur Aegle emptis ossibus Indicoque cornu.

meos: my countrymen, as Verona was a Transpadane town.

puriter: an antique word, used also in Catul. 76.19; cf. such forms as Catul. 63.49 miseriter .

inepto ineptior: on the collocation cf. Catul. 22.14

vester: i.e. the teeth of Egnatius as representative of those of his countrymen.

dens: collective, as in Catul. 37.20.[^e018939863a5435d962b62f0eb1a8770]

  
## To Parthanum

From Abodiacum to Parthanum is a journey of about 40 miles when travelling by road. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. By the road is a salt spring. The sun beats down. A grove of Minerva is hard by the road, a grove of poplar trees. There a spring wells up, and around about it is a meadow. As they go up from Abodiacum, they see the ruined walls. Mercurio / cuius sedes a tergo / sunt / Appius Cl(audius) Lateranus / XVvir sacr(is) fac(iundis) / co(n)s(ul) design(atus) / leg(atus) Aug(usti) pr(o) pr(aetore) / leg(ionis) III Ital(icae) / v(otum) s(olvit) l(ibens) m(erito) was carved into the stone. The road narrows here, an orchard wall encroaching on it. On the road from Abodiacum to Parthanum there is a village, in which there is a temple and grove. 

All of this brought to his mind what Cornelius Tacitus had said about Aquileia:

## A Story About Aquileia


Meanwhile the operations of Vespasian were hastened by the zeal of the army of Illyricum, which had come over to his side. The third legion set the example to the other legions of Mœsia. These were the eighth and seventh (Claudius's), who were possessed with a strong liking for Otho, though they had not been present at the battle of Bedriacum. They had advanced to Aquileia, and by roughly repulsing the messengers who brought the tidings of Otho's defeat, by tearing the colours which displayed the name of Vitellius, by finally seizing on the military chest and dividing it among themselves, had assumed a hostile attitude. Then they began to fear; fear suggested a new thought, that acts might be made a merit of with Vespasian, which would have to be excused to Vitellius. Accordingly, the three legions of Mœsia sought by letter to win over the army of Pannonia, and prepared to use force if they refused. During this commotion, Aponius Saturnius, governor of Mœsia, ventured on a most atrocious act. He despatched a centurion to murder Tettius Julianus, the legate of the 7th legion, to gratify a private pique, which he concealed beneath the appearance of party zeal. Julianus, having discovered his danger, and procured some guides, who were acquainted with the country, fled through the pathless wastes of Mœsia beyond Mount Hamus, nor did he afterwards take any part in the civil war. He set out to join Vespasian, but contrived to protract his journey by various pretexts, lingering or hastening on his way, according to the intelligence he received.[^6765d0d24b9e45f38269ca2f0824d74e]

  
## To Veldidena

Virgil departed from Parthanum, intending to travel by road to Veldidena, about 32 miles away. 

There a spring wells up, and around about it is a meadow. Next to the straight road that leads to Veldidena, there is visible a sculpted tomb. On the road from Parthanum to Veldidena there is a village, in which there is a temple and grove. Now the road is quieter. His shoes are covered in dust from the road. The sun beats down. Workers are raising the level of the road. The road narrows here, an orchard wall encroaching on it. Water has washed out the road, making for slow going. 

He would later record what E. T. Merrill had said about the countryside near that place.

## An Extract From _Commentary On Catullus_ By E. T. Merrill


This poem, often called in the later MSS. and earlier editions the Epithalamium of Peleus and Thetis, is rather a brief epic, or epyllion, after the Alexandrian style, having for its basis the wedding of Peleus and Thetis, and for one of its divisions the marriage-song of the Parcae. But into this epyllion is wrought another which details the story of Theseus and Anadne under the guise of describing the embroidered drapery of the marriage-couch of Thetis. This second epyllion is even longer than the first, covering vv. 50-266, while the entire poem contains but 408 verses.—The date of composition is uncertain, though the finish of thought and expression seem to point to maturity of development on the part of the author.—Meter, dactylic hexameter.

Introductory, explaining the circumstances that led to the marriage of Peleus and Thetis.

Peliaco: cf. the imitation of this proem by Ov. Am. 2.11.1 prima malas docuit, mirantibus aequoris undis, Peliaco pinus vertice caesa vias ; Prop. 4.22.11 tuque tuo Colchum propellas remige Phasin, Peliacaeque trabis totum iter ipse legas .

prognatae: cf. the similar figure in Hor. Carm. 1.14.12 [pinus] silvae filia nobilis.

dicuntur: the poet makes it clear that he is repeating an ancient tradition; cf. vv. 19 _fertur_, 76 and 124 _perhibent_, 212 _ferunt_.

liquidas: not an otiose epithet, but indicating the unstable water as unfitted to support a heavy body; cf. Verg. A. 5.859 liquidas proiecit in undas praecipitem ; Nemes. Buc. 2.76 nec tremulum liquidis lumen splenderet in undis.

nasse: cf. Catul. 4.3 natantis trabis ; Catul. 66.45 iuventus per medium navit Athon .

Phasidos: the chief river of Colchis, rising in the Caucasus and flowing into the Euxine Sea at its eastern end.

Aceteos: Gr. \rendergreek{Αἰητείους}: Aeetes was king of Colchis and father of Medea.

lecti iuuenes: so the Argonauts are called by Ennius Med. Exsul 209 R. Argivi delecti viri ) and Verg. Ecl. 4.34 altera quae vehat Argo delectos heroas ); cf. also Theocr. 13.18 πασᾶν ἐκ πολίων προλελεγμένοι (of the Argonauts).

auratam pellem: for the story of the Argonautic expedition see Hom. Od. 12.69; Hes. Theog. 992; Apollod. 1.9.16ff; and the poems by Pind. Pyth. 4.1ff., Apollonius, and Valerius Flaccus.

avertere: to win; especially used of plunder; cf. Caes. BC 3.59.4 praedam omnem domum avertebant ; Cic. Verr. 2.69.163 innumerabilem frumenti numerum aversum ab re publica esse ; Verg. A. 8.207 quattuor a stabulis tauros avertit .

vada salsa: cf. Verg. A. 5.158 longa sulcant vada salsa carina.

cito decurrere puppi: cf. Ov. Fast. 6.777 celeri decurrite cumba .

caerula verrentes aequora: cf. Verg. A. 3.208 adnixi torquent spumas et caerula verrunt .

palmis: cf. Catul. 4.4n._palmulis_.

diva retinens: etc. i.e. Athena Polias; cf. Verg. Ecl. 2.61 Pallas quas condidit arces ipsa colat .

quibus: referring to v. 4 _lecti iuvenes_.

summis: with the partitive force.

ipsa fecit: Catullus here follows the tradition of Apollonius 1.111, with which cf. Phaedr. 4.7.9 fabricasset Argus opere Palladio ratem ; Sen. Med. 368 non Palladia compacta manu Argo ; Val. Flac. 1.94.

currum: the newly invented vehicle for the sea is described by its similarity to those in use on land; cf. Cic. ND 2.35.89 divinum et novum vehiculum Argonautarum ; and v. 6 _decurrere_.

cursu imbuit: cf. Val. Flac. 1.69 ignaras Cereris qui vomere terras imbuit ; Sil. Ital. 3.64 iuvenem primo Hymenaeo imbuerat coniunx .

Amphitriten: i.e. the sea, as in Ov. Met. 1.14 bracchia porrexerat Amphitrite . For the descent of the goddess see v. 29 n. _Tethys_.

ventosum aequor: cf. Verg. A. 6.335 a Troia ventosa per aequora vectos ; Ov. Her. 16.5 ventosa per aequora vectum .

torta: cf.Verg. A. 3.208, cited on v. 7.

incanduit unda: cf. Ov. Met. 4.530 percussa recanduit unda ; and with _incanduit_ in this sense Plin. Pan. 30 pars magna terrarum alto pulvere incanduit .

With the general picture cf. Sil. Ital. 7.412ff. ac totus multo spumabat remige pontus, cum trepidae fremitu vitreis e sedibus antri aequoreae pelago simul emersere sorores .

freti: the MS. _feri_ hardly describes the beautiful faces and forms of Thetis and her companions, being usually joined with such adjectives as _immanis, inhumanus, immansuetum_; but on _freti_ cf. Oct. 720 talis emersam freto spumante Peleus coniugem accepit Thetim .

candenti e gurgite: cf. v. 13 _incanduit unda_; v. 18 _e gurgite cano_; Lucr. 2.767 [mare] vertitur in canos candenti marmore fluctus ; Sil. Ital. 14.362 spumat canenti sulcatus gurgite limes .

monstrum admirantes: cf. the wonder expressed by the shepherd at the sight of the Argo in Accius ap. Cic. ND 2.35.89.

Nereides: sea-nymphs, daughters of Nereus and Doris; cf. v. 29 n _Tethys_.

oculis: emphasizing the reality of the wonderful sight; cf. Ter. Eun. 677 hunc oculis suis nostrarum nunquam quisquam vidit .

nutricum: the word occurs only here in the sense of _papillarum_.

tenus: with the genitive, as in Cic. Arat. 83 lumborum tenus , Verg. G. 3.53 crurum tenus .

gurgite cano: cf. v. 14 n.; Ciris 514 cano degurgite .

tum: Catullus represents this as the first meeting of Peleus and Thetis; but, according to Apollonius 1.558, Peleus, though an Argonaut, was long since married; while Val. Flacc. 1.130 represents the wedding of Peleus and Thetis as pictured among the adornments of the Argo itself, and Achilles as brought by Chiron to bid his father good-by before the sailing (Val. Flacc. 1.255).

fertur: cf. v. 2 n. _dicuntur_.

hymenaeos: plural, as in v. 141; but singular with the same meaning in Catul. 66.2. On the lengthening of the preceding short syllable see Intr. 86g.

pater ipse: i.e. Zeus, who had himself intended to wed Thetis; but being warned by the Fates (or, according to other stories by Themis, or by Prometheus) that the son of Thetis would be greater than his father, he gave up his purpose, and furthermore, fearing that his own throne might be endangered by the existence of a rival, declared that Thetis should wed no immortal; cf. Aesch. PV 167ff., Aesch. PV 907 ff.; Ov. Met. 11.221 ff.

nimis optato: cf. Catul. 43.4n. _nimis_, and with the general sentiment of the verse, Verg. A. 6.649 magnanimi heroes, nati melioribus annis.

salvete … salvete iterum: cf. Verg. A. 5.80 salve, sancte parens; iterum salvete , etc.

matrum: either there is hypallage of the adjective, or _bonarum_ must be supplied in the lacuna, as Peerlkamp suggested. With the idea cf. Catul. 61.226ff.

Cf. Crit. App.

Cf. Theocr. 1.144 ὦ χαίρετε πολλάκι Μοῖσαι, χαίρετ᾽: ἐγω δ᾽ ὕμμιν και ἐς ὕστερον ἅδιον ᾀσῶ .

taedis aucte: cf. Catul. 66.11 auctus hymenaeo .

Thessaliae columen: cf. Ter. Phor. 287 columen familiae ; Hor. Carm. 2.17.3 mearum columen rerum ; Sen. Troad. 128 columen patriae ; Hom. Il. _e)/rkos *)axaiw=n_.

amores: not of Thetis herself (cf. Catul. 6.16n.), but of the passion of Zeus for her,—'in whose favor the father of the gods himself resigned his passion.' With the plural cf. Catul. 38.6; Catul. 64.334, Catul. 64.372; Catul. 68.69; Catul. 96.3; Pl. Merc. 2 et argumentum et meos amores eloquar ; Hor. Carm. 2.9.10 nec tibi Vespero surgente decedunt amores ; Verg. Ecl. 9.56 nostros in longum ducis amores.

tenuit: sc. _complexu_; cf. Catul. 72.2; but otherwise in Catul. 11.18; Catul. 55.17.

Nereine: Gr. \rendergreek{Νηρηΐνη}; but elsewhere the Latins use either _Nereis_ (cf. v. 15) or _Nerine_ (cf. Verg. Ecl. 7.37 Nerine Galatea ).

Tethys: the daughter of Uranus and Ge, and the wife of her own brother Oceanus, by whom she became the mother of the sea-nymphs called Oceanides, of the rivers of earth, and of Nereus. From the marriage of Nereus with his sister Doris, one of the Oceanides, sprang the sea-nymphs called Nereides, of whom the most famous were Thetis, Amphitrite, the wife of Poseidon, and Galatea, the beloved of Polyphemus.

totum amplectitur orbem: cf. Hom. Il. 18.399 ἀψοπ̓π̓όου Ὠκεανοῖο ; Aesch. Prom. 138 τοῦ περι πᾶσάν θ᾽ εἱλισσομένου χθόν᾽ ἀκοιμήτῳ ῥεύματι … πατρο , Ὠκεανοῦ ; Val. Flac. 1.195 terras salo complecteris omnes ; Tib. 4.1.147 Oceanus ponto qua continet orbem ; Bryant, Thanatopsis 42 "and, poured round all, Old Ocean's gray and melancholy waste."

The introductory narrative finished, the poet turns to the main theme, and describes first the gathering of the mortal wedding-guests.

quae luces: with a general reference to the fixing of the wedding-day in v. 29.

simul: sc. _atque_; cf. Catul. 22.15n.

optatae: cf. with the thought, Catul. 62.30; Catul. 66.79.

domum: sc. of Peleus.

dona: wedding-gifts, not propiatory offerings to a superior.

prae se: thus commonly of things carried in the hands; cf. Verg. A. 11.249 munera praeferimus .

Cieros: otherwise Cierium, a town of Thessaliotis, according to Strabo 435.

Phthiotica Tempe: with a poet's license concerning geography, Catullus calls the famous vale of Tempe through which the Peneus flows (cf. v. 285) Phthiotic, as synonymous with Thessalian in general, though in strictness the district of Phthiotis was the southernmost of the divisions of Thessaly, extending not so far north even as Pharsalus.

Crannon and Larisa were both towns of Pelasgiotis near the Peneus.

Pharsalum coeunt: the commoner form of the legend made Mt. Pelion the place of the wedding, and Chiron the host.

mollescunt colla invencis: since they no longer bore the yoke; in this expression, as in the following verses, the absolute desertion of the farm is pictured by representing it as if it had lasted a long time.

Cf. Verg. Ecl. 4.40f. non rastros patietur humus, non vinea falcem; robustus quoque iam tauris iuga solvet arator .

humilis vinea: here, as, according to Varro RR 1.8, in Spain and some parts of Asia, the vines were not trained on trees, but either ran along the ground or were so cut as to be kept low. The latter plan is followed to-day in the great vineyards of California, and to some extent in Italy itself.

curvis: perhaps referring to the crescent-shaped iron, the two points of which form the teeth of the rastrum pictured in Rich's Dict. Ant. s.v.

rastris: the _rastrum_ was a heavy sort of rake of from two to four strong iron teeth, used to break up clods and to loosen the surface of the ground.

prono: of the point of the share down-pressed, that it may cut a deep furrow; cf. Verg. G. 1.45 depresso aratro ; Verg. Georg. 2.203 presso sub vomere .

attenuat arboris umbram: that the sun may reach and ripen the grapes. Attempts have been made by various critics to rearrange vv. 38-42 so as to produce a more consistent picture by bringing together details that concern the same objects; but there seems to be no good reason for criticising the alternation of the description between the tasks which men performed alone and those in which cattle shared (after the general statement made in v. 38 that men and beasts ceased from toil).

The adornment of the palace of Peleus.

ipsius: i.e. Peleus; such a remote reference of _ipse_, so that it is equivalent to some such word as _dominus_, is not uncommon; cf. Catul. 114.6; Ter. Andr. 360 paululum obsoni; ipsus tristis ; Verg. Ecl. 3.3 ipse Neaeram dum fovet ; Juv. 1.61 lora tenebat ipse .

opulenta recessit regia: the guest standing at the door looks through an imposing vista of room succeeding room; cf. on the word Verg. A. 2.300 Anchisae domus arboribus obtecta recessit ; Plin. Ep. 2.17.21 contra parietem medium zotheca recedit ; and with the idea, the description of the first series of rooms in Pliny's villa (Ep. 2.17.5).

Cf. Vergil's description of Dido's palace in Verg. A. 1.637ff.

candet ebur sollis: the couches arranged about the tables have ivory legs; cf. v. 303 and 61.115; like _mensae, solus_ is a dative.

gaudet: i.e. wears a festive appearance, as Sirmio was to do at the master's return (Catul. 31.12); cf. Hor. Carm. 4.11.6 ridet argento domus .

pulvinar geniale: for _lectus genialis_, as a more formal and imposing term, and one especially connected with divinity.

sedibus in mediis: the poet is apparently thinking of a Roman house, where the _lectus genialis_ stood in the _atrium_.

Indo dente politum: = _ebore polito_; cf. Ov. Met. 8.288 dentes [apri] aequantur dentibus Indis .

Observe the favorite contrast of color between the ivory of the couch and its crimson drapery; cf. Hor. S. 2.6.102 rubro ubi cocco tincta super lectos canderet vestis eburnos .

With this verse begins the episode of Ariadne's Lament, which extends through v. 266, thus forming more than half of the entire poem, and setting in striking contrast the unhappy love of Ariadne with the happy love of Thetis. Episodic digressions of a similar character, depicting actions represented in graving or embroidery, are as old as the description of the shield of Achilles (Hom. Il. 18.478ff.), and are multiplied in later writers. With the episode of Catullus may be compared the story of Ariadne as told by Ov. AA 1.527ff.; Ov. Her. 10.

fluentisono: \rendergreek{ἅπαξ λεγόμενον}, though _fluctisonus_ and _undisonus_ are found in post-Augustan poets. The word has reference to the crash of breakers upon a rock-bound coast, perhaps here to point the impossibility of escape; v. 121 _spumosa ad litora Diae_ and the more neutral epithet used by Hom. Od. 11.325 Δίῃ ἐν ἀμφιρύτῃ .

Diae: asserted by several of the Greeks to be but an earlier name for Naxos. But Hom. Od. 11.321ff.) very probably thought of the island of Dia that lies very near the north coast of Crete, whence the tradition may have been transferred to Naxos, the favorite haunt of Dionysus, as the later story of Ariadne's rescue by Dionysus gained ground. Catullus certainly must have followed the later tradition, if he had any definite tradition in mind.

A favorite subject in the Pompeian frescoes is Ariadne awaking from sleep and gazing after the departing ship of Theseus; cf. Roux, Herc. et Pompeii, passim.

classe: cf. v. 212 n.

indomitos furores: of uncontrollable love; cf. Catul. 50.11; Catul. 64.94; Catul. 68.129.

Cf. Ov. Her. 10.31 aut vidi, aut tanquam quae me vidisse putarem .

faliaci: sleep is traitorous since he made the secret flight of Theseus possible; cf. Ov. Her. 10.5 in quo me somnusque meus male prodidit et tu.

desertam, miseram: with this use of the adjective _miser_, instead of the adverb, with another adjective, cf. Catul. 65.21 miserae oblitae .

immemor: used absolutely and with similar meaning in Catul. 30.1.

cf. Catul. 30.10n.

ex alga: i.e. from the beach; v. 168; Mart. 10.16.5 quidquid Erythraea niger invenit Indus in alga .

The figure is that of a Bacchante speechless, motionless, and utterly forgetful of her own appearance through the very exaltation of her wild emotions; cf. Hor. Carm. 3.25.8 non secus in iugis Edonis stupet Euhias Hebrum prospiciens ; _Ovid Her. 10.49_ _mare prospiciens in saxo frigida sedi, quamque lapis sedes, tam lapis spsa fui_.

prospicit, eheu, prospicit: she stands absorbed in long-continued, but alas, fruitless gazing.

curarum: cf. Catul. 2.10n.

undis: with the figure cf. Lucr. 3.298 irarum fluctus ; Lucr. 6.34 volvere curarum tristis in pectare fluctus ; Verg. A. 4.532 saevit amor, magnoque irarum fluctuat aestu ; Verg. A. 8.19 magno curarum fluctuat aestu .

flavo: etc. cf. the apparent reminiscence in Ciris 511 purpureas flavo retinentem vertice vittas . Fair hair is traditionally a mark of beauty in the poets.

subtilem mitram: the finely-woven, variegated coif worn by Greek women, as by Orientals in general. In Greece it seems to have consisted of a sort of scarf arranged either as headdress or as girdle.

non contecta: etc. her breast unshielded by its veil of light drapery. With the reinforcement of the idea by the introduction of _velatum_ cf. v. 103 _ingrata … frustra_ (but see Crit. App.).

levi amictu: doubtless the _chiton_; cf. Ov. AA 1.529 ut erat e somno tunica velata recincta, nuda pedem, croceas inreligata comas .

strophio: a girdle woven or wound like a cord (cf. _tereti_, and the mother's dress in the well-known Herculanean Toilet of the Bride), and worn by women over the inner tunic just below the breasts, to which it was apparently designed to furnish support.

lactentis: not of the color, but of the full development, of the breasts in the mature woman; cf. Verg. G. 1.315 frumenta in viridi stipula lactentia turgent ; Ov. Fast. 1.351 sata vere novo teneris lactentia sucis ; and especially Petron. 86 implevi lactentibus papillis manus .

adludebant: with the figure cf. Cic. ND 2.39.100 ipsum mare terram appetens litoribus adludit ; Top. 7.32 solebat Aquilius quaerentibus iis quid esset litus ita definire, qua fluctus eluderet .

toto pectore, toto animo, tota mente: cf. Vulg. Luc. 10.27 diliges dominum deum tuum ex toto corde tuo, et ex tota anima tua … et ex omni mente tua.

exsternavit: apparently the first appearance of this rare word; cf. also only v. 165; Ov. Met. 1.641; Ov. Met. 11.77; and much later Latin.

Erycina: Venus was so called by the Romans from her ancient and famous shrine on Mt. Eryx in western Sicily.

illa tempestate quo ex tempore: a variation of the ordinary prose pleonasm _illo die quo die_. For one simple ablative repeated by another with ex cf. Catul. 35.13 quo tempore … ex eo , where, as here, the starting-point of a continued effect is indicated.

ferox: used absolutely, as in v. 247.

curvis litoribus: embracing the harbor.

iniusti: so called of course from the Athenian standpoint, since he required such a heavy penalty for the death of one man, his son; but cf. Ov. Her. 10.69 pater et tellus iusto regnata parenti , and the references to Minos as appointed because of his justice to judge souls in the lower world, cf. Hom. Od. 11.568 ἔνθ᾽ ἦ τοι Μίνωα ἴδον, Διο ἀγλαὸν υἱόν, χρύσεον σκῆπτρον ἔχοντα, θεμιστεύοντα νέκυσσιν ; Hor. C. 4.7.21 cum semel occideris et de splendida Minos fecerit arbitria .

Gortynia: probably simply 'Cretan'; cf. v. 172 _Gnosia litora_.

nam perhibent: the poet drops the thread of his story for a moment to relate the circumstances that led to the present condition of Ariadne; cf. v. 2 n. _dicuntur_.

Androgeoneae caedis: Androgeos, son of Minos and Pasiphae, conquered all his competitors at wrestling in Athens, and was through jealousy assassinated while on his way to the games at Thebes. According to another story, King Aegeus himself caused his death by sending him against the fire-breathing Marathonian bull. Minos thereupon besieged the Athenians, who were compelled to yield to him by a pestilence sent by the gods, and to accept his hard conditions of peace.

electos: cf. v. 4 _lecti iuvenes_. The number is commonly given as seven of each sex (as also, perhaps, in Verg. A. 6.20ff.).

innuptarum: for _virginum_, as in Catul. 62.6.

Cecropiam: traditionally the ancient name of the city of King Cecrops, which was called Athenae after the goddess Athena became recognized as its patron.

angusta: of the small size of the young city, and not of the straitening by the hardships of siege.

funera nec funera: with the oxymoron cf. Catul. 112.1 multus neque multus (where, however, there is an \rendergreek{ἀμφιβολία}); Cic. Phil. 1.2.5 insepultam sepulturam ; Ov. AA 2.93 pater nec iam pater (repeated in Ov. Met. 8.231); and especially such favorite Greek expressions as \rendergreek{πόλεμος ἀπόλεμος, τάφος ἄταφος}, etc. The reference is doubtless to the life-in-death of the victims on their way to Crete, who were mourned as dead from the moment of their sailing.

atque ita: i.e. with the purpose mentioned in the preceding verses; cf. v. 315 atque ita .

nauve levi et lenibus auris: the happy indications of a swift and prosperous voyage are contrasted with the shrinking horror and dread in the hearts of the passengers.

nitens: pressing forward.

magnanimum: the Homeric \rendergreek{μεγάθυμος}.

sedes superbas: the abode of tyranny; with reference to v. 75 _iniusti regis_.

This account of the sudden love of Ariadne for Theseus closely' resembles that given by Apollonius 3.275ff. in describing Medea's love for Jason.

virgo regia: i.e. Ariadne; cf. Ov. Met. 11.570 fueramque ego regia virgo .

suavis exspirans odores lectulus: cf. Ciris 3 suaves exspirans hortulus auras . The idea seems to have been suggested by the Homeric phrase \rendergreek{θάλαμος θυώδης} (e.g. Od. 4.121).

in molli complexu matris: cf. Catul. 61.58; Catul. 62.21.

quales: etc. cf. Catul. 61.22n.

aura educit: cf. v. 282; Catul. 62.41n.

colores: by metonymy for _flores_; cf. Val. Flac. Arg. 6.492 lilia per varios lucent velut alba colores .

non prius, etc.: cf. Catul. 51.6 (and note), and contrast the idea with the more complex treatment of Medea's first passion in Ov. Met. 7.86ff.

cuncto: etc. cf., however, the commoner phrase in Verg. A. 7.356 necdum animus toto percepit pectore flammam ; Ov. Met. 7.17 excute virgineo conceptas pectore flammas ; Petron. 127 Iuppiter et toto concepit pectore flammas . On the figure see Catul. 2.8n.

imis medullis: cf. Catul. 35.15n.

sancte: a general epithet of divinity; cf. Catul. 36.3n.; Tib. 2.1.81 sancte [Amor], veni dapibus festis, sed pone sagittas .

curis: etc. cf. the similar phrase concerning Venus in Catul. 68.18 quae dulcem curis miscet amaritiem.

cf. Catul. 36.12ff.

flavo hospite: cf. v. 63 n.

quanto magis expalluit: with the construction cf. Cic. Acad.1.3.10 quanto magis philosophi delectabunt ; with the figure, Catul. 81.4. Dark-complexioned people, as the people of southern Europe usually are, turn yellow lather than white when pale.

ingrata, frustra: with the pleonasm cf. v. 64 _contecta, velatum_; with _ingrata_ in this passive sense, 'without due return,' cf. Catul. 73.3; Catul. 76.6; but in the active sense, 'ungrateful,' Catul. 76.9.

tacito succendit vota labello: the beautiful figure of the incense of prayer is unique in Latin in this pure form, but is so simple that its authenticity is above reasonable suspicion. The connection of prayers with incense-offering is not infrequently noted; cf. Stat. Theb. 11.236 vota incepta tamen libataque tura ferebat . Ariadne's prayer was offered silently, as became her maidenly feeling, and the necessary concealment of her love from her friends.

velut: etc. with the figure cf. Verg. A. 2.626ff.; Hor. Carm. 4.6.9ff.; and often.

saevum: apparently used here, though perhaps here only, as a substantive, indicating the distinctive characteristic of this monster, as _ferus_, so often used substantively, (e.g. Catul. 63.85), characterizes ordinary wild beasts.

nequiquam: etc. cf. Cic. Att. 8.5.1 πολλὰ μάτην κεράεσσιν ἐς ἠέρα θυμήναντα ; cf. also Verg. A. 12.105 [taurus] ventos lacessit ictibus.

vanis: unsubstantial, offering no resistance; cf. Val. Flac. 1.421 saltem in vacuos ut bracchia ventos spargat ; but Shelley, Medusa of Da Vinci 23 to saw The solid air with many a ragged jaw.

pedem reflexit: perhaps the verb is selected because it suggests the turnings (v. 114) of the labyrinth.

multa cum laude: cf. Hor. Carm. 4.4.66 multa proruit integrum cum laude victorem .

Cf. of the same incident Verg. A. 6.30 caeca regens filo vestigia ; Prop. 3.14.8 Daedalium lino cum duce rexit iter ; Ov. Her. 10.103 nec tibi quae reditus monstrarent fila dedissem.

labyrintheis: \rendergreek{ἅπαξ λεγόμενον}.

inobservabilis error: cf. Verg. A. 5.501 irremeabilis error ; Verg. A. 6.27 inextricabilis error (of the Labyrinth); Apoll. Sid. Ep. 2.5 inextricabilem labyrinthum negotii multiplicis ; Plin. NH 36.85 itinerum ambages occursusque ac recursus inexplicabiles continet ; Ov. Met. 8.160 turbatque notas, et lumina flexum ducit in errorem variarum ambage viarum ; Shelley, Medusa of Da Vinci 35 "that inextricable error."

consanguineae: for _sororis_. Apollod. 3.1.2 speaks of three other daughters of Minos besides Ariadne, Acale, Xenodice, and Phaedra, of whom Catullus probably had in mind Phaedra, who is the most prominent of them in mythology, and was later the wife of Theseus himself.

misera: contrasting the present wretched condition of Ariadne, betrayed by a false love, with the affection formerly lavished upon her by her family.

deperdita: of the limitless love of the mother, rather than of her present unhappiness; cf. Catul. 45.3; Catul. 104.3.

Thesci: dissyllabic, like v. 382 _Pelei_, and Culex 278 Orphei (cited on v. 139).

praeoptarit: with the synizesis cf. Pl. Trin. 648 praeóptavisti amórem tuom uti virtuti praepóneres ; Ter. Hec. 532 ádeon pervicáci esse animo ut púerum praeoptarés perire .

spumosa litora Diae: cf. v. 52 n.

devinctam lumina somno: cf. Ciris 206 iamque adeo dulci devinctus lumina somno Nisus erat .

perhibent: cf. v. 2 n. _dicuntur_.

ardenti corde: cf. v. 197 _ardens_.

clarisonas: a rare word, occurring only here (of the shrill cries of anguish), in v. 320 (of the shrill voice of age), and in Cic. Arat. 280 a clarisonis auris Aquitenis (of the shrilling blast).

imo ex pectore: i.e. after a long-drawn, sighing inspiration; cf. Verg. A. 1.371 suspirans imoque trahens a pectore vocem .

Cf. Ov. Her. 10.25ff.

tremuli: rippling; cf. Ov. Her. 11.75 ut mare fit tremulum, tenui cum stringitur aura.

procurrere: with the vain impulse to follow the fleeing vessel.

mollia: soft; cf. Catul. 65.21 molli sub veste .

nudatae: proleptic.

extremis: for her grief so far overcomes her that she supposes herself to be dying; cf. Prop. 4.7.55 flens tamen extremis dedit haec mandata querelis .

frigidulos singultus: carrying on the idea of _extremis_, indicating the last panting breaths as chill death creeps on; cf. Ciris 347 super morientis alumnae frigidulos ocellos .

With the complaint of Ariadne cf. similar passages in Verg. A. 4.590ff. (the complaint of Dido); Ov. Met. 8.108ff. (of Scylla).

patrus ab aris: = _a domo_; cf. Verg. A. 11.269 patriis redditus aris , and often; Charis. 33 K. arae pro penatibus .

neglecto numine divum: the gods punish infidelity of all sorts; cf. Catul. 30.3f.

devota: i.e. under the ban of Ariadne's curse; cf. v. 192ff.

blanda voce: after the wont of persuasive lovers; cf. Enn. Ann. 51 blanda voce vocabam ; Culex 278 turba ferarum blanda voce sequax regionem insederat Orphei ; Ov. AA 1.703 quid blanda voce moraris? Ov. AA 3.795 nec blandae voces cessent .

miserae: the dative with _dedisti_ seems to be continued into the _iubebas_-clause, though a simple infinitive and dative is a rare construction with that verb.

sed: etc. cf. the close verbal and metrical resemblance of Verg. A. 4.316 per conubia nostra, per inceptos hymenaeos . The repetition of _sed_ corresponds to that of _non haec_ in v. 139f.

conubia: plural with singular meaning, as in v. 158; but singnlar in Catul. 62.57.

hymenaeos: cf. v. 20 n.

venti: etc. cf. Catul. 30.10n.

nunc: etc. cf. Ov. Fast. 3.475 nunc quoque 'nulla viro' clamabo 'femina credat' (spoken by Ariadne with reference to the infidelity of Bacchus).

praegestit: the word apparently occurs only here, in Cic. Cael. 67 praegestit animus iam videre , and in Hor. Carm. 2.5.9 iuvencae ludere cum vitulis praegestientis .

turbine leti: cf. Val. Flac. 6.179 doloris turbine .

germanum: i.e. the Minotaur; cf. v. 181; Ov. Her. 10.115 dextera crudelis quae me fratremque necavit .

crevi: archaic for _decrevi_; cf. Lucil. 13.1 acribus inter se cum armis confligere cernit ; Pl. Cist. 1 mihi amicam esse crevi matrem tuam .

supremo in tempore: i.e. in extreme danger of life; cf. v. 169 _extremo tempore_; Hor. Carm. 2.7.1 tempus in ultimum .

dilaceranda: etc. cf. Hom. Il. 1.4 αὐτοὺς δὲ ἑλώρια τεῦχε κύνεσσιν οἰωνοῖσί τε πᾶσι ; Verg. A. 9.485 canibus data praeda Latinis alitibusque iaces ; Ov. Her. 10.96 destituor rapidis praeda cibusque feris .

iniecta … terra: the passage of the soul across the Styx was secured only by due burial under at least three handfuls of earth; cf. Hor. Carm. 1.28.36 licebit iniecto ter pulvere curras .

Cf. c. 60.

mare: etc. cf. Hom. Il. 16.34 γλαυκὴ δέ σε τίκτε θάλασσα πέτραι τ᾽ ἠλίβατοι, ὅτι τοι νόος ἐστὶν ἀπηνής .

Scylla rapax: cf. Ap. Sid. C. 9.165 Scyllae rabidum voracis inguen .

dulci vita: cf. Hom. Od. 5.152 γλυκὺς αἰών

tibi cordi conubia: cf. Catul. 44.3; cf. Catul. 81.5; Catul. 95.9; Ter. Andr. 328 tibi nuptiae haec sunt cordi .

prisci: stern, as the older days were proverbially the stricter; cf. Hor. Carm. 3.21.11 narratur et prisci Catonis saepe mero caluisse virtus .

parentis: of course Aegeus, and not Minos, is meant, and the commands that would shut Ariadne, the rescuer of his son, out of his home she justly calls _saeva_; cf. Hyg. Fab. 43 Theseus in insula Dia cogitans, si Ariadnen in patriam portasset, sibi opprobrium futurum , etc.

vestras: i.e. of Theseus and his family; cf. v. 176 _nostris_.

serva: etc: cf. Shakespeare, Tempest 3.1 to be your fellow You may deny me; but I'll be your servant, Whether you will or no.

permulcens: etc. a common duty of female slaves, and Ariadne would especially delight in performing personal service for her hero; cf. Hom. Od. 19.386 ὣς ἄρ᾽ ἔφη, γρηῢς δὲ λέβηθ᾽ ἕλε παμφανόωντα τοῦ πόδας ἐξαπένιζεν , etc.

vestigia: for _pedes_, an extremely rare use; but cf. Sen. Thy. 1043 _rupta fractis cruribus vestigia_; Sen. Oed. 833 forata ferro vestigia .

sed quid: etc. with the rhetorical question in self-address cf. v. 116ff.

exsternata: cf. v. 71 n. _exsternavit_.

auctae: endowed; cf. Lucr. 3.628 animas sensibus auctas .

alga: cf. v. 60 n.

extremo tempore: _at my last hour_; cf. v. 151 n.

Gnosia: doubtless simply 'Cretan'; cf. v. 75 _Gortynia tecta_.

tauro: so the Minotaur is called also in v. 230.

religasset funem: of mooring to the shore; cf. Verg. A. 7.106 gramineo ripae religavit ab aggere classem ; Luc. Phar. 7.860 nullus ab Emathio religasset litore funem navita .

malus hic: cf. Catul. 29.21n.

Cf. Eur. Med. 502ff.; Ov. Met. 8.113ff. nam quo deserta revertar? in patriam? deserta iacet … patris ad ora? quem tibi donavi? C. Gracchus (Cic. De. Or. 3.214) _quo me miser conferam? quo vertam? in Capitoliumne? at fratris sanguine madet. an domum? matremne ut miseram lamentantem videam et abiectam?_

Ariadne proposes to herself three courses, and rejects them successively as impossible, the first, because of her isolation from home, the other two, because also of her past deeds.

Idaeos montes: i.e. Crete, the thought being simply of returning home.

sperem: sc. even if I could reach Crete.

quemne: = _quippe quem_; cf. v. 183; Catul. 68.91. The interrogative particle _-ne_ is not infrequently joined to relatives to point the reason for controverting a previous assertion, or for answering in the negative a previous question; cf. Pl. Trin. 360 quin comedit quod fuit, quod non fuit? Ter. Phor. 923 quodne ego discripsi porro illis quibus debui? and Minton Warren, Amer. Jour. Phil. Vol. 2 p. 50ff.

fraterna: cf. v. 150

quine: etc. i.e. as if it were not my husband who is now fleeing from me.

nullo: etc. the appositive phrase _sola insula_ is inserted between the subject and its modifying ablative of characteristic _tecto_ in a somewhat unusual form of hyperbaton; cf. however Juv. 3.48 mancus ci exstinctae corpus non utile dextrae .

nulla spes: on the lengthening of the final syllable see Intr. 86g.

omnia muta: as no ear was open to her grief (v. 170), so there was no voice to speak sympathy; cf. Prop. 1.18.1 haec certe deserta loca et taciturna querenti.

anguino redimita capillo: cf. Aesch. Lib. 1049 peplektanhme/nai puknoi=s dra/kousin ; Hor. Carm. 2.13.35 intorti capillis Eumenidum angues ; Verg. A. 6.280 discordia demens, vipereum crinem vittis innexa cruentis.

exspirantis: i.e. the angry, hissing serpents but betoken the anger that breathes forth from the breasts of the furies.

praeportat: of a thing prominently displayed; cf. Lucr. 2.621 tela praeportant violenti signa furoris.

huc huc adventate: Catul. 61.8 huc huc veni .

vae miserae: cf. Catul. 8.15n.; Ter. Andr. 743 vae miserae mihi ; Ov. Her. 3.82 hic mihi, vae miserae, concutit ossa metus .

extremis medullis: from my inmost soul; but this instance of the ablative alone with _proferre_ is perhaps unique. cf. Catul. 35.15n.

ardens: like v. 124 _ardenti corde_.

quali: etc. i.e. as Theseus forgot his vows (v. 58 _immemor iuvenis_; v. 123 _immemori pectore_), let forgetfulness bring upon him the fatal penalty (cf. vv. 247-248).

anxia: explained by v. 197; cf. Catul. 68.8. 204ff. _adnuit_: etc. cf. Hom. Il. 1.528ff.; Verg. A. 9.106 adnuit et totum nutu tremefecit Olympum ; Stat. Theb. 7.3 concussisque caput, motu quo celsa laborant sidera proclamatque adici cervicibus Atlas .

mundus: the firmament, as in 66.1; but cf. Catul. 47.2.

caeca caligine: cf. Cic. Arat. 345 adiment lucem caeca caligine nubes ; Lucr. 3.304 caecae caliginis umbra ; Verg. A. 3.203 incertos caeca caligine soles .

consitus: beset; very rare in this figurative sense till postclassical times; but cf. Pl. Men. 756 consitus sum senectute .

Cf. the close verbal resemblance of v. 238; Lucr. 2.582 memori mandatum mente teneri .

Erechtheum portum: so Homer calls the Athenians by the name of their fabulous king in Hom. Il. 2.547 δῆμον Ἐρεχθῆος μεγαλήτορος .

classi: perhaps of a single ship; cf. v. 53 with vv. 84 and 121.

divae: the use of the unmodified noun to indicate Athena seems to be made possible by the unmistakable reference to Athens in v. 211 _Erechtheum portum._

incundior vita: cf. Catul. 68.106 ita dulcius atque anima ; and on similar expressions, Catul. 3.5n.

extrema: etc. Theseus passed his early life with his mother Aethra in the home of her father Pittheos, king of Troezene, and when he finally came to Athens, found Aegeus already an old man.

fine: feminine, as regularly in Lucretius, and not very infrequently in other writers of all ages, in the singular; but note the masculine plural in Catul. 64.3; Catul. 66.12.

gaudens laetanti pectore: cf. Catul. 67.26n.

fortunae signa secundae: in this instance, white sails. On white as the color proverbially connected with good fortune, cf. Catul. 68.148n.; Pers. 1.110 per me equidem sint omnia protinus alba .

terra: etc., a common sign of extreme grief among the ancients; cf. Vulg. Iob 2.12 ploraverunt, scissisque vestibus sparserunt pulverem super caput suum in caelum ; Hom. Il. 18.23 ἀμφοτέρῃσι δὲ χερσὶν ἑλὼν κόνιν αἰθαλόεσσαν χεύατο κὰκ κεφαλῆς, χαρίεν δ᾽ ᾔσχυνε πρόσωπον ; _Verg. A. 12.611_ _canitiem immundo perfusam pulvere turpans._

vago: swaying; cf. Enn. frag. 151 R. arbores vento vagant .

obscurata ferrugine Hibera: cf. Verg. A. 9.582 ferrugine clarus Hibera ; Verg. G. 1.467 caput obscura ferragine texit ; Ov. Met. 5.404 obscura tinctas ferrugine habenas . The dye was apparently produced from a variety of ochre, and its hue is described by Pl. Mil. 1181 palliolum habea: ferrugineum (nam is colos thalasicust) , and by Servius on Verg. ll. cc. _vicinus purpurae subnigrae; purpura nigrior_. It was, therefore, a sort of dull, dark violet.

sancti incola Itoni: the shrine of Athena in the Boeotian city (and mountain) of Itonus was well known to the Romans; cf. Liv. 36.20 ibi statua regis Antiochi posita in templo Minervae Itoniae iram accendit .

defendere: the simple complementary infinitive with _adnuere_ in this sense is very rare, but is justified by the similar construction with other verbs of promising.

Erechthei: genitive; cf. v. 120 _Thesei_ (but v. 382 _Pelei_, Catul. 66.94 Hydrochoi , dative).

tauri: cf. v. 173 n.

oblitteret aetas: cf. Catul. 68.43; Catul. 64.322 In these three places, and in v. 237, _aetas_ has the sense of _tempus_; elsewhere in Catullus, of _vita_.

invisent: cf. Catul. 31.4n.

funestam vestem: the garb of mourning; cf Acc. Trag. 86 R. sed quaenam haec mulier est funesta veste, tonsu lugubri?

undique: the word is probably used merely to emphasize the urgency of the bidding,—'every stitch of mourning.'

te reducem sistet: cf. Liv. 29.27.3 domos reduces sistatis .

aetas: cf. v. 232 n.

Cf. v. 209

ceu: etc. cf. Hom. Il. 5.522ff.

summa ex arce: i.e. from the Acropolis, whence he would have an unimpeded view over the sea southward. This form of the story is followed also by Diod. 4.61.7 and Paus. 1.22.5; but another form makes the promontory of Sunium the place whence Aegeus watched for the return of the ship, on descrying which he threw himself into the thence-named Aegean Sea; cf. Stat. Theb. 12.624ff. linquitur Eois longe speculabile proris Sunion, unde vagi casurum in nomina ponti Cresia decepit falso ratis Aegea velo .

inflati: the spread of canvas made the vessel the sooner visible to his straining eye.

ferox: cf. with the absolute use of the adjective v. 73.

Minoidi: Gr. dative; cf. Catul. 66.70 Tethyi^ .

247f. qualem Minoidi: etc. cf. v. 200 f.

quae tum: etc. the poet has hastened on to describe the effect of Ariadne's curse, and now returns to tell her own fate.

saucia: of the wounds of love; cf. Verg. A. 4.1 regina gravi iam dudum saucia cura .

at: etc. in immediate contrast with the absorbing grief of Ariadne is brought the joyous revelry of the Bacchic rout, the leader of which comes to fill the place of the fugitive lover.

parte: sc. of the coverlet.

florens: cf. Catul. 17.14n.

Iacchus: a mystical name of Bacchus especially used by the poets.

thiaso: cf. Catul. 63.28n.

satyrorum, silenis: of the male attendants upon Bacchus the poets usually designate the wanton younger as _satyri_ and the drunken elder as _sileni_.

Nysigenis: Bacchus is apparently thought of as returning from his great journey to the far East; cf. Verg. A. 6.804 qui pampineis victor iuga flectit habenis Liber, agens celso Nysae de vertice tigris , and Apollonius 4.431 calls Dionysus the prince of Nysa, when speaking of his marriage with Anadne. Nysa is variously described by ancient authorities as a city (or mountain) in India (Plin.), Arabia (Diod.), or Thrace (Hom.; Strabo).

tuo: for the objective genitive, a not very common use; cf. Catul. 87.4 amore tuo ; Sall. Iug. 14.8 vos in mea iniuria despecti estis.

quae: the following actions are those characteristic of the female followers of Bacchus (cf. also v. 256 _harum_), while only his male followers have thus far been referred to. Bergk is therefore correct in believing that a verse has been lost after v. 253.

lymphata mente: i.e. crazed with the mad enthusiasm inspired by the god; cf. Hor. Carm. 1.37.14 mentem lymphatam Mareotico .

capita inflectentes: cf. Catul. 63.23n.

tecta cuspide thyrsos: i.e. the vine-rod, or spear, the traditional sceptre and weapon of Bacchus. Its stroke inspired madness; cf. Hor. Carm. 2.19.5 _euhoe, parce, Liber, parce, gravi metuende thyrso_. It was also carried by his worshippers, as here, and was tipped with a pine cone or with a bunch of vine leaves ( Verg. A. 7.396 pampineas gerunt hastas ), or ivy leaves ( Prop. 4.3.35 haec hederas legit in thyrsos ). All forms of the _thyrsus_ are seen in the frequent representations of Bacchic processions in ancient wall-paintings and bas-reliefs (cf. Rich Dict. Antiq. s.v.).

e divulso: etc. cf. Pers. 1.100 raptum vitulo caput ablatura superbo Bassaris . The action is often represented in ancient monuments. So the frenzied Bacchantes tore Pentheus in pieces (Ov. Met. 3.701ff.).

tortis: etc. cf. Hor. Carm. 2.19.18 tu separatis uvidus in iugis nodo coerces viperino Bistonidum sine fraude crines ; Ov. Met. 4.483 [Tisiphone] torto incingitur angue .

obscura: etc. cf. Hor. Carm. 1.18.12 nec variis obsita frondibus sub divum rapiam (addressing Bassareus). The _cista_ was either a cylindrical basket or a box, in which the secret emblems (orgia) of the worship of Bacchus, or of Ceres, were concealed from uninitiated eyes when carried in procession (_celebrabant_).

plangebant: etc. cf. Catul. 63.21n.; Lucr. 2.618ff. tympana tenta tonant palmis et cymbala circum concava, raucisonoque minantur cornua cantu, et Phrygio stimulat numero cava tibia mentis .

proceris: perhaps with the unusual meaning of lifted high (see the monuments).

tereti aere: i.e. the hemispherical cymbals; cf. Catul. 63.21.

tenuis tinnitus, the sharp shrill, as contrasted with _raucisonos bombos_ of the horns. Note the alliteration, and cf. Lucr. l.c., and the triple alliteration in v. 320.

raucisonos: cf. Lucr. l.c.; Lucr. 4.544 et reboat raucum regio cita barbara bombum.

barbara: i.e. Phrygian; cf. Catul. 63.22. Catullus speaks from the standpoint of a Greek; cf. Lucr. l.c.; Hor. Epod. 9.5 sonante mixtum tibiis carmen lyra, hac Dorium, illis barbarum .

talibus: etc. the story of Ariadne is left when happiness in a divine marriage is just coming to her; these verses, concluding the description of the embroidered spread, virtually repeat vv. 50-51, with which it began.

The mortal guests give place to the immortals, who come also bringing gifts (278-302), and sit down to the marriage-feast (303-304), while the Parcae, still pursuing their endless task of spinning the thread of fate (305-322), sing the prophetic marriage-song (323-381).

Thessala pubes: cf. v. 32 _tota Thessalia_.

sanctis: cf. Catul. 36.3n.

hic: temporal, as in Catul. 68.63.

horrificans: the word occurs only here in the sense of 'ruffling,' but in later writers in that of 'shudder-causing.' But cf. v. 205 _horrida aequora_; Acc. ap. Non. 422.33 mare cum horret fluctibus ; Hor. Epod. 2.6 horret iratum mare .

vagi solis: the journeying sun, in distinction from the fixed heavenly lights; cf. Catul. 61.117n.; Tib. 4.1.76 vagi pascua solis ; Hor. S. 1.8.21 vaga luna.

leviter sonant plangore: cf. Sen. Ag. 717f. licet alcyones Cecya suum fluctu leviter plangente sonent .

cachinni: genitive singular; for the figure cf. Aesch. Prom. 89 ποντίων τε κυμάτων ἀνήριθμον γέλασμα .

magis magis: cf. Catul. 38.3n.

purpurea luce: i.e. the rosy light of dawn, reflecting which the more distant surface of the sea (_undae procul nantes_) loses in the gleam its own color.

ad se: to his own home; cf. Pl. Mil. 121 in aedis med ad se adduxit domum ; and often.

vago pede: corroborating _passim_, with reference to the diverse directions in which the homes lay, and not with the implication of 63.86.

Chiron: the famous centaur, a near neighbor and friend of Peleus, and later the trainer of Achilles.

silvestria dona: but according to Homer one gift of Chiron to Peleus was more warlike; cf. Hom. Il. 16.143 Πηλιάδα μελίην, τὴν πατρὶ φίλῳ πόρε Χείρων Πηλίου ἐκ κορυφῆς, φόνον ἔμμεναι ἡρώεσσιν .

quoscumque: continued by the simple _quos_ in the two following clauses, in the latter of which occurs the noun _flores_, which the relatives modify. Chiron has gathered the wealth of blossoms from plain, mountain, and riverside to deck the interior of the house, while Peneus (v. 285) brings masses of foliage to adorn the approaches to it.

ora: i.e. the region; cf. Cic. ND 2.164 quacumque in ora ac parte terrarum ; Mark 5.17 to depart out of their coasts.

aura parit: cf. v. 90; Catul. 62.41n.

indistinctis: the great number of the flowers precluded their artistic assortment.

plexos corollis: flowers were usually woven into long cords for decorative use at banquets, and were sold among the Romans in that form; cf. the frescoes from Pompeii representing _Amoretti_ in the business of preparing such cords.

permulsa: often used of the delightful effect of pleasing sounds, but not often of odors; cf., however, Stat. Silv. 1.3.11 permulsit crocis blandumque reliquit odorem.

risit odore: cf. HHymn. 4.13 κὦζ᾽ ἥδιστ᾽ ὀδμή, πᾶς τ᾽ οὐρανὸς εὐρὺς ὕπερθεν γαῖά τε πᾶσ᾽ ἐγελάσσε καὶ ἁλμυρὸν οἶδμα θαλάσσης.

Tempe : etc. cf. the description of the famous vale in Ov. Met. 1.568ff.; Plin. NH 4.8.31; Anth. Lat. 315.3 Mey. frondosis Tempe cinguntur Thessala silvis .

Naiasin: i.e. the nymphs of the vale of Tempe; cf. Cul. 18 Pierii laticis decus, ite, sorores Naides ; Cul. 115ff. hic etiam viridi ludentes Panes in herba et Satyri Dryadesque choros egere puellae Naiadum coetu. This form of the Greek dative plural apparently occurs here first in extant Latin; but cf. citations from Varro Charis. 1.15, p. 38 schemasin , and Non. p. 374 ethesin ; Prop. 1.20.12 Adryasin , 32 _Hamadryasin_, 34 _Thyniasin_; Ov. Her. 13.137 Troasin ; Ov. AA 3.672 Lemniasin , etc.

linquens: (= _relinquens_, as often in Catullus) the nymphs who dance with and in honor of the river god are this day left to dance alone.

Doris: see Crit. App.

vacuus: empty-handed the word is rare in this meaning, but cf. Juv. 10.22 cantabit vacuus coram latrone viator ; Vulg. Exod. 23.15 non apparebis in conspectu meo vacuus ; Hom. Il. 2.298 κενεὸν νέεσθαι .

ille: in contrast with Chiron.

radicitus: roots and all. cf. the figurative meaning in Pl. Most. 1092 omnia malefacta vostra repperi radicitus but in v. 108 the meaning is the more usual one, 'from the roots.'

fagos: etc. the wooded banks of the Peneus (v. 286) made trees his most natural gift.

sorore flammati Phaethontis: i.e. the poplar. On the transformation of the Heliades into poplar-trees see Ov. Met. 2.340ff.; Verg. A. 10.189ff. namque ferunt luctu Cycnum Phaethontis amati, populeas inter frondes umbramque sororum dum canit , etc.; Cul. 127ff.

sollerti corde: cf. Aesch. Prom. 506 πᾶσι τέχναι βροτοῖσιν ἐκ Προμηθέως .

Prometheus: according to the accounts of Hyginus Astr. 2.15 and Servius (on Verg. Ecl. 6.42), Prometheus warned Zeus of the prophecy concerning the son of Thetis (cf. v. 21 n.), and was therefore released from his confinement on Mt. Caucasus. So Prometheus is here a chief guest, as the promoter of the marriage.

extenuata vestigia: the fading scars, not the bit of rock set in a ring, mentioned by Servius (l.c.) and Pliny NH 37.2, which Zeus forced Prometheus to wear as a reminder of his punishment.

silici: dative modifying _restrictus_.

sancta: cf. Catul. 36.3n. With the hypermeter cf. Catul. 34.22; Catul. 115.5.

caelo: ablative of place.

unigenam: here twin-sister; but cf. Catul. 66.53.

montibus: dative modifying _cultricem_; cf. Catul. 66.58 Canopus incola litoribus ; and with the idea, Catul. 34.9ff n.

Idri: if the reading be correct, the name is perhaps that of the district in Caria called Idrias by Herodotus and Stephen of Byzantium, where Artemis was worshipped as Hecate.

Pelea adspernata: no story accounting for this disdain is known, and Hom. Il. 24.62 expressly speaks of the presence of all the gods at the wedding, and of a marriage-song sung by Phoebus (cf. also Aesch. ap. Plat. Rep. 2.383).

niveis: being of ivory; cf. v. 45.

cum interea: cf. Catul. 95.3.

infirmo: etc. i.e. tremulous with age; cf. v. 307; Catul. 61.161.

neridicos cantus: cf. Hor. CS 25ff. vosque veraces cecinisse, Parcae, quod semel dictum stabilis per aevum terminus servat .

roseae: the contrast between the white robe and its crimson border (v. 308) matches that between the crimson fillets and the snowy locks; cf. Prop. 4.9.52 [sacerdos] puniceo canas stamine vincta comas .

niveo vertice: cf. Hor. Carm. 4.13.12 capitis nives .

aeternum: the Fates never cease from their task even to engage in festivities, and the course of destiny is never interrupted.

311ff.. The picture of the spinning is entirely realistic. A mass of prepared wool but loosely fastened together is attached to one end of the distaff (_colus_), which is held in the left hand. With the right hand the spinner draws the filaments from the mass and twists them between thumb and finger into a thread, the firmness of the twisting being assisted by attaching the end of the thread to the spindle (_fusus_), weighted by the _turbo_, which acts as a fly-wheel.

supinis: the hand is turned palm upward as the fingers draw the filaments from the elevated distaff, but palm downward (_prono pollice_) as they grasp the hanging thread near the spindle and set it twirling; cf. Tib. 2.1.64 fusus apposito pollice versat opus ; Ov. Met. 6.22 levi teretem versabat pollice fusum .

tereti turbine: a small circular plate of heayy material with a hole through the center somewhat smaller than the thicker part of the long, tapering _fusus_. Through this the smaller end of the _fusus_ was passed as far as it would go, and the symmetrically distributed weight of the _turbo_ thus gave additional momentum to the whirling spindle. When the thread was spun to a convenient length, its lower part was wound around the _fusus_, and the process continued as before.

atque ita: i.e. while the process thus described was going on; cf. v. 84 _atque ita._

decerpens: while both hands were busy, the yarn was passed between the lips to strip off the outstanding fibers, or to smooth them down so that they might be included in the twist.

aridulis, morsa: both \rendergreek{ἅπαξ λεγόμενον}. On the diminutive of both noun and adjective in _aridulis labellis_ see Catul. 3.8n.

fuerant exstantia: (= _exstiterant_) this periphrastic form is not very common, and where occurring is generally with the present tense of _esse_, as in Catul. 63.57 carens est .

custodibant: older form, chiefly poetic or colloqulal, except from _ire_; cf. Catul. 68.85; Catul. 84.8.

haec: for _hae_; so Varro, Lucretius, Vergil, etc., passim.

clarisona: cf. v. 125 n. _clarisonas_.

vellentes vellera: i.e. beginning their spinning by drawing from the mass of wool on the distaff the filaments to form the yarn cf. Ov. Met. 14.264 quae vellera motis nulla trahunt digitis nec fila sequentia ducunt . With the triple alliteration cf. v. 262.

aetas: cf. v. 232 n.

The marriage-song of Peleus and Thetis, arranged in twelve strophes, but without precise correspondence in the number of verses in each (cf. on this point c. 62). In theme and general treatment, and in certain details (eg. the address in vv. 372ff., with which cf. Catul. 61.211ff.), the song is a true _epithalamium_, such as might be sung outside the closed door of the marriage-chamber, and the conclusion of the description of the wedding with the song reinforces this impression of it. But it is represented as sung by the Fates while the other guests were feasting, and vv. 328ff. suggest that the bride is yet to arrive. Evidently the poet is not attempting to reproduce the exact features of a marriage ceremonial, and precise interpretation from an archaeological standpoint is impossible.

Peleus boasts a glorious descent, and has made this glory greater by his own great deeds, but is to find his greatest glory in his son.

Emathiae: the name meant to the Greeks Macedonia, but with common poetic inexactness is here used of Thessaly; cf. Verg. G. 1.491 nec fuit indignum superis sanguine nostro Emathiam pinguescere (of the battle of Pharsalus).

sorores: cf. Ov. Trist. 5.3.17 dominae fati quidquid cecinere sorores ; Mart. 5.1.3 veridicae sorores .

quae fata secuntur: which the fates follow; the clause modifies _subtegmina_; cf. Stat. Theb. 1.213 vocem fata secuntur ; Anth. Lat. 227 Baehr. consultum fata secuntur .

subtegmina: = _fila_; cf. Hor. Epod. 13.15 reditum certo subtegmine Parcae rupere .

Hesperus: cf. c. 62 passim nn.

adveniet coniunx: see introductory note to vv. 323-381.

flexanimo: heart-compelling; cf. Pac. fr. 177 R. o flexanima atque omnium regina rerum oratio ; Verg. G. 4.516 non ulli animum flexere hymenaei .

languidulos somnos: cf. Verg. A. 12.908 languida quies ; Tib. 4.1.181 languida otia .

substernens: etc. cf. Ov. Am. 3.7.7 illa quidem nostri subiecit eburnea collo bracchia .

levia bracchia: cf. Catul. 66.10.

contexit: sheltered, doubtless with the notion of privacy usually connected with the verb.

adest concordia: with the arrangement cf. Catul. 30.3n.

Peleo: with synizesis, as in v. 382 _Pelei_, which is, however, the regular Greek dative.

haud tergo: etc. cf. Hom. Il. 13.289f. οὐκ ἂν ἐν αὐχέν᾽ ὄπισθε πέσοι βέλος οὐδ᾽ ἐνὶ νώτῳ, ἀλλά κεν ἢ στέρνων ἢ νηδύος ἀντιάσειε .

cursus: the commonest epithets of Achilles in the Iliad describe him as swift of foot.

Cf. Pind. Nem. 3.51 κτείνοντ᾽ ἐλάφους ἄνευ κυνῶν δολίων θ᾽ ἑρκέων: ποσσὶ γὰρ κράτεσκε ; Stat Ach. 2.111 volucres praevertere cervos et Lapithas cogebat equos … Chiron .

flammea: fiery-fleet; on the figure cf. Verg. A. 11.718 virgo pernicibus ignea plantis ; Ov. Met. 2.392 ignipedum vires expertus equorum .

non illi: etc., Achilles claims this pre-eminence for himself in Hom. Il. 18.105 τοῖος ἐὼν οἷος οὔ τις Ἀχαιῶν χαλκοχιτώνων ἐν πολέμῳ

campi: the vigorous emendation is supported by Stat. Ach. 1.86 cum tuus Aeacides tepido modo sanguine Teucros undabit campos ; Il. Lat. 384 sanguine Dardanii manabant undique campi .

longinquo: of the length of the war, not of its distance from Greece.

periuri Pelopis: Pelops won the chariot-race, and so the hand of Hippodamia, from her father, Oenomaus, by offering half of his kingdom to the latter's charioteer, Myrtilus, if he would loosen the linchpins of the chariot, or substitute pins of wax. Upon the success of the plot, Pelops refused to carry out his agreement, and threw Myrtilus into the sea near Geraestus in Euboea. But the dying curse of Myrtilus followed the house of Pelops thereafter. Cf. Pind. O. 1.114ff.; Apoll. Rh. 1.752; Hyg. Fab. 84.

tertius heres: i.e. Agamemnon, the succession being Pelops, Atreus, Thyestes, Agamemnon, as Homer shows in Hom. Il. 2.105ff.

The traditional signs of grief on the part of women; cf. Hom. Il. 18.30 χερσὶ δὲ πᾶσαι στήθεα πεπλήγοντο ; Verg. A. 1.480 crinibus Iliades passis suppliciter tristes et tunsae pectora palmis ; Ov. Met. 13.491 [Hecuba] consueta pectora plangit . Baehrens supports his emendation by citing Ov. Her. 9.125 nec venit incultis captarum more capillis ; Stat. Theb. 6.32 incultam ferali pulvere barbam .

cano: here as elsewhere (cf. Catul. 17.13; Catul. 61.51; Catul. 68.142) Catullus emphasizes the relations between parent and child, and appeals to our sympathy, by representing the former as in advanced age; cf. _putrida_ ( Hor. Epod. 8.7 pectus et mammae putres ) and _infirmis_.

variabunt: of the discoloration produced by the blows, which, to mark the depth of woe, were violent, though from weak hands; observe the juxtaposition of _infirmis_ and _variabunt_; cf. Pl. Poen. 26 ne et hic varientur virgis et loris domi .

353ff.. velut: etc. the figure is Homeric; cf. Hom. Il. 11.67ff.

praecerpens: clipping down (before him as he advances); the word apparently occurs only here in this meaning, though the figurative meaning in Gell. 2.30.2 cuius rei causam, cum Aristotelis libros problematorum praecerperemus, notavi seems to point in the same direction; cf. Apoll. Rh. 3.1386 προτάμωνται ἀρούρας .

messor aristas … demetit: cf. Il. Lat. 886 maturasque metit robustus messor aristas .

sole sub ardenti: cf. Verg. Ecl. 2.13 sole sub ardenti resonant arbusta cicadis.

flaventia arva: cf. Verg. G. 4.126 qua niger umectat flaventia culta Galaesus.

Referring to the great repulse of the Trojans at the hands of Achilles in Hom. Il. 21.

passim diffunditur: of the smaller stream losing itself in the larger.

rapido: perhaps of rushing waves rather than of swift current; cf. Catul. 63.16 rapidum salum ; Hom. Il. 2.845 Ἑλλήσποντος ἀγάῥῥοος

caesis corporum acervis: with hypallage of the adjective, as not infrequently in poetry.

angustans: etc. cf. Hom. Il. 21.218ff πλήθει γὰρ δή μοι νεκύων ἐρατεινὰ ῥέεθρα, οὐδέ τί πῃ δύναμαι προχέειν ῥόον εἰς ἅλα δῖαν στεινόμενος νεκύεσσι, σὺ δὲ κτείνεις ἀϊδήλως (from the address of the Scamander to Achilles; Verg. A. 5.806ff. [Achilles] milia multa daret leto, gemerentque repleti amnes, nec reperire viam atque evoluere posset in mare se Xanthus .

tepe_faciet: see Intr. 86f.

morti quoque reddita praeda: i.e. the power of Achilles will be shown by the fact that he continues even after death to make the Trojans his prey. Polyxena, daughter of Priam, in the course of the siege betrothed on pretence of peace to Achilles, was at the capture of the city sacrificed to his manes by Pyrrhus; cf. Ov. Met. 13.439ff.; Serv. on Verg. A. 3.321; Hyg. Fab. 110; Eur. Hec. 37ff.; Eur. Hec. 521ff.

teres: round, i.e. circular; cf. v. 314.

bustum: Servius and Hyginus apparently think of the tomb of Achilles as on the Sigean shore; Ovid, following Euripides, has in mind a cenotaph on the shore of Thrace.

copiam: with a dependent infinitive, _solvere_; cf. Sall. Cat. 17.6 molliter vivere copia ; Verg. A. 9.483 te adfari data copia.

Neptunia: i.e. built by Neptune.

solvere vincla: cf. Hom. Il. 16.100 ὄφρ᾽ οἶοι τροίης ἱερὰ κρήδεμνα λύωμεν ; similariy according to Polybius 17.11.5 the fortresses of Chalcis, Corinth, and Demetrias were called \rendergreek{πέδαι Ἑλληνικαί}.

made^fient: cf. v. 360 n. _tepefaciet_.

quae: referring to the adjective Polyxenia (= Polyxenae); cf. Liv. 2.53.1 Veiens bellum exortum, quibus Sabini arma coniunxerunt .

ancipiti: two-edged; probably with reference to the _bipennis_, used both as a weapon of warfare and as a sacrificial axe; cf. Lucil. 751 Lachm. _vecte atque ancipiti ferro effringam cardines_.

truncum: headless.

summisso poplite: cf. Ov. Met. 13.477 super terram defecto poplite labens (of Polyxena).

animi amores: with this use of an apparently otiose genitive cf. Catul. 2.10 animi curas ; Catul. 68.26 delicias animi ; Catul. 102.2 fides animi . On the plural see v. 27 n.

iam dudum: forthwith, modifying _dedatur_; the emphasis rests on _iam_, as the speaker looks from a distant beginning; cf. Verg. G. 1.213 papaver tempus humo tegere et iam dudum incumbere aratris ; Aen. 2.103 iam dudum sumite poenas . But in Plautus the phrase generally means 'a long time ago,' the emphasis usually resting upon _dudum_, as the speaker looks backward from the present; though the play on Amphitruo's misunderstanding of the term as a synonym for _modo_ (Pl. Amph. 692) points toward the beginning of the use here fairly inaugurated by Catullus.

376 f.. The belief indicated by these verses was widespread in antiquity; cf. Nem. Ecl. 2.10ff.

nutrix: the nurse continued to be the girl's confidential attendant throughout her married life, as was often the case in the times of slavery in the southern part of the United States.

orienti luce: with the morning light; cf. Lucr. 5.664 orienti lumine ; Ov. Fast. 4.832 oriens dies .

cf. Catul. 66.15f.

Epilogue, commenting upon the withdrawal of divine presence from the ceremonies of men after the heroic age, on account of the impiety of the race.

Pelei: with synizesis, as in v. 336 _Peleo_, which is, however, the pure Latin dative; but cf. Catul. 66.94 hydrochoi (dat.), and v. 120 _Thesei_, v. 229 _Erechthei_ (gen.).

Ellis quotes Hes. frag. 218 ξυναὶ γὰρ τότε δαῖτες ἔσαν ξυνοὶ δὲ θόωκοι ἀθανάτοισι θεοῖσι καταθνητοῖς τ᾽ ἀνθρώποις .

praesentes: in bodily presence; cf. Hor. Carm. 3.5.2 praesens divus habebitur Augustus .

namque: cf. Catul. 66.65n.

coetu: dative, as in Catul. 66.37.

caelicolae: cf. Catul. 30.4; Catul. 68.138.

templo in fulgente: modifying v. 389 _conspexit_, etc. Evidently the poet is thinking of the splendid temples of a later date rather than of the simple structures of heroic times.

revisens: if the correct reading, probably used absolutely; cf. the ordinary use of _revisere_ with _ad_.

annua: etc. doubtless a typical occasion only, rather than a known festival.

vagus: often used of the aimless, frenzied rushing to and fro of the god's followers; cf. Catul. 63.13, Catul. 63.86.

Parnasi: this famous mountain of Phocis, the haunt of the gods, rose just behind Delphi.

effusis: etc. cf. the descripion of the Bacchic rout in vv. 254ff.; Ov. Fast. 6.514 Thyiades, effusis per sua colla comis .

Delphi: i.e. the inhabitants of the city; cf. Just. 24.7.8 urbem suam Delphi aucti viribus sociorum permuniucre , and Grk. \rendergreek{Δελφοί} often. The city was early connected with the worship of Bacchus as of Apollo; cf. Aesch. Eum. 25 ἐξ οὗτε^[[i.e. \rendergreek{Δελφῶν}]] Βάκχαις ἐστρατήγησεν θεός, λαγὼ δίκην Πενθεῖ καταρράψας μόρον ; Paus. 10.4.3 αἱ δὲ Θυιάδες γυναῖκες μέν εἰσιν Ἀττικαί, φοιτῶσαι δὲ ἐς τὸν Παρνασσὸν παρὰ ἔτος αὐταί τε καὶ αἱ γυναῖκες Δελφῶν ἄγουσιν ὄργια Διονύσῳ .

Mavors: antique and poetic form for Mars.

rapidi Tritonis hera: i.e. Athena, called \rendergreek{Τριτογένεια} by Hom. Il. 8.39, etc., probably from the river Triton in Boeotia (Strab. IX. 407; Paus. 9.33.7), rather than from the lake, or river, Triton in Libya (Hdt. 4.178; Plin. NH 5.28).

Rhamnusia virgo: i.e. Nemesis, so called from her famous temple at Rhamnus in Attica; cf. Catul. 66.71; Catul. 68.77; Ov. Met. 3.406 adsensit precibus Rhamnusia iustis ; Stat. Silv. 3.5.5 audiat infesto licet hoc Rhamnusia vultu . Ares and Athena often encourage men to battle in the Iliad, but this function on the part of Nemesis is nowhere else mentioned. Perhaps it is from an unknown Alexandrian source, or else the conjecture of Baehrens is right (_Amarunsia virgo_ = Artemis of Amarynthus in Euboea; cf. Strab. X.448; Paus. 1.31.4).

With this description of the iron age cf. Hes. WD 182ff.; Ov. Met. 1.127ff.; Verg. G. 2.1ff.

institiam: etc. cf. Ov. Fast. 1.249 nondum iustitiam facinus mortale fugarat.

perfudere: etc. cf. Lucr. 3.72 crudeles gaudent in tristi funere fratris ; Verg. G. 2.510 gaudent perfusi sanguine fratrum .

genitor etc.: was the optimate Catullus thinking of Catiline in his own day (cf. Sall. Cat. 15.2), or of the story of Hippolytus (to which, however, v. 402 hardly applies)? Cf., however, v. 402 n.

innuptae: virgin; the idea apparently is that the father conceives a passion for his son's promised bride, has him put out of the way upon the eve of the marriage, and proceeds to contract a practically incestuous union with her himself, uniting two unnatural crimes. And as the father sins with the daughter, so (v.403) the mother with the son.

novercae: said by a sort of anticipation, to emphasize the unnaturalness of the position of the former wife and sister, now become the stepmother.

ignaro: etc. again, is the story from the poet's own day, or only that of Jocasta (though _impia_ hardly applies to the action of the innocent mother, equally ignorant with her son)?

divos parentes: i.e. the deified ancestors of the family, who would be especially outraged by such impiety in their descendants; cf. Grk. \rendergreek{θεοὶ πατρῷοι}; Leg. Reg. divis parentum sacer esto ; CIL 1.1241 _deis inferum parentum sacrum_.

fanda nefanda: cf. similar phrases in Ter. Ad. 990 iusta iniusta ; Hor. Ep. 1.7.72 dicenda tacenda ; Verg. A. 12.811 digna indigna ; but without asyndeton in Verg. A. 1.543 fandi atque nefandi ; Ov. AA 1.739 mixtum fas omne nefasque.

instificam: justly-dealing; \rendergreek{ἅπαξ λεγόμενον}.

lumine claro: i.e. the open light of day, as distinct from the cloud in which the gods commonly hide themselves.[^85cde56b6a6d4b85ac55fb357fd1e868]

\newpage

# Veldidena To A Village
  
## From Veldidena To Parthanum

Virgil departed from Veldidena, intending to travel by road to Parthanum, a distance of about 32 miles. 

They pass a pillar on the right surmounted by a stone urn. As they go up from Veldidena, they see the ruined walls. Virgil saw this on a roadside tomb: $] / [- - -]I[- - -] / [- - -]AE T [- - -] / [&. On the road from Veldidena to Parthanum there is a village, in which there is a temple and grove. He had set out from Veldidena amidst a throng travelling the same way. Above the roads are ruins, among which is a cave sacred to Asclepius. The road narrows here, an orchard wall encroaching on it. This is a smooth road, by which many wagons were bringing wood to Parthanum. By the road is a salt spring. 

While he was visiting Verona, he made a point of copying down what John Conington had written.

## A Story By John Conington About Verona From _Commentary On Vergil'S Aeneid, Volume 2_


For "abitum" Med. (second reading), Pal., Rom., fragm. Verona, and originally Gud. have "aditum," which was the old reading before Heins. Serv. however distinctly prefers "abitum," which is required by the sense. "Coronant" i. q. cingunt, as in Lucr. 2.802, pluma columbarum . . . Quae sita cervices circum collumque coronat and other instances quoted by Forc., with a further reference to the use of corona as a military term for besiegers surrounding a place (Forc. corona).[^384c290e1868481795494569c37be8c1]

  
## Travelling By Road To Veldidena

From Parthanum to Veldidena is a distance of about 32 miles when travelling by road. 

A cloud passes in front of the sun. The sun beats down. On the road from Parthanum to Veldidena there is a village, in which there is a temple and grove. He had set out from Parthanum amidst a throng travelling the same way. By the road is a salt spring. Along the road are graves, and a cenotaph. 

The library at Patavium happened to have a copy of _Civil War_, where Virgil encountered it.

## An Account Of Patavium


  
'Since all desire it, and the fates prevail,  
' So let it be; your leader now no more,  
' I share the labours of the battle-field.  
' Let Fortune roll the nations of the earth  
' In one red ruin; myriads of mankind  
' See their last sun to-day. Yet, Rome, I swear,  
' This day of blood was forced upon thy son.  
' Without a wound, the prizes of the war  
' Might have been thine, and he who broke the peace  
' In peace forgotten. Whence this lust for crime?  
' Shall bloodless victories in civil war  
' Be shunned, not sought? We've ravished from our foe  
All boundless seas, and land; his starving troops  
' Have snatched earth's crop half-grown, in vain attempt  
' Their hunger to appease; they prayed for death,  
' Sought for the sword-thrust, and within our ranks  
' Were fain to mix their life-blood with your own.  
' Much of the war is done: the conscript youth  
' Whose heart beats high, who burns to join the fray  
' (Though men fight hard in terror of defeat),  
' The shock of onset need no longer fear.  
' Bravest is he who promptly meets the ill  
' When fate commands it and the moment comes,  
Yet brooks delay, in prudence; and shall we,  
' Our happy state enjoying, risk it all?  
' Trust to the sword the fortunes of the world?  
' Not victory, but battle, ye demand.  
' Do thou, O Fortune, of the Roman state  
' Who mad'st Pompeius guardian, from his hands  
' Take back the charge grown weightier, and thyself  
' Commit its safety to the chance of war.  
· Nor blame nor glory shall be mine to-day.  
'Thy prayers unjustly, Caesar, have prevailed:  
' We fight! What wickedness, what woes on men,  
' Destruction on what realms this dawn shall bring!  
' Crimson with Roman blood yon stream shall run.  
' Would that (without the ruin of our cause)  
' The first fell bolt hurled on this cursed day  
' Might strike me lifeless! Victory to me  
' Were not more joyful, for this battle brings  
' A name of pity or a name of hate.  
' The loser bears the burden of defeat;  
' The victor wins, but conquest is a crime.'  
Thus to the soldiers, burning for the fray,  
He yields, forbidding, and throws down the reins.  
So may a sailor give the winds control  
Upon his barque, which, driven by the seas,  
Bears him an idle burden. Now the camp  
Hums with impatience, and the brave man's heart  
With beats tumultuous throbs against his breast;  
And all the host had standing in their looks  
The paleness of the death that was to come.^[These two lines are taken from Ben Jonson's 'Catiline,' act v., scene 6.]  
On that day's fight 'twas manifest that Rome  
And all the future destinies of man  
Hung trembling; and by weightier dread possessed,  
They knew not danger. Who would fear for self  
Should ocean rise and whelm the mountain tops,  
And sun and sky descend upon the earth  
In universal chaos? Every mind  
Is bent upon Pompeius, and on Rome.  
They trust no sword until its deadly point  
Glows on the sharpening stone; no lance will serve  
Till straightened for the fray; each bow is strung  
Anew, and arrows chosen for their work  
Fill all the quivers; horsemen try the curb  
And fit the bridle rein and whet the spur.  
If toils divine with human may compare,  
'Twas thus, when Phlegra bore the giant crew,^[See Book IV., 668. 'Pallene' (line 175) is to be understood as meaning Phlegra.]  
In Etna's furnace glowed the sword of Mars,  
Neptunus' trident felt the flame once more;  
And great Apollo after Python slain  
Sharpened his darts afresh: on Pallas' shield  
Was spread anew the dread Medusa's hair;  
And for the battle in Pallene's fields  
The Cyclops forged new thunderbolts for Jove.  
Yet Fortune failed not, as they sought the field,  
In various presage of the ills to come;  
All heaven opposed their march: portentous fire  
In columns filled the plain, and torches blazed:  
And thirsty whirlwinds mixed with meteor bolts  
Smote on them as they strode, whose sulphurous flames  
Perplexed the vision. Crests were struck from helms;  
The melted sword-blade flowed upon the hilt:  
The spear ran liquid, and the hurtful steel  
Smoked with a sulphur that had come from heaven.  
Nay, more, the standards, hid by swarms of bees  
Innumerable, weighed the bearer down,  
Scarce lifted from the earth; bedewed with tears;  
No more of Rome the standards,^[Henceforth to be the standards of the Emperor.] or her state.  
And from the altar fled the frantic bull  
To fields afar; nor was a victim found  
To grace the sacrifice of coming doom.  
But thou, O Caesar, to what gods of ill  
Didst thou appeal? What furies didst thou call,  
What powers of madness and what Stygian Kings  
Whelmed in th' abyss of hell? Didst favour gain  
By sacrifice in this thine impious war?  
Strange sights were seen; or caused by hands divine  
Or due to fearful fancy. Haemus' top  
Plunged headlong in the valley, Pindus met  
With high Olympus, while at Ossa's feet  
Red ran Boebeis,^[A lake at the foot of Mount Ossa. Pindus, Ossa, Olympus, and, above all, Haemus (the Balkans) were at a long distance from Pharsalia. Comp. Book VI., 678.] and Pharsalia's field  
Gave warlike voices as in depth of night.  
Now darkness came upon their wondering gaze,  
Now daylight pale and wan, their helmets wreathed  
In pallid mist; the spirits of their sires  
Hovered in air, and shades of kindred dead  
Passed flitting through the gloom. Yet had the host,  
Conscious of guilty prayers, and of the hope  
To do to death their brothers and their sires,  
One solace: that they found in hearts amazed  
With horrors, and in earth and air distraught,  
A happy omen of the crimes to come.  
Was't strange that peoples whom their latest day  
Of happy life awaited (if the mind  
Of man foreknows) should tremble with affright?  
Romans who dwelt by far Araxes' stream,  
And Tyrian Gades,^[Gades (Cadiz) is stated to have been founded by the Phoenicians about 1000 BC.] in whatever clime,  
'Neath every sky, struck by mysterious dread  
Were plunged in sorrow-yet rebuked the tear,  
For yet they knew not of the fatal day.  
Thus on Euganean hills^[This alludes to the story told by Plutarch ('Caesar,' 47), that, at Patavium, Caius Cornelius, a man reputed for skill in divination, and a friend of Livy the historian, was sitting to watch the birds that day. 'And first of all (as Livius says) he discovered the time of the battle, and he said to those present that the affair was now deciding and the men were going into action. Looking again, and observing the signs, he sprang up with enthusiasm and called out, "You conquer, Caesar."' (Long's translation.)] where sulphurous fumes  
Disclose the rise of Aponus^[The Fontes Aponi were warm springs near Padua. An altar, inscribed to Apollo Aponus, was found at Ribchester, and is now at St. John's College, Cambridge. (Wright, 'Celt, Roman, and Saxon,' p. 320.)] from earth,  
And where Timavus broadens in the meads,  
An augur spake: 'The last great day is come;  
' To-day in battle meet the impious arms  
' Of Caesar and of Magnus.' Or he saw  
The bolts of Jupiter, predicting ill;  
Or else the sky discordant o'er the space  
Of heaven, from pole to pole; or else perchance  
The sun was sad and misty in the height  
And told the battle by his wasted beams.  
By Nature's fiat that Thessalian day  
Passed not as others; if the gifted sense  
Of reading portents had been given to all,  
All men had known Pharsalia. Gods of heaven!  
How do ye mark the great ones of the earth!  
The world gives tokens of their weal or woe;  
The sky records their fates: in distant climes  
To future races shall their tale be told,  
Or by the fame alone of mighty deeds  
Had in remembrance, or by this my care  
Borne through the centuries: and men shall read  
In hope and fear the story of the war  
And breathless pray, as though it were to come,  
For that long since accomplished; and for thee  
E'en then, Pompeius, shall that prayer be given.  
[^aae5683c83b94cafaeeb35258ab2d71c]

  
## To A Village By Road

From Veldidena to a village is at least 41 miles when travelling by road. 

He had set out from Veldidena amidst a throng travelling the same way. He passes another milestone. His shoes are covered in dust from the road. On the road from Veldidena to a village there is a village, in which there is a temple and grove. There is a fountain of cold water springing from the rock. Next to the straight road that leads to a village, there is visible a sculpted tomb. 

  
## A Village To Aguntum By Road

From a village to Aguntum is at least 60 miles when travelling by road. 

He left the city early, before the rising of the sun. Next to the straight road that leads to Aguntum, there is visible a sculpted tomb. He had set out from a village amidst a throng travelling the same way. On the road from a village to Aguntum there is a village, in which there is a temple and grove. By the road is a salt spring. There is a fountain of cold water springing from the rock. They pass a pillar on the right surmounted by a stone urn. 

While he was visiting the countryside near that place, he made a point of copying down what Pausanias, fl. ca. 150-175 had written.

## On The Subject Of The Countryside Near That Place


Smyrna, one of the twelve Aeolian cities, built on that site which even now they call the old city, was seized by Ionians who set out from Colophon and displaced the Aeolians; subsequently, however, the Ionians allowed the Smyrnaeans to take their place in the general assembly at Panionium. The modern city was founded by Alexander, the son of Philip, in accordance with a vision in a dream.

It is said that Alexander was hunting on Mount Pagus, and that after the hunt was over he came to a sanctuary of the Nemeses, and found there a spring and a plane-tree in front of the sanctuary, growing over the water. While he slept under the plane-tree it is said that the Nemeses appeared and bade him found a city there and to remove into it the Smyrnaeans from the old city.

So the Smyrnaeans sent ambassadors to Clarus to make inquiries about the circumstance, and the god made answer:—Thrice, yes, four times blest will those men beWho shall dwell in Pagus beyond the sacred Meles.So they migrated of their own free will, and believe now in two Nemeses instead of one, saying that their mother is Night, while the Athenians say that the father of the goddess^[That is, Nemesis.] in Rhamnus is Ocean.

The land of the Ionians has the finest possible climate, and sanctuaries such as are to be found nowhere else. First because of its size and wealth is that of the Ephesian goddess, and then come two unfinished sanctuaries of Apollo, the one in Branchidae, in Milesian territory, and the one at Clarus in the land of the Colophonians. Besides these, two temples in Ionia were burnt down by the Persians, the one of Hera in Samos and that of Athena at Phocaea. Damaged though they are by fire, I found them a wonder.

You would be delighted too with the sanctuary of Heracles at Erythrae and with the temple of Athena at Priene, the latter because of its image and the former on account of its age. The image is like neither the Aeginetan, as they are called, nor yet the most ancient Attic images; it is absolutely Egyptian, if ever there was such. There was a wooden raft, on which the god set out from Tyre in Phoenicia. The reason for this we are not told even by the Erythraeans themselves.

They say that when the raft reached the Ionian sea it came to rest at the cape called Mesate ( Middle) which is on the mainland, just midway between the harbor of the Erythraeans and the island of Chios. When the raft rested off the cape the Erythraeans made great efforts, and the Chians no less, both being keen to land the image on their own shores.

At last a man of Erythrae (his name was Phormio) who gained a living by the sea and by catching fish, but had lost his sight through disease, saw a vision in a dream to the effect that the women of Erythrae must cut off their locks, and in this way the men would, with a rope woven from the hair, tow the raft to their shores. The women of the citizens absolutely refused to obey the dream;

but the Thracian women, both the slaves and the free who lived there, offered themselves to be shorn. And so the men of Erythrae towed the raft ashore. Accordingly no women except Thracian women are allowed within the sanctuary of Heracles, and the hair rope is still kept by the natives. The same people say that the fisherman recovered his sight and retained it for the rest of his life.

There is also in Erythrae a temple of Athena Polias and a huge wooden image of her sitting on a throne; she holds a distaff in either hand and wears a firmament on her head. That this image is the work of Endoeus we inferred, among other signs, from the workmanship, and especially from the white marble images of Graces and Seasons that stand in the open before the entrance. A sanctuary too of Asclepius was made by the Smyrnaeans in my time between Mount Coryphe and a sea into which no other water flows.

Ionia has other things to record besides its sanctuaries and its climate. There is, for instance, in the land of the Ephesians the river Cenchrius, the strange mountain of Pion and the spring Halitaea. The land of Miletus has the spring Biblis, of whose love the poets have sung. In the land of Colophon is the grove of Apollo, of ash-trees, and not far from the grove is the river Ales, the coldest river in Ionia.

In the land of Lebedus are baths, which are both wonderful and useful. Teos, too, has baths at Cape Macria, some in the clefts of the rock, filled by the tide, others made to display wealth. The Clazomenians have baths (incidentally they worship Agamemnon) and a cave called the cave of the mother of Pyrrhus; they tell a legend about Pyrrhus the shepherd.

The Erythraeans have a district called Calchis, from which their third tribe takes its name, and in Calchis is a cape stretching into the sea, and on it are sea baths, the most useful baths in Ionia. The Smyrnaeans have the river Meles, with its lovely water, and at its springs is the grotto, where they say that Homer composed his poems.

One of the sights of Chios is the grave of Oenopion, about whose exploits they tell certain legends. The Samians have on the road to the Heraeum the tomb of Rhadine and Leontichus, and those who are crossed in love are wont to go to the tomb and pray. Ionia, in fact, is a land of wonders that are but little inferior to those of Greece.[^3831e69162544136b02d7d2ff40fbd21]

  
## Leaving Aguntum By Road

Intending to travel by road to Iulium Carnicum, Virgil left Aguntum. It was a journey of about 33 miles. 

This is a smooth road, by which many wagons were bringing wood to Iulium Carnicum. Virgil saw this on a roadside tomb: Liq(uamen) ar(gutum) / sum(aur) / exce[l(lens)] / C[- - -]. As they go up from Aguntum, they see the ruined walls. There is a fountain of cold water springing from the rock. 

While he was visiting the countryside near that place, he made a point of copying down what Pausanias, fl. ca. 150-175 had written.

## A Story By Pausanias, Fl. Ca. 150-175 About The Countryside Near That Place From _Description Of Greece_


The ancient image of Athena Alea, and with it the tusks of the Calydonian boar, were carried away by the Roman emperor Augustus after his defeat of Antonius and his allies, among whom were all the Arcadians except the Mantineans.

It is clear that Augustus was not the first to carry away from the vanquished votive offerings and images of gods, but was only following an old precedent. For when Troy was taken and the Greeks were dividing up the spoils, Sthenelus the son of Capaneus was given the wooden image of Zeus Herceius (Of the Courtyard); and many years later, when Dorians were migrating to Sicily, Antiphemus the founder of Gela, after the sack of Omphace, a town of the Sicanians, removed to Gela an image made by Daedalus.

Xerxes, too, the son of Dareius, the king of Persia, apart from the spoil he carried away from the city of Athens, took besides, as we know, from Brauron the image of Brauronian Artemis, and furthermore, accusing the Milesians of cowardice in a naval engagement against the Athenians in Greek waters, carried away from them the bronze Apollo at Branchidae. This it was to be the lot of Seleucus afterwards to restore to the Milesians, but the Argives down to the present still retain the images they took from Tiryns; one, a wooden image, is by the Hera, the other is kept in the sanctuary of Lycian Apollo.

Again, the people of Cyzicus, compelling the people of Proconnesus by war to live at Cyzicus, took away from Proconnesus an image of Mother Dindymene. The image is of gold, and its face is made of hippopotamus teeth instead of ivory. So the emperor Augustus only followed a custom in vogue among the Greeks and barbarians from of old. The image of Athena Alea at Rome is as you enter the Forum made by Augustus.

Here then it has been set up, made throughout of ivory, the work of Endoeus. Those in charge of the curiosities say that one of the boar's tusks has broken off; the remaining one is kept in the gardens of the emperor, in a sanctuary of Dionysus, and is about half a fathom long.[^9e91ff36edf744a8a20ad4aba0ed56ce]

  
## From Iulium Carnicum To A Village

Virgil departed from Iulium Carnicum, intending to travel by road to a village, about 9 miles away. 

Now the road is quieter. He passes another milestone. Water has washed out the road, making for slow going. He left the city early, before the rising of the sun. On the road from Iulium Carnicum to a village there is a village, in which there is a temple and grove. He had set out from Iulium Carnicum amidst a throng travelling the same way. By the road is a salt spring. A cloud passes in front of the sun. A caravan from a village passed by. 

  
## From A Village To Santicum

Leaving a village, Virgil set out for Santicum by road, about 47 miles away. 

There is a fountain of cold water springing from the rock. Next to the straight road that leads to Santicum, there is visible a sculpted tomb. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Lucius Pinxit: he pondered the sight of this inscription. 

He would later record what Herodotus had said about the countryside near that place.

## A Story About The Countryside Near That Place


This is enough of the story told by Etearchus the Ammonian; except he said that the Nasamonians returned, as the men of Cyrene told me, and that the people to whose country they came were all wizards; as to the river that ran past the city, Etearchus guessed it to be the Nile; and reason proves as much. For the Nile flows from Libya, right through the middle of it; and as I guess, reasoning about things unknown from visible signs, it rises proportionally as far away as does the Ister.^[\rendergreek{ἐκ τῶν ἴσων μέτρων} is an obscure expression. What Hdt. appears to mean is, that as the Nile (according to him) flows first from W. to E. and then turns northward, so the Danube flows first from W. to E. and then (as he says) from N. to S.; and so the rivers in a manner correspond: one crosses Africa, the other Europe.] For the Ister flows from the land of the Celts and the city of Pyrene through the very middle of Europe; now the Celts live beyond the Pillars of Heracles, being neighbors of the Cynesii, who are the westernmost of all the peoples inhabiting Europe. The Ister, then, flows clean across Europe and ends its course in the Euxine sea, at Istria, which is inhabited by Milesian colonists.[^27d8b0f312324788955119d50ee80276]

  
## Travelling By Road To A Village

Leaving Santicum, Virgil set out for a village by road, a journey of about 47 miles. 

An oxcart passes, loaded with grain. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Now the road is quieter. A cloud passes in front of the sun. This is a smooth road, by which many wagons were bringing wood to a village. His shoes are covered in dust from the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

\newpage

# A Village To A Village
  
## After A Village

Virgil departed from a village, intending to travel by road to Santicum, a distance of about 47 miles. 

His shoes are covered in dust from the road. There is a fountain of cold water springing from the rock. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He left the city early, before the rising of the sun. As they go up from a village, they see the ruined walls. Along the road are graves, and a cenotaph. Water has washed out the road, making for slow going. They pass a pillar on the right surmounted by a stone urn. On the road from a village to Santicum there is a village, in which there is a temple and grove. 

While he visited his friend at Aquileia, he was pleased to discover _On Architecture_, by Vitruvius Pollio. Picking it up, he read:

## A Story By Vitruvius Pollio About Aquileia From _On Architecture_


1\. FOR fortified towns the following general principles are to be observed. First comes the choice of a very healthy site. Such a site will be high, neither misty nor frosty, and in a climate neither hot nor cold, but temperate; further, without marshes in the neighbourhood. For when the morning breezes blow toward the town at sunrise, if they bring with them mists from marshes and, mingled with the mist, the poisonous breath of the creatures of the marshes to be wafted into the bodies of the inhabitants, they will make the site unhealthy. Again, if the town is on the coast with a southern or western exposure, it will not be healthy, because in summer the southern sky grows hot at sunrise and is fiery at noon, while a western exposure grows warm after sunrise, is hot at noon, and at evening all aglow.

2\. These variations in heat and the subsequent cooling off are harmful to the people living on such sites. The same conclusion may be reached in the case of inanimate things. For instance, nobody draws the light for covered wine rooms from the south or west, but rather from the north, since that quarter is never subject to change but is always constant and unshifting. So it is with granaries: grain exposed to the sun's course soon loses its good quality, and provisions and fruit, unless stored in a place unexposed to the sun's course, do not keep long.

3\. For heat is a universal solvent, melting out of things their power of resistance, and sucking away and removing their natural strength with its fiery exhalations so that they grow soft, and hence weak, under its glow. We see this in the case of iron which, however hard it may naturally be, yet when heated thoroughly in a furnace fire can be easily worked into any kind of shape, and still, if cooled while it is soft and white hot, it hardens again with a mere dip into cold water and takes on its former quality.

4\. We may also recognize the truth of this from the fact that in summer the heat makes everybody weak, not only in unhealthy but even in healthy places, and that in winter even the most unhealthy districts are much healthier because they are given a solidity by the cooling off. Similarly, persons removed from cold countries to hot cannot endure it but waste away; whereas those who pass from hot places to the cold regions of the north, not only do not suffer in health from the change of residence but even gain by it.

5\. It appears, then, that in founding towns we must beware of districts from which hot winds can spread abroad over the inhabitants. For while all bodies are composed of the four elements (in Greek \rendergreek{στοιχεῖα}), that is, of heat, moisture, the earthy, and air, yet there are mixtures according to natural temperament which make up the natures of all the different animals of the world, each after its kind.

6\. Therefore, if one of these elements, heat, becomes predominant in any body whatsoever, it destroys and dissolves all the others with its violence. This defect may be due to violent heat from certain quarters of the sky, pouring into the open pores in too great proportion to admit of a mixture suited to the natural temperament of the body in question. Again, if too much moisture enters the channels of a body, and thus introduces disproportion, the other elements, adulterated by the liquid, are impaired, and the virtues of the mixture dissolved. This defect, in turn, may arise from the cooling properties of moist winds and breezes blowing upon the body. In the same way, increase or diminution of the proportion of air or of the earthy which is natural to the body may enfeeble the other elements; the predominance of the earthy being due to overmuch food, that of air to a heavy atmosphere.

7\. If one wishes a more accurate understanding of all this, he need only consider and observe the natures of birds, fishes, and land animals, and he will thus come to reflect upon distinctions of temperament. One form of mixture is proper to birds, another to fishes, and a far different form to land animals. Winged creatures have less of the earthy, less moisture, heat in moderation, air in large amount. Being made up, therefore, of the lighter elements, they can more readily soar away into the air. Fish, with their aquatic nature, being moderately supplied with heat and made up in great part of air and the earthy, with as little of moisture as possible, can more easily exist in moisture for the very reason that they have less of it than of the other elements in their bodies; and so, when they are drawn to land, they leave life and water at the same moment. Similarly, the land animals, being moderately supplied with the elements of air and heat, and having less of the earthy and a great deal of moisture, cannot long continue alive in the water, because their portion of moisture is already abundant.

8\. Therefore, if all this is as we have explained, our reason showing us that the bodies of animals are made up of the elements, and these bodies, as we believe, giving way and breaking up as a result of excess or deficiency in this or that element, we cannot but believe that we must take great care to select a very temperate climate for the site of our city, since healthfulness is, as we have said, the first requisite.

9\. I cannot too strongly insist upon the need of a return to the method of old times. Our ancestors, when about to build a town or an army post, sacrificed some of the cattle that were wont to feed on the site proposed and examined their livers. If the livers of the first victims were dark-coloured or abnormal, they sacrificed others, to see whether the fault was due to disease or their food. They never began to build defensive works in a place until after they had made many such trials and satisfied themselves that good water and food had made the liver sound and firm. If they continued to find it abnormal, they argued from this that the food and water supply found in such a place would be just as unhealthy for man, and so they moved away and changed to another neighbourhood, healthfulness being their chief object.

10\. That pasturage and food may indicate the healthful qualities of a site is a fact which can be observed and investigated in the case of certain pastures in Crete, on each side of the river Pothereus, which separates the two Cretan states of Gnosus and Gortyna. There are cattle at pasture on the right and left banks of that river, but while the cattle that feed near Gnosus have the usual spleen, those on the other side near Gortyna have no perceptible spleen. On investigating the subject, physicians discovered on this side a kind of herb which the cattle chew and thus make their spleen small. The herb is therefore gathered and used as a medicine for the cure of splenetic people. The Cretans call it \rendergreek{ἄσπληνον}. From food and water, then, we may learn whether sites are naturally unhealthy or healthy.

11\. If the walled town is built among the marshes themselves, provided they are by the sea, with a northern or north-eastern exposure, and are above the level of the seashore, the site will be reasonable enough. For ditches can be dug to let out the water to the shore, and also in times of storms the sea swells and comes backing up into the marshes, where its bitter blend prevents the reproductions of the usual marsh creatures, while any that swim down from the higher levels to the shore are killed at once by the saltness to which they are unused. An instance of this may be found in the Gallic marshes surrounding Altino, Ravenna, Aquileia, and other towns in places of the kind, close by marshes. They are marvellously healthy, for the reasons which I have given.

12\. But marshes that are stagnant and have no outlets either by rivers or ditches, like the Pomptine marshes, merely putrefy as they stand, emitting heavy, unhealthy vapours. A case of a town built in such a spot was Old Salpia in Apulia, founded by Diomede on his way back from Troy, or, according to some writers, by Elpias of Rhodes. Year after year there was sickness, until finally the suffering inhabitants came with a public petition to Marcus Hostilius and got him to agree to seek and find them a proper place to which to remove their city. Without delay he made the most skilful investigations, and at once purchased an estate near the sea in a healthy place, and asked the Senate and Roman people for permission to remove the town. He constructed the walls and laid out the house lots, granting one to each citizen for a mere trifle. This done, he cut an opening from a lake into the sea, and thus made of the lake a harbour for the town. The result is that now the people of Salpia live on a healthy site and at a distance of only four miles from the old town.[^1ca5eac8079446e19a0aab6873e3c277]

  
## Travelling By Road

Virgil departed from Santicum, intending to travel by road to Virunum, a distance of about 28 miles. 

Along the road are graves, and a cenotaph. An oxcart passes, loaded with grain. This is a smooth road, by which many wagons were bringing wood to Virunum. Next to the straight road that leads to Virunum, there is visible a sculpted tomb. 

The library at Aquileia happened to have a copy of _Tiberius_, where Virgil encountered it.

## A Story About Aquileia


After assuming the manly habit, he spent his youth, and the rest of his life until he succeeded to the government, in the following manner: he gave the people an entertainment of gladiators, in memory of his father, and another for his grandfather Drusus, at different times and in different places: the first in the forum, the second in the amphitheatre; some gladiators who had been honourably discharged, being induced to engage again, by a reward of a hundred thousand sesterces. He likewise exhibited public sports, at which he was not present himself. All these he performed with great magnificence, at the expense of his mother and father-in-law. He married Agrippina, the daughter of Marcus Agrippa, and granddaughter of Caecilius Atticus, a Roman knight, the same person to whom Cicero has addressed so many epistles. After having by her his son Drusus, he was obliged to part with her,^[A.U.C. 744] though she retained his affection, and was again pregnant, to make way for marrying Augustus's daughter Julia. But this he did with extreme reluctance; for, besides having the warmest attachment to Agrippina, he was disgusted with the conduct of Julia, who had made indecent advances to him during the lifetime of her former husband; and that she was a woman of loose character, was the general opinion. At divorcing Agrippina he felt the deepest regret; and upon meeting her afterwards, he looked after her with eyes so passionately expressive of affection, that care was taken she should never again come in his sight. At first, however, he lived quietly and happily with Julia; but a rupture soon ensued, which became so violent, that after the loss of their son, the pledge of their union, who was born at Aquileia and died in infancy,^[A.U.C. 735] he never would sleep with her more. He lost his brother Drusus in Germany, and brought his body to Rome, travelling all the way on foot before it.[^27cf1bf7a7344b2494b84dc0916c18be]

  
## To Poetovio By River

Leaving Virunum, Virgil set out for Poetovio on a boat heading downstream, at least 96 miles. 

The sun beats down. 

While he visited his friend at Siscia, he was pleased to discover _Against Verres_, by Cicero, Marcus Tullius. Picking it up, he read:

## An Extract From _Against Verres_ By Cicero, Marcus Tullius


At that time the same Diana of which I am speaking is restored with the greatest care to the Segestans. It is taken back to Segesta; it is replaced in its ancient situation, to the greatest joy and delight of all the citizens. It was placed at Segesta on a very lofty pedestal, on which was cut in large letters the name of Publius Africanus; and a statement was also engraved that "he had restored it after having taken Carthage." It was worshipped by the citizens; it was visited by all strangers; when I was quaestor it was the very first thing, they showed me. It was a very large and tall statue with a flowing robe, but in spite of its large size it gave the idea of the age and dress of a virgin; her arrows hung from her shoulder, in her left hand she carried her bow, her right hand held a burning torch.[^03b5e5e4e51a498ebb2ad29337cdf7f1]

  
## To Mursa

From Poetovio to Mursa is a distance of about 187 miles when travelling on a military boat floating downstream. 

The countryside is quieter than the city. Dis Manib(us) sacrum // Asper / eq(ues) alae / Hisp(anorum) I Aurian(ae) / Iucundo Talal/ni f(ilio) [[principi]] civ/itatis Azalior/um patri vivo et / [&: he pondered the sight of this inscription. 

While he was visiting Siscia, he made a point of copying down what Cicero, Marcus Tullius had written.

## Siscia In _Against Verres_


As he did not relax in his demand, but urged it every day with daily increasing earnestness, the matter was brought before their senate. His demand raises a violent outcry on all sides. And so at that time, and at his first arrival at Segesta, it is refused. Afterwards, whatever burdens could be imposed on any city in respect of exacting sailors and rowers, or in levying corn, he imposed on the Segestans beyond all other cities, and a good deal more than they could bear. Besides that, he used to summon their magistrates before him; he used to send for all the most noble and most virtuous of the citizens, to hurry them about with him to all the courts of justice in the province, to threaten every one of them separately to be the ruin of him, and to announce to them all in a body that he would utterly destroy their city. Therefore, at last, the Segestans, subdued by much ill-treatment and by great fear, resolved to obey the command of the praetor. With great grief and lamentation on the part of the whole city, with many tears and wailings on the part of all the men and women, a contract is advertised for taking down the statue of Diana.[^0c096088cb344ccb925802c8d3782054]

  
## From Mursa To Cibalae

From Mursa to Cibalae is at least 21 miles when travelling by road. 

Now the road is quieter. Water has washed out the road, making for slow going. There a spring wells up, and around about it is a meadow. They pass a pillar on the right surmounted by a stone urn. Along the road are graves, and a cenotaph. His shoes are covered in dust from the road. On the road from Mursa to Cibalae there is a village, in which there is a temple and grove. A cloud passes in front of the sun. There is a fountain of cold water springing from the rock. 

The library at the countryside near that place happened to have a copy of _Historiae_, where Virgil encountered it.

## A Story About The Countryside Near That Place By Cornelius Tacitus


"The entire army of Vitellius," he said, "has already arrived. Nor have they much strength in their rear, since Gaul is ready to rise, and to abandon the banks of the Rhine, when such hostile tribes are ready to burst in, would not answer his purpose. A hostile people and an intervening sea keep from him the army of Britain; Spain is not over full of troops; Gallia Narbonensis has been cowed by the attack of our ships and by a defeat; Italy beyond the Padus is shut in by the Alps, cannot be relieved from the sea, and has been exhausted by the passage of his army. For that army there is nowhere any corn, and without supplies an army cannot be kept together. Then the Germans, the most formidable part of the enemy's forces, should the war be protracted into the summer, will sink with enfeebled frames under the change of country and climate. Many a war, formidable in its first impetuosity, has passed into nothing through the weariness of delay. We, on the other hand, have on all sides abundant resources and loyal adherents. We have Pannonia, Mœsia, Dalmatia, the East with its armies yet intact, we have Italy and Rome, the capital of the Empire, the Senate, and the people, names that never lose their splendour, though they may sometimes be eclipsed. We have the wealth of the State and of private individuals. We have a vast supply of money, which in a civil war is a mightier weapon than the sword. Our soldiers are inured to the climate of Italy or to yet greater heat. We have the river Padus on our front, and cities strongly garrisoned and fortified, none of which will surrender to the enemy, as the defence of Placentia has proved. Let Otho therefore protract the war. In a few days the 14th legion, itself highly renowned, will arrive with the troops from Mœsia. He may then again consider the question, and should a battle be resolved on, we shall fight with increased strength."[^59ef153628cc426ab9611bca33eb09f1]

  
## To Sirmium By Road

Virgil departed from Cibalae, intending to travel by road to Sirmium, a distance of about 46 miles. 

Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. The road narrows here, an orchard wall encroaching on it. A grove of Minerva is hard by the road, a grove of poplar trees. He had set out from Cibalae amidst a throng travelling the same way. There a spring wells up, and around about it is a meadow. He passes another milestone. Workers are raising the level of the road. This is a smooth road, by which many wagons were bringing wood to Sirmium. 

All of this brought to his mind what Julius Caesar had said about the countryside near that place:

## What Julius Caesar Once Said About The Countryside Near That Place


Young Pompey, who commanded the Egyptian fleet, having notice of this, came to Oricum; weighed up the vessel that had been sunk in the mouth of the harbour; and, after an obstinate resistance, took the other, which had been placed there by Acilius, to guard the haven. He then brought forward his fleet, on which he had raised towers, to fight with the greater advantage; and having surrounded the town on all sides, attacked it by land with scaling ladders, and by sea from the towers, sending fresh men continually in the place of those that were fatigued, and thereby obliging us to yield, through weariness and wounds. At the same time he seized an eminence, on the other side of the town, which seemed a kind of natural mole, and almost formed a peninsula over against Oricum; and by means of this neck of land, carried four small galleys, upon rollers, into the inner part of the haven. Thus the galleys, that were made fast to the land, and destitute of troops, being attacked on all sides, four were carried off, and the rest burned. This affair despatched, he left D. Laelius, whom he had taken from the command of the Asiatic fleet, to prevent the importation of provisions from Biblis and Amantia; and sailing for Lissus, attacked and burned the thirty transports which Antony had left in that haven. He endeavoured likewise to take the town; but the Roman citizens of that district, aided by the garrison Caesar had left, defended it so well, that at the end of three days, he retired without effecting his purpose, having lost some men in the attempt.[^c7b390c4a59540129de75c4961df96f5]

  
## Travelling By Road

Leaving Sirmium, Virgil set out for a village by road, about 56 miles away. 

Workers are raising the level of the road. The sun beats down. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There a spring wells up, and around about it is a meadow. A grove of Minerva is hard by the road, a grove of poplar trees. By the road is a salt spring. 

  
## The Journey To A Village

Virgil departed from a village, intending to travel by road to a village, a distance of about 130 miles. 

Water has washed out the road, making for slow going. They pass a pillar on the right surmounted by a stone urn. A caravan from a village passed by. An oxcart passes, loaded with grain. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A grove of Minerva is hard by the road, a grove of poplar trees. The road narrows here, an orchard wall encroaching on it. 

\newpage

# A Village To Viminacium
  
## Departing From A Village

Virgil departed from a village, intending to travel by road to Narona, a distance of about 15 miles. 

An oxcart passes, loaded with grain. Next to the straight road that leads to Narona, there is visible a sculpted tomb. This is a smooth road, by which many wagons were bringing wood to Narona. Now the road is quieter. A caravan from Narona passed by. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

While he visited his friend at the countryside near that place, he was pleased to discover _Divus Claudius_, by Suetonius ca. 69-ca. 122. Picking it up, he read:

## An Account Of The Countryside Near That Place


Conspiracies, however, were formed against him, not only by individuals separately, but by a faction; and at last his government was disturbed with a civil war. A low fellow was found with a poniard about him, near his chamber, at midnight. Two men of the equestrian order were discovered waiting for him in the streets, armed with a tuck and a huntsman's dagger; one of them intending to attack him as he came out of the theatre, and the other as he was sacrificing in the temple of Mars. Gallus Asinius and Statilius Corvinus, grandsons of the two orators, Pollio and Messala,^[Pollio and Messala were distinguished orators, who flourished under the Caesars Julius and Augustus. ] formed a conspiracy against him, in which they engaged many of his freedmen and slaves. Furius Camillus Scribonianus, his lieutenant in Dalmatia, broke into rebellion, but was reduced in the space of five days; the legions which he had seduced from their oath of fidelity relinquishing their purpose, upon an alarm occasioned by ill omens. For when orders were given them to march, to meet their new emperor, the eagles could not be decorated, nor the standards pulled out of the ground, whether it was by accident, or a divine interposition.[^7c1c87235fde437f8a22842ad537d2ec]

  
## From Narona To A Village

Leaving Narona, Virgil set out for a village by road, about 15 miles away. 

As they go up from Narona, they see the ruined walls. A grove of Minerva is hard by the road, a grove of poplar trees. There a spring wells up, and around about it is a meadow. He left the city early, before the rising of the sun. They pass a pillar on the right surmounted by a stone urn. By the road is a salt spring. He passes another milestone. Water has washed out the road, making for slow going. 

  
## From A Village To A Village

Intending to travel by road to a village, Virgil left a village. It was a distance of about 130 miles. 

This is a smooth road, by which many wagons were bringing wood to a village. There a spring wells up, and around about it is a meadow. He left the city early, before the rising of the sun. He passes another milestone. Water has washed out the road, making for slow going. By the road is a salt spring. On the road from a village to a village there is a village, in which there is a temple and grove. A grove of Minerva is hard by the road, a grove of poplar trees. Workers are raising the level of the road. 

  
## After A Village

Virgil departed from a village, intending to travel by road to Domavium, about 18 miles away. 

He had set out from a village amidst a throng travelling the same way. This is a smooth road, by which many wagons were bringing wood to Domavium. The road narrows here, an orchard wall encroaching on it. He left the city early, before the rising of the sun. His shoes are covered in dust from the road. An oxcart passes, loaded with grain. Along the road are graves, and a cenotaph. Next to the straight road that leads to Domavium, there is visible a sculpted tomb. A caravan from Domavium passed by. 

While he was visiting the countryside near that place, he made a point of copying down what Polybius had written.

## An Extract From _Histories_ By Polybius


The Epirotes and King Philip on hearing the ambassadors consented to admit the Messenians to alliance; but though the conduct of the Aetolians caused them momentary indignation, they were not excessively moved by it, because it was no more than what the Aetolians habitually did. Their anger, therefore, was short-lived, and they presently voted against going to war with them. So true is it that an habitual course of wrong-doing finds readier pardon than when it is spasmodic or isolated. The former, at any rate, was the case with the Aetolians: they perpetually plundered Greece, and levied unprovoked war upon many of its people: they did not deign either to make any defence to those who complained, but answered only by additional insults if any one challenged them to arbitration for injuries which they had inflicted, or indeed which they meditated inflicting. And yet the Lacedaemonians, who had but recently been liberated by means of Antigonus and the generous zeal of the Achaeans, and though they were bound not to commit any act of hostility towards the Macedonians and Philip, sent clandestine messages to the Aetolians, and arranged a secret treaty of alliance and friendship with them.

The army had already been enrolled from the Achaeans of military age, and had been assigned to the duty of assisting the Lacedaemonians and Messenians, when Scerdilaidas and Demetrius of Pharos sailed with ninety galleys beyond Lissus, contrary to the terms of their treaty with Rome. These men first touched at Pylos, and failing in an attack upon it, they separated: Demetrius making for the Cyclades, from some of which he exacted money and plundered others; while Scerdilaidas, directing his course homewards, put in at Naupactus with forty galleys at the instigation of Amynas, king of the Athamanes, who happened to be his brother-in-law; and after making an agreement with the Aetolians, by the agency of Agelaus, for a division of spoils, he promised to join them in their invasion of Achaia. With this agreement made with Scerdilaidas, and with the co-operation of the city of Cynaetha, Agelaus, Dorimachus, and Scopas, collected a general levy of the Aetolians, and invaded Achaia in conjunction with the Illyrians.[^d7e5f655093349cfb50201c608932fee]

  
## Leaving Domavium By Road

From Domavium to a village is at least 18 miles when travelling by road. 

On the road from Domavium to a village there is a village, in which there is a temple and grove. He left the city early, before the rising of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. The road narrows here, an orchard wall encroaching on it. $?] / [- - - - - -] / [- - -]ABV[- - -] / [&?: he pondered the sight of this inscription. A cloud passes in front of the sun. The sun beats down. This is a smooth road, by which many wagons were bringing wood to a village. 

  
## The Journey To Sirmium

Intending to travel by road to Sirmium, Virgil left a village. It was about 56 miles away. 

There a spring wells up, and around about it is a meadow. He passes another milestone. The sun beats down. A cloud passes in front of the sun. 

The library at the countryside near that place happened to have a copy of _Histories_, where Virgil encountered it.

## An Extract From _Histories_ By Polybius


As soon therefore as the Macedonians approached, they began pouring out of the town, confident in their numbers and in the strength of the places. The king stationed his peltasts on the level ground, and ordered the light-armed troops to advance towards the hills and energetically engage the enemy. These orders being obeyed, the fight remained doubtful for a time; but presently Philip's men yielded to the inequality of the ground, and the superior number of the enemy, and gave way. Upon their retreating within the ranks of the peltasts, the sallying party advanced with feelings of contempt, and having descended to the same level as the peltasts joined battle with them. But the garrison of the citadel seeing Philip moving his divisions one after the other slowly to the rear, and believing that he was abandoning the field, allowed themselves to be insensibly decoyed out, in their confidence in the strength of their fortifications; and thus, leaving the citadel by degrees, kept pouring down by bye-ways into the lower plain, under the belief that they would have an opportunity of getting booty and completing the enemy's discomfiture. Meanwhile the division, which had been lying concealed on the side of the mainland, rose without being observed, and advanced at a rapid pace. At their approach the peltasts also wheeled round and charged the enemy. On this the troops from Lissus were thrown into confusion, and, after a straggling retreat, got safely back into the town; while the garrison which had abandoned the citadel got cut off from it by the rising of the troops which had been lying in ambush. The result accordingly was that what seemed hopeless, namely the capture of the citadel, was effected at once and without any fighting; while Lissus did not fall until next day, and then only after desperate struggles, the Macedonians assaulting with vigour and even terrific fury. Thus Philip having, beyond all expectation, made himself master of these places, reduced by this exploit all the neighbouring populations to obedience; so much so that the greater number of the Illyrians voluntarily surrendered their cities to his protection; for it had come to be believed that, after the storming of such strongholds as these, no fortification and no provision for security could be of any avail against the might of Philip.[^8c9d27258f4d4d17ae1eec01ec66277d]

  
## To Singidunum By River

Intending to travel on a military boat floating downstream to Singidunum, Virgil left Sirmium. It was about 85 miles away. 

He presses onward. 

While he was visiting the countryside near that place, he made a point of copying down what Thucydides had written.

## What Thucydides Once Said About The Countryside Near That Place


Meanwhile Sitacles opened negotiations with Perdiccas on the objects of his expedition; and finding that the Athenians, not believing that he would come, did not appear with their fleet, though they sent presents and envoys, despatched a large part of his army against the Chalcidians and Bottiaeans, and cutting them up inside their walls laid waste their country. While he remained in these parts, the people farther south, such as the Thessalians, and the Hellenes as far as Thermopylae, all feared that the army might advance against them, and prepared accordingly. These fears were shared by the Thracians beyond the Strymon to the north, who inhabited the plains, such as the Panaeans, the Odomanti, the Droi and the Dersaeans, all of whom are independent. It was even matter of conversation among the Hellenes who were enemies of Athens whether he might not be invited by his ally to advance also against them. Meanwhile he held Chalcidice and Bottice and Macedonia, and was ravaging them all; but finding that he was not succeeding in any of the objects of his invasion, and that his army was without provisions and was suffering from the severity of the season, he listened to the advice of Seuthes, son of Sparadocus, his nephew and highest officer, and decided to retreat without delay. This Seuthes had been secretly gained by Perdiccas by the promise of his sister in marriage with a rich dowry. In accordance with this advice, and after a stay of thirty days in all, eight of which were spent in Chalcidice, he retired home as quickly as he could; and Perdiccas afterwards gave his sister Stratonice to Seuthes as he had promised. Such was the history of the expedition of Sitalces.

[^418fb29555b042bd973dd1aed7e66e6d]

  
## From Singidunum To Viminacium

Virgil departed from Singidunum, intending to travel on a military boat floating downstream to Viminacium, about 49 miles away. 

He presses onward. The journey is more tiring than you might expect. 

All of this brought to his mind what Apollodorus had said about the countryside near that place:

## An Account Of The Countryside Near That Place


When Hercules heard that, he went to Tiryns and did as he was bid by Eurystheus. First, Eurystheus ordered him to bring the skin of the Nemean lion;^[As to the Nemean lion, compare Hes. Th. 326ff.; Bacch. 8.6ff., ed. Jebb; Soph. Trach. 1091ff.; Theocritus xxv.162ff.; Diod. 4.11.3ff.; Eratosthenes, Cat. 12; Tzetzes, Chiliades ii.232ff.; Hyginus, Fab. 30. According to Hesiod, the Nemean lion was begotten by Orthus, the hound of Geryon, upon the monster Echidna. Hyginus says that the lion was bred by the Moon.] now that was an invulnerable beast begotten by Typhon. On his way to attack the lion he came to Cleonae and lodged at the house of a day-laborer, Molorchus;^[As to Herakles and Molorchus, compare Tibullus iv.1.12ff.; Verg. G. 3.19, with Servius's note; Martial iv.64.30, ix.43.13; Statius, Sylv. iii.1.28.] and when his host would have offered a victim in sacrifice, Hercules told him to wait for thirty days, and then, if he had returned safe from the hunt, to sacrifice to Saviour Zeus, but if he were dead, to sacrifice to him as to a hero.^[The Greeks had two distinct words for sacrificing, according as the sacrifice was offered to a god or to a hero, that is, to a worshipful dead man; the former sacrifice was expressed by the verb \rendergreek{θύειν}, the latter by the verb \rendergreek{ἐναγίζειν.} The verbal distinction can hardly be preserved in English, except by a periphrasis. For the distinction between the two, see Paus. 2.10.1; Paus. 2.11.7; Paus. 3.19.3; and for more instances of \rendergreek{ἐναγίζειν} in this sense, see Paus. 3.1.8; Paus. 4.21.11; Paus. 7.17.8; Paus. 7.19.10; Paus. 7.20.9; Paus. 8.14.10-11; Paus. 8.41.1; Paus. 9.5.14; Paus. 9.18.3-4; Paus. 9.38.5; Paus. 10.24.6; Inscriptiones Graecae Megaridis, Oropiae, Boeotiae, ed. G. Dittenberger, p. 32, No. 53. For instances of the antithesis between \rendergreek{θύειν} and \rendergreek{ἐναγίζειν}, see Hdt. 2.44; Plut. De Herodoti malignitate 13; Ptolemy Hephaest., Nauck 2nd ed., Nov. Hist. iii. in Westermann's Mythographi Graeci, p. 186; Pollux viii.91; Scholiast on Eur. Ph. 274. The corresponding nouns \rendergreek{θυσίαι} and \rendergreek{ἐναγίσματα} are similarly opposed to each other. See Aristot. Ath. Pol. 58. Another word which is used only of sacrificing to heroes or the dead is \rendergreek{ἐντέμνειν} See, for example, Thuc. 5.11, \rendergreek{ὠς ἥρωΐ τε ἐντέμνουσι} (of the sacrifices offered at Amphipolis to Brasidas). Sometimes the verbs \rendergreek{ἐναγίζειν} and \rendergreek{ἐντέμνειν} are coupled in this sense. See Philostratus, Her. xx.27, 28. For more evidence as to the use of these words, see Fr. Pfister, Der Reliquienkult im Altertum (Giessen, 1909-1912), pp. 466ff. Compare P. Foucart, Le culte des héros chez les Grecs (Paris, 1918), pp. 96, 98 (from the Memoires de l' Académie des Inscriptions et Belles Lettres, vol. xlii).] And having come to Nemea and tracked the lion, he first shot an arrow at him, but when he perceived that the beast was invulnerable, he heaved up his club and made after him. And when the lion took refuge in a cave with two mouths, Hercules built up the one entrance and came in upon the beast through the other, and putting his arm round its neck held it tight till he had choked it; so laying it on his shoulders he carried it to Cleonae. And finding Molorchus on the last of the thirty days about to sacrifice the victim to him as to a dead man, he sacrificed to Saviour Zeus and brought the lion to Mycenae. Amazed at his manhood, Eurystheus forbade him thenceforth to enter the city, but ordered him to exhibit the fruits of his labours before the gates. They say, too, that in his fear he had a bronze jar made for himself to hide in under the earth,^[Compare Diod. 4.12.1, who however places this incident after the adventure with the Erymanthian boar.] and that he sent his commands for the labours through a herald, Copreus,^[As to the herald Copreus, compare Hom. Il. 15.639ff., with the note of the Scholiast.] son of Pelops the Elean. This Copreus had killed Iphitus and fled to Mycenae, where he was purified by Eurystheus and took up his abode.

As a second labour he ordered him to kill the Lernaean hydra.^[Compare Eur. Herc. 419ff.; Diod. 4.11.5ff.; Paus. 2.37.4; Paus. 5.5.10; Paus. 5.17.11; Zenobius, Cent. vi.26; Quintus Smyrnaeus, Posthomerica vi.212ff.; Tzetzes, Chiliades ii.237ff.; Verg. A. 8.299ff.; Ov. Met. 9.69ff.; Hyginus, Fab. 30. Diodorus and Ovid multiply the hydra's heads to a hundred; the sceptical Pausanias (Paus. 2.37.4) would reduce them to one. Both Diodorus and Pausanias, together with Zenobius and Hyginus, mention that Herakles poisoned his arrows with the gall of the hydra. The account which Zenobius gives of the hydra is clearly based on that of Apollodorus, though as usual he does not name his authority.] That creature, bred in the swamp of Lerna, used to go forth into the plain and ravage both the cattle and the country. Now the hydra had a huge body, with nine heads, eight mortal, but the middle one immortal. So mounting a chariot driven by Iolaus, he came to Lerna, and having halted his horses, he discovered the hydra on a hill beside the springs of the Amymone, where was its den. By pelting it with fiery shafts he forced it to come out, and in the act of doing so he seized and held it fast. But the hydra wound itself about one of his feet and clung to him. Nor could he effect anything by smashing its heads with his club, for as fast as one head was smashed there grew up two. A huge crab also came to the help of the hydra by biting his foot.^[For this service the crab was promoted by Hera, the foe of Herakles, to the rank of a constellation in the sky. See Eratosthenes, Cat. 11 (who quotes as his authority the Heraclia of Panyasis); Hyginus, Ast. ii.23.] So he killed it, and in his turn called for help on Iolaus who, by setting fire to a piece of the neighboring wood and burning the roots of the heads with the brands, prevented them from sprouting. Having thus got the better of the sprouting heads, he chopped off the immortal head, and buried it, and put a heavy rock on it, beside the road that leads through Lerna to Elaeus. But the body of the hydra he slit up and dipped his arrows in the gall. However, Eurystheus said that this labour should not be reckoned among the ten because he had not got the better of the hydra by himself, but with the help of Iolaus.

As a third labour he ordered him to bring the Cerynitian hind alive to Mycenae.^[Compare Pind. O. 3.28(50)ff.; Eur. Herc. 375ff.; Diod. 4.13.1; Tzetzes, Chiliades 11.265ff.; Hyginus, Fab. 30. Pindar says that in his quest of the hind with the golden horns Herakles had seen "the land at the back of the cold north wind." Hence, as the reindeer is said to be the only species of deer of which the female has antlers, Sir William Ridgeway argues ingeniously that the hind with the golden horns was no other than the reindeer. See his Early Age of Greece 1. (Cambridge, 1901), pp. 360ff. Later Greek tradition, as we see from Apollodorus, did not place the native land of the hind so far away. Oenoe was a place in Argolis. Mount Artemisius is the range which divides Argolis from the plain of Mantinea. The Ladon is the most beautiful river of Arcadia, if not of Greece. The river Cerynites, from which the hind took its name, is a river which rises in Arcadia and flows through Achaia into the sea. The modern name of the river is Bouphousia. See Paus. 7.25.5, with my note.] Now the hind was at Oenoe; it had golden horns and was sacred to Artemis; so wishing neither to kill nor wound it, Hercules hunted it a whole year. But when, weary with the chase, the beast took refuge on the mountain called Artemisius, and thence passed to the river Ladon, Hercules shot it just as it was about to cross the stream, and catching it put it on his shoulders and hastened through Arcadia. But Artemis with Apollo met him, and would have wrested the hind from him, and rebuked him for attempting to kill her sacred animal.^[The hind is said to have borne the inscription "Taygete dedicated (me) to Artemis." See Pind. O. 3.29(53)ff., with the Scholiast.] Howbeit, by pleading necessity and laying the blame on Eurystheus, he appeased the anger of the goddess and carried the beast alive to Mycenae.

As a fourth labour he ordered him to bring the Erymanthian boar alive;^[As to the Erymanthian boar and the centaurs, see Soph. Trach. 1095ff.; Diod. 4.12; Tzetzes, Chiliades ii.268ff.; Hyginus, Fab. 30. The boar's tusks were said to be preserved in a sanctuary of Apollo at Cumae in Campania (Paus. 8.24.5).] now that animal ravaged Psophis, sallying from a mountain which they call Erymanthus. So passing through Pholoe he was entertained by the centaur Pholus, a son of Silenus by a Melian nymph.^[As to these nymphs, see Hesiod, Th. 187. The name perhaps means an ash-tree nymph (from \rendergreek{μελία}, an ash tree), as Dryad means an oak tree nymph (from \rendergreek{δρῦς}, an oak tree).] He set roast meat before Hercules, while he himself ate his meat raw. When Hercules called for wine, he said he feared to open the jar which belonged to the centaurs in common.^[Compare Tzetzes, Chiliades ii.271; Theocritus vii.149ff. The jar had been presented by Dionysus to a centaur with orders not to open it till Herakles came (Diodorus Siculus iv.12.3).] But Hercules, bidding him be of good courage, opened it, and not long afterwards, scenting the smell, the centaurs arrived at the cave of Pholus, armed with rocks and firs. The first who dared to enter, Anchius and Agrius, were repelled by Hercules with a shower of brands, and the rest of them he shot and pursued as far as Malea. Thence they took refuge with Chiron, who, driven by the Lapiths from Mount Pelion, took up his abode at Malea. As the centaurs cowered about Chiron, Hercules shot an arrow at them, which, passing through the arm of Elatus, stuck in the knee of Chiron. Distressed at this, Hercules ran up to him, drew out the shaft, and applied a medicine which Chiron gave him. But the hurt proving incurable, Chiron retired to the cave and there he wished to die, but he could not, for he was immortal. However, Prometheus offered himself to Zeus to be immortal in his stead, and so Chiron died. The rest of the centaurs fled in different directions, and some came to Mount Malea, and Eurytion to Pholoe, and Nessus to the river Evenus. The rest of them Poseidon received at Eleusis and hid them in a mountain. But Pholus, drawing the arrow from a corpse, wondered that so little a thing could kill such big fellows; howbeit, it slipped from his hand and lighting on his foot killed him on the spot.^[Compare Servius on Verg. A. 8.294.] So when Hercules returned to Pholoe, he beheld Pholus dead; and he buried him and proceeded to the boar hunt. And when he had chased the boar with shouts from a certain thicket, he drove the exhausted animal into deep snow, trapped it, and brought it to Mycenae.

The fifth labour he laid on him was to carry out the dung of the cattle of Augeas in a single day.^[As to Augeas and his cattle-stalls, see Theocritus xxv.7ff.; Diod. 4.13.3; Paus. 5.1.9ff.; Tzetzes, Chiliades ii.278ff. (who seems to follow Apollodorus); Scholiast on Hom. Il. ii.629, xi.700; Scholiast on Ap. Rhod., Argon. i.172; Hyginus, Fab. 30. According to the rationalistic Pausanias, the name of the father of Augeas was Eleus (Eleios), which was popularly corrupted into Helios, "Sun"; Serv. Verg. A. 8.300.] Now Augeas was king of Elis; some say that he was a son of the Sun, others that he was a son of Poseidon, and others that he was a son of Phorbas; and he had many herds of cattle. Hercules accosted him, and without revealing the command of Eurystheus, said that he would carry out the dung in one day, if Augeas would give him the tithe of the cattle. Augeas was incredulous, but promised. Having taken Augeas's son Phyleus to witness, Hercules made a breach in the foundations of the cattle-yard, and then, diverting the courses of the Alpheus and Peneus, which flowed near each other, he turned them into the yard, having first made an outlet for the water through another opening. When Augeas learned that this had been accomplished at the command of Eurystheus, he would not pay the reward; nay more, he denied that he had promised to pay it, and on that point he professed himself ready to submit to arbitration. The arbitrators having taken their seats, Phyleus was called by Hercules and bore witness against his father, affirming that he had agreed to give him a reward. In a rage Augeas, before the voting took place, ordered both Phyleus and Hercules to pack out of Elis. So Phyleus went to Dulichium and dwelt there,^[Compare Hom. Il. 2.629, with the Scholiast; Paus. 5.1.10, Paus. 5.3.1-3.] and Hercules repaired to Dexamenus at Olenus.^[Compare Bacchylides, referred to by the Scholiast on Hom. Od. xi.295; Bacch., ed. R. C. Jebb, p. 430; Diod. 4.33.1; Paus. 7.18.1; Hyginus, Fab. 33.] He found Dexamenus on the point of betrothing perforce his daughter Mnesimache to the centaur Eurytion, and being called upon by him for help, he slew Eurytion when that centaur came to fetch his bride. But Eurystheus would not admit this labour either among the ten, alleging that it had been performed for hire.

The sixth labour he enjoined on him was to chase away the Stymphalian birds.^[As to the Stymphalian birds, see Ap. Rhod., Argon. ii.1052-1057, with the Scholiast on 1054; Diod. 4.13.2; Strab. 8.6.8; Paus. 8.22.4; Quintus Smyrnaeus, Posthomerica vi.227ff.; Tzetzes, Chiliades ii.291ff.; Hyginus, Fab. 20, 30; Serv. Verg. A. 8.300. These fabulous birds were said to shoot their feathers like arrows. Compare D'Arcy Wentworth Thompson, Glossary of Greek Birds, p. 162. From the Ap. Rhod., Argon. ii.1052-1057, with the Scholiast on 1054 we learn that the use of a brazen rattle to frighten the birds was mentioned both by Pherecydes and Hellanicus.] Now at the city of Stymphalus in Arcadia was the lake called Stymphalian, embosomed in a deep wood. To it countless birds had flocked for refuge, fearing to be preyed upon by the wolves.^[In no other ancient account of the Stymphalian birds, so far as I know, are wolves mentioned. There is perhaps a reminiscence of an ancient legend in the name of the Wolf's Ravine, which is still given to the deep glen, between immense pine-covered slopes, through which the road runs southwestward from Stymphalus to Orchomenus. The glen forms a conspicuous feature in the landscape to anyone seated on the site of the ancient city and looking across the clear shallow water of the lake to the high mountains that bound the valley on the south. See Frazer on Paus. vol. iv. p. 269.] So when Hercules was at a loss how to drive the birds from the wood, Athena gave him brazen castanets, which she had received from Hephaestus. By clashing these on a certain mountain that overhung the lake, he scared the birds. They could not abide the sound, but fluttered up in a fright, and in that way Hercules shot them.

The seventh labour he enjoined on him was to bring the Cretan bull.^[As to the Cretan bull see Diod. 4.13.4; Paus. 1.27.9ff., Paus. 5.10.9; Tzetzes, Chiliades ii.293- 298 (who seems to follow Apollodorus); Hyginus, Fab. 30.] Acusilaus says that this was the bull that ferried across Europa for Zeus; but some say it was the bull that Poseidon sent up from the sea when Minos promised to sacrifice to Poseidon what should appear out of the sea. And they say that when he saw the beauty of the bull he sent it away to the herds and sacrificed another to Poseidon; at which the god was angry and made the bull savage. To attack this bull Hercules came to Crete, and when, in reply to his request for aid, Minos told him to fight and catch the bull for himself, he caught it and brought it to Eurystheus, and having shown it to him he let it afterwards go free. But the bull roamed to Sparta and all Arcadia, and traversing the Isthmus arrived at Marathon in Attica and harried the inhabitants.

The eighth labour he enjoined on him was to bring the mares of Diomedes the Thracian to Mycenae.^[As to the man-eating mares of Diomedes, see Diod. 4.15.3ff.; Philostratus, Im. ii.25; Quintus Smyrnaeus, Posthomerica vi.245ff.; Tzetzes, Chiliades ii.299-308 (who seems to follow Apollodorus, except that he speaks of the animals in the masculine as horses, not mares); Strab. 7 Fr. 44, 47, ed. A. Meineke; Stephanus Byzantius, s.v. \rendergreek{Ἄβδηρα}; Hyginus, Fab. 30 (who gives the names of four horses, not mares). According to Diod. 4.13.4, Herakles killed the Thracian king Diomedes himself by exposing him to his own mares, which devoured him. Further, the historian tells us that when Herakles brought the mares to Eurystheus, the king dedicated them to Hera, and that their descendants existed down to the time of Alexander the Great.] Now this Diomedes was a son of Ares and Cyrene, and he was king of the Bistones, a very warlike Thracian people, and he owned man-eating mares. So Hercules sailed with a band of volunteers, and having overpowered the grooms who were in charge of the mangers, he drove the mares to the sea. When the Bistones in arms came to the rescue, he committed the mares to the guardianship of Abderus, who was a son of Hermes, a native of Opus in Locris, and a minion of Hercules; but the mares killed him by dragging him after them. But Hercules fought against the Bistones, slew Diomedes and compelled the rest to flee. And he founded a city Abdera beside the grave of Abderus who had been done to death,^[Compare Strab. 7 Fr. 44, 47, ed. A. Meineke; Stephanus Byzantius, s.v. \rendergreek{Ἄβδηρα}; Philostratus, Im. ii.25. From Philostratus we learn that athletic games were celebrated in honour of Abderus. They comprised boxing, wrestling, the pancratium, and all the other usual contests, with the exception of racing—no doubt because Abderus was said to have been killed by horses. We may compare the rule which excluded horses from the Arician grove, because horses were said to have killed Hippolytus, with whom Virbius, the traditionary founder of the sanctuary, was identified. See Verg. A. 7.761-780; Ovid, Fasti iii.265ff. When we remember that the Thracian king Lycurgus is said to have been killed by horses in order to restore the fertility of the land (see Apollod. 3.5.1), we may conjecture that the tradition of the man-eating mares of Diomedes, another Thracian king who is said to have been killed by horses, points to a custom of human sacrifice performed by means of horses, whether the victim was trampled to death by their hoofs or tied to their tails and rent asunder. If the sacrifice was offered, as the legend of Lycurgus suggests, for the sake of fertilizing the ground, the reason for thus tearing the victim to pieces may have been to scatter the precious life-giving fragments as widely and as quickly as possible over the barren earth. Compare Adonis, Attis, Osiris ii.97ff. The games at Abdera are alluded to by the poet Machon, quoted by Athenaeus viii.41, p. 349 B.] and bringing the mares he gave them to Eurystheus. But Eurystheus let them go, and they came to Mount Olympus, as it is called, and there they were destroyed by the wild beasts.

The ninth labour he enjoined on Hercules was to bring the belt of Hippolyte.^[As to the expedition of Herakles to fetch the belt of the Amazon, see Eur. Herc. 408ff.; Ap. Rhod., Argon. ii.777ff., 966ff., with the Scholiast on 778, 780; Diod. 4.16; Paus. 5.10.9; Quintus Smyrnaeus, Posthomerica vi.240ff.; Tzetzes, Chiliades ii.309ff.; Tzetzes, Scholiast on Lycophron 1327(who follows Apollodorus and cites him by name); Hyginus, Fab. 30.] She was queen of the Amazons, who dwelt about the river Thermodon, a people great in war; for they cultivated the manly virtues, and if ever they gave birth to children through intercourse with the other sex, they reared the females; and they pinched off the right breasts that they might not be trammelled by them in throwing the javelin, but they kept the left breasts, that they might suckle. Now Hippolyte had the belt of Ares in token of her superiority to all the rest. Hercules was sent to fetch this belt because Admete, daughter of Eurystheus, desired to get it. So taking with him a band of volunteer comrades in a single ship he set sail and put in to the island of Paros, which was inhabited by the sons of Minos,^[According to Diod. 5.79.2, Rhadamanthys bestowed the island of Paros on his son Alcaeus. Combined with the evidence of Apollodorus, the tradition points to a Cretan colony in Paros.] to wit, Eurymedon, Chryses, Nephalion, and Philolaus. But it chanced that two of those in the ship landed and were killed by the sons of Minos. Indignant at this, Hercules killed the sons of Minos on the spot and besieged the rest closely, till they sent envoys to request that in the room of the murdered men he would take two, whom he pleased. So he raised the siege, and taking on board the sons of Androgeus, son of Minos, to wit, Alcaeus and Sthenelus, he came to Mysia, to the court of Lycus, son of Dascylus, and was entertained by him; and in a battle between him and the king of the Bebryces Hercules sided with Lycus and slew many, amongst others King Mygdon, brother of Amycus. And he took much land from the Bebryces and gave it to Lycus, who called it all Heraclea.

Having put in at the harbor of Themiscyra, he received a visit from Hippolyte, who inquired why he was come, and promised to give him the belt. But Hera in the likeness of an Amazon went up and down the multitude saying that the strangers who had arrived were carrying off the queen. So the Amazons in arms charged on horseback down on the ship. But when Hercules saw them in arms, he suspected treachery, and killing Hippolyte stripped her of her belt. And after fighting the rest he sailed away and touched at Troy.

But it chanced that the city was then in distress consequently on the wrath of Apollo and Poseidon. For desiring to put the wantonness of Laomedon to the proof, Apollo and Poseidon assumed the likeness of men and undertook to fortify Pergamum for wages. But when they had fortified it, he would not pay them their wages.^[Compare Hom. Il. 7.452ff., Hom. Il. 21.441-457. According to the former of these passages, the walls of Troy were built by Poseidon and Apollo jointly for king Laomedon. But according to the latter passage the walls were built by Poseidon alone, and while he thus toiled as a mason, Apollo served as a herdsman, tending the king's cattle in the wooded glens of Ida. Their period of service lasted for a year, and at the end of it the faithless king not only dismissed the two deities without the stipulated wages which they had honestly earned, but threatened that, if they did not take themselves off, he would tie Apollo hand and foot and sell him for a slave in the islands, not however before he had lopped off the ears of both of them with a knife. Thus insulted as well as robbed, the two gods retired with wrath and indignation at their hearts. This strange tale, told by Homer, is alluded to by Pind. O. 8.30(40)ff., who adds to it the detail that the two gods took the hero Aeacus with them to aid them in the work of fortification; and the Scholiast on Pindar (pp. 194ff. ed. Boeckh) explains that, as Troy was fated to be captured, it was necessary that in building the walls the immortals should be assisted by a mortal, else the city would have been impregnable. The sarcastic Lucian tells us (Lucian, De sacrificiis 4) that both Apollo and Poseidon laboured as bricklayers at the walls of Troy, and that the sum of which the king cheated them was more than thirty Trojan drachmas. The fraud is alluded to by Verg. G. 1.502 and Hor. Carm. 3.3.21ff. Compare Hyginus, Fab. 89; Ov. Met. 11.194ff.; Serv. Verg. A. 8.157; Scriptores rerum mythicarum Latini, ed. Bode, i. pp. 43ff., 138 (First Vatican Mythographer 136; Second Vatican Mythographer 193). Homer does not explain why Apollo and Poseidon took service with Laomedon, but his Scholiast on Hom. Il. xxi.444, in agreement with Tzetzes, Scholiast on Lycophron 34, says that their service was a punishment inflicted on them by Zeus for a conspiracy into which some of the gods had entered for the purpose of putting him, the supreme god, in bonds. The conspiracy is mentioned by Hom. Il. 1.399ff.), who names Poseidon, Hera, and Athena, but not Apollo, among the conspirators; their nefarious design was defeated by the intervention of Thetis and the hundred-handed giant Briareus. We have already heard of Apollo serving a man in the capacity of neatherd as a punishment for murder perpetrated by the deity (see above, Apollod. 1.9.15, with the note). These back-stair chronicles of Olympus shed a curious light on the early Greek conception of divinity.] Therefore Apollo sent a pestilence, and Poseidon a sea monster, which, carried up by a flood, snatched away the people of the plain. But as oracles foretold deliverance from these calamities if Laomedon would expose his daughter Hesione to be devoured by the sea monster, he exposed her by fastening her to the rocks near the sea.^[For the story of the rescue of Hesione by Herakles, see Diod. 4.42; Scholiast on Hom. Il. xx.146; Tzetzes, Scholiast on Lycophron 34; Ov. Met. 11.211ff.; Valerius Flaccus, Argon. ii.451ff.; Hyginus, Fab. 89; Serv. Verg. A. 8.157; Scriptores rerum mythicarum Latini, ed. Bode, i. p. 44 (First Vatican Mythographer 136). A curious variant of the story is told, without mention of Hesione, by the Second Vatican Mythographer (193, i. p. 138). Tzetzes says that Herakles, in full armour, leaped into the jaws of the sea-monster, and was in its belly for three days hewing and hacking it, and that at the end of the three days he came forth without any hair on his head. The Scholiast on Hom. Il. xx.146 tells the tale similarly, and refers to Hellanicus as his authority. The story of Herakles and Hesione corresponds closely to that of Perseus and Andromeda (see Apollod. 2.4.3). Both tales may have originated in a custom of sacrificing maidens to be the brides of the Sea. Compare The Magic Art and the Evolution of Kings, ii.150ff.] Seeing her exposed, Hercules promised to save her on condition of receiving from Laomedon the mares which Zeus had given in compensation for the rape of Ganymede.^[The horses were given by Zeus to Tros, the father of Ganymede. See Hom. Il. 5.265ff.; HH Aphr. 210ff.; Paus. 5.24.5. According to another account, which had the support of a Cyclic poet, the compensation given to the bereaved father took the shape, not of horses, but of a golden vine wrought by Hephaestus. See Scholiast on Eur. Or. 1391. As the duty of Ganymede was to pour the red nectar from a golden bowl in heaven (HH Aphr. 206), there would be a certain suitability in the bestowal of a golden vine to replace him in his earthly home.] On Laomedon's saying that he would give them, Hercules killed the monster and saved Hesione. But when Laomedon would not give the stipulated reward,^[As to the refusal of Laomedon to give the horses to Herakles, see Hom. Il. 5.638-651, Hom. Il. 21.441-457; Ov. Met. 11.213ff.; Hyginus, Fab. 69. Laomedon twice broke his word, first to Poseidon and Apollo and afterwards to Herakles. Hence Ovid speaks of "the twice-perjured walls of Troy" (Ov. Met. 11.215).] Hercules put to sea after threatening to make war on Troy.^[As to the siege and capture of Troy by Herakles, see below, Apollod. 2.6.4.]

And he touched at Aenus, where he was entertained by Poltys. And as he was sailing away he shot and killed on the Aenian beach a lewd fellow, Sarpedon, son of Poseidon and brother of Poltys. And having come to Thasos and subjugated the Thracians who dwelt in the island, he gave it to the sons of Androgeus to dwell in. From Thasos he proceeded to Torone, and there, being challenged to wrestle by Polygonus and Telegonus, sons of Proteus, son of Poseidon, he killed them in the wrestling match.^[Compare Tzetzes, Chiliades ii.320 sq.] And having brought the belt to Mycenae he gave it to Eurystheus.

As a tenth labour he was ordered to fetch the kine of Geryon from Erythia.^[As to Herakles and the cattle of Geryon, see Hes. Th. 287-294ff.; Hes. Th. 979-983; Pind. Frag. 169(151) ed. Sandys; Hdt. 4.8; Plat. Gorg. 484b; Diod. 4.17ff.; Paus. 3.18.13, Paus. 4.36.3; Quintus Smyrnaeus, Posthomerica vi.249ff.; Tzetzes, Chiliades ii.322-352 (who seems to follow Apollodorus); Scholiast on Plato, Tim. 24e; Pliny, Nat. Hist. iv.120; Solinus xxiii.12; Serv. Verg. A. 8.300.] Now Erythia was an island near the ocean; it is now called Gadira.^[Compare Hdt. 4.8; Strab. 3.2.11, Strab. 3.5 4; Pliny, Nat. Hist. iv.120; Solinus xxiii.12. Gadira is Cadiz. According to Pliny, Nat. Hist. iv.120, the name is derived from a Punic word gadir, meaning "hedge." Compare Dionysius, Perieg. 453ff. The same word agadir is still used in the south of Morocco in the sense of "fortified house," and many places in that country bear the name. Amongst them the port of Agadir is the best known. See E. Doutté, En tribu (Paris, 1914), pp. 50ff. The other name of the island is given by Solinus xxiii.12 in the form Erythrea, and by Mela iii.47 in the form Eythria.] This island was inhabited by Geryon, son of Chrysaor by Callirrhoe, daughter of Ocean. He had the body of three men grown together and joined in one at the waist, but parted in three from the flanks and thighs.^[As to the triple form of Geryon, compare Hes. Th. 287; Aesch. Ag. 870; Eur. Herc. 423ff.; Scholiast on Plat. Tim. 24e; Paus. 5.19.1; Lucian, Toxaris 62; Tzetzes, Scholiast on Lycophron 652; Lucretius v.28; Hor. Carm. 2.14.7ff.; Verg. A. 6.289; Ov. Met. 9.184ff.; Hyginus, Fab. 30, 151.] He owned red kine, of which Eurytion was the herdsman and Orthus,^[The watchdog's name is variously given as Orthus (Orthos) and Orthrus (Orthros). See Hes. Th. 293 (where Orthos seems to be the better reading); Quintus Smyrnaeus, Posthomerica vi.253 (Orthros); Scholiast on Pind. I. 1.13(15) (Orthos); Scholiast on Plat. Tim. 24e (Orthros, so Stallbaum); Tzetzes, Chiliades ii.333 (Orthros); Pediasmus, De Herculis laboribus 10 (Orthos); Serv. Verg. A. 8.300 (Orthrus).] the two-headed hound, begotten by Typhon on Echidna, was the watchdog. So journeying through Europe to fetch the kine of Geryon he destroyed many wild beasts and set foot in Libya,^[Compare Diod. 4.17.3ff., who says that Herakles completely cleared Crete of wild beasts, and that he subdued many of the wild beasts in the deserts of Libya and rendered the land fertile and prosperous.] and proceeding to Tartessus he erected as tokens of his journey two pillars over against each other at the boundaries of Europe and Libya.^[The opinions of the ancients were much divided on the subject of the Pillars of Herakles. See Strab. 3.5.5. The usual opinion apparently identified them with the rock of Calpe (Gibraltar) and the rock of Abyla, Abila, or Abylica (Ceuta) on the northern and southern sides of the straits. See Strab. 3.5.5; Tzetzes, Scholiast on Lycophron 649; Pliny, Nat. Hist. iii.4; Mela i.27, ii.95; Martianus Capella vi.624. Further, it seems to have been commonly supposed that before the time of Herakles the two continents were here joined by an isthmus, and that the hero cut through the isthmus and so created the straits. See Diod. 4.18.5; Seneca, Herakles Furens 235ff.; Seneca, Herakles Oetaeus 1240; Pliny, Nat. Hist. iii.4; Pliny, Nat. Hist. iii.4; Mela i.27; Martianus Capella vi.625. Some people, however, on the contrary, thought that the straits were formerly wider, and that Herakles narrowed them to prevent the monsters of the Atlantic ocean from bursting into the Mediterranean (Diod. 4.18.5). An entirely different opinion identified the Pillars of Herakles with two brazen pillars in the sanctuary of Herakles at Gadira (Cadiz), on which was engraved an inscription recording the cost of building the temple. See Strab. 3.5.5; compare Pliny, Nat. Hist. ii.242, who speaks of "the columns of Herakles consecrated at Gadira." For other references to the Pillars of Herakles, see Pind. O. 3.43ff., Pind. N. 3.21, Pind. I. 4.11ff.; Athenaeus vii.98, p. 315 CD; Tzetzes, Chiliades ii.339 (who here calls the pillars Alybe and Abinna); Scholiast on Plat. Tim. 24e; Dionysius of Halicarnassus, Orbis Descriptio 64-68, with the commentary of Eustathius (Geographi Graeci Minores, ed. C. Müller, ii. pp. 107, 228). According to Eustathius, Calpe was the name given to the rock of Gibraltar by the barbarians, but its Greek name was Alybe; and the rock of Ceuta was called Abenna by the barbarians but by the Greeks Cynegetica, that is, the Hunter's Rock. He tells us further that the pillars were formerly named the Pillars of Cronus, and afterwards the Pillars of Briareus.] But being heated by the Sun on his journey, he bent his bow at the god, who in admiration of his hardihood, gave him a golden goblet in which he crossed the ocean.^[Apollodorus seems to be here following Pherecydes, as we learn from a passage which Athenaeus xi.39, p. 470 CD quotes from the third book of Pherecydes as follows: "And Herakles drew his bow at him as if he would shoot, and the Sun bade him give over; so Herakles feared and gave over. And in return the Sun bestowed on him the golden goblet which carried him with his horses, when he set, through the Ocean all night to the east, where the Sun rises. Then Herakles journeyed in that goblet to Erythia. And when he was on the open sea, Ocean, to make trial of him, caused the goblet to heave wildly on the waves. Herakles was about to shoot him with an arrow; and the Ocean was afraid, and bade him give over." Stesichorus described the Sun embarking in a golden goblet that he might cross the ocean in the darkness of night and come to his mother, his wedded wife, and children dear. See Athenaeus xi.38, p. 468 E; compare Athenaeus xi.16, p. 781 D. The voyage of Herakles in the golden goblet was also related by the early poets Pisander and Panyasis in the poems, both called Heraclia, which they devoted to the exploits of the great hero. See Athenaeus xi.38, p. 469 D; compare Macrobius, Sat. v.21.16, 19. Another poet, Mimnermus, supposed that at night the weary Sun slept in a golden bed, which floated across the sea to Ethiopia, where a chariot with fresh horses stood ready for him to mount and resume his daily journey across the sky. See Athenaeus xi.39, p. 470 A.] And having reached Erythia he lodged on Mount Abas. However the dog, perceiving him, rushed at him; but he smote it with his club, and when the herdsman Eurytion came to the help of the dog, Hercules killed him also. But Menoetes, who was there pasturing the kine of Hades, reported to Geryon what had occurred, and he, coming up with Hercules beside the river Anthemus,^[Compare Tzetzes, Scholiast on Lycophron 652, who probably follows Apollodorus.] as he was driving away the kine, joined battle with him and was shot dead. And Hercules, embarking the kine in the goblet and sailing across to Tartessus, gave back the goblet to the Sun.

And passing through Abderia^[Abderia, the territory of Abdera, a Phoenician city of southern Spain, not to be confused with the better known Abdera in Thrace. See Strab. 3.4.3; Stephanus Byzantius, s.v. \rendergreek{Ἄβδηρα}.] he came to Liguria,^[Apollodorus has much abridged a famous adventure of Herakles in Liguria. Passing through the country with the herds of Geryon, he was attacked by a great multitude of the warlike natives, who tried to rob him of the cattle. For a time he repelled them with his bow, but his supply of arrows running short he was reduced to great straits; for the ground, being soft earth, afforded no stones to be used as missiles. So he prayed to his father Zeus, and the god in pity rained down stones from the sky; and by picking them up and hurling them at his foes, the hero was able to turn the tables on them. The place where this adventure took place was said to be a plain between Marseilles and the Rhone, which was called the Stony Plain on account of the vast quantity of stones, about as large as a man's hand, which were scattered thickly over it. In his play Prometheus Unbound, Aeschylus introduced this story in the form of a prediction put in the mouth of Prometheus and addressed to his deliverer Herakles. See Strab. 4.1.7; Dionysius of Halicarnassus, Antiq. Rom. i.41; Eustathius, Commentary on Dionysius Perieg. 76 (Geographi Graeci Minores, ed. C. Müller, ii.231); Hyginus, Ast. ii.6; TGF (Nauck 2nd ed.), pp. 66ff. The Stony Plain is now called the Plaine de la Crau. It "attracts the attention of all travellers between Arles and Marseilles, since it is intersected by the railway that joins those two cities. It forms a wide level area, extending for many square miles, which is covered with round rolled stones from the size of a pebble to that of a man's head. These are supposed to have been brought down from the Alps by the Durance at some early period, when this plain was submerged and formed the bed of what was then a bay of the Mediterranean at the mouth of that river and the Rhone" (H. F. Tozer, Selections from Strabo, p. 117).] where Ialebion and Dercynus, sons of Poseidon, attempted to rob him of the kine, but he killed them^[Compare Tzetzes, Chiliades ii.340ff., who calls the victims Dercynus and Alebion.] and went on his way through Tyrrhenia. But at Rhegium a bull broke away^[The author clearly derives the name of Rhegium from this incident (\rendergreek{Ρήγιον} from \rendergreek{ἀπορρήγνυσι}). The story of the escape of the bull, or heifer, and the pursuit of it by Herakles was told by Hellanicus. See Dionysius of Halicarnassus, Ant. Rom. i.35.2. It is somewhat singular that Apollodorus passes so lightly over the exploits of Herakles in Italy, and in particular that he says nothing about those adventures of his at Rome, to which the Romans attached much significance. For the Italian adventures of the hero, and his sojourn in Rome, see Diod. 4.20-22; Dionysius of Halicarnassus, Antiq. Rom. i.34ff., 38-44; Prop. iv.9; Verg. A. 8.201ff.; Ovid, Fasti i.543ff. On the popularity of the worship of Herakles in Italy, see Dionysius of Halicarnassus, Antiq. Rom. i.40.6, who says: "And in many other parts of Italy (besides Rome) precincts are consecrated to the god, and altars are set up both in cities and beside roads; and hardly will you find a place in Italy where the god is not honoured."] and hastily plunging into the sea swam across to Sicily, and having passed through the neighboring country since called Italy after it, for the Tyrrhenians called the bull italus,^[Some of the ancients supposed that the name of Italy was derived from the Latin _vitulus_, "a calf." See Varro, Re. Rust. ii.1.9; Dionysius of Halicarnassus, Antiq. Rom. i.35.2; compare Aulus Gellius xi.1.2.] came to the plain of Eryx, who reigned over the Elymi.^[As to Herculus and Eryx, see Diod. 4.23.2; Paus. 3.16.4ff.; Paus. 4.36.4; Tzetzes, Chiliades ii.346ff.; Tzetzes, Scholiast on Lycophron 866; Verg. A. 5.410ff.; Serv. Verg. A. 1.570.] Now Eryx was a son of Poseidon, and he mingled the bull with his own herds. So Hercules entrusted the kine to Hephaestus and hurried away in search of the bull. He found it in the herds of Eryx, and when the king refused to surrender it unless Hercules should beat him in a wrestling bout, Hercules beat him thrice, killed him in the wrestling, and taking the bull drove it with the rest of the herd to the Ionian Sea. But when he came to the creeks of the sea, Hera afflicted the cows with a gadfly, and they dispersed among the skirts of the mountains of Thrace. Hercules went in pursuit, and having caught some, drove them to the Hellespont; but the remainder were thenceforth wild.^[The story was apparently told to account for the origin of wild cattle in Thrace.] Having with difficulty collected the cows, Hercules blamed the river Strymon, and whereas it had been navigable before, he made it unnavigable by filling it with rocks; and he conveyed the kine and gave them to Eurystheus, who sacrificed them to Hera.

When the labours had been performed in eight years and a month,^[This period for the completion of the labours of Herakles is mentioned also by the Scholiast on Hom. Il. viii.368 and Tzetzes, Chiliades ii.353ff., both of whom, however, may have had the present passage of Apollodorus before them. It is possible that the period refers to the eight years' cycle, which figured prominently in the religious calendar of the ancient Greeks; for example, the Pythian games were originally held at intervals of eight years. See Geminus, Element. Astron. viii.25ff., ed. C. Manitius; Censorinus, De die natali 18. It is to be remembered that the period of service performed by Herakles for Eurystheus was an expiation for the murder of his children (see Apollod. 2.4.12). Now Cadmus is said to have served Ares for eight years as an expiation for the slaughter of the dragon, the offspring of Ares (see Apollod. 3.4.2). But in those days, we are told, the "eternal year" comprised eight common years (Apollod. 3.4.2). Now Apollo served Admetus for a year as an expiation for the slaughter of the Cyclopes (Apollod. 3.10.4); but according to Serv. Verg. A. 7.761, the period of Apollo's service was not one but nine years. In making this statement Servius, or his authority, probably had before him a Greek author, who mentioned an \rendergreek{ἐννεατηρίς} as the period of Apollo's service. But though \rendergreek{ἐννεατηρίς} means literally "nine years," the period, in consequence of the Greek mode of reckoning, was actually equivalent to eight years (compare Celsus, De die natali 18.4, "_Octaeteris facta, quae tunc enneateris vocitata, quia primus eius annus nono quoque anno redibat_.") These legends about the servitude of Cadmus, Apollo, and Herakles for eight years, render it probable that in ancient times Greek homicides were banished for eight years, and had during that time to do penance by serving a foreigner. Now this period of eight years was called a "great year" (Censorinus, De die natali 18.5), and the period of banishment for a homicide was regularly a year. See Apollod. 2.8.3; Eur. Hipp.34-37, Eur. Or. 1643-1645; Nicolaus Damascenus, Frag 20 (Fragmenta Historicorum Graccorum, ed. C. Müller, iii.369); Hesychius, s.v. \rendergreek{ἀπενιαυτισμός}; Suidas, s.v. \rendergreek{ἀπεναυτίσαι}. Hence it seems probable that, though in later times the period of a homicide's banishment was a single ordinary year, it may formerly have been a "great year," or period of eight ordinary years. It deserves to be noted that any god who had forsworn himself by the Styx had to expiate his fault by silence and fasting for a full year, after which he was banished the company of the gods for nine years (Hes. Th. 793-804ff.); and further that any man who partook of human flesh in the rites of Lycaean Zeus was supposed to be turned into a wolf for nine years. See Paus. 8.2; Pliny, Nat. Hist. viii.81; Augustine, De civitate Dei xviii.17. These notions point to a nine years' period of expiation, which may have been observed in some places instead of the eight years' period. In the present passage of Apollodorus, the addition of a month to the eight years' period creates a difficulty which I am unable to explain. Ancient mathematicians defined a "great year" as the period at the end of which the sun, moon, and planets again occupy the same positions relatively to each other which they occupied at the beginning; but on the length of the period opinions were much divided. See Cicero, De natura deorum ii.20.51ff. Different, apparently, from the "great year" was the "revolving" (_vertens_) or "mundane" (_mundanus_) year, which was the period at the end of which, not only the sun, moon, and planets, but also the so-called fixed stars again occupy the positions relatively to each other which they occupied at the beginning; for the ancients recognized that the so-called fixed stars do move, though their motion is imperceptible to our senses. The length of a "revolving" or "mundane" year was calculated by ancient physicists at fifteen thousand years. See Cicero, Somnium Scipionis 7, with the commentary of Macrobius, ii.11.] Eurystheus ordered Hercules, as an eleventh labour, to fetch golden apples from the Hesperides,^[As to the apples of the Hesperides, see Hes. Th. 215ff.; Eur. Herc. 394ff.; Ap. Rhod., Argon. iv.1396ff.; with the Scholiast Ap. Rhod. Argon. iv.1396; Diod. 4.26; Paus. 5.11.6; Paus. 5.18.4; Paus. 6.19.8; Eratosthenes, Cat. 3; Tzetzes, Chiliades ii.355ff.; Ov. Met. 4.637ff., ix.190; Hyginus, Fab. 30; Hyginus, Ast. ii.3; Scholia in Caesaris Germanici Aratea, pp. 382ff., in Martianus Capella, ed. Fr. Eyssenhardt; Scriptores rerum mythicarum Latini, ed. Bode, i. pp. 13ff., 130 (First Vatican Mythographer 38; Second Vatican Mythographer 161). From the Scholiast on Ap. Rhod., Argon. iv.1396ff. we learn that the story of Herakles and the apples of the Hesperides was told by Pherecydes in the second book of his work on the marriage of Hera. The close resemblance which the Scholiast's narrative bears to that of Apollodorus seems to show that here, as in many other places, our author followed Pherecydes. The account given by Pherecydes of the origin of the golden apples is as follows. When Zeus married Hera, the gods brought presents to the bride. Among the rest, Earth brought golden apples, which Hera so much admired that she ordered them to be planted in the garden of the gods beside Mount Atlas. But, as the daughters of Atlas used to pilfer the golden fruit, she set a huge serpent to guard the tree. Such is the story told, on the authority of Pherecydes, by Eratosthenes, Hyginus, Astr. ii.3, and the Scholiast on the Aratea of Germanicus.] for he did not acknowledge the labour of the cattle of Augeas nor that of the hydra. These apples were not, as some have said, in Libya, but on Atlas among the Hyperboreans.^[Here Apollodorus departs from the usual version, which placed the gardens of the Hesperides in the far west, not the far north. We have seen that Herakles is said to have gone to the far north to fetch the hind with the golden horns (see above, Apollod. 2.5.3 note); also he is reported to have brought from the land of the Hyperboreans the olive spray which was to form the victor's crown at the Olympic games. See Pind. O. 3.11(20)ff.; Paus. 5.7.7, compare Paus. 5.15.3.] They were presented < by Earth> to Zeus after his marriage with Hera, and guarded by an immortal dragon with a hundred heads, offspring of Typhon and Echidna, which spoke with many and divers sorts of voices. With it the Hesperides also were on guard, to wit, Aegle, Erythia, Hesperia, and Arethusa. So journeying he came to the river Echedorus. And Cycnus, son of Ares and Pyrene, challenged him to single combat. Ares championed the cause of Cycnus and marshalled the combat, but a thunderbolt was hurled between the two and parted the combatants.^[Compare Hyginus, Fab. 31, who describes the intervention of Mars (Ares) on the side of his son Cycnus, and the fall of the thunderbolt which parted the combatants; yet he says that Herakles killed Cycnus. This combat, which, according to Apollodorus, ended indecisively, was supposed to have been fought in Macedonia, for the Echedorus was a Macedonian river (Hdt. 7.124, Hdt. 7.127). Accordingly we must distinguish this contest from another and more famous fight which Herakles fought with another son of Ares, also called Cycnus, near Pagasae in Thessaly. See Apollod. 2.7.7, with the note. Apparently Hyginus confused the two combats.] And going on foot through Illyria and hastening to the river Eridanus he came to the nymphs, the daughters of Zeus and Themis. They revealed Nereus to him, and Hercules seized him while he slept, and though the god turned himself into all kinds of shapes, the hero bound him and did not release him till he had learned from him where were the apples and the Hesperides.^[The meeting of Herakles with the nymphs, and his struggle with Nereus, are related also by the Scholiast on Ap. Rhod., Argon. iv.1396, citing as his authority Pherecydes, whom Apollodorus also probably follows. The transformations of the reluctant sea-god Nereus in his encounter with Herakles are like those of the reluctant sea-god Proteus in his encounter with Menelaus (Hom. Od. 4.354- 570), and those of the reluctant sea-goddess Thetis with her lover Peleus (see below, Apollod. 3.13.5).] Being informed, he traversed Libya. That country was then ruled by Antaeus, son of Poseidon,^[As to Herakles and Antaeus, see Pind. I. 4.52(87)ff., with the Scholiast on Pind. I. 4.52(87) and 54(92); Diod. 4.17.4; Paus. 9.11.6; Philostratus, Im. ii.21; Quintus Smyrnaeus, Posthomerica vi.285ff.; Tzetzes, Chiliades ii.363ff.; Scholiast on Plat. Laws, vii, 796a (whose account agrees almost verbally with that of Apollodorus); Ovid, Ibis 393-395, with the Scholia; Hyginus, Fab. 31; Lucan, Pharsal. iv.588-655; Juvenal iii.89; Statius, Theb. vi.893ff.; Lactantius Placidus on Statius, Theb. vi.869(894); Scriptores rerum mythicarum Latini, ed. Bode, i. pp. 19, 131 (First Vatican Mythographer 55; Second Vatican Mythographer 164). According to Pindar, the truculent giant used to roof the temple of his sire Poseidon with the skulls of his victims. The fable of his regaining strength through contact with his mother Earth is dwelt on by Lucan with his usual tedious prolixity. It is briefly alluded to by Ovid, Juvenal, and Statius. Antaeus is said to have reigned in western Morocco, on the Atlantic coast. Here a hillock was pointed out as his tomb, and the natives believed that the removal of soil from the hillock would be immediately followed by rain, which would not cease till the earth was replaced. See Mela iii.106. Sertorius is said to have excavated the supposed tomb and to have found a skeleton sixty cubits long. See Plut. Sertorius 9; Strab. 17.3.8.] who used to kill strangers by forcing them to wrestle. Being forced to wrestle with him, Hercules hugged him, lifted him aloft,^[More literally, "lifted him aloft with hugs." For this technical term (\rendergreek{ἅμμα}) applied to a wrestler's hug, see Plut. Fabius Maximus 23, and Plut. Alc. 2.] broke and killed him; for when he touched earth so it was that he waxed stronger, wherefore some said that he was a son of Earth.

After Libya he traversed Egypt. That country was then ruled by Busiris,^[For Herakles and Busiris, see Diod. 4.18.1, Diod. 4.27.2ff.; Plut. Parallela 38; Scholiast on Ap. Rhod., Argon. iv.1396; Tzetzes, Scholiast on Lycophron ii.367ff.; Ov. Met. 9.182ff.; Ovid, Ars Am. i.647-652; Scholiast on Ovid, Ibis 397 (p. 72, ed. R. Ellis); Hyginus, Fab. 31, 56; Serv. Verg. A. 8.300 and Georg. iii.5; Philargyrius on Verg. G. 3.5; Lactantius Placidus on Statius, Theb. xii.155. Ovid, with his Scholiasts, Hyginus and Philargyrius, like Apollodorus, allege a nine or eight years' dearth or drought as the cause of the human sacrifices instituted by Busiris. Their account may be derived from Pherecydes, who is the authority cited by the Scholiast on Ap. Rhod., Argon. iv.1396. Hyginus, Fab. 56 adds that the seer Phrasius, who advised the sacrifice, was a brother of Pygmalion. Herodotus, without mentioning Busiris, scouts the story on the ground that human sacrifices were utterly alien to the spirit of Egyptian religion (Hdt. 2.45). Isocrates also discredited the tradition, in so far as it relates to Herakles, because Herakles was four generations younger, and Busiris more than two hundred years older, than Perseus. See Isoc. 11.15. Yet there are grounds for thinking that the Greek tradition was substantially correct. For Manetho, our highest ancient authority, definitely affirmed that in the city of Ilithyia it was customary to burn alive "Typhonian men" and to scatter their ashes by means of winnowing fans (Plut. Isis et Osiris 73). These "Typhonian men" were red-haired, because Typhon, the Egyptian embodiment of evil, was also redhaired (Plut. Isis et Osiris 30, 33). But redhaired men would commonly be foreigners, in contrast to the black-haired natives of Egypt; and it was just foreigners who, according to Greek tradition, were chosen as victims. Diodorus Siculus points this out (Diod. 1.88.5) in confirmation of the Greek tradition, and he tells us that the redhaired men were sacrificed at the grave of Osiris, though this statement may be an inference from his etymology of the name Busiris, which he explains to mean "grave of Osiris." The etymology is correct, Busiris being a Greek rendering of the Egyptian Asir "place of Osiris." See A. Wiedemann, Herodots Zweites Buch (Leipsic, 1890), p. 213. Porphyry informs us, on the authority of Manetho, that the Egyptian custom of sacrificing human beings at the City of the Sun was suppressed by Amosis (Amasis), who ordered waxen effigies to be substituted for the victims. He adds that the human victims used to be examined just like calves for the sacrifice, and that they were sealed in token of their fitness for the altar. See Porphyry, De abstinentia iii.35. Sextus Empiricus even speaks of human sacrifices in Egypt as if they were practised down to his own time, which was about 200 A.D. See Sextus Empiricus, p. 173, ed. Bekker. Seleucus wrote a special treatise on human sacrifices in Egypt (Athenaeus iv.72, p. 172 D). In view of these facts, the Greek tradition that the sacrifices were offered in order to restore the fertility of the land or to procure rain after a long drought, and that on one occasion the king himself was the victim, may be not without significance. For kings or chiefs have been often sacrificed under similar circumstances (see Apollod. 3.5.1; Adonis, Attis, Osiris, 3rd ed. ii.97ff.; The Magic Art and the Evolution of Kings, i.344ff., 352ff.); and in ancient Egypt the rulers are definitely said to have been held responsible for the failure of the crops (Ammianus Marcellinus xxviii.5.14); hence it would not be surprising if in extreme cases they were put to death. Busiris was the theme of a Satyric play by Euripides. See TGF (Nauck 2nd ed.), pp. 452ff.] a son of Poseidon by Lysianassa, daughter of Epaphus. This Busiris used to sacrifice strangers on an altar of Zeus in accordance with a certain oracle. For Egypt was visited with dearth for nine years, and Phrasius, a learned seer who had come from Cyprus, said that the dearth would cease if they slaughtered a stranger man in honor of Zeus every year. Busiris began by slaughtering the seer himself and continued to slaughter the strangers who landed. So Hercules also was seized and haled to the altars, but he burst his bonds and slew both Busiris and his son Amphidamas.^[The Scholiast on Ap. Rhod., Argon. iv.1396 calls him Iphidamas, and adds "the herald Chalbes and the attendants" to the list of those slain by Herakles.]

And traversing Asia he put in to Thermydrae, the harbor of the Lindians.^[Thermydra is the form of the name given by Stephanus Byzantius, s.v.. In his account of this incident Tzetzes calls the harbour Thermydron (Tzetzes. Chiliades ii.385). Lindus was one of the chief cities of Rhodes.] And having loosed one of the bullocks from the cart of a cowherd, he sacrificed it and feasted. But the cowherd, unable to protect himself, stood on a certain mountain and cursed. Wherefore to this day, when they sacrifice to Hercules, they do it with curses.^[Compare Conon 11; Philostratus, Im. ii.24; Tzetzes, Chiliades ii.385ff.; Lactantius, Divin. Inst. i.21. According to all these writers except Tzetzes (who clearly follows Apollodorus), Herakles's victim in this affair was not a waggoner, but a ploughman engaged in the act of ploughing; Philostratus names him Thiodamus, and adds: "Hence a ploughing ox is sacrificed to Herakles and they begin the sacrifice with curses such as, I suppose, the husbandman then made use of; and Herakles is pleased and blesses the Lindians in return for their curses." According to Lactantius, it was a pair of oxen that was sacrificed, and the altar at which the sacrifice took place bore the name of _bouzygos_, that is, "yoke of oxen." Hence it seems probable that the sacrifice which the story purported to explain was offered at the time of ploughing in order to ensure a blessing on the ploughman's labours. This is confirmed by the ritual of the sacred ploughing observed at Eleusis, where members of the old priestly family of the Bouzygai or Ox-yokers uttered many curses as they guided the plough down the furrows of the Rarian Plain. See Etymologicum Magnum, s.v. \rendergreek{Βουζυγία}, p. 206, lines 47ff.; Anecdota Graeca, ed. Bekker, i.221; Hesychius, s.v. \rendergreek{Βουζύγης}; Paroemiographi Graeci, ed. Leutsch and Schneidewin, i. p. 388; Scholiast on Soph. Ant. 255; Plut. Praecepta Conjugalia 42. Compare J. Toepffer, Attische Genealogie (Berlin, 1889), rr. 136ff.; Spirits of the Corn and of the Wild, i.108ff. The Greeks seem to have deemed curses of special efficacy to promote the fertility of the ground; for we are told that when a Greek sowed cummin he was expected to utter imprecations or the corn would not turn out well. See Theophrastus, Historia plantarum vii.3.3, ix.8.8; Plut. Quaest. Conviv. vii.2.3; Pliny, Nat. Hist. xix.120. Roman writers mention a like custom observed by the sowers of rue and basil. See Palladius, De re rustica, iv.9; Pliny, Nat. Hist. xix.120. As to the beneficent effect of curses, when properly directed, see further The Magic Art and the Evolution of Kings, i.278ff.]

And passing by Arabia he slew Emathion, son of Tithonus,^[Compare Tzetzes, Chiliades ii.369ff., who as usual follows Apollodorus. According to Diod. 4.27.3, after Herakles had slain Busiris, he ascended the Nile to Ethiopia and there slew Emathion, king of Ethiopia.] and journeying through Libya to the outer sea he received the goblet from the Sun. And having crossed to the opposite mainland he shot on the Caucasus the eagle, offspring of Echidna and Typhon, that was devouring the liver of Prometheus, and he released Prometheus,^[As to Herakles and Prometheus, see Diod. 4.15.2; Paus. 5.11.6; Tzetzes, Chiliades ii.370ff.; Scholiast on Ap. Rhod., Argon. ii.1248, iv.1396; Hyginus, Ast. ii.15; Hyginus, Fab. 31, 54, and 144; Serv. Verg. Ecl. 6.42. The Scholiast on Ap. Rhod., Argon. ii.1248 agrees with Apollodorus as to the parentage of the eagle which preyed on Prometheus, and he cites as his authority Pherecydes; hence we may surmise that Apollodorus is following the same author in the present passage. The time during which Prometheus suffered on the Caucasus was said by Aeschylus to be thirty thousand years (Hyginus, Ast. ii.15); but Hyginus, though he reports this in one passage, elsewhere reduces the term of suffering to thirty years (Hyginus, Fab. 54, 144).] after choosing for himself the bond of olive,^[The reference seems to be to the crown of olive which Herakles brought from the land of the Hyperboreans and instituted as the badge of victory in the Olympic games. See Pind. O. 3.11(20)ff.; Paus. 5.7.7. The ancients had a curious notion that the custom of wearing crowns or garlands on the head and rings on the fingers was a memorial of the shackles once worn for their sake by their great benefactor Prometheus among the rocks and snows of the Caucasus. In order that the will of Zeus, who had sworn never to release Prometheus, might not be frustrated by the entire liberation of his prisoner from his chains, Prometheus on obtaining his freedom was ordered to wear on his finger a ring made out of his iron fetters and of the rock to which he had been chained; hence, in memory of their saviour's sufferings, men have worn rings ever since. The practice of wearing crowns or garlands was explained by some people in the same way. See Hyginus, Ast. ii.15; Serv. Verg. Ecl. 6.42; Pliny, Nat. Hist. xxxvii.2; Isidore, Orig. xix.32.1. According to one version of the legend, the crown which the sufferer on regaining his liberty was doomed to wear was a crown of willow; and the Carians, who used to crown their brows with branches of willow, explained that they did so in imitation of Prometheus. See Athenaeus xv.11-13, pp. 671-673 EB. In the present passage of Apollodorus, if the text is correct, Herakles, as the deliverer of Prometheus, is obliged to bind himself vicariously for the prisoner whom he has released; and he chooses to do so with his favourite olive. Similarly he has to find a substitute to die instead of Prometheus, and he discovers the substitute in Chiron. As to the substitution of Chiron for Prometheus, see Apollod. 2.5.4. It is remarkable that, though Prometheus was supposed to have attained to immortality and to be the great benefactor, and even the creator, of mankind, he appears not to have been worshipped by the Greeks; Lucian says that nowhere were temples of Prometheus to be seen (Lucian, Prometheus 14).] and to Zeus he presented Chiron, who, though immortal, consented to die in his stead.

Now Prometheus had told Hercules not to go himself after the apples but to send Atlas, first relieving him of the burden of the sphere; so when he was come to Atlas in the land of the Hyperboreans, he took the advice and relieved Atlas. But when Atlas had received three apples from the Hesperides, he came to Hercules, and not wishing to support the sphere< he said that he would himself carry the apples to Eurystheus, and bade Hercules hold up the sky in his stead. Hercules promised to do so, but succeeded by craft in putting it on Atlas instead. For at the advice of Prometheus he begged Atlas to hold up the sky till he should>^[The passage in angular brackets is wanting in the manuscripts of Apollodorus, but is restored from the Scholiast on Ap. Rhod., Argon. iv.1396, who quotes as his authority Pherecydes, the writer here seemingly followed by Apollodorus. See the Critical Note. The story of the contest of wits between Herakles and Atlas is represented in one of the extant metopes of the temple of Zeus at Olympia, which were seen and described by Paus. 5.10.9. See Frazer, note on Pausanias (vol. iii. pp. 524ff.).] put a pad on his head. When Atlas heard that, he laid the apples down on the ground and took the sphere from Hercules. And so Hercules picked up the apples and departed. But some say that he did not get them from Atlas, but that he plucked the apples himself after killing the guardian snake. And having brought the apples he gave them to Eurystheus. But he, on receiving them, bestowed them on Hercules, from whom Athena got them and conveyed them back again; for it was not lawful that they should be laid down anywhere.

A twelfth labour imposed on Hercules was to bring Cerberus from Hades.^[As to Herakles and Cerberus, see Hom. Il. 8.366ff.; Hom. Od. 11.623ff.; Bacch. 5.56ff., ed. Jebb; Eur. Herc. 23ff.; Eur. Her. 1277ff.; Diod. 4.25.1, Diod. 4.26.1; Paus. 2.31.6; Paus. 2.35.10; Paus. 3.18.13; Paus. 3.25.5ff.; Paus. 5.26.7; Paus. 9.34.5; Tzetzes, Chiliades ii.388-405 (who seems to follow Apollodorus); Scholiast on Hom. Il. viii.368; Ov. Met. 7.410ff.; Hyginus, Fab. 31; Seneca, Agamemnon 859ff.; Eur. Herc. 50ff.; Scriptores rerum mythicarum Latini, ed. Bode, i. p. 20 (First Vatican Mythographer 57). Ancient writers differ as to the number of Cerberus's heads. Hesiod assigned him fifty (Hes. Th. 311ff.); Pindar raised the number to a hundred (Scholiast on Hom. Il. viii.368), a liberal estimate which was accepted by Tzetzes in one place (Tzetzes, Scholiast on Lycophron 699) and by Horace in another (Hor. Carm. 2.13.34). Others reduced the number to three. See Soph. Trach. 1098; Eur. Herc. 24; Eur. Herc. 1277; Paus. 3.25.6; Hor. Carm. 2.19.29ff., iii.11.17ff.; Verg. G. 4.483, Aen. vi.417ff.; Ov. Met. 4.451ff.; Hyginus, Fab. 151; Seneca, Agamemnon 62; Seneca, Herakles Furens 783ff. Apollodorus apparently seeks to reconcile these contradictions, and he is followed as usual by Tzetzes (Tzetzes, Chiliades ii.390ff.), who, however, at the same time speaks of Cerberus as fifty-headed. The whole of the present passage of Apollodorus, from the description of Cerberus down to Herakles's slaughter of one of the kine of Hades, is quoted, with a few small variations, by a Scholiast on Hom. Il. viii.368. See Dindorf's edition of the Scholia, vol. i. p. 287. The quotation is omitted by Bekker in his edition of the Scholia p. 233.] Now this Cerberus had three heads of dogs, the tail of a dragon, and on his back the heads of all sorts of snakes. When Hercules was about to depart to fetch him, he went to Eumolpus at Eleusis, wishing to be initiated. However it was not then lawful for foreigners to be initiated: since he proposed to be initiated as the adoptive son of Pylius. But not being able to see the mysteries because he had not been cleansed of the slaughter of the centaurs, he was cleansed by Eumolpus and then initiated.^[As to the initiation of Herakles at Eleusis, compare Diod. 4.25.1; Tzetzes, Chiliades ii.394. According to Diodorus, the rites were performed on this occasion by Musaeus, son of Orpheus. Elsewhere (Tzetzes, Chiliades iv.14.3) the same writer says that Demeter instituted the lesser Eleusinian mysteries in honour of Herakles for the purpose of purifying him after his slaughter of the centaurs. The statement that Pylius acted as adoptive father to Herakles at his initiation is repeated by Plut. Thes. 33, who mentions that before Castor and Pollux were initiated at Athens they were in like manner adopted by Aphidnus. Herodotus says (Hdt. 8.65) that any Greek who pleased might be initiated at Eleusis. The initiation of Herakles is represented in ancient reliefs. See A. B. Cook, Zeus, i.425ff.] And having come to Taenarum in Laconia, where is the mouth of the descent to Hades, he descended through it.^[Compare Eur. Herc. 23ff.; Paus. 3.25.5; Seneca, Herakles Furens 807ff. Sophocles seems to have written a Satyric drama on the descent of Herakles into the infernal regions at Taenarum. See The Fragments of Sophocles, ed. A. C. Pearson, vol. i. pp. 167ff. According to another account, Herakles descended, not at Taenarum but at the Acherusian Chersonese, near Heraclea Pontica on the Black Sea. The marks of the descent were there pointed out to a great depth. See Xen. Ana. 6.2.2.] But when the souls saw him, they fled, save Meleager and the Gorgon Medusa. And Hercules drew his sword against the Gorgon, as if she were alive, but he learned from Hermes that she was an empty phantom.^[So Bacch. 5.71ff., ed. Jebb represents Herakles in Hades drawing his bow against the ghost of Meleager in shining armour, who reminds the hero that there is nothing to fear from the souls of the dead; so, too, Verg. A. 6.290ff. describes Aeneas in Hades drawing his sword on the Gorgons and Harpies, till the Sibyl tells him that they are mere flitting empty shades. Apollodorus more correctly speaks of the ghost of only one Gorgon (Medusa), because of the three Gorgons she alone was mortal. See Apollod. 2.4.2. Compare Hom. Od. 11.634ff.] And being come near to the gates of Hades he found Theseus and Pirithous,^[On Theseus and Pirithous in hell, see Apollod. E.1.23ff.; Hom. Od. 1.631; Eur. Herc. 619; Ap. Rhod., Argon. i.101ff., with the Scholiast on 101; Diod. 4.26.1, Diod. 4.63.4ff.; Paus. 1.17.4; Paus. 9.31.5; Paus. 10.29.9; Apostolius, Cent. iii.36; Suidas, s.v. \rendergreek{λίσποι};Scholiast on Aristoph. Kn. 1368; Verg. A. 6.392ff., 617ff.; Hor. Carm. 3.4.79ff., iv.7.27ff.; Hyginus, Fab. 79; Aulus Gellius x.16.13; Serv. Verg. A. 6.617; Scriptores rerum mythicarum Latini, ed. Bode, i. p. 18 (First Vatican Mythographer 48). The general opinion seems to have been that Herakles rescued Theseus, but that he could not save Pirithous. Others, however, alleged that he brought up both from the dead (Hyginus, Fab. 79); others again affirmed that he brought up neither (Diod. 4.63.5). A dull rationalistic version of the romantic story converted Hades into a king of the Molossians or Thesprotians, named Aidoneus, who had a wife Persephone, a daughter Cora, and a dog Cerberus, which he set to worry his daughter's suitors, promising to give her in marriage to him who could master the ferocious animal. Discovering that Theseus and Pirithous were come not to woo but to steal his daughter, he arrested them. The dog made short work of Pirithous, but Theseus was kept in durance till the king consented to release him at the intercession of Herakles. See Plut. Thes. 31.4-35.1ff.; Ael., Var. Hist. iv.5; Paus. 1.17.4, Paus. 1.18.4, Paus. 2.22.6, Paus. 3.18.5; Tzetzes, Chiliades ii.406ff.] him who wooed Persephone in wedlock and was therefore bound fast. And when they beheld Hercules, they stretched out their hands as if they should be raised from the dead by his might. And Theseus, indeed, he took by the hand and raised up, but when he would have brought up Pirithous, the earth quaked and he let go. And he rolled away also the stone of Ascalaphus.^[See Apollod. 1.5.3.] And wishing to provide the souls with blood, he slaughtered one of the kine of Hades. But Menoetes, son of Ceuthonymus, who tended the king, challenged Hercules to wrestle, and, being seized round the middle, had his ribs broken;^[Compare Tzetzes, Chiliades ii.396ff., who calls the herdsman Menoetius.] howbeit, he was let off at the request of Persephone. When Hercules asked Pluto for Cerberus, Pluto ordered him to take the animal provided he mastered him without the use of the weapons which he carried. Hercules found him at the gates of Acheron, and, cased in his cuirass and covered by the lion's skin, he flung his arms round the head of the brute, and though the dragon in its tail bit him, he never relaxed his grip and pressure till it yielded.^[Literally, "till he persuaded (it)."] So he carried it off and ascended through Troezen.^[Compare Paus. 2.31.2. According to others, the ascent of Herakles with Cerberus took place at Hermione (Paus. 2.35.10) or on Mount Laphystius in Boeotia (Paus. 9.34.5).] But Demeter turned Ascalaphus into a short-eared owl,^[Compare Ov. Met. 5.538ff. As to the short-eared owl (\rendergreek{ὦτος}), see D'Arcy Wentworth Thompson, Glossary of Greek Birds, pp. 200ff.] and Hercules, after showing Cerberus to Eurystheus, carried him back to Hades.[^bd2e726c74fe4d95af1bce38b0de2b3f]

\newpage

# Viminacium To Naissus
  
## After Viminacium

Virgil departed from Viminacium, intending to travel by road to Tibiscum, a distance of about 96 miles. 

This is a smooth road, by which many wagons were bringing wood to Tibiscum. There was written there these words: Silvano / Aug(usto) sac(rum) / Acutianus / (ene)f(iciarius) co(n)s(ularis) leg(ionis) XIIII / gem(inae) Gordian(ae) / d(omino) n(ostro) Gordiano Aug(usto) / et Aviola co(n)s(ulibus) l(ibens)(?) a(nimo)(?). There a spring wells up, and around about it is a meadow. Next to the straight road that leads to Tibiscum, there is visible a sculpted tomb. Now the road is quieter. A grove of Minerva is hard by the road, a grove of poplar trees. 

All of this brought to his mind what Horace had said about the countryside near that place:

## A Story About The Countryside Near That Place


Come down, Calliope, from above:  
Breathe on the pipe a strain of fire:  
Or if a graver note thou love,  
With Phoebus' cittern and his lyre.  
You hear her? or is this the play  
Of fond illusion? Hark! meseems  
Through gardens of the good I stray,  
'Mid murmuring gales and purling streams.  
Me, as I lay on Vultur's steep,  
A truant past Apulia's bound,  
O'ertired, poor child, with play and sleep,  
With living green the stock-doves crown'd—  
A legend, nay, a miracle,  
By Acherontia's nestlings told,  
By all in Bantine glade that dwell,  
Or till the rich Forentan mould.  
"Bears, vipers, spared him as he lay,  
The sacred garland deck'd his hair,  
The myrtle blended with the bay:  
The child's inspired: the gods were there."  
Your grace, sweet Muses, shields me still  
On Sabine heights, or lets me range  
Where cool Praeneste, Tibur's hill,  
Or liquid Baiae proffers change.  
Me to your springs, your dances true,  
Philippi bore not to the ground,  
Nor the doom'd tree in falling slew,  
Nor billowy Palinurus drown'd.  
Grant me your presence, blithe and fain  
Mad Bosporus shall my bark explore;  
My foot shall tread the sandy plain  
That glows beside Assyria's shore;  
'Mid Briton tribes, the stranger's foe,  
And Spaniards, drunk with horses' blood,  
And quiver'd Scythians, will I go  
Unharm'd, and look on Tanais' flood.  
When Caesar's self in peaceful town  
The weary veteran's home has made,  
You bid him lay his helmet down  
And rest in your Pierian shade.  
Mild thoughts you plant, and joy to see  
Mild thoughts take root. The nations know  
How with descending thunder he  
The impious Titans hurl'd below,  
Who rules dull earth and stormy seas,  
And towns of men, and realms of pain,  
And gods, and mortal companies,  
Alone, impartial in his reign.  
Yet Jove had fear'd the giant rush,  
Their upraised arms, their port of pride,  
And the twin brethren bent to push  
Huge Pelion up Olympus' side.  
But Typhon, Mimas, what could these,  
Or what Porphyrion's stalwart scorn,  
Rhoetus, or he whose spears were trees,  
Enceladus, from earth uptorn,  
As on they rush'd in mad career  
'Gainst Pallas' shield? Here met the foe  
Fierce Vulcan, queenly Juno here,  
And he who ne'er shall quit his bow,  
Who laves in clear Castalian flood  
His locks, and loves the leafy growth  
Of Lycia next his native wood,  
The Delian and the Pataran both.  
Strength, mindless, falls by its own weight;  
Strength, mix'd with mind, is made more strong  
By the just gods, who surely hate  
The strength whose thoughts are set on wrong.  
Let hundred-handed Gyas bear  
His witness, and Orion known  
Tempter of Dian, chaste and fair,  
By Dian's maiden dart o'erthrown.  
Hurl'd on the monstrous shapes she bred,  
Earth groans, and mourns her children thrust  
To Orcus; Aetna's weight of lead  
Keeps down the fire that breaks its crust;  
Still sits the bird on Tityos' breast,  
The warder of Unlawful love;  
Still suffers lewd Pirithous, prest  
By massive chains no hand may move.  
[^ad4d364d9590419abd5af1ca18a87154]

  
## To Viminacium By Road

Intending to travel by road to Viminacium, Virgil left Tibiscum. It was a journey of about 96 miles. 

He had set out from Tibiscum amidst a throng travelling the same way. They pass a pillar on the right surmounted by a stone urn. By the road is a salt spring. He left the city early, before the rising of the sun. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. 

While he visited his friend at the countryside near that place, he was pleased to discover _Histories_, by Polybius. Picking it up, he read:

## The Story Of The Countryside Near That Place


But the increased power and national advancement which these events brought to the Achaeans excited the envy of the Aetolians; who, besides their natural inclination to unjust and selfish aggrandisement, were inspired with the hope of breaking up the union of Achaean states, as they had before succeeded in partitioning those of Acarnania with Alexander,^[Alexander II. of Epirus, son of Pyrrhus, whom he succeeded B. C. 272. The partition of Acarnania took place in B. C. 266.] and had planned to do those of Achaia with Antigonus Gonatas. Instigated once more by similar expectations, they had now the assurance to enter into communication and close alliance at once with Antigonus (at that time ruling Macedonia as guardian of the young King Philip), and with Cleomenes, King of Sparta. They saw that Antigonus had undisputed possession of the throne of Macedonia, while he was an open and avowed enemy of the Achaeans owing to the surprise of the Acrocorinthus; and they supposed that if they could get the Lacedaemonians to join them in their hostility to the league, they would easily subdue it, by selecting a favourable opportunity for their attack, and securing that it should be assaulted on all sides at once. And they would in all probability have succeeded, but that they had left out the most important element in the calculation, namely, that in Aratus they had to reckon with an opponent to their plans of ability equal to almost any emergency. Accordingly, when they attempted this violent and unjust interference in Achaia, so far from succeeding in any of their devices, they, on the contrary, strengthened Aratus, the then president of the league, as well as the league itself. So consummate was the ability with which he foiled their plan and reduced them to impotence. The manner in which this was done will be made clear in what I am about to relate.[^84ff20c73b9940148ad16e5907a9fd75]

  
## Travelling By River, Upstream

Intending to travel on a military boat headed upstream to Singidunum, Virgil left Viminacium. It was a distance of about 49 miles. 

The sun beats down. Birds sing their greetings. No backward glances for the city left behind. 

All of this brought to his mind what Lucan, 39-65 had said about the countryside near that place:

## The Story Of The Countryside Near That Place


  
Then a hurricane  
Swooped on the boat and tore away the sheet:  
The fluttering sail fell on the fragile mast:  
And groaned the joints. From all the universe  
Commingled perils rushed. In Atlas' seas  
First Corus^[Book I., 464.] raised his head, and stirred the depths  
To fury, and had forced upon the rocks  
Whole seas and oceans; but the chilly north  
Drove back the deep that doubted which was lord.  
But Scythian Aquilo prevailed, whose blast  
Tossed up the main and showed as shallow pools  
Each deep abyss; and yet was not the sea  
Heaped on the crags, for Corus' billows met  
The waves of Boreas: such seas had clashed  
Even were the winds withdrawn; Eurus enraged  
Burst from the cave, and Notus black with rain,  
And all the winds from every part of heaven  
Strove for their own; and thus the ocean stayed  
Within his boundaries. No petty seas  
Rapt in the storm are whirled. The Tuscan deep  
Invades th' AEgean; in Ionian gulfs  
Sounds wandering Hadria. How long the crags  
Which that day fell, the Ocean's blows had braved!  
What lofty peaks did vanquished earth resign!  
And yet on yonder coast such mighty waves  
Took not their rise; from distant regions came  
Those monster billows, driven on their course  
By that great current which surrounds the world.^[The ocean current, which, according to Hecataeus, surrounded the world. But Herodotus of this theory says, 'For my part I know of no river called Ocean, and I think that Homer or one of the earlier poets invented the name and introduced it into his poetry.' (Book II., 23, and Book IV., 36.) In 'Oceanus' Eschylus seems to have intended to personify the great surrounding stream. ('Prom. Vinc.,' lines 291, 308.)]  
Thus did the King of Heaven, when length of years  
Wore out the forces of his thunder, call  
His brother's trident to his help, what time  
The earth and sea one second kingdom formed  
And ocean knew no limit but the sky.  
Now, too, the sea had risen to the stars  
In mighty mass, had not Olympus' chief  
Pressed down its waves with clouds: that night from heaven  
Came not, as others; but the murky air  
Was dim with pallor of the realms below;^[Comp. VI., 615.]  
The sky lay on the deep; within the clouds  
The waves received the rain : the lightning flash  
Clove through the parted air a path obscured  
By mist and darkness: and the heavenly vaults  
Re-echoed to the tumult, and the frame  
That holds the sky was shaken. Nature feared  
Chaos returned, as though the elements  
Had burst their bonds, and night had come to mix  
Th' infernal shades with heaven.  
In such turmoil  
Not to have perished was their only hope.  
Far as from Leucas point the placid main  
Spreads to the horizon, from the billow's crest  
They viewed the dashing of th' infuriate sea;  
Thence sinking to the middle trough, their mast  
Scarce topped the watery height on either hand,  
Their sails in clouds, their keel upon the ground.  
For all the sea was piled into the waves,  
And drawn from depths between laid bare the sand.  
The master of the boat forgot his art,  
For fear o'ercame; he knew not where to yield  
Or where to meet the wave: but safety came  
From ocean's self at war: one billow forced  
The vessel under, but a huger wave  
Repelled it upwards, and she rode the storm  
Through every blast triumphant. Not the shore  
Of humble Sason,^[Sason is a small island just off the Ceraunian rocks, the point of which is now called Cape Linguetta, and is nearly opposite to Brindisi.] nor Thessalia's coast  
Indented, not Ambracia's scanty ports  
Dismayed the mariners, but the giddy tops  
Of high Ceraunia's cliffs.  
But Caesar now,  
Thinking the peril worthy of his fates:  
Are such the labours of the gods? ' exclaimed,  
Bent on my downfall have they sought me thus,  
Here in this puny skiff in such a sea?  
If to the deep the glory of my fall  
Is due, and not to war, intrepid still  
Whatever death they send shall strike me down.  
Let fate cut short the deeds that I would do  
And hasten on the end: the past is mine.  
The northern nations fell beneath my sword;  
'My dreaded name compels the foe to flee.  
'Pompeius yields me place; the people's voice  
Gave at my order what the wars denied.  
And all the titles which denote the powers  
Known to the Roman state my name shall bear.  
Let none know this but thou who hear'st my prayers,  
Fortune! that Caesar summoned to the shades,  
Dictator, Consul, full of honours, died  
Ere his last prize was won. I ask no pyre  
Or tomb, ye gods! wherein my dust may rest:  
Nay! plunge in middle deep this battered frame!  
All earth shall look for me, nor shall men cease  
At Caesar's name to fear.' Such words he spake,  
When lo! a tenth gigantic billow raised  
The feeble keel, and where between the rocks  
A cleft gave safety, placed it on the shore.  
Thus in a moment fortune, kingdoms, lands,  
Once more were Caesar's.  
But on his return  
When daylight came, he entered not the camp  
Silent as when he parted; for his friends  
Soon pressed around him, and with weeping eyes  
In accents welcome to his ears began:  
'Whither in reckless daring hast thou gone,  
Unpitying Caesar? Were these humble lives  
Left here unguarded while thy limbs were given,  
Unsought for, to be scattered by the storm?  
'When on thy breath so many nations hang  
For life and safety, and so great a world  
Calls thee its master, to have courted death  
Proves want of heart. Were none of all thy friends  
Deserving held to join their fate with thine?  
'When thou wast tossed upon the stormy main  
We lay in slumber! Shame upon such sleep!  
'And why thyself didst seek Italia's shores?  
'"Twere cruel (such thy thought) to speak the word  
That bade another dare the furious sea.  
All men must bear what chance or fate may bring,  
The sudden peril and the stroke of death;  
But shall the ruler of the world attempt  
'The raging ocean? With incessant prayers  
Why weary heaven? is it indeed enough  
To crown the war, that Fortune and the deep  
'Have cast thee on our shores? And wouldst thou use  
'The grace of favouring deities, to gain  
Not lordship, not the empire of the world,  
'But lucky shipwreck! ' Night dispersed, and soon  
The sun beamed on them, and the wearied deep,  
The winds permitting, lulled its waves to rest.  
And when Antonius saw a breeze arise  
Fresh from a cloudless heaven, to break the sea,  
He loosed his ships which, by the pilots' hands  
And by the wind in equal order held,  
Swept as a marching host across the main.  
But night unfriendly from the seamen snatched  
All governance of sail, parting the ships  
In divers paths asunder. Like as cranes  
Deserting frozen Strymon for the streams  
Of Nile, when winter falls, in casual lines  
Of wedge-like figures^[Compare Paradise Lost, VII.. 125.] first ascend the sky;  
But when in loftier heaven the southern breeze  
Strikes on their pinions tense, in loose array  
Dispersed at large, in flight irregular,  
They wing their journey onwards. Stronger winds  
With day returning blew the navy on,  
Past Lissus' shelter which they vainly sought,  
Till bare to northern blasts, Nymphaeum's port,  
But safe in southern, gave the fleet repose.  
[^c6916853c5324ab18da8397ff2c027f1]

  
## Departing From Singidunum

From Singidunum to Viminacium is about 49 miles away when travelling on a military boat floating downstream. 

The sun beats down. 

The library at the countryside near that place happened to have a copy of _Metamorphoses_, where Virgil encountered it.

## A Story By Ovid 43 B.C.-17 Or 18 A.D About The Countryside Near That Place From _Metamorphoses_


So ended she; at once Leuconoe  
took the narrator's thread; and as she spoke  
her sisters all were silent.  
"Even the Sun  
that rules the world was captive made of Love.  
My theme shall be a love-song of the Sun.  
'Tis said the Lord of Day, whose wakeful eye  
beholds at once whatever may transpire,  
witnessed the loves of Mars and Venus. Grieved  
to know the wrong, he called the son of Juno,  
Vulcan, and gave full knowledge of the deed,  
showing how Mars and Venus shamed his love,  
as they defiled his bed. Vulcan amazed,—  
the nimble-thoughted Vulcan lost his wits,  
so that he dropped the work his right hand held.  
But turning from all else at once he set  
to file out chains of brass, delicate, fine,  
from which to fashion nets invisible,  
filmy of mesh and airy as the thread  
of insect-web, that from the rafter swings.—  
Implicit woven that they yielded soft  
the slightest movement or the gentlest touch,  
with cunning skill he drew them round the bed  
where they were sure to dally. Presently  
appeared the faithless wife, and on the couch  
lay down to languish with her paramour.—  
Meshed in the chains they could not thence arise,  
nor could they else but lie in strict embrace,—  
cunningly thus entrapped by Vulcan's wit.—  
At once the Lemnian cuckold opened wide  
the folding ivory doors and called the Gods,—  
to witness. There they lay disgraced and bound.  
I wot were many of the lighter Gods  
who wished themselves in like disgraceful bonds.—  
The Gods were moved to laughter: and the tale  
was long most noted in the courts of Heaven.  
The Cytherean Venus brooded on  
the Sun's betrayal of her stolen joys,  
and thought to torture him in passion's pains,  
and wreak requital for the pain he caused.  
Son of Hyperion! what avails thy light?  
What is the profit of thy glowing heat?  
Lo, thou whose flames have parched innumerous lands,  
thyself art burning with another flame!  
And thou whose orb should joy the universe  
art gazing only on Leucothea's charms.  
Thy glorious eye on one fair maid is fixed,  
forgetting all besides. Too early thou  
art rising from thy bed of orient skies,  
too late thy setting in the western waves;  
so taking time to gaze upon thy love,  
thy frenzy lengthens out the wintry hour!  
And often thou art darkened in eclipse,  
dark shadows of this trouble in thy mind,  
unwonted aspect, casting man perplexed  
in abject terror. Pale thou art, though not  
betwixt thee and the earth the shadowous moon  
bedims thy devious way. Thy passion gives  
to grief thy countenance—for her thy heart  
alone is grieving—Clymene and Rhodos,  
and Persa, mother of deluding Circe,  
are all forgotten for thy doting hope;  
even Clytie, who is yearning for thy love,  
no more can charm thee; thou art so foredone.  
Leucothea is the cause of many tears,  
Leucothea, daughter of Eurynome,  
most beauteous matron of Arabia's strand,  
where spicey odours blow. Eurynome  
in youthful prime excelled her mother's grace,  
and, save her daughter, all excelled besides.  
Leucothea's father, Orchamas was king  
where Achaemenes whilom held the sway;  
and Orchamas from ancient Belus' death  
might count his reign the seventh in descent.  
The dark-night pastures of Apollo's steeds  
are hid below the western skies; when there,  
and spent with toil, in lieu of nibbling herbs  
they take ambrosial food: it gives their limbs  
restoring strength and nourishes anew.  
Now while these coursers eat celestial food  
and Night resumes his reign, the god appears  
disguised, unguessed, as old Eurynome  
to fair Leucothea as she draws the threads,  
all smoothly twisted from her spindle. There  
she sits with twice six hand-maids ranged around,  
and as the god beholds her at the door  
he kisses her, as if a child beloved  
and he her mother. And he spoke to her:  
"Let thy twelve hand-maids leave us undisturbed,  
for I have things of close import to tell,  
and seemly, from a mother to her child.",  
so when they all withdrew the god began,  
"Lo, I am he who measures the long year;  
I see all things, and through me the wide world  
may see all things; I am the glowing eye  
of the broad universe! Thou art to me  
the glory of the earth!" Filled with alarm,  
from her relaxed fingers she let fall  
the distaff and the spindle, but, her fear  
so lovely in her beauty seemed, the God  
no longer brooked delay: he changed his form  
back to his wonted beauty and resumed  
his bright celestial. Startled at the sight  
the maid recoiled a space; but presently  
the glory of the god inspired her love;  
and all her timid doubts dissolved away;  
without complaint she melted in his arms.  
So ardently the bright Apollo loved,  
that Clytie, envious of Leucothea's joy,  
where evil none was known, a scandal made;  
and having published wide their secret love,  
leucothea's father also heard the tale.  
Relentlessly and fierce, his cruel hand  
buried his living daughter in the ground,  
who, while her arms implored the glowing Sun,  
complained. "For love of thee my life is lost."  
And as she wailed her father sowed her there.  
Hyperion's Son began with piercing heat  
to scatter the loose sand, a way to open,  
that she might look with beauteous features forth  
too late! for smothered by the compact earth,  
thou canst not lift thy drooping head; alas!  
A lifeless corse remains.  
No sadder sight  
since Phaethon was blasted by the bolt,  
down-hurled by Jove, had ever grieved the God  
who daily drives his winged steeds. In vain  
he strives with all the magic of his rays  
to warm her limbs anew. — The deed is done—  
what vantage gives his might if fate deny?  
He sprinkles fragrant nectar on her grave,  
and lifeless corse, and as he wails exclaims,  
"But naught shall hinder you to reach the skies."  
At once the maiden's body, steeped in dews  
of nectar, sweet and odourate, dissolves  
and adds its fragrant juices to the earth:  
slowly from this a sprout of Frankincense  
takes root in riched soil, and bursting through  
the sandy hillock shows its top.  
No more  
to Clytie comes the author of sweet light,  
for though her love might make excuse of grief,  
and grief may plead to pardon jealous words,  
his heart disdains the schemist of his woe;  
and she who turned to sour the sweet of love,  
from that unhallowed moment pined away.  
Envious and hating all her sister Nymphs,  
day after day,—and through the lonely nights,  
all unprotected from the chilly breeze,  
her hair dishevelled, tangled, unadorned,  
she sat unmoved upon the bare hard ground.  
Nine days the Nymph was nourished by the dews,  
or haply by her own tears' bitter brine;—  
all other nourishment was naught to her.—  
She never raised herself from the bare ground,  
though on the god her gaze was ever fixed;—  
she turned her features towards him as he moved:  
they say that afterwhile her limbs took root  
and fastened to the around.  
A pearly white  
overspread her countenance, that turned as pale  
and bloodless as the dead; but here and there  
a blushing tinge resolved in violet tint;  
and something like the blossom of that name  
a flower concealed her face. Although a root  
now holds her fast to earth, the Heliotrope  
turns ever to the Sun, as if to prove  
that all may change and love through all remain.  
[^cb1364d7359840a2875666e3785c439d]

  
## Viminacium To Horreum Margi By Road

Virgil departed from Viminacium, intending to travel by road to Horreum Margi, about 57 miles away. 

He passes another milestone. D(is) M(anibus) / M(- - -) Pra[- - -] / anno(rum) XX[- - -] / Ianuarius / [- - -]AVIS[- - -] / [- - - - - -] / [&?: he pondered the sight of this inscription. He had set out from Viminacium amidst a throng travelling the same way. There is a fountain of cold water springing from the rock. A cloud passes in front of the sun. Now the road is quieter. Water has washed out the road, making for slow going. His shoes are covered in dust from the road. 

  
## The Journey To Naissus

From Horreum Margi to Naissus is a journey of about 51 miles when travelling by road. 

Above the roads are ruins, among which is a cave sacred to Asclepius. A caravan from Naissus passed by. The sun beats down. He passes another milestone. 

All of this brought to his mind what Polybius had said about the countryside near that place:

## What Polybius Once Said About The Countryside Near That Place


I thought this was the best point; first, because it is there that Aratus leaves off, and I meant my work, as far as it was Greek history, to be a continuation of his; and, secondly, because the period thus embraced in my history would fall partly in the life of my father, and partly in my own; and thus I should be able to speak as eye-witness of some of the events, and from the information of eye-witnesses of others. To go further back and write the report of a report, traditions at second or third hand, seemed to me unsatisfactory either with a view to giving clear impressions or making sound statements.But, above all, I began at this period because it was then that the history of the whole world entered on a new phase. Demetrius, had just become the boy king Achaeus, prince of Asia on this side of Taurus, had converted his show of power into a reality; Antiochus the Great had, a short time before, by the death of his brother Seleucus, succeeded while quite a young man to the throne of Syria; Ariarathes to that of Cappadocia; and Ptolemy Philopator to that of Egypt. Not long afterwards Lycurgus became King of Sparta, and the Carthaginians had recently elected Hannibal general to carry on the war lately described. Every government therefore being changed about this time, there seemed every likelihood of a new departure in policy: which is but natural and usual, and in fact did at this time occur. For the Romans and Carthaginians entered upon the war I have described; Antiochus and Ptolemy on one for the possession of Coele-Syria; and the Achaeans and Philip one against the Aetolians and Lacedaemonians. The causes of this last war must now be stated.[^e20bbe09d7bd406e9ecc16c27f2e9df6]

  
## Travelling By Road To Ulpiana

Leaving Naissus, Virgil set out for Ulpiana by road, a distance of about 80 miles. 

Along the road are graves, and a cenotaph. The road narrows here, an orchard wall encroaching on it. Now the road is quieter. An oxcart passes, loaded with grain. The sun beats down. As they go up from Naissus, they see the ruined walls. There is a fountain of cold water springing from the rock. 

  
## Travelling By Road To Naissus

Intending to travel by road to Naissus, Virgil left Ulpiana. It was at least 80 miles. 

He passes another milestone. Along the road are graves, and a cenotaph. An oxcart passes, loaded with grain. The road narrows here, an orchard wall encroaching on it. There a spring wells up, and around about it is a meadow. 

While he was visiting the countryside near that place, he made a point of copying down what Pausanias, fl. ca. 150-175 had written.

## On The Subject Of The Countryside Near That Place


Of the successes and failures of the Thebans in battle I found the most famous to be the following. They were overcome in battle by the Athenians, who had come to the aid of the Plataeans, when a war had arisen about the boundaries of their territory. They met with a second disaster when arrayed against the Athenians at Plataea,^[479 B.C] at the time when they are considered to have chosen the cause of King Xerxes rather than that of Greece.

The Theban people are in no way responsible for this choice, as at that time an oligarchy was in power at Thebes and not their ancestral form of government. In the same way, if it had been while Peisistratus or his sons still held Athens under a despotism that the foreigner had invaded Greece, the Athenians too would certainly have been accused of favouring Persia.

Afterwards, however, the Thebans won a victory over the Athenians at Delium in the territory of Tanagra,^[424 B.C] where the Athenian general Hippocrates, son of Ariphron, perished with the greater part of the army. During the period that began with the departure of the Persians and ended with the war between Athens and the Peloponnesus, the relations between Thebes and the Lacedaemonians were friendly. But when the war was fought out and the Athenian navy destroyed, after a brief interval Thebes along with Corinth was involved in the war with Lacedaemon.^[394 B.C]

Overcome in battle at Corinth and Coroncia, they won on the other hand at Leuctra the most famous victory we know of gained by Greeks over Greeks. They put down the boards of ten, which the Lacedaemonians had set up in the cities, and drove out the Spartan governors. Afterwards they also waged for ten years consecutively the Phocian war, called by the Greeks the Sacred war.

I have already said in my history of Attica^[See Paus. 1.25.3.] that the defeat at Chaeroneia was a disaster for all the Greeks; but it was even more so for the Thebans, as a garrison was brought into their city. When Philip died, and the kingship of Macedonia devolved on Alexander, the Thebans succeeded in destroying the garrison. But as soon as they had done so, heaven warned them of the destruction that was coming on them, and the signs that occurred in the sanctuary of Demeter Lawgiver were the opposite of those that occurred before the action at Leuctra.

For then spiders spun a white web over the door of the sanctuary, but on the approach of Alexander with his Macedonians the web was black. It is also said that there was a shower of ashes at Athens the year before the war waged against them by Sulla, which brought on them such great sufferings.[^1faeb86b63424adf998f36575ae3156a]

\newpage

# Naissus To Taliata
  
## Leaving Naissus By Road

Virgil departed from Naissus, intending to travel by road to Bononia (Moesia), a journey of about 76 miles. 

There a spring wells up, and around about it is a meadow. He left the city early, before the rising of the sun. Workers are raising the level of the road. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. By the road is a salt spring. His shoes are covered in dust from the road. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Next to the straight road that leads to Bononia (Moesia), there is visible a sculpted tomb. They pass a pillar on the right surmounted by a stone urn. 

He would later record what Thucydides had said about the countryside near that place.

## A Story By Thucydides About The Countryside Near That Place From _History Of The Peloponnesian War_


Assembling in Doberus, they prepared for descending from the heights upon Lower Macedonia, where the dominions of Perdiccas lay; for the Lyncestae, Elimiots, and other tribes more inland, though Macedonians by blood and allies and, dependents of their kindred, still have their own separate governments. The country on the sea coast, now called Macedonia, was first acquired by Alexander, the father of Perdiccas, and his ancestors, originally Temenids from Argos. This was effected by the expulsion from Pieria of the Pierians, who afterwards inhabited Phagres and other places under Mount Pangaeus, beyond the Strymon (indeed the country between Pangaeus and the sea is still called the Pierian gulf) of the Bottiaeans, at present neighbors of the Chalcidians, from Bottia, and by the acquisition in Paeonia of a narrow strip along the river Axius extending to Pella and the sea; the district of Mygdonia, between the Axius and the Strymon, being also added by the expulsion of the Edonians. From Eordia also were driven the Eordians, most of whom perished, though a few of them still live round Physca, and the Almopians from Almopia. These Macedonians also conquered places belonging to the other tribes, which are still theirs—Anthemus, Crestonia, Bisaltia, and much of Macedonia proper. The whole is now called Macedonia, and at the time of the invasion of Sitalces, Perdiccas, Alexander's son, was the reigning king.

[^ff0a827dd0584ebf9d59cf6cb95f7342]

  
## 58 Miles To Taliata

Intending to travel by road to Taliata, Virgil left Bononia (Moesia). It was a journey of about 58 miles. 

He passes another milestone. The road narrows here, an orchard wall encroaching on it. Above the roads are ruins, among which is a cave sacred to Asclepius. Next to the straight road that leads to Taliata, there is visible a sculpted tomb. Here is an ancient sanctuary common to all the gods, and around it is a grove containing springs. A caravan from Taliata passed by. 

All of this brought to his mind what Horace had said about the countryside near that place:

## A Story About The Countryside Near That Place


The touch of Zephyr and of Spring has loosen'd Winter's thrall;  
The well-dried keels are wheel'd again to sea:  
The ploughman cares not for his fire, nor cattle for their stall,  
And frost no more is whitening all the lea.  
Now Cytherea leads the dance, the bright moon overhead;  
The Graces and the Nymphs, together knit,  
With rhythmic feet the meadow beat, while Vulcan, fiery red,  
Heats the Cyclopian forge in Aetna's pit.  
'Tis now the time to wreathe the brow with branch of myrtle green,  
Or flowers, just opening to the vernal breeze;  
Now Faunus claims his sacrifice among the shady treen,  
Lambkin or kidling, which soe'er he please.  
Pale Death, impartial, walks his round: he knocks at cottage-gate  
And palace-portal. Sestius, child of bliss!  
How should a mortal's hopes be long, when short his being's date?  
Lo here! the fabulous ghosts, the dark abyss,  
The void of the Plutonian hall, where soon as e'er you go,  
No more for you shall leap the auspicious die  
To seat you on the throne of wine; no more your breast shall glow  
For Lycidas, the star of every eye.  
[^43734f36646d4396b9cd26e1cbca767f]

  
## Travelling By Road To Bononia (Moesia)

From Taliata to Bononia (Moesia) is about 58 miles away when travelling by road. 

The road narrows here, an orchard wall encroaching on it. Water has washed out the road, making for slow going. A grove of Minerva is hard by the road, a grove of poplar trees. On the road from Taliata to Bononia (Moesia) there is a village, in which there is a temple and grove. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Wondering if it was related to his journey, he read the words that were carved there: $] / [- - -]ER[- - -] / [- - -]ET O[- - -] / [- - -]I(?)I(?)[- - -] / [&. A cloud passes in front of the sun. 

All of this brought to his mind what Julius Caesar had said about the countryside near that place:

## On The Countryside Near That Place, According To Julius Caesar


Whilst these things passed in Achaia and at Dyrrhachium, and it was now known that Scipio was arrived in Macedonia. Caesar still adhering to his former views of peace, despatched Clodius to him, an intimate friend of both, whom he had taken into his service upon Scipio's recommendation. At his departure, he charged him with letters and instructions to this effect: "That he had tried all ways to bring about a peace; but believed he had hitherto miscarried, through the fault of those to whom his proposals were addressed, because they dreaded presenting them to Scipio's authority to be such, as not only privileged him to advise freely, but even to enforce his counsels, and compel the obstinate to hearken to reason: that he was possessed of an independent command, and had an army at his disposal to give weight to his interposition: that in employing it for so desirable an end, he would gain the indisputable praise of having restored quiet to Italy, peace to the provinces, and saved the empire." Clodius reported this commission to Scipio, and at first met with a favourable reception, but was afterwards denied audience: for Favonius having sharply reprimanded Scipio, as we learned after the conclusion of the war, the negotiation was discontinued, and Clodius returned to Caesar without success.[^b29094328cf744c6b136e3b053946e9e]

  
## Departing From Bononia (Moesia)

Virgil departed from Bononia (Moesia), intending to travel by road to Taliata, about 58 miles away. 

Wondering if it was related to his journey, he read the words that were carved there: $] / [S]abina Labrio/nis v(ixit) a(nnos) L Sen/ecio Suri v(ixit) a(nnos) XX. A caravan from Taliata passed by. His shoes are covered in dust from the road. He had set out from Bononia (Moesia) amidst a throng travelling the same way. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. There a spring wells up, and around about it is a meadow. 

While he was visiting the countryside near that place, he made a point of copying down what Plautus, Titus Maccius had written.

## An Extract From _Menaechmi_ By Plautus, Titus Maccius


I've catered well, and to my mind. I'll set a good breakfast before the breakfasters. But see, I perceive Menaechmus. Woe to my back; the guests are now already walking before the door, before I've returned with the provisions. I'll go and accost him. Save you, Menaechmus.

The Gods bless you, whoever you are.

who I am?

I' faith, not I, indeed.

Where are the other guests?

What guests are you enquiring about?

Your Parasite.

My Parasite? Surely this fellow's deranged.

Didn't I tell you that there were many swindlers here?

What Parasite of mine, young man, are you enquiring about?

Peniculus.

Where is my ?

See, I've got your sponge^[I've got your sponge: Menaechmus takes Cylindrus to mean as though he were really talking about a "_peniculus_," or "sponge," used for the purposes of a napkin. He turns to Messenio, and probably says (in the mutilated passage), "Where is my _peniculus_?" on which the servant, taking it out of the "_vidulus_," or travelling-bag. says, "Here it is, quite safe." ] [Peniculus] all safe in the wallet.

Menaechmus, you've come here too soon for breakfast; I'm but now returning with the provisions.

Answer me this, young man: at what price do pigs sell here^[Do pigs sell here: Pigs without blemish were sacrificed to the Lares, or household Gods, in behalf of those who were afflicted with insanity. Menaechmus Sosicles adopts this as a quiet way of telling Cylindrus that he must be mad.], unblemished ones, for sacrifice?

At a didrachm a-piece.

holding out his hand. Receive, then, a didrachm of me; bid a sacrifice be made for you at my expense; for, by my faith, I really am sure in very truth that you are deranged, who are annoying me, a person that's a stranger, whoever you are.

I am Cylindrus; don't you know my name?

Whether you are Cylindrus or Caliendrus^[Cylindrus or Caliendrus: Probably Cylindrus is so called from the words "_cylindrus_," "a cylinder," in the sense of a "rolling-pin." Sosicles plays upon its resemblance to "_caliendrus_," which perhaps meant a "peruke" or "wig," as the Latin word "_caliendrum_" had that signification.], confound you. I don't know you, and, in fact, I don't want to know you.

Well, your name, however, is Menaechmus, that I do know.

You speak like a sane person when you call me by my name. But where have you known me?

Where have I known you, you who have Erotium, this mistress of mine pointing to the house, for your lady?

By my troth, I have not, nor do I know yourself what person you are.

Not know who I am, who have many a time filled the cups for your own self at our house, when you've been drinking?

Woe to me, that I've got nothing with which to break this fellow's head.

Are you in the habit of filling the cups for me, who, before this day, have never beheld Epidamnus, nor been there?

Do you deny it?

Upon my honor,, I decidedly do deny it.

Don't you live in that house? Pointing to the house of MENAECHMUS of Epidamnus.

May the Gods send to perdition those that live there.

Surely, this fellow's mad, who is thus uttering curses against his own self. Do you hear, Menaechmus?

What do you want?

If you take my advice, that didrachm, which you just now promised to give me--you would order, if you were wise, a pig to be procured with it for yourself. For, i' faith, you really for sure are not in your senses, Menaechmus, who are now uttering curses against your own self.

Alas! By my faith, a very silly fellow, and an annoyance to me.

to MESSENIO. He's in the habit of often joking with me in this fashion. How very droll he is, when his wife isn't present. How say you----?

What do you mean, you rascal?

pointing to the basket. Has this that you see been provided in sufficient quantity for three persons, or am I to provide still more for yourself and the Parasite and the lady?

What ladies--what Parasites are you talking about?

What, you villain, urges you to be an annoyance to him?

Pray what business have you with me? I don't know you; I'm talking to this person, whom I do know.

By my troth, you are not a person in his right senses, that I know for sure.

I'll have these things cooked directly; there shall be no delay. Don't you be going after this anywhere at a distance from the house. Do you want anything?

You to go to utter and extreme perdition.

I' faith, 'twere better for you to go in-doors at once and take your place, while I'm subjecting these things to the strength of the fire^[Strength of the fire: _Vulcani ad violentiam_. Literally "to the violence of Vulcan," the God of fire]. I'll go in-doors now, and tell Erotium that you are standing here, that she may fetch you away hence, rather than you be standing here out of doors. He goes into the house.

Is he gone then? He is gone. By my faith, I find by experience that your words are not untrue.

Do you only be on your guard; for I do believe that some woman in the harlot line is living here, as, in fact. this madman said, who has just gone away from here.

But I wonder how he came to know my name.

I' faith, 'tis far from surprising: courtesans have this custom; they send servant-boys and servant-girls down to the harbour; if any foreign ship comes into port, they enquire of what country it is, and what its name is; after that, at once they set themselves to work, and fasten themselves upon him; if they inveigle him, they send him home a ruined man. Now in this harbour there stands a piratical craft, against which I really think that we must be on our guard.

I' troth, you really counsel aright.

Then, in fine, shall I be sure that I've counselled aright, if you are rightly on your guard.

Be silent for a moment, then; for the door makes a noise. Let's see who's coming out from there.

Meanwhile, I'll lay this down. He puts down the wallet. Do you keep watch upon these things, if you please, you sailors^[You sailors: Some Commentators think that by the words "_navales pedes_" he means "oars," as being the feet, or source of motion to the ship, and that Messenio puts his luggage upon some oars on the ground close by, telling them to be good enough to keep it all safe. It is more probable, however, that he is addressing some of the crew, perhaps the rowers who have carried the luggage from the ship. Others suggest that the luggage-porters, who awaited the arrival of ships with passengers and merchandize, are here referred to. This line, in Cotter's translation, is rendered, "Observe these things now, if you please. Behold the ship!" with this note, "_Navales pedes_, the oars of a ship, put for the ship itself."! De l'Oeuvre ingeniously suggests that "_paedes_" is the correct reading, and the word is the Greek \rendergreek{παιδές} Latinized, and signifying, in the present instance, the "ship-boys" or "servants." ].[^bb28b1b133fe41d8831ab0174d643232]

  
## From Taliata To Drobeta

Intending to travel by road to Drobeta, Virgil left Taliata. It was at least 35 miles. 

As they go up from Taliata, they see the ruined walls. Along the road are graves, and a cenotaph. There a spring wells up, and around about it is a meadow. A caravan from Drobeta passed by. 

While he visited his friend at the countryside near that place, he was pleased to discover _Metamorphoses_, by Ovid 43 B.C.-17 or 18 A.D. Picking it up, he read:

## The Story Of The Countryside Near That Place


"Nor am I to be blamed, if Vulcan's isle  
of Lemnos has become the residence  
of Philoctetes. Greeks, defend yourselves,  
for you agreed to it! Yes, I admit  
I urged him to withdraw from toils of war  
and those of travel and attempt by rest  
to ease his cruel pain. He took my advice  
and lives! The advice was not alone well meant  
(that would have been enough) but it was wise.  
Because our prophets have declared, he must  
lead us, if we may still maintain our hope  
for Troy's destruction—therefore, you must not  
intrust that work to me. Much better, send  
the son of Telamon. His eloquence  
will overcome the hero's rage, most fierce  
from his disease and anger: or else his  
invention of some wile will skilfully  
deliver him to us.—The Simois  
will first flow backward, Ida stand without  
its foliage, and Achaia promise aid  
to Troy itself; ere, lacking aid from me,  
the craft of stupid Ajax will avail.  
"Though, Philoctetes, you should be enraged  
against your friends, against the king and me;  
although you curse and everlastingly  
devote my head to harm; although you wish,  
to ease your anguish, that I may be given  
into your power, that you may shed my blood;  
and though you wait your turn and chance at me;  
still I will undertake the quest and will  
try all my skill to bring you back with me.  
If my good fortune then will favor me,  
I shall obtain your arrows; as I made  
the Trojan seer my captive, as I learned  
the heavenly oracles and fate of Troy,  
and as I brought back through a host of foes  
Minerva's image from the citadel.  
"And is it possible, Ajax may now  
compare himself with me? Truly the Fates  
will hold Troy from our capture, if we leave  
the statue. Where is valiant Ajax now,  
where are the boasts of that tremendous man?  
Why are you trembling, while Ulysses dares  
to go beyond our guards and brave the night?  
In spite of hostile swords, he goes within  
not only the strong walls of Troy but even  
the citadel, lifts up the goddess from  
her shrine, and takes her through the enemy!  
If I had not done this, Telamon's son  
would bear his shield of seven bull hides in vain.  
That night I gained the victory over Troy—  
'Twas then I won our war with Pergama,  
because I made it possible to win.  
"Stop hinting by your look and muttered words  
that Diomed was my partner in the deed.  
The praise he won is his. You, certainly  
fought not alone, when you held up your shield  
to save the allied fleet: a multitude  
was with you, but a single man gave me  
his valued help.  
"And if he did not know  
a fighting man can not gain victory  
so surely as the wise man, that the prize  
is given to something rarer than a brave right hand,  
he would himself be a contender now  
for these illustrious arms. Ajax the less  
would have come forward too, so would the fierce  
Eurypylus, so would Andraemon's son.  
Nor would Idomeneus withhold his claim,  
nor would his countryman Meriones.  
Yes, Menelaus too would seek the prize.  
All these brave men, my equals in the field,  
have yielded to my wisdom.  
"Your right hand  
is valuable in war, your temper stands  
in need of my direction. You have strength  
without intelligence; I look out for  
the future. You are able in the fight;  
I help our king to find the proper time.  
Your body may give service, and my mind  
must point the way: and just as much as he  
who guides the ship must be superior  
to him who rows it; and we all agree  
the general is greater than the soldier; so,  
do I excel you. In the body lives  
an intellect much rarer than a hand,  
by that we measure human excellence.  
"O chieftains, recompense my vigilance!  
For all these years of anxious care, award  
this honor to my many services.  
Our victory is in sight; I have removed  
the opposing fates and, opening wide the way  
to capture Pergama, have captured it.  
Now by our common hopes, by Troy's high walls  
already tottering and about to fall,  
and by the gods that I won from the foe,  
by what remains for wisdom to devise  
or what may call for bold and fearless deeds—  
if you think any hope is left for Troy,  
remember me! Or, if you do not give  
these arms to me, then give them all to her!"  
And he pointed to Minerva's fateful head.  
The assembled body of the chiefs was moved;  
and then, appeared the power of eloquence:  
the fluent man received, amid applause,  
the arms of the brave man. His rival, who  
so often when alone, stood firm against  
great Hector and the sword, and flames and Jove,  
stood not against a single passion, wrath.  
The unconquerable was conquered by his grief.  
He drew his sword, and said:—"This is at least  
my own; or will Ulysses also claim  
this, for himself. I must use this against  
myself—the blade which often has been wet,  
dripping with blood of Phrygians I have slain,.  
Will drip with his own master's:blood,  
lest any man but Ajax vanquish Ajax."  
Saying this, he turned toward the vital spot  
in his own breast, which never had felt a wound,  
the fated sword and plunged it deeply in.  
though many sought to aid, no hand had strength  
to draw that steel—deep driven. The blood itself  
unaided drove it out. The ensanguined earth  
sprouted from her green turf that purple flower  
which grew of old from Hyacinthine blood.  
Its petals now are charged with double freight—  
the warrior's name, Apollo's cry of woe.  
[^65ffdbba66324345a08b55e2a5ee58d8]

  
## To Taliata By Road

From Drobeta to Taliata is a journey of about 35 miles when travelling by road. 

His shoes are covered in dust from the road. By the road is a salt spring. On the road from Drobeta to Taliata there is a village, in which there is a temple and grove. Above the roads are ruins, among which is a cave sacred to Asclepius. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. He left the city early, before the rising of the sun. He passes another milestone. There is a fountain of cold water springing from the rock. Workers are raising the level of the road. 

While he visited his friend at the countryside near that place, he was pleased to discover _Amphitruo_, by Plautus, Titus Maccius. Picking it up, he read:

## An Extract From _Amphitruo_ By Plautus, Titus Maccius


to himself. What other person is there more bold than I, or who more stout of heart, who know the humours of young men^[Of young men: He alludes to the broils of the night, occasioned by the vagaries of wild and dissolute young men--perhaps not much unlike the Mohawks, whose outrageous pranks are mentioned in the Spectator and Swift's Journal to Stella.], and who am walking at this hour of night alone? What shall I do, if now the officers of the watch^[Officers of the watch: Literally, the "Tresviri." As usual, though the Scene is laid in Greece, Roman usages are introduced by Plautus. The officers here mentioned were called "nocturni Tresviri." It was their province to take up all suspicious characters found abroad during the night. They were attended, probably, by lictors, or subordinate officers, who are here referred to as 'homines octo validi," "eight sturdy fellows."] should thrust me into prison. To-morrow shall I be dealt out from there^[Dealt out from there: He compares the gaol, or place of confinement, to a store-closet, and means to say, that as food is brought thence to be dressed, so shall he be brought from the gaol to be dressed, in the way of having his back lashed.], just as though from a store-closet, for a whipping; nor will it be allowed me to plead my cause, nor will there be a bit of aid from my master; nor will there be a person but that they will imagine, all of them, that I am deserving. And so will eight sturdy fellows be thumping on wretched me just like an anvil; in this way, just come from foreign parts, I shall be received with hospitality by the public. The inconsiderateness of my master compels me to this, who has packed me off from the harbour at this time of night whether I would or no. Couldn't he as well have sent me here by daylight? For this reason, is servitude to a man of high station a greater hardship; for this reason is the servant of a wealthy man the more wretched: both night and day, without ceasing, there is enough, and more than enough of work for him; for doing or for saying occasion is ever arising, so that you can't be at rest. The master, abounding in servants^[Abounding in servants: "Dives operis." Literally, "rich in labour," abounding in slaves to labour for him.], and free from labour himself; thinks that whatever he happens to choose, can be done; he thinks that just, and reckons not what the labour is; nor will he ever consider whether he commands a thing that's reasonable or unreasonable. Wherefore, in servitude many hardships do befall us; in pain this burden must be borne and endured.

(to the AUDIENCE). 'Twere with better reason for me to complain of servitude after this fashion; I, who to-day was free, and whom my father is now employing as a slave: this fellow is complaining, who was born a slave.

to himself. Really I am a rascal beyond a doubt; for only this moment it has suggested itself to me, that on my arrival I should give thanks, and address the Gods for their kindnesses vouchsafed. For surely, by my troth, if they were only desirous to give me a return according to my deserts, they would commission some person on my arrival soundly to box my ears, since those kindnesses which they have done me I have held as worthless and of no value.

apart. He does what people are not generally in the habit of doing, in knowing what his deserts are.

to himself. What I never expected, nor any one else of my townsmen, to befall him, that same has come to pass, for us to come home safe and sound. Victorious, the enemy conquered, the troops are returning home, this very mighty war brought to an end, and the enemy slain. A city that has caused many a bitter death for the Theban people, that same has been conquered by the strength and valour of our soldiers, and taken by storm, under the command and conduct of my master Amphitryon in especial. With booty, territory, and glory^[And glory: "Adoreâ." This was literally the allowance or largest of corn which was distributed to troops after a victory; hence it figuratively signifies "honor" or "glory."], too, has he loaded his fellow-citizens, and for Creon, King of Thebes, has he firmly fixed his sway. From the harbour he has sent me before him to his house that I may bear these tidings to his wife, how he has promoted the public good by his guidance, conduct, and command. This now will I consider, in what manner I shall address her, when I've arrived there. If I tell a falsehood. I shall be doing as I am accustomed after my usual wont; for when they were fighting with all their might, then with all my might I ran away. But still I shall pretend as though I was present, and I'll tell her what I heard. But in what manner and with what expressions it is right for me to tell my story, I still wish first to consider here with myself. He assumes an attitude of thought. In these terms will I give this narrative. "In the first place, when we arrived there, when first we made land, Amphitryon immediately made choice of the powerful men among the chieftains. Those he despatched on the embassy, and bade them tell his mind to the Teleboans; that if without constraint and without warfare they should be ready to deliver up what was plundered and the plunderers, and if they should be ready to restore what they had carried off, he would immediately conduct the army homewards, that the Greeks would depart from their territory, and that he would grant peace and quietness to them : but if they should be otherwise disposed, and not concede the things which he demanded, he, in consequence, would attack their city with extreme violence and with his men. When the embassadors had repeated these things, which Amphitryon had enjoined, in order to the Teleboans, being men stout of heart, relying on their valour, and confident in their prowess, they rebuked our embassadors very rudely. They answered that they were able in warfare to protect themselves and theirs, and that at once they must lead the army with all haste out of their territories. When the embassadors brought back this message, straightway Amphitryon drew out all his army from the encampment; on the other side, the Teleboans led forth their legions from the town, furnished with most gorgeous arms. After they had gone forth on either side in full array, the soldiers were marshalled, the ranks were formed. We, after our manner and usage, drew up our legions; the enemy, too, drew up their legions facing us. Then either general went forth into the mid-space beyond the throng of the ranks, and they parleyed together. It was agreed between them, that, which ever side should be conquered in that battle, they should surrender up their city, lands, altars, hearths. and theraselves. After that was done, the trumpets on either side gave the signal; the earth re-echoed, they raised a shout on either side. Each general, both upon this side and on that, offered vows to Jupiter, and then encouraged his troops. Each man according to his ability does that which each one can and has the strength to do; he smites with his falchion; the weapons crash; the welkin bellows with the uproar of the men; of breaths and pantings a cloud is formed; men fall by wounds inflicted by men. At length, as we desired, our troops conquered; the foe fell in numbers; ours, on the other hand, pressed on; firm in our strength, we were victorious. But still not one betook himself to flight, nor yet gave way at his post, but standing there^[Standing there: This seems to be the true meaning of "statim" in this passage.] he waged the combat. Sooner than quit the spot, they parted with their lives; each, as he stood, lay there and kept his rank in death. When my master Amphitryon saw this, at once he ordered the cavalry on the right to charge. The cavalry obeyed directly; from the right wing, with a tremendous shout, with brisk onset they rushed on; and rightfully did they slaughter and trample down the impious forces of the foe."

apart. Not even one word of these has he yet uttered correctly; for I was there in the battle personally, and my father too, when it was fought.

continuing. "The enemy betook themselves to flight. Then was new spirit added to our men, the Teleboans flying, with darts were their bodies filled, and Amphitryon himself, with his own hand, struck off the head of Pterelas their king. This battle was being fought there even from the morning till the evening. This do I the better remember for this reason; because on that day I went without my breakfast. But night at last, by its interposing, cut short this combat. The next day, the chiefs came weeping from the city to us at the camp. With covered hands^[With covered hands: He alludes here to the carrying of the "velamenta," which were branches of olive, surrounded with bandages of wool, and held in the hands of those who sued for mercy or pardon. The wool covered the hand, and was emblematical of peace, the hand being thereby rendered powerless to effect mischief.], they entreated us to pardon their offences; and they all surrendered rendered up themselves. and all things divine and human, their city and their children, into the possession and unto the disposal of the Theban people. Lastly, by reason of his valour, a golden goblet was presented to my master Amphitryon, from which king Pterelas^[King Pterelas: Pterela, or Pterelas, was the son of Hippothoë, the cousin of Amphitryon and Alcmena. He had a daughter named Cymetho, or Cometho, and his fate was said to depend upon the preservation of a certain lock of his hair. Cymetho, smitten with love for Amphitryon, or, according to some accounts, for Cephalus, his associate in the enterprise, cut off the fatal lock, and, like Scylla, betrayed her father, who was afterwards slain by Amphitryon.] had been used to drink." These things I'll thus tell my mistress. I'll now proceed to obey my master's order and to betake me home. He moves.

apart. Heyday! he's about to come this way; I'll go meet him; and I'll not permit this fellow at any time to-day to approach this house. Since I have his form upon myself, I'm resolved to play the fellow off. And indeed, since I have taken upon me his figure and his station, it is right for me likewise to have actions and manners like to his. Therefore it befits me to be artful, crafty, very cunning, and by his own weapon, artfulness, to drive him from the door. But what means this? He is looking up at the sky. I'll watch what scheme he's about.

looking up at the sky. Upon my faith, for sure, if there is aught besides that I believe, or know for certain, I do believe that this night the God of Night^[God of Night: "Nocturnus" is generally supposed here to mean the "God of Night," though some Commentators have fancied that by it the Evening Star is signified.] has gone to sleep drunk; for neither does the Wain move itself in any direction in the sky, nor does the Moon bestir herself anywhere from where she first arose; nor does Orion^[Nor does Orion: "Jugula" means either the three stars composing the girdle of Orion or the Constellation Orion itself. It also was the name of two stars in the Constellation Cancer, or the Crab, which were also called "Aselli," or "the Little Asses." The plural, "Jugulæ," is more generally used. "Septentriones" was a name of the "Ursa Major," or "Greater Bear," also called by us "Charles's Wain." It received its name from "septem," "seven," and "terriones," "oxen that ploughed the earth," from its fancied resemblance to a string of oxen.], or the Evening Star^[The Evening Star: "Vesperugo" is a name of Hesperus, or the Evening Star; while the Constellation of the Pleiades was sometimes known by the name of "Vergiliæ."], or the Pleiades, set. In such a fashion are the stars standing stock-still, and the night is yielding not a jot to the day.

apart. Go on, Night, as you've begun, and pay obedience to my father. In best style^[In best style: "Optumo optume optumam operam." There is a clumsy attempt at wit in this alliteration.], the best of services are you performing for the best of beings; in giving this, you reap a fair return.

to himself. I do not think that I have ever seen a longer night than this, except one of like fashion, which livelong night I was hanging up, having been first whipped. Even that as well, by my troth, does this one by far exceed in its length. I' faith, I really do believe that the Sun's asleep, and is thoroughly drenched. It's a wonder to me if he hasn't indulged himself a little too much at dinner.

apart. Do you really say so, you scoundrel? Do you think that the Gods are like yourself? I' faith, you hang-dog, I'll entertain you for these speeches and misdeeds of yours; only come this way, will you, and you'll find your ruin.

to himself. Where are those wenchers, who unwillingly lie a-bed alone? A rare night this for making the best of what was a bad bargain at first^[Bad bargain at first: This line has been a little modified in the translation.].

apart. My father then, according to this fellow's words, is doing rightly and wisely, who in his amorousness, indulging his passion, is lying in the embraces of Alcmena.

to himself. I'll go tell Alcmena, as my master ordered me. (Advancing, he discovers MERCURY.) But who is this fellow that I see before the house at this time of night? I don't like it.

aside. There is not in existence another such cowardly fellow as this.

aside. Now, when I think of it, this fellow wishes to take my mantle off once more^[Take my mantle off once more: "Detexere." This term was properly applied to the act of taking cloth, when woven, from off the loom. Sosia here uses it in the sense of stripping himself of It.].

aside. The fellow's afraid; I'll have some sport with him.

aside. I'm quite undone, my teeth are chattering. For sure, on my arrival, he is about to receive me with the hospitality of his fist. He's a merciful person, I suppose; now, because my master has obliged me to keep awake, with his fists just now he'll be making me go to sleep. I'm most confoundedly undone. Troth now, prithee, look, how big and how strong he is.

aside. I'll talk at him aloud, he shall hear what I say. Therefore indeed, in a still greater degree, shall he conceive fears within himself. In a loud voice, holding up his fists. Come, fists, it's a long time now since you found provision for my stomach; it seems to have taken place quite a long time ago, when yesterday you laid four men asleep, stript naked.

aside. I'm dreadfully afraid lest I should be changing my name here, and become a Quintus^[A Quintus: This is a poor attempt at wit. Mercury tells his fists that they thrashed four men into a lethargy yesterday; on which Sosia, in his apprehension, says that in that case he shall have to change his own name to "Quintus;" which signified "the fifth," and was also in use as a name among the Romans; implying thereby that he shall be the fifth to be so mauled.] instead of a Sosia. He declares that he has laid four men asleep; I fear lest I should be adding to that number.

throwing about his arms. Well, now then for it. This is the way I intend.

aside. He is girded tight; for sure, he's getting himself ready.

He shan't get off without getting a thrashing.

aside. What person, I wonder? MERC. Beyond a doubt, whatever person comes this way, he shall eat my fists.

aside. Get out with you, I don't wish to eat at this time of night; I've lately dined. Therefore do you, if you are wise, bestow your dinner on those who are hungry.

The weight of this fist is no poor one.

aside. I'm done for; he is poising his fists.

What if I were to touch him, stroking him down^[Stroking him down: He probably alludes to the soporific power of his."caduceus," or "wand."], so that he may go to sleep?

aside. You would be proving my salvation; for I've been watching most confoundedly these three nights running^[Three nights running: He alludes to the length of the night, which was prolonged by Jupiter for the purpose of his intrigue. According to other writers, it was on the occasion when Hercules was begotten, seven months before this period, that three nights were made into one.].

My hand refuses to learn to strike his cheek; it cannot do a disgraceful action. Hand of mine, of a changed form must he become whom you smite with this fist.

aside. This fellow will be furbishing me up, and be moulding my face anew.

to his fist. The man that you hit full, his face must surely be boned.

aside. It's a wonder if this fellow isn't thinking of boning me just like a lamprey. Away with a fellow that bones people! If he sees me, I'm a dead man.

Some fellow is stinking to his destruction.

aside. Woe to me! Is it I that stink?

And he cannot be very far off; but he has been a long way off from here.

aside. This person's a wizard^[This person's a wizard: We must remember that this is supposed to take place in the dark; and Sosia says that the man must surely be a wizard to guess that another person is so near him, and that he has been abroad till just now.].

My fists are longing.

aside. If you are going to exercise them upon me, I beg that you'll first cool them down against the wall.

A voice has come flying to my ears.

aside. Unlucky fellow, for sure, was I, who didn't clip its wings. I've got a voice with wings, it seems.

This fellow is demanding of me for himself a heavy punishment for his beast's back^[His beast's back: "Jumento suo." Literally, "on his beast of burden."].

aside. As for me, I've got no beast's back.

He must be well loaded with my fists.

aside. I' faith, I'm fatigued, coming from board ship, when I was brought hither; even now I'm sea-sick. Without a burden, I can hardly creep along, so don't think that with a load I can go.

Why, surely, somebody^[Somebody: "Nescio quis." Literally, "I know not who." For the sake of the joke, he pretends to think that this is the name of some one mentioned by Mercury; and says that as he is not that person, he is all right.] is speaking here.

aside. I'm all right, he doesn't see me; he thinks it's "Somebody" speaking: Sosia is certainly my name.

But here, from the right-hand side, the voice, as it seems, strikes upon my ear.

aside. I'm afraid that I shall be getting a thrashing here this day, in place of my voice, that's striking him. Moves.

Here he is--he's coming towards me, most opportunely.

aside. I'm terrified--I'm numbed all over. Upon my faith, I don't know where in the world I now am, if any one should ask me; and to my misfortune, I cannot move myself for fright. It's all up with me; the orders of his master and Sosia are lost together. But I'm determined boldly to address this fellow to his face, so that I may be able to appear valiant to him; that he may keep his hands off me Advances towards the door.

accosting him. Where are you going, you that are carrying Vulcan enclosed in your horn^[Vulcan enclosed in your horn: "Volcanum in cornu." Literally, "Vulcan in your horn;" alluding to the horn lantern which Sosia is carrying.]?

Why do you make that enquiry, you who are boning men's heads with your fists?

Are you slave or free man?

Just as it suits my inclination.

Do you really say so?

I really do say so.

Whip-scoundrel^[Whip-scoundrel: "Verbero." This word, as a substantive, properly means a bad slave, who had been whipped--"a rascal" or "scoundrel." As a verb, it means "I beat." Sosia chooses, for the sake of the quibble, to take it in the latter sense, and tells Mercury that he lies; meaning to say that he (Mercury) is not beating him (Sosia).]!

Now you are telling a lie.

But I'll soon make you own that I'm telling the truth.

What necessity is there for it?

Can I know whence you have set out, whose you are, or why you are come?

pointing. This way I'm going, and I'm the servant of my master. Are you any the wiser now?

I'll this day make you be holding that foul tongue of yours.

You can't; it is kept pure^[It is kept pure: , It is generally supposed that in these words indelicate allusion is intended; but it is not so universally agreed on what nature is.] and becomingly.

Do you persist in chattering? What business now have you at this house? Points to the house.

Aye, and what business have you?

King Creon always sets a watch every night.

He does right; because we were abroad, he has been protecting our house. But however, do go in now, and say that some of the family servants have arrived.

How far you are one of the family servants I don't know. But unless you are off from here this instant, family servant as you are, I'll make you to be received in no familiar style.

Here, I say, I live, and of these people I am the servant.

But do you understand how it is? Unless you are off, I'll make you to be exalted^[To be exalted: He probably means by this, that he will beat him to such a degree that he will be obliged to be carried off, either dead or unable to move a limb--"elevated" on the shoulders of other men.] this day.

In what way, pray?

You shall be carried off, you shan't walk away, if I take up a stick.

But I declare that I am one of the domestics of this family.

Consider, will you, how soon you want a drubbing, unless you are off from here this instant.

Do you want, as I arrive from foreign parts, to drive me from my home?

Is this your home?

It is so, I say.

Who is your master, then?

Amphitryon, who is now the general of the Theban forces, to whom Alcmena is married.

How say you? What's your name?

The Thebans call me Sosia, the son of my father Davus.

Assuredly, at your peril have you come here this day, with your trumped-up lies, your patched-up knaveries, you essence of effrontery.

Why no, it's rather with garments patched-up that I'm arrived here, not with knaveries.

Why, you are lying again; you come with your feet, surely, and not with your garments.

Yes, certainly.

Then certainly take that for your lie. He strikes him.

By my troth, I certainly don't wish for it of course.

But by my faith, you certainly shall have it of course, whether you wish or not: for, in fact, this is certainly my determination, and it is not at your own option. He strikes him.

Mercy, I entreat of you.

Do you dare to say that you are Sosia, when I myself am he? Strikes him.

crying at the top of his voice. I'm being murdered.

Why, you are crying out for a trifle as yet, compared with what it will be. Whose are you now?

Your own; for with your fists you have laid hands on me^[Laid hands on me: "Usufecisti." "Usufacere" was a term used in law, to signify the taking possession of a thing by the laying of hands thereon. this, Sosia means to say, Mercury has most effectually done.]. Help, help, citizens of Thebes. MERCURY striking him.

What, still bawling, you scoundrel? Speak--what have you come for?

For there to be somebody for you to belabour with your fists.

Whose are you?

Amphitryon's Sosia, I tell you.

For this reason then you shall be beaten the more, because you prate thus idly; I am Sosia, not you.

aside. I wish the Gods would have it so, that you were he in preference, and that I were thrashing you.

What, muttering still? Strikes him.

I'll hold my tongue then.

Who is your master?

Whoever you like.

How then? What's your name now?

Nothing but what you shall command.

You said that you were Amphitryon's Sosia.

I made a mistake; but this I meant to say, that I was Amphitryon's associate^[Associate: This poor pun is founded on the similarity of sound between Sosia and "socius," a "companion" or "associate."].

Why, I was sure that we had no servant called Sosia except myself. Your senses are forsaking you.

I wish that those fists of yours had done so.

I am that Sosia, whom you were just now telling me that you are.

I pray that I may be allowed to discourse with you in quietness, so as not to be beaten.

Well then, let there be a truce for a short time, if you want to say anything.

I'll not speak unless peace is concluded, since you are the stronger with your fists.

If you wish to say anything, speak; I'll not hurt you.

Am I to trust in your word?

Yes, in my word.

What, if you deceive me?

Why, then may Mercury be angry with Sosia^[Angry with Sosia: There is something comical in the absurdity of this oath. Mercury, personating Sosia, says that if he breaks it, the result must be that Mercury (i. e., himself): will be angry with Sosia, the person in whose favour he is pretending to take the oath.].

Then give attention: now I'm at liberty to say in freedom anything I please. I am Sosia, servant of Amphitryon.

What, again? Offering to strike him.

I have concluded the peace, ratified the treaty--I speak the truth.

Take that, then. Hie strikes him.

As you please, and what you please, pray do, since you are the stronger with your fists. But whatever you shall do, still, upon my faith, I really shall not be silent about that.

So long as you live, you shall never make me to be any other than Sosia at this moment.

I' faith, you certainly shall never make me to be any other person than my own self; and besides myself we have no other servant of the name of Sosia--myself, who went hence on the expedition together with Amphitryon.

This fellow is not in his senses.

The malady that you impute to me, you have that same yourself. How, the plague, am I not Sosia, the servant of Amphitryon? Has not our ship, which brought me, arrived here this night from the Persian port^[The Persian port: Plautus is here guilty of an anachronism; for the "Portus Persicus," which was on the coast of Eubœa, was so called from the Persian fleet lying there on the occasion of the expedition to Greece, many ages after the time of Amphitryon.]? Has not my master sent me here? Am I not now standing before our house? Have I not a lantern in my hand? Am I not talking? Am I not wide awake? Has not this fellow been thumping me with his fists? By my troth^[By my troth: "Hercle." Literally, "by Hercules." Hypercritical Commentators have observed, that Plautus is guilty in this Play of a grammatical anachronism, in putting the expletive, "Hercle," in the mouths of persous at a time when Hercules is supposed to be yet unborn. They might with as much justice accuse him of anachronism in putting the Roman language into the mouths of persons at a time when that language did not as yet exist. He merely professes to embody the sentiments of persons in bygone days in such language as may render them the most easily intelligible to a Roman audience.], he has been doing so; for even now, to my pain, my cheeks are tingling. Why, then, do I hesitate? Or why don't I go in-doors into our house? He makes towards the door.

stepping between. How--your house?

Indeed it really is so.

Why, all that you have been saying just now, you have trumped up; I surely am Amphitryon's Sosia. For in the night this ship of ours weighed anchor from the Persian port, and where king Pterelas reigned, the city we took by storm, and the legions of the Teleboans in fighting we took by arms, and Amphitryon himself cut off the head of king Pterelas in battle.

aside. I do not trust my own self, when I hear him affirm these things; certainly, he really does relate exactly the things that were done there. Aloud. But how say you? What spoil from the Teleboans was made a present to Amphitryon?

A golden goblet, from which king Pterelas used to drink.

aside. He has said the truth. Where now is this goblet?

'Tis in a casket, sealed with the seal of Amphitryon.

Tell me, what is the seal?

The Sun rising with his chariot. Why are you on the catch for me, you villain?

aside. He has overpowered me with his proofs. I must look out for another name. I don't know from whence he witnessed these things. I'll now entrap him finely; for what I did alone by myself, and when not another person was present in the tent, that, he certainly will never be able this day to tell me. Aloud. If you are Sosia, when the armies were fighting most vigorously, what were you doing in the tent? If you tell me that, I'm vanquished.

There was a cask of wine; from it I filled an earthen pot^[An earthen pot: "Hirneam." "Hirnea" was an earthen vessel for holding wine. It was said to receive its name from the Greek word \rendergreek{ὄρνις} "a bird," because it originally bore the figure of a bird.].

aside. He has got upon the track.

That I drew full of pure wine, just as it was born from the mother grape.

aside. It's a wonder if this fellow wasn't lying hid inside of that earthen pot. It is the fact, that there I did drink an earthen pot full of wine.

Well--do I now convince you by my proofs that you are not Sosia?

Do you deny that I am?

Why should I not deny it, who am he myself?

By Jupiter I swear that I am he, and that I do not say false.

But by Mercury, I swear that Jupiter does not believe you; for I am sure that he will rather credit me without an oath than you with an oath.

Who am I, at all events, if I am not Sosia? I ask you that.

When I choose not to be Sosia, then do you be Sosia; now, since I am he, you'll get a thrashing, if you are not off hence, you fellow without a name.

aside. Upon my faith, for sure, when I examine him and recollect my own figure, just in such manner as I am (I've often looked in a glass^[Looked in a glass: He seems to speak of looking in a mirror as something uncommon for a slave to do. Probably the expense of them did not allow of their being used by slaves. The "specula," or "looking-glasses," of the ancients, were usually made of metal, either a composition of tin and copper or of silver; but in later times, alloy was mixed with the silver. Pliny mentions the obsidian stone, or, as it is now called, Icelandic agate, as being used for this purpose. He also says that mirrors were made in the glass-houses of Sidon, which consisted of glass plates with leaves of metal at the back. These were probably of an inferior character. Those of copper and tin were made chiefly at Brundisium. The white metal formed from this mixture soon becoming dim, a sponge, with powdered pumice-stone, was usually fastened to the mirrors made of that composition. They were generally small, of round or oval shape, and having a handle. The female slaves usually held them while their mistresses were performing the duties of the toilet. Sometimes they were fastened to the walls, and they were occasionally of the length of a person's body, like the cheval glasses of our day]): , he is exactly like me. He has the broad-brimmed hat and clothing just the same; he is as like me as I am myself. His leg, foot, stature, shorn head, eyes, nose, even his lips, cheeks, chin, beard, neck--the whole of him. What need is there of words? If his back is marked with scars, than this likeness there is nothing more like. But when I reflect, really, I surely am the same person that I always was. My master I know, I know our I house; I am quite in my wits and senses. I'm not going to I obey this fellow in what he says; I'll knock at the door. Goes towards the door.

Whither are you betaking yourself?

Home.

If now you were to ascend the chariot of Jove and fly away from here, then you could hardly be able to escape destruction.

Mayn't I be allowed to deliver the message to my mistress that my master ordered me to give?

If you want to deliver any message to your own mistress; this mistress of mine I shall not allow you to approach. But if you provoke me, you'll be just now taking hence your loins broken.

In preference, I'll be off. Aside. Immortal Gods, I do beseech your mercy. Where did I lose myself? Where have I been transformed? Where have I parted with my figure? Or have I left myself behind there, if perchance I have forgotten it? For really this person has possession of all my figure, such as it formerly was. While living, that is done for me, which no one will ever do for me when dead^[When dead: It is generally thought that he is punning here upon the word "imago," and alludes to the practice of carrying the "imagines," or "waxen images" of their ancestors, in the funeral processions of the Patricians--an honor, he says, that will never befall him when he is dead. Douza, however, thinks that he is playing upon the expression "ludos facere," which has the double meaning of "to impose upon" a person, or "to give a spectacle" of gladiators after the death of a person of Patrician rank; and that he means to say that the act "_ludos faciendi_" is being applied to him (in the first sense): while alive, a thing that (in the second sense) will never befall him when dead.]. I'll go to the harbour, and I'll tell my master these things as they have happened--unless even he as well shall not know me, which may Jupiter grant, so that this day, bald, with shaven crown, I may assume the cap of freedom^[Cap of freedom: When a slave was made free, after his manumission his head was shaved, and a cap put upon it in the Temple of Feronia, the Goddess of Freedmen.]. (Exit.)[^a48ba4451a35410eb46b414bd00dfe2b]

  
## The Journey To Dierna

From Taliata to Dierna is a journey of about 22 miles when travelling on a military boat floating downstream. 

The sun beats down. No backward glances for the city left behind. The journey is more tiring than you might expect. 

While he was visiting the countryside near that place, he made a point of copying down what Plautus, Titus Maccius had written.

## A Story About The Countryside Near That Place By Plautus, Titus Maccius


Come out of the Temple, you most sacrilegious of men, as many as have ever been born. Do you go calling to the WOMEN and sit by the altar. Not seeing them near the door. But where are they?

Look round here.

looking round. Very good; I wanted that^[I wanted that: He means that the women have done as he wished them to do, in flying to the altar for refuge.]. Now bid him come this way. To LABRAX. Are you attempting here among us to commit a violation of the laws against the Deities? To the SERVANTS, who obey with alacrity. Punch his face with your fists.

I'm suffering these indignities at your own cost.

Why, the insolent fellow's threatening even.

I've been robbed of my rights; you are robbing me of my female slaves against my will.

Do you then find some wealthy man of the Senate of Cyrene as judge, whether these women ought to be yours, or whether they oughtn't to be free, or whether it isn't right that you should be clapped into prison, and there spend your life, until you have worn the whole gaol out with your feet.

I wasn't prepared to prophesy for this day that I should be talking with a hang-gallows^[A hang-gallows: "Furcifero." He sneeringly alludes to Trachalio's position as a slave, and his liability to have the punishment of the "furca" inflicted on him.] like yourself. Turning to DÆMONES. You do I summon to judgment.

pointing to TRACHALIO. In the first place, try it with him who knows you.

to DÆMONES. My suit is with yourself.

But it must be with myself. Pointing to the WOMEN. Are these your female slaves?

They are.

Just come then, touch either of them with your little finger only.

What if I do touch them?

That very instant, upon my faith, I'll make a hand-ball^[A hand-ball: -2. These lines are thus rendered in one version: "Instantly I will make you a prize-fighting pair of bellows, and while you are drawing breath, will belabour you with my fists." The allusion, however, is clearly to a ball blown up like our footballs, and struck with the clenched fist, the merit of the game being not to let it come to the ground.] of you, and while you're in the air I'll belabour you with my fists, you most perjured villain.

Am I not to be allowed to take away my female slaves from the altar of Venus?

You may not; such is the law with us.

I've no concern with your laws; for my part, I shall at once carry them both away from here^[Away from here: "Foras." Probably in allusion to the court before the Temple]. If you are in love with them, old gentleman holding out his hand, you must down here with the ready cash.

But these women have proved pleasing to Venus.

She may have them, if she pays the money.

A Goddess, pay you money? Now then, that you may understand my determination, only do you commence in mere joke to offer them the very slightest violence; I'll send you away from here with such a dressing, that you won't know your own self. You, therefore turning to his SERVANTS, when I give you the signal, if you don't beat his eyes out of his head, I'll trim you round about with rods just like beds of myrtle^[Beds of myrtle: "Myrteta." This may allude to bundles of myrtle (which was sacred to Venus), bound with rushes and hung about the Temple, or else to beds of myrtle in front of the Temple, with small fences round them, made of rushes.] with bulrushes.

You are treating me with violence.

What, do you even upbraid us with violence, you flagrant specimen of flagitiousness?

You, you thrice-dotted villain^[Thrice-dotted villain: "Trifurcifer." Literally, "one punished with the 'furca' three times," meaning a "thief;" or "villain three times over." See the Aulularia, l. 281, and the Note (where read "punished with the 'furca'")], do you dare to speak abusively to me?

I am a thrice-dotted villain; I confess it; you are a strictly honorable man; ought these women a bit the less to be free?

What--free?

Aye, and your mistresses, too, i' faith, and from genuine Greece^[Genuine Greece: Perhaps in contradistinction to Sicily, which was only colonized by Greeks.]; for one of them was born at Athens of free-born parents.

What is it I hear from you?

That she pointing to PALÆSTRA was born at Athens, a free-born woman.

to TRACHALIO. Prithee is she a countrywoman of mine?

Are you not a Cyrenian?

No; born at Athens in Attica, bred and educated there.

Prithee, aged sir, do protect your countrywomen.

aside. O daughter, when I look on her, separated from me you remind me of my miseries: aloud she who was lost by me when three years old; now, if she is living, she's just about as tall, I'm sure, as she. Pointing to PALÆSTRA.

I paid the money down for these two, to their owners, of whatever country they were. What matters it to me whether they were born at Athens or at Thebes, so long as they are rightfully in servitude as my slaves?

it so, you impudent fellow? What, are you, a cat prowling after maidens, to be keeping children here kidnapped from their parents and destroying them in your disgraceful calling? But as for this other one, I really don't know what her country is; I only know that she's more deserving than yourself, you most abominable rascal.

Are these women your property?

Come to the trial, then, which of the two according to his back is the more truthful; if you don't bear more compliments^[Compliments: "Offerumenta," according to Festus, signified an offering to the Gods; and as these were fixed to the walls of the Temples, Trachalio calls the lashes of the scourge or rod, when applied to the back of the delinquent slave, by the same term.] upon your back than any ship of war^[Ship of war: "Longa navis." Literally, "a long ship." Ships of war were thus called by the Greeks.] has nails, then I'm the greatest of liars. Afterwards, do you examine mine, when I've examined yours; if it shall not prove to be so untouched, that any leather flask maker^[Leather flask maker: "Ampullarius." "A maker of ampullæ,' or leather bottles. They were of a big-bellied form, with a narrow neck.] will say that it is a hide most capital and most sound for the purposes of his business, what reason is there why I shouldn't mangle you with stripes, even till you have your belly full? Why do you stare at them? If you touch them I'll tear your eyes out.

Yet notwithstanding, although you forbid me to do so, I'll at once carry them off both together with me.

What will you do?

I'll bring Vulcan; he is an enemy to Venus^[An enemy to Venus: In so saying, he alludes to the intrigue of Venus with Mars, which was discovered by the device of Vulcan, her injured husband. For the story, see the Metamorphoses of Ovid, B. 4, l. 73, and the Art of Love, B. 2, l. 562.]. Goes towards DÆMONES' cottage.

Whither is he going?

calling at the door. Hallo! Is there anybody here? Hallo! I say.

If you touch the door, that very instant, upon my faith, you shall get a harvest upon your face with fists for your pitchforks^[Fists for your pitchforks: "Mergis pugneis." Echard, in his translation, explains this: "As they lift up their pitchforks to heap corn, so will I lift up my fists, and heap a whole harvest of cuffs on your face." "Merga' means 'a pitchfork;" and, according to Festus, it was so called from its resemblance when dipped into the hay to the action of the "mergus," or "didapper when dipping into the sea,].

We keep no fire, we live upon dried figs.

I'll find the fire, if only I have the opportunity of kindling it upon your head.

Faith, I'll go somewhere to look for some fire.

What, when you've found it?

I'll be making a great fire here.

What, to be burning^[To be burning: Festus tells us that "humanum" was a "mortuary sacrifice," or "offering to the dead." In his question, therefore, Dæmones inplies a wish to know whether Labrax is about to put an end to himself. It was allowable to drive away those who fled to the altar by the agency of fire.] a mortuary sacrifice for yourself?

No, but I'll burn both of these alive here upon the altar.

I'd like that. For, by my troth, I'll forthwith seize you by the head and throw you into the fire, and, half-roasted, I'll throw you out as food for the great birds. Aside. When I come to a consideration of it with myself, this is that ape, that wanted to take away those swallows from the nest against my will, as I was dreaming in my sleep.

Aged sir, do you know what I request of you? That you will protect these females and defend them from violence, until I fetch my master.

Go look for your master, and fetch him here.

But don't let him----

At his own extreme peril, if he touches them, or if he attempts to do so.

Take care.

Due care is taken; do you be off.

And watch him too, that he doesn't go away anywhere. For we have promised either to give the executioner a great talent, or else to produce this fellow this very day.

Do you only be off. I'll not let him get away, while you are absent.

I'll be back here soon. (Exit TRACHALIO.)[^9e7d7793261b4229884c20b1129688d3]

  
## After Dierna

Leaving Dierna, Virgil set out for Taliata on a boat heading upstream, at least 22 miles. 

A breeze from an unexpected quarter cools the air. 

All of this brought to his mind what Lucan, 39-65 had said about the countryside near that place:

## On The Subject Of The Countryside Near That Place


  
Now from the Casian rock looked forth the Sun  
Flooding the land of Egypt with a day  
Warm from its earliest dawn, when from the walls  
Not wandering in disorder are they seen,  
But drawn in close array, as though to meet  
A foe opposing; ready to receive  
Or give the battle. Caesar, in the town  
Placing no trust, within the palace courts  
Lay in ignoble hiding place, the gates  
Close barred : nor all the kingly rooms possessed,  
But in the narrowest portion of the space  
He drew his band together. There in arms  
They stood, with dread and fury in their souls.  
He feared attack, indignant at his fear.  
Thus will a noble beast in little cage  
Imprisoned, fume, and break upon the bars  
His teeth in frenzied wrath; nor more would rage  
The flames of Vulcan in Sicilian depths  
Should Etna's top be closed. He who but now  
By Haemus' mount against Pompeius chief,  
Italia's leaders and the Senate line,  
His cause forbidding hope, looked at the fates  
He knew were hostile, with unfaltering gaze,  
Now fears before the crime of hireling slaves,  
And in mid palace trembles at the blow:  
He whom nor Scythian nor Alaun had dared  
To violate, nor the Moor who aims the dart  
Upon his victim slain, to prove his skill.  
The Roman world but now did not suffice  
To hold him, nor the realms from furthest Ind  
To Tyrian Gades. Now, as puny boy,  
Or woman, trembling when a town is sacked,  
Within the narrow corners of a house  
He seeks for safety; on the portals closed  
His hope of life: and with uncertain gait  
He treads the halls; yet not without the King;  
In purpose, Ptolemaeus, that thy life  
For his shall give atonement; and to hurl  
Thy severed head among the servant throng  
Should darts and torches fail. So story tells  
The Colchian princess^[Medea, who fled from Colchis with her brother, Absyrtus. Pursued by her father AEetes, she killed her brother and strewed the parts of his body into the sea. The king paused to collect them.] with sword in hand,  
And with her brother's neck bared to the blow,  
Waited her sire, avenger of his realm  
Despoiled, and of her flight. In the imminent risk  
Caesar, in hopes of peace, an envoy sent  
To the fierce vassals, from their absent lord  
Bearing a message, thus : ' At whose command  
Wage ye the war?' But not the laws which bind  
All nations upon earth, nor sacred rights,  
Availed to save or messenger of peace,  
Or King's ambassador; or thee from crime  
Such as befitted thee, thou land of Nile  
Fruitful in monstrous deeds: not Juba's realm,  
Vast though it be, nor Pontus, nor the land  
Thessalian, nor the arms of Pharnaces,  
Nor yet the tracts which chill Iberus girds,  
Nor Libyan coasts such wickedness have dared,  
As thou, and all thy minions. Closer now  
War hemmed them in, and weapons in the courts,  
Shaking the innermost recesses, fell.  
Yet did no ram, fatal with single stroke,  
Assail the portal, nor machine of war;  
Nor flame they called in aid; but blind of plan  
They wander purposeless, in separate bands  
Around the circuit, nor at any spot  
With strength combined attempt to breach the wall.  
The fates forbad, and Fortune from their hands  
Held fast the palace as a battlement.  
Nor failed they to attack from ships of war  
The regal dwelling, where its frontage bold  
Made stand apart the waters of the deep :  
There, too, was Caesar's all-protecting arm;  
For these at point of sword, and those with fire  
He forces back, and though besieged he dares  
To storm th' assailants: and as lay the ships  
Joined rank to rank, bids drop upon their sides  
Lamps drenched with reeking tar. Nor slow the fire  
To seize the hempen cables and the decks  
Oozing with melting pitch; the oarsman's bench  
All in one moment, and the topmost yards  
Burst into flame: half merged the vessels lay  
While swam the foemen, all in arms, the wave;  
Nor fell the blaze upon the ships alone,  
But seized with writhing tongues the neighbouring homes,^[It was in this conflagration that a large part of the library of the Ptolemies was destroyed. 400,000 volumes are stated to have perished.]  
And fanned to fury by the Southern breeze  
Tempestuous, it leaped from roof to roof;  
Not otherwise than on its heavenly track,  
Unfed by matter, glides the ball of light,  
By air alone aflame.  
This pest recalled  
Some of the forces to the city's aid  
From the besieged halls. Nor Caesar gave  
To sleep its season; swifter than all else  
To seize the crucial moment of the war.  
Quick in the darkest watches of the night  
He leaped upon his ships, and Pharos^[The island of Pharos, which lay over against the port of Alexandria, had been connected with the mainland in the middle by a narrow causeway. On it stood the lighthouse. (See Book IX., 1192.) Proteus, the old man of the sea, kept here his flock of seals, according to the Homeric story. ('Odyssey,' Book IV., 400.)] seized,  
Gate of the main; an island in the days  
Of Proteus seer, now bordering the walls  
Of Alexander's city. Thus he gained  
A double vantage, for his foes were pent  
Within the narrow entrance, which for him  
And for his aids gave access to the sea.  
Nor longer was Pothinus' doom delayed,  
Yet not with cross or flame, nor with the wrath  
His crime demanded; nor by savage beasts  
Torn, did he suffer; but by Magnus' death,  
Alas the shame! he fell; his head by sword  
Hacked from his shoulders. Next by frauds prepared  
By Ganymede her base attendant, fled  
Arsinoe^[Younger sister of Cleopatra.] from the Court to Caesar's foes;  
There in the absence of the King she ruled  
As of Lagean blood: there at her hands,  
The savage minion of the tyrant boy,  
Achillas, fell by just avenging sword.  
Thus did another victim to thy shade  
Atone, Pompeius; but the gods forbid  
That this be all thy vengeance! Not the King  
Nor all the stock of Lagos for thy death  
Would make fit sacrifice! So Fortune deemed;  
And not till patriot swords shall drink the blood  
Of Caesar, Magnus, shalt thou be appeased.  
Still, though was slain the author of the strife,  
Sank not their rage: with Ganymede for chief  
Again they rush to arms; in deeds of fight  
Again they conquer. So might that one day  
Have witnessed Caesar's fate; so might its fame  
Have lived through ages.  
As the Roman Chief,  
Crushed on the narrow surface of the mole,  
Prepared to throw his troops upon the ships,  
Sudden upon him the surrounding foes  
With all their terrors came. In dense array  
Their navy lined the shores, while on the rear  
The footmen ceaseless charged. No hope was left,  
For flight was not, nor could the brave man's arm  
Achieve or safety or a glorious death.  
Not now were needed for great Caesar's fall,  
Caught in the toils of nature, routed host  
Or mighty heaps of slain: his only doubt  
To fear or hope for death: while on his brain  
Brave Scaeva's image flashed, now vainly sought,  
Who on the wall by Epidamnus' fields  
Earned fame immortal, and with single arm  
Drove back Pompeius as he trod the breach.  
[^4cc58b5abac643a0b96e4a6076670620]

\newpage

# Taliata To Dyrrhachium
  
## To Bononia (Moesia) By Road

Intending to travel by road to Bononia (Moesia), Virgil left Taliata. It was a distance of about 58 miles. 

He had set out from Taliata amidst a throng travelling the same way. On the road from Taliata to Bononia (Moesia) there is a village, in which there is a temple and grove. He passes another milestone. His shoes are covered in dust from the road. Now the road is quieter. Above the roads are ruins, among which is a cave sacred to Asclepius. 

The library at the countryside near that place happened to have a copy of _Description of Greece_, where Virgil encountered it.

## What Pausanias, Fl. Ca. 150-175 Once Said About The Countryside Near That Place


Worsted on this occasion Pyrrhus put back with the remainder of his vessels to Tarentum. Here he met with a serious reverse, and his retirement, for he knew that the Romans would not let him depart without striking a blow, he contrived in the following manner. On his return from Sicily and his defeat, he first sent various dispatches to Asia and to Antigonus, asking some of the kings for troops, some for money, and Antigonus for both. When the envoys returned and their dispatches were delivered, he summoned those in authority, whether Epeirot or Tarentine, and without reading any of the dispatches declared that reinforcements would come. A report spread quickly even to the Romans that Macedonians and Asiatic tribes also were crossing to the aid of Pyrrhus. The Romans, on hearing this, made no move, but Pyrrhus on the approach of that very night crossed to the headlands of the mountains called Ceraunian.

After the defeat in Italy Pyrrhus gave his forces a rest and then declared war on Antigonus, his chief ground of complaint being the failure to send reinforcements to Italy. Overpowering the native troops of Antigonus an his Gallic mercenaries he pursued them to the coast cities, and himself reduced upper Macedonia and the Thessalians. The extent of the fighting and the decisive character of the victory of Pyrrhus are shown best by the Celtic armour dedicated in the sanctuary of Itonian Athena between Pherae and Larisa, with this inscription on them:—Pyrrhus the Molossian hung these shields

taken from the bold Gauls as a gift to ItonianAthena, when he had destroyed all the hostof Antigonus. 'Tis no great marvel. TheAeacidae are warriors now, even as they wereof old.These shields then are here, but the bucklers of the Macedonians themselves he dedicated to Dodonian Zeus. They too have an inscription:—These once ravaged golden Asia, and broughtslavery upon the Greeks. Now ownerlessthey lie by the pillars of the temple of Zeus,spoils of boastful Macedonia.Pyrrhus came very near to reducing Macedonia entirely, but,

being usually readier to do what came first to hand, he was prevented by Cleonymus. This Cleonymus, who persuaded Pyrrhus to abandon his Macedonian adventure and to go to the Peloponnesus, was a Lacedaemonian who led an hostile army into the Lacedaemonian territory for a reason which I will relate after giving the descent of Cleonymus. Pausanias, who was in command of the Greeks at Plataea^[479 B.C.], was the father of Pleistoanax, he of Pausanias, and he of Cleombrotus, who was killed at Leuctra fighting against Epaminondas and the Thebans. Cleombrotus was the father of Agesipolis and Cleomenes, and, Agesipolis dying without issue, Cleomenes ascended the throne.

Cleomenes had two sons, the elder being Acrotatus and the younger Cleonymus. Now Acrotatus died first; and when afterwards Cleomenes died, a claim to the throne was put forward by Areus son of Acrotatus, and Cleonymus took steps to induce Pyrrhus to enter the country. Before the battle of Leuctra^[371 B.C.] the Lacedaemonians had suffered no disaster, so that they even refused to admit that they had yet been worsted in a land battle. For Leonidas, they said, had won the victory^[480 B.C.], but his followers were insufficient for the entire destruction of the Persians; the achievement of Demosthenes and the Athenians on the island of Sphacteria^[425 B.C.] was no victory, but only a trick in war.

Their first reverse took place in Boeotia, and they afterwards suffered a severe defeat at the hands of Antipater and the Macedonians^[330 B.C.]. Thirdly the war with Demetrius^[295 B.C.] came as an unexpected misfortune to their land. Invaded by Pyrrhus and seeing a hostile army for the fourth time, they arrayed themselves to meet it along with the Argives and Messenians who had come as their allies. Pyrrhus won the day, and came near to capturing Sparta without further fighting, but desisted for a while after ravaging the land and carrying off plunder.^[272 B.C.] The citizens prepared for a siege, and Sparta even before this in the war with Demetrius had been fortified with deep trenches and strong stakes, and at the most vulnerable points with buildings as well.

Just about this time, while the Laconian war was dragging on, Antigonus, having recovered the Macedonian cities, hastened to the Peloponnesus being well aware that if Pyrrhus were to reduce Lacedaemon and the greater part of the Peloponnesus, he would not return to Epeirus but to Macedonia to make war there again. When Antigonus was about to lead his army from Argos into Laconia, Pyrrhus himself reached Argos. Victorious once more he dashed into the city along with the fugitives, and his formation not unnaturally was broken up.

When the fighting was now taking place by sanctuaries and houses, and in the narrow lanes, between detached bodies in different parts of the town, Pyrrhus left by himself was wounded in the head. It is said that his death^[272 B.C.] was caused by a blow from a tile thrown by a woman. The Argives however declare that it was not a woman who killed him but Demeter in the likeness of a woman. This is what the Argives themselves relate about his end, and Lyceas, the guide for the neighborhood, has written a poem which confirms the story. They have a sanctuary of Demeter, built at the command of the oracle, on the spot where Pyrrhus died, and in it Pyrrhus is buried.

I consider it remarkable that of those styled Aeacidae three met their end by similar heaven-sent means; if, as Homer says, Achilles was killed by Alexander, son of Priam, and by Apollo, if the Delphians were bidden by the Pythia to slay Pyrrhus, son of Achilles, and if the end of the son of Aeacides was such as the Argives say and Lyceas has described in his poem. The account, how ever, given by Hieronymus the Cardian is different, for a man who associates with royalty cannot help being a partial historian. If Philistus was justified in suppressing the most wicked deeds of Dionysius, because he expected his return to Syracuse, surely Hieronymus may be fully forgiven for writing to please Antigonus.[^0e77eefe65d2486085f7d1385e36d8c2]

  
## Leaving Bononia (Moesia) By Road

Intending to travel by road to Naissus, Virgil left Bononia (Moesia). It was at least 76 miles. 

A cloud passes in front of the sun. As they go up from Bononia (Moesia), they see the ruined walls. A grove of Minerva is hard by the road, a grove of poplar trees. The sun beats down. Now the road is quieter. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. Workers are raising the level of the road. This is a smooth road, by which many wagons were bringing wood to Naissus. Virgil saw this on a roadside tomb: D(is) M(anibus) / M(arco) Antonio / M(arci) f(ilio) Pap(iria) Ian/uario do/[m]o Oesci O(?) / [- - - vi]xit an/[nos - - -]T(?)I(?) / [&. 

While he visited his friend at the countryside near that place, he was pleased to discover _On the Embassy_, by Aeschines. Picking it up, he read:

## On The Subject Of The Countryside Near That Place


the third cause of their ruin was mutiny, such as usually attends armies which are poorly supplied with funds. The fourth cause was Phalaecus' inability to foresee the future. For it was plain that the Thessalians and Philip were going to take the field; and shortly before the peace with you was concluded, ambassadors came to you from the Phocians, urging you to help them, and offering to hand over to you Alponus, Thronion, and Nicaea, the posts which controlled the roads to Thermopylae.[^23aa5e35494b4cca89cd1bb5dc5da8c6]

  
## Travelling By Road

Intending to travel by road to Serdica, Virgil left Naissus. It was about 92 miles away. 

A grove of Minerva is hard by the road, a grove of poplar trees. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. A caravan from Serdica passed by. Wondering if it was related to his journey, he read the words that were carved there: Imp(eratori) Caesari / L(uci) Septimi Severi / Pii Pertenacis(!) Aug(usti) / Arabici Adiabenici / Parthici Maximi filio divi / Marci Antonini Pii Germani/ci Sarmatici nepoti divi Anto/nini Pii pronepoti divi Hadri/ani abnepoti divi Traiani Par/thici et divi Nervae ad/nepoti / M(arco) Aurelio Antonino / Pio Aug(usto) trib(unicia) potest(ate) V / [co(n)s(uli) pro]co(n)s(uli) / [r(es) p(ublica) sua] Ulp(iana) / [curante] / [Q(uinto) Anicio Fau]sto leg(ato) / [A]ug[u]storum pr(o) pr(aetore). Next to the straight road that leads to Serdica, there is visible a sculpted tomb. By the road is a salt spring. There a spring wells up, and around about it is a meadow. Along the road are graves, and a cenotaph. 

While he visited his friend at the countryside near that place, he was pleased to discover _Historical Library_, by Diodorus Siculus. Picking it up, he read:

## A Story By Diodorus Siculus About The Countryside Near That Place From _Historical Library_


^[464 B.C.]When Archedemides was archon in Athens, the Romans elected as consuls Aulus Verginius and Titus Minucius,^[Titus Numicius Priscus, according to Livy 2.63.] and the Seventy-ninth Olympiad was celebrated, that in which Xenophon of Corinth^[A victory celebrated by Pind. O. 13.] won the "stadion." In this year the Thasians revolted from the Athenians because of a quarrel over mines^[Those of Mt. Pangaeus (now Pirnari) on the mainland, which yielded both gold and silver. The seizure of these mines by Philip of Macedon in 357 B.C., from which he derived in time an income of 1000 talents a year, laid the financial basis for the rise of Macedonia to supreme power in Greece.]; but they were forced to capitulate by the Athenians and compelled to subject themselves again to their rule. Similarly also, when the Aeginetans revolted, the Athenians, intending to reduce them to subjection, undertook the siege of Aegina; for this state, being often successful in its engagements at sea, was puffed up with pride and was also well provided with both money and triremes, and, in a word, was constantly at odds with the Athenians. Consequently they sent an army against it and laid waste its territory, and then, laying siege to Aegina, they bent every effort on taking it by storm. For, speaking generally, the Athenians, now that they were making great advances in power, no longer treated their allies fairly, as they had formerly done, but were ruling them harshly and arrogantly. Consequently most of the allies, unable longer to endure their severity, were discussing rebellion with each other, and some of them, scorning the authority of the General Congress,^[Of the Delian League; cp. chap. 47.] were acting as independent states. While these events were taking place, the Athenians, who were now masters of the sea, dispatched ten thousand colonists to Amphipolis, recruiting a part of them from their own citizens and a part from the allies. They portioned out the territory in allotments, and for a time held the upper hand over the Thracians, but at a later time, as a result of their further advance into Thrace, all who entered the country of the Thracians were slain^[In the battle of Drabescus; cp. Book 12.68.2, Thuc. 1.100.] by a people known as the Edones.[^ec280568736348978efceb275e36fade]

  
## Leaving Serdica By Road

Leaving Serdica, Virgil set out for Stobi by road, a distance of about 125 miles. 

There is a fountain of cold water springing from the rock. By the road is a salt spring. He had set out from Serdica amidst a throng travelling the same way. Workers are raising the level of the road. The road narrows here, an orchard wall encroaching on it. Now the road is quieter. An oxcart passes, loaded with grain. 

All of this brought to his mind what Plautus, Titus Maccius had said about the countryside near that place:

## The Story Of The Countryside Near That Place


to himself. Where now shall I find Libanus, or my master's son, that I may make them more mirthful than is Mirth herself^[Mirth herself: "Lubentia," or "Venus lubentina," was the Goddess of pleasure, mirth, and delight.]? Great booty and a triumph do I bring them on my arrival. Inasmuch as together with me they drink, together with me they are wont to wench, why, this booty that I've got, together with them will I share it.

apart. This fellow has been robbing a house, if he has been acting after his usual manner. Woe to the person that has so carelessly kept the door!

to himself. I could be ready to be a slave for an age, if I could only meet with Libanus.

apart. I' faith, with my assistance, indeed, you shall never be free a bit the sooner.

to himself. I'd give two hundred teeming lashes^[Teeming lashes: "Plagas prægnantes." Literally, "pregnant stripes"--"blows that generate other blows."] on my back as well.

apart. He's giving away all his substance, for he carries his treasures on his back^[Treasures on his back: "Talk of giving,"--he says, "stripes on his back are all that he has to give."].

to himself. But if time should intervene upon this opportunity, never, upon my faith, will he hereafter obtain it again, oven with white horses^[With white horses: White horses were most esteemed by the ancients, and were supposed to excel others in swiftness.]. He'll be deserting his master in the siege; he'll be increasing the courage of the foe. But if with me he is desirous to seize hold upon this opportunity which has presented itself, very great bounties brimful of joyousness, will he, together with myself, be producing for his masters, both for the son and the father. So that, for life, they will be indebted to us both, bound by our services.

apart. He's talking of persons being bound^[Talking of persons being bound: He catches, or pretends to catch, the two last syllables of the word "devincti," "obligated," and then says that Leonida is speaking of people being "vincti," "chained" or "bound." This he deems, or pretends to deem, to be ominous of ill.], I don't know who. I don't like it; I fear for us in common, lest he may have been cheating in some cheatery.

to himself. I'm utterly undone, unless I find Libanus at once, wherever in the world he is.

apart. This fellow's looking out for an accomplice, to unite with himself in a bad design. I don't like it: 'tis a portentous sign that instant, when a person trembles that sweats^[Person trembles that sweats: Probably Leonida is out of breath and in a perspiration; Libanus considers this as a bad omen. By his remark he is supposed to allude to the "sudiculum," a kind of scourge, which received its name from making those sweat who were punished with it.].

to himself. But why, as I hasten, do I loiter here with my feet, and make myself so bounteous with my tongue? Why don't I bid it be quiet, that in its talkativeness is wearing out the day?

apart. Upon my faith, an unfortunate man, to check his patroness; for if he has done anything roguishly, his tongue perjures itself in his behalf.

to himself. I'll make haste, lest I should be providing a safe keeping for my spoil too late.

apart. What spoil is this? I'll go meet him, and enquire what it is. He accosts him. I wish you health in as loud a voice as my strength admits of.

Exerciser of the whip, health to you.

Keeper of the gaol, how do you do?

Ha! colonizer of the chains.

Ha! delight of the scourges.

When naked, how many pounds do you say you are in weight?

Upon my faith, I don't know.

I know that you don't know; but, i' faith, I who have weighed you do know. Tied up naked, you were a hundred pounds in weight, when you were hanging with your feet downwards.

On what evidence is that?

I'll tell you on what evidence, and in what way. When you are tied up with a full hundred pounds to your feet^[Hundred pounds to your feet: When slaves were hung up by the arms to be scourged, it was usual to fasten heavy weights to their feet, to prevent them from kicking those who scourged them. The peor wit of Leonida seems to have this meaning: punning upon the word "pendeo," which signifies either "to hang from" or "to weigh," he says, that when Libanus is tied up with the weight at his feet, he weighs just as much as the weight and no more; for, being a worthless fellow, he has no weight whatever as a good man.], when the manacles are fastened to your hands, and tied to the beam, you are weighing neither more nor less, than as being a worthless and good-for-nothing fellow.

Woe be to you!

That, Servitude bequeaths to you by her will.

I wish this skirmishing of words to be cut short. What matter is this?

Am I sure in trusting you?

You may, without hesitation.

If you wish to assist our master's son in his amour, there is so much of a good opportunity on a sudden, but still mingled with evil--all the hangman's days will be rendered famous by ourselves. Libanus, now have we occasion to find some boldness and inventiveness. An exploit so great have I thought of just now, that we two may be pronounced the most deserving of all for torture to befall us.

'Twas on that account I was wondering why my shoulder-blades were aching just now, which were beginning to prognosticate that there was some danger for them at home. Whatever it is, speak out.

'Tis great booty with great risk.

If indeed all persons by compact were to collect all the tortures, I have, I fancy, a back at home, so that I need not seek it out of doors.

If you maintain such firmness of resolve, then we are all right.

Why, if the matter were to be atoned for by my back, I could wish to seize the public money: I'll persist in my denial, and I'll endure all; in fine, I'll forswear myself.

Ah! that's true valour, when occasion is, for one to endure misfortune with boldness. He that endures misfortune with boldness, that man afterwards enjoys good fortune.

Why don't you tell the matter at once? I'm longing to tempt the scourge.

breathing hard. Ask deliberately each particular then, that I may rest me. Don't you see that I'm still out of breath with running?

Well, well, I'll wait your pleasure, even, in fact, till you die.

Where's our master, pray?

The old one is at the Forum, the young one is here in-doors.

That's enough for me then.

Is it then that you've become a rich man?

Leave off your raillery.

I'll have done; for my ears are in expectation of what you are bringing me.

Give your attention, that equally with myself you may learn this.

I'm silent, then.

You oblige me. Don't you remember that our chamberlain sold some Arcadian asses to a dealer of Pella^[Dealer of Pella: Pella was a wealthy city of Macedonia, famed for the opulence of its merchants. It was the birthplace of Alexander the Great]?

I remember it; after that, what then?

Well, he has sent some money here then to be paid to Saurea, for the asses; a young man has just now come who has brought this money.

Where is this person?

You think he ought to be devoured this instant, if you could see him.

Aye, to be sure. But, however, you are speaking, I suppose, of those asses, aged and lame, whose hoofs were quite worn away to their very thighs?

Those same ones, that carried the elm twigs hither from the country, for your use.

I understand you; and the same ones carried you from here, bound, into the country^[Bound, into the country: Namely, to the "ergastulum," of "puteus," the place to which refractory slaves were sent for hard labour, and which was generally at the country-house of the master.].

You say what's quite correct. But as I was sitting in the barber's shop, he began to make enquiries of me, whether I knew a certain Demænetus, the son of Strato. At once I said that I knew him, and that I was his servant; and I pointed out our house.

After that, what then?

He said that he was bringing the money for the asses to the chamberlain Saurea, twenty minæ in amount; but that he himself didn't know the individual, who he was, but that he knew Demænetus quite well. Since he spoke thus to this effect----

What then?

Listen then, and you'll know. At once I made myself courteous, and a person of consequence. I said that I was the chamberlain. Thus, in these terms did he answer me: "Upon my faith, I don't know Saurea, nor yet of what appearance he is. It isn't fair for you to blame me; but if you like, bring here Demænetus, your master, whom I do know; I'll not prevent you taking the money then." I said that I would bring him, and that I should be at home immediately. He's about to go to the baths^[To go to the baths: It was very natural that after a long journey he should first go to the barber's shop, and then repair to the public baths to refresh himself.], from there he'll afterwards come here. What plan do you think, now, I ought to adopt? Tell me.

Why, I'm thinking of this, how to get between the money, and the stranger, and Saurea. At present this matter is rough-hewn; but if this stranger brings here the money first, then are we both at once shut out from it. But the old man to-day took me apart at a distance from the house, and threatened me and yourself that we should be tasters of the elm twigs, if Argyrippus didn't this very day get twenty mine of silver. He commanded that we should cheat either the chamberlain or his own wife, and said that he would give the aid he promised. Now, do you go to the Forum to our master, and tell him this, how we are going to manage; that you, from Leonida, are going to be the chamberlain Saurea, until the dealer has brought the money for the asses.

I'll do as you request me.

In the meantime, I'll amuse him here, if by chance he should come first.

But what say you----?

What do you want?

If I give you a blow on the cheek with my fist, by-and-by, while I'm personating Saurea^[Personating Saurea: Saurea, as the "atriensis," "chamberlain" or "gentleman-usher," was the head of the slave family; and it was his privilege to beat the other slaves, if they offended him or neglected their duties.], don't you be offended.

I' faith, but you'll have a care not to be touching me, if you are wise; you'll surely have changed your name to day with a bad omen^[Your name to-day with a bad omen: Limiers says that this is said in allusion to his having assumed the name of "Saurea," which meant "a lash" or "scourge."].

Prithee, do endure it with resolution.

Do you endure the cuff that I, too, shall be giving you in return.

I speak as it's in the habit of being done.

I' faith, and I speak, too, of how I'm likely to act.

Don't refuse me.

Why I promise, I tell you, to give you a like return, just as you deserve.

I'm off; I know that you'll put up with it by-and-by. But who's this? 'Tis he--'tis the very man himself. I'll return here just now; in the meantime do you detain him here; I want to inform the old gentleman. (Exit.)

Well, do your duty, then, and fly.[^faee018e04794de4af769a59777975f5]

  
## 54 Miles To Heraklea

From Stobi to Heraklea is a journey of about 54 miles when travelling by road. 

He left the city early, before the rising of the sun. This is a smooth road, by which many wagons were bringing wood to Heraklea. Above the roads are ruins, among which is a cave sacred to Asclepius. A cloud passes in front of the sun. They pass a pillar on the right surmounted by a stone urn. The road narrows here, an orchard wall encroaching on it. On the road from Stobi to Heraklea there is a village, in which there is a temple and grove. Not far from the road is a grave, on which is mounted a soldier standing by a horse. Who it is I do not know, but both horse and soldier were carved by Praxiteles. 

While he visited his friend at the countryside near that place, he was pleased to discover _Histories_, by Polybius. Picking it up, he read:

## An Account Of The Countryside Near That Place


Then Gnaeus Fulvius sailed back to Rome with the larger part of the naval and military forces, while Postumius, staying behind and collecting forty vessels and a legion from the cities in that district, wintered there to guard the Ardiaei and other tribes that had committed themselves to the protection of Rome. Just before spring in the next year, Teuta sent envoys to Rome and concluded a treaty; in virtue of which she consented to pay a fixed tribute, and to abandon all Illyricum, with the exception of some few districts: and what affected Greece more than anything, she agreed not to sail beyond Lissus with more than two galleys, and those unarmed. When this arrangement had been concluded, Postumius sent legates to the Aetolian and Achaean leagues, who on their arrival first explained the reasons for the war and the Roman invasion; and then stated what had been accomplished in it, and read the treaty which had been made with the Illyrians. The envoys then returned to Corcyra after receiving the thanks of both leagues: for they had freed Greece by this treaty from a very serious cause for alarm, the fact being that the Illyrians were not the enemies of this or that people, but the common enemies of all alike.

Such were the circumstances of the first armed interference of the Romans in Illyricum and that part of Europe, and their first diplomatic relations with Greece; and such too were the motives which suggested them. But having thus begun, the Romans immediately afterwards sent envoys to Corinth and Athens. And it was then that the Corinthians first admitted Romans to take part in the Isthmian games.[^7b51196a96824839a279dd2cb4b4e4fa]

  
## Departing From Heraklea

Leaving Heraklea, Virgil set out for a village by road, about 109 miles away. 

Water has washed out the road, making for slow going. Next to the straight road that leads to a village, there is visible a sculpted tomb. A caravan from a village passed by. A grove of Minerva is hard by the road, a grove of poplar trees. They pass a pillar on the right surmounted by a stone urn. 

  
## Departing From A Village

Intending to travel by road to Apollonia (Epirus), Virgil left a village. It was at least 23 miles. 

A grove of Minerva is hard by the road, a grove of poplar trees. He passes another milestone. He had set out from a village amidst a throng travelling the same way. By the gate of Apollonia (Epirus), these words were carved: Lucius Pinxit. 

The library at the countryside near that place happened to have a copy of _Odyssey_, where Virgil encountered it.

## What Homer Once Said About The Countryside Near That Place


So here Odysseus slept, overcome by sleep and toil; but Athena went off to the dêmos and city of the Phaeacians - a people who used to live in the fair town of Hypereia, near the lawless Cyclopes. Now the Cyclopes were stronger in force [biê] than they and plundered them, so their king Nausithoos moved them thence and settled them in Scheria, far from all other people. He surrounded the city with a wall, built houses and temples, and divided the lands among his people; but he was dead and gone to the house of Hades, and King Alkinoos, whose counsels were inspired of heaven, was now reigning. To his house, then, did Athena go in furtherance of the return [nostos] of Odysseus.

She went straight to the beautifully decorated bedroom in which there slept a girl who was as lovely as a goddess, Nausicaa, daughter to King Alkinoos. Two maid servants were sleeping near her, both very pretty, one on either side of the doorway, which was closed with well-made folding doors. Athena took the form of the famous sea leader Dymas' daughter, who was a bosom friend of Nausicaa and just her own age; then, coming up to the girl's bedside like a breath of wind, she hovered over her head and said:

"Nausicaa, what can your mother have been about, to have such a lazy daughter? Here are your clothes all lying in disorder, yet you are going to be married almost immediately, and should not only be well dressed yourself, but should find good clothes for those who attend you. This is the way to get yourself a good name, and to make your father and mother proud of you. Suppose, then, that we make tomorrow a washing day, and start at daybreak. I will come and help you so that you may have everything ready as soon as possible, for all the best young men throughout your own dêmos are courting you, and you are not going to remain a young girl much longer. Ask your father, therefore, to have a wagon and mules ready for us at daybreak, to take the rugs, robes, and belts; and you can ride, too, which will be much pleasanter for you than walking, for the washing-cisterns are some way from the town."

When she had said this Athena went away to Olympus, which they say is the everlasting home of the gods. Here no wind beats roughly, and neither rain nor snow can fall; but it abides in everlasting sunshine and in a great peacefulness of light, wherein the blessed gods are illumined for ever and ever. This was the place to which the goddess went when she had given instructions to the girl.[^426fd5bac41a432bb817025ba39f5316]

  
## To Dyrrhachium

From Apollonia (Epirus) to Dyrrhachium is a distance of about 42 miles when travelling by ship down the coast. 

A dusky shower drew up overhead carrying night and tempest.   
  
A fair harbor lies on either side of the city and the entrance is narrow. Here they shape the thin oar-blades. 

While he was visiting Dyrrhachium, he made a point of copying down what Cicero, Marcus Tullius had written.

## An Extract From _For Plancius_ By Cicero, Marcus Tullius


For it does not follow because Plancius has lived in such a manner as never willfully to offend any one, or because you have made such a mistake as unintentionally to select such men that we find we are come before judges, and not before executioners, that on that account that selection, if looked at by itself, is not a severe measure.[^082f28cca05845809101db2aa0cab627]

\newpage
[^8cd27d4de0744700b482aeceda589443]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.78} 


[^fb5d69db56b34e41b73b5448942ccd02]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.63} 


[^9106d3e0c33a4bc68e76fa67e72e1a79]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=108} 


[^3425c35a991c4abb9e28a729c55a6a3a]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:2.9} 


[^d392fd190949443cad9c7ac1924d8d42]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.8} 


[^6c98eda8b3504d4db04506bafd3c7e79]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.11} 


[^8ee15fb50aef41608d3dc2b0bb7eef8c]: From the Perseus Digital Library:      Strabo. ed. H. L. Jones, The Geography of Strabo. Cambridge, Mass.: Harvard University Press; London: William Heinemann, Ltd. 1924. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0099.tlg001.perseus-eng1:6.3} 


[^dae3b29eacc7468e8014b017dceec3b0]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.8} 


[^ab2a6957b5864c6ebe57c39eabc138c4]: From the Perseus Digital Library:      Strabo. ed. H. L. Jones, The Geography of Strabo. Cambridge, Mass.: Harvard University Press; London: William Heinemann, Ltd. 1924. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0099.tlg001.perseus-eng1:6.1} 


[^f12aa0107c3d41e19828808a5f7c9168]: From the Perseus Digital Library:      Aristotle. Aristotle in 23 Volumes, Vol. 18, translated by G.C. Armstrong. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1935. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0086.tlg029.perseus-eng1:2.1352a} 


[^5ef1a5880e3444d79887c121fa441f08]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.9} 


[^88962ea5db354054954ea7c5430f2238]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:4.402} 


[^218461c3301e4ae9adeca61a2b85bd4e]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:2.48} 


[^3eb8faafbb834f38a17da2cc90440190]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi002.perseus-eng1:9} 


[^75a6e222274c4482be3df92b07dbfc55]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie  Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo020.perseus-eng1:1} 


[^86c0b69cb98f49659fb1621144dd8b68]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0051:book=7:commline=517} 


[^b0c063a26f004f28ba36b3ee4d6fab65]: From the Perseus Digital Library:      Ovid. Metamorphoses. Arthur Golding. London. W. Seres. 1567. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0959.phi006.perseus-eng2:2.301} 


[^8b8fa88085374db6aeeb3edb8a63a234]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo016.perseus-eng1:31} 


[^3992eae6099f4698ae00d4fefdc8c698]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0051:book=7:commline=800} 


[^76d321a74fc94d9ba741745dfbb1cee0]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo014.perseus-eng1:59} 


[^de8763598f3d42ed8bc8bb865ccc2260]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0051:book=7:commline=45} 


[^baff5834469c4f91bc9d079eb3919198]: From the Perseus Digital Library:      Horace. The Works of Horace. C. Smart. Theodore Alois Buckley. New York. Harper  Brothers. 1863. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0893.phi004.perseus-eng1:1.5} 


[^99afe678f22d4e83b05ab27cd64e6e7c]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi011.perseus-eng1:2.14} 


[^f47d2ae39ebb42218adf3ff0981edae9]: From the Perseus Digital Library:      Horace. The Odes and Carmen Saeculare of Horace. John Conington. trans. London. George Bell and Sons. 1882. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0893.phi001.perseus-eng1:3.17} 


[^431993fc03c74a87aa9650a70e768943]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.76} 


[^2c3f72703e6c403a847d63cfd90c75e6]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:3.24} 


[^2ee18131884e46abb67b71b4500714f1]: From the Perseus Digital Library:      Horace. The Odes and Carmen Saeculare of Horace. John Conington. trans. London. George Bell and Sons. 1882. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0893.phi001.perseus-eng1:4.15} 


[^59ae4583f7ac48c0ad7169bdb776b074]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0051:book=7:commline=670-677} 


[^db3ebbb2bbb549f9aab373b883346d54]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.58} 


[^2f6d12b0dad9459d9eafb75408b11b8f]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi011.perseus-eng1:2.30} 


[^9db735a74d2549dd8c176b2655cf5281]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.79} 


[^27018263a3964e74a99f6952d33a2bd2]: From the Perseus Digital Library:      Livy. History of Rome. English Translation by. Rev. Canon Roberts. New York, New York. E. P. Dutton and Co. 1912. 1. Livy. History of Rome. English Translation. Rev. Canon Roberts. New York, New York. E. P. Dutton and Co. 1912. 2. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0914.phi0012.perseus-eng3:39} 


[^95f2851bdf30454880fb872c6007a6e7]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:5.1} 


[^8edd19034673482b9e3a0bde03101a47]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi008.perseus-eng1:35} 


[^554de7e5295a466ba0f0373398ef0a84]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:1.33} 


[^c931b563038f46bda97774cbb3fd5670]: From the Perseus Digital Library:      Catullus. The Carmina of Gaius Valerius Catullus. Leonard C. Smithers. London. Smithers. 1894. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0472.phi001.perseus-eng2:59} 


[^cc4a81cf5b174bac9357f7ff26d9f32e]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:3.67} 


[^dc31ad3fdf1249e0bbc7c0c27178b805]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:1.70} 


[^76f5b5ac6dd646f79e431c1f0d06a57a]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=intro:section=8} 


[^74c23d1d04f640afa8cc559f4b423313]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.6} 


[^cac6180032734088a65f964017b051ff]: From the Perseus Digital Library:      Herodotus, with an English translation by A. D. Godley. Cambridge. Harvard University Press. 1920. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0016.tlg001.perseus-eng1:1.46} 


[^45f0ee7d275f448fa521a172af5d7432]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.5} 


[^5934e4f43ff44fd69d01cc0190aa2577]: From the Perseus Digital Library:      Flavius Josephus. The Works of Flavius Josephus. Translated by. William Whiston, A.M. Auburn and Buffalo. John E. Beardsley. 1895. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0526.tlg002.perseus-eng1:30} 


[^2c0d53cad4e44f96900adac123d3c27f]: From the Perseus Digital Library:      Pausanias. Pausanias Description of Greece with an English Translation by W.H.S. Jones, Litt.D., and H.A. Ormerod, M.A., in 4 Volumes. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1918. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0525.tlg001.perseus-eng1:9.10} 


[^bf732909d26440f2a4ba7c8382ec66ef]: From the Perseus Digital Library:      C. Julius Caesar. Caesar's Gallic War. Translator. W. A. McDevitte. Translator. W. S. Bohn. 1st Edition. New York. Harper & Brothers. 1869. Harper's New Classical Library. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi001.perseus-eng1:1.10} 


[^da512b1fdacf4be68172ed946f994959]: From the Perseus Digital Library:      Horace. The Odes and Carmen Saeculare of Horace. John Conington. trans. London. George Bell and Sons. 1882. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0893.phi001.perseus-eng1:3.9} 


[^3e42876587ac478fb78038e070a8174d]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.8} 


[^07ad232c4c234e9fad55509b24f7878e]: From the Perseus Digital Library:      Herodotus, with an English translation by A. D. Godley. Cambridge. Harvard University Press. 1920. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0016.tlg001.perseus-eng1:6.19} 


[^d214c7458e45479a9e3ae89cde96822f]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.19} 


[^f18766d4d75b40b8adaebdf883237460]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=intro:section=2} 


[^58f9f43c8ffd49ffb60b1994fbde155e]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.7} 


[^6b1e445bdf524a0dafd17422e7a68b85]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=intro:section=10} 


[^3095733f96bc4d469f1704ee22c85c5a]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=intro:section=4} 


[^93f72077f7c344e79713cf54eee1b77f]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo012.perseus-eng1:21} 


[^a6a42fbc857e4dfc9fdd1f25334b71e1]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo017.perseus-eng1:9} 


[^54d08dc974f042a890af72984ca14af8]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:4.61} 


[^c36aafa457aa406780bb819d292fef06]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=35} 


[^5d53476bb7844371ae3bc80612de59ee]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo011.perseus-eng1:28} 


[^5a251c747dae49c0968e4a270e7b0e24]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=63} 


[^20cecc1e1c654086baa40dc4bc458db7]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:4.70} 


[^934cbc67ca064be0b16287e9b1697d16]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:2.32} 


[^d8d8fdbb6738483c8f8274eefe4c31cf]: From the Perseus Digital Library:      Catullus. Carmina. Sir Richard Francis Burton. trans. London. For translator for private use. 1894. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0472.phi001.perseus-eng1:35} 


[^8f3b8bbe64ca4a02867b163dec933325]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo012.perseus-eng1:20} 


[^4420d57f0ae24c9cb38862b9a9fe9304]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:10.42} 


[^577270aac2184be59b3772e9f7d39a67]: From the Perseus Digital Library:      Vergil. Bucolics, Aeneid, and Georgics Of Vergil. J. B. Greenough. Boston. Ginn & Co. 1900. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0690.phi002.perseus-eng1:4.251} 


[^d3433e3491264951ab51ae691d070d14]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.33} 


[^f60a6248c51245699e2f012ce022f71c]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:2.88} 


[^d4c5b2952791418f9682b8eef40086d1]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi035.perseus-eng1:6.3} 


[^4ab38884283243c382cf9dfa23b0cdb7]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:2.23} 


[^e018939863a5435d962b62f0eb1a8770]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=39} 


[^6765d0d24b9e45f38269ca2f0824d74e]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:2.85} 


[^85cde56b6a6d4b85ac55fb357fd1e868]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=64} 


[^384c290e1868481795494569c37be8c1]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0051:book=9:commline=380} 


[^aae5683c83b94cafaeeb35258ab2d71c]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:7.87} 


[^3831e69162544136b02d7d2ff40fbd21]: From the Perseus Digital Library:      Pausanias. Pausanias Description of Greece with an English Translation by W.H.S. Jones, Litt.D., and H.A. Ormerod, M.A., in 4 Volumes. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1918. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0525.tlg001.perseus-eng1:7.5} 


[^9e91ff36edf744a8a20ad4aba0ed56ce]: From the Perseus Digital Library:      Pausanias. Pausanias Description of Greece with an English Translation by W.H.S. Jones, Litt.D., and H.A. Ormerod, M.A., in 4 Volumes. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1918. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0525.tlg001.perseus-eng1:8.46} 


[^27d8b0f312324788955119d50ee80276]: From the Perseus Digital Library:      Herodotus, with an English translation by A. D. Godley. Cambridge. Harvard University Press. 1920. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0016.tlg001.perseus-eng1:2.33} 


[^1ca5eac8079446e19a0aab6873e3c277]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:1.4} 


[^27cf1bf7a7344b2494b84dc0916c18be]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo013.perseus-eng1:7} 


[^03b5e5e4e51a498ebb2ad29337cdf7f1]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi005.perseus-eng1:2.4.74} 


[^0c096088cb344ccb925802c8d3782054]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi005.perseus-eng1:2.4.76} 


[^59ef153628cc426ab9611bca33eb09f1]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:2.32} 


[^c7b390c4a59540129de75c4961df96f5]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.40} 


[^7c1c87235fde437f8a22842ad537d2ec]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo015.perseus-eng1:13} 


[^d7e5f655093349cfb50201c608932fee]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:4.16} 


[^8c9d27258f4d4d17ae1eec01ec66277d]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:8.16} 


[^418fb29555b042bd973dd1aed7e66e6d]: From the Perseus Digital Library:      Thucydides. The Peloponnesian War. London, J. M. Dent; New York, E. P. Dutton. 1910. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0003.tlg001.perseus-eng3:2.101} 


[^bd2e726c74fe4d95af1bce38b0de2b3f]: From the Perseus Digital Library:      Apollodorus. Apollodorus, The Library, with an English Translation by Sir James George Frazer, F.B.A., F.R.S. in 2 Volumes. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1921. Includes Frazers notes. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0548.tlg001.perseus-eng1:2.5} 


[^ad4d364d9590419abd5af1ca18a87154]: From the Perseus Digital Library:      Horace. The Odes and Carmen Saeculare of Horace. John Conington. trans. London. George Bell and Sons. 1882. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0893.phi001.perseus-eng1:3.4} 


[^84ff20c73b9940148ad16e5907a9fd75]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:2.45} 


[^c6916853c5324ab18da8397ff2c027f1]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:5.593} 


[^cb1364d7359840a2875666e3785c439d]: From the Perseus Digital Library:      Ovid. Metamorphoses. Brookes More. Boston. Cornhill Publishing Co. 1922. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0959.phi006.perseus-eng1:4.167} 


[^e20bbe09d7bd406e9ecc16c27f2e9df6]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:4.2} 


[^1faeb86b63424adf998f36575ae3156a]: From the Perseus Digital Library:      Pausanias. Pausanias Description of Greece with an English Translation by W.H.S. Jones, Litt.D., and H.A. Ormerod, M.A., in 4 Volumes. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1918. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0525.tlg001.perseus-eng1:9.6} 


[^ff0a827dd0584ebf9d59cf6cb95f7342]: From the Perseus Digital Library:      Thucydides. The Peloponnesian War. London, J. M. Dent; New York, E. P. Dutton. 1910. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0003.tlg001.perseus-eng3:2.99} 


[^43734f36646d4396b9cd26e1cbca767f]: From the Perseus Digital Library:      Horace. The Odes and Carmen Saeculare of Horace. John Conington. trans. London. George Bell and Sons. 1882. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0893.phi001.perseus-eng1:1.4} 


[^b29094328cf744c6b136e3b053946e9e]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.57} 


[^bb28b1b133fe41d8831ab0174d643232]: From the Perseus Digital Library:      The Comedies of Plautus. Henry Thomas Riley. London. G. Bell and Sons. 1912. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0119.phi010.perseus-eng1:2.2} 


[^65ffdbba66324345a08b55e2a5ee58d8]: From the Perseus Digital Library:      Ovid. Metamorphoses. Brookes More. Boston. Cornhill Publishing Co. 1922. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0959.phi006.perseus-eng1:13.313} 


[^a48ba4451a35410eb46b414bd00dfe2b]: From the Perseus Digital Library:      The Comedies of Plautus. Henry Thomas Riley. London. G. Bell and Sons. 1912. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0119.phi001.perseus-eng1:1.1} 


[^9e7d7793261b4229884c20b1129688d3]: From the Perseus Digital Library:      The Comedies of Plautus. Henry Thomas Riley. London. G. Bell and Sons. 1912. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0119.phi017.perseus-eng1:3.4} 


[^4cc58b5abac643a0b96e4a6076670620]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:10.434} 


[^0e77eefe65d2486085f7d1385e36d8c2]: From the Perseus Digital Library:      Pausanias. Pausanias Description of Greece with an English Translation by W.H.S. Jones, Litt.D., and H.A. Ormerod, M.A., in 4 Volumes. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1918. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0525.tlg001.perseus-eng1:1.13} 


[^23aa5e35494b4cca89cd1bb5dc5da8c6]: From the Perseus Digital Library:      Aeschines. Aeschines with an English translation by Charles Darwin Adams, Ph.D. Cambridge, MA, Harvard University Press; London, William Heinemann Ltd. 1919. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0026.tlg002.perseus-eng1:132} 


[^ec280568736348978efceb275e36fade]: From the Perseus Digital Library:      Diodorus Siculus. Diodorus of Sicily in Twelve Volumes with an English Translation by C. H. Oldfather. Vol. 4-8. Cambridge, Mass.: Harvard University Press; London: William Heinemann, Ltd. 1989. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0060.tlg001.perseus-eng1:11.70} 


[^faee018e04794de4af769a59777975f5]: From the Perseus Digital Library:      The Comedies of Plautus. Henry Thomas Riley. London. G. Bell and Sons. 1912. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0119.phi002.perseus-eng1:2.2} 


[^7b51196a96824839a279dd2cb4b4e4fa]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:2.12} 


[^426fd5bac41a432bb817025ba39f5316]: From the Perseus Digital Library:      Homer. The Odyssey. Rendered into English prose for the use of those who cannot read the original. Samuel Butler. Based on public domain edition, revised by Timothy Power and Gregory Nagy. A. C. Fifield, London. 1900 (?). \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0012.tlg002.perseus-eng2:6.1} 


[^082f28cca05845809101db2aa0cab627]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. George Bell & Sons, York Street, Covent Garden. 1891. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi028.perseus-eng1:41} 


