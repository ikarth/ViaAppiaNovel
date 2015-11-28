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
    Virgil departed from Roma, intending to travel on a boat heading upstream to Ocriculum, a 64.936997726 mile journey. 

### Ocriculum in Historiae



While these successes were being achieved on the side of Vitellius, the army of Vespasian had left Narnia, and was passing the holiday of the Saturnalia in idleness at Ocriculum. The reason alleged for so injurious a delay was that they might wait for Mucianus. Some persons indeed there were who assailed Antonius with insinuations, that he lingered with treacherous intent, after receiving private letters from Vitellius, which conveyed to him the offer of the consulship and of the Emperor's daughter in marriage with a vast dowry, as the price of treason. Others asserted that this was all a fiction, invented to please Mucianus. Some again alleged that the policy agreed upon by all the generals was to threaten rather than actually to attack the capital, as Vitellius' strongest cohorts had revolted from him, and it seemed likely that, deprived of all support, he would abdicate the throne, but that the whole plan was ruined by the impatience and subsequent cowardice of Sabinus, who, after rashly taking up arms, had not been able to defend against three cohorts the great stronghold of the Capitol, which might have defied even the mightiest armies. One cannot, however, easily fix upon one man the blame which belongs to all. Mucianus did in fact delay the conquerors by ambig- uously-worded dispatches; Antonius, by a perverse acquiescence, or by an attempt to throw the odium upon another, laid himself open to blame; the other generals, by imagining that the war was over, contrived a distinction for its closing scene. Even Petilius Cerialis, though he had been sent on with a thousand cavalry by cross roads through the Sabine district so as to enter Rome by the Via Salaria, had not been sufficiently prompt in his movements, when the report of the siege of the Capitol put all alike on the alert.[^f119f8a329344fafa4de979f8a60d239]

Virgil departed from Ocriculum, intending to travel by road to Narnia, a 8.118212115 mile journey. 

### What Cornelius Tacitus once said about Narnia



Finding all their hopes cut off, the troops of Vitellius, intending to pass over to the side of the conqueror, but to do so with honour, marched down with their standards and colours into the plains beneath Narnia. The army of Vespasian, prepared and equipped as if for action, was drawn up in dense array on both sides of the road. The Vitellianists were received between the two columns; when they were thus surrounded, Antonius addressed them kindly. One division was ordered to remain at Narnia, another at Interamna; with them were left some of the victorious legions, which would not be formidable to them if they remained quiet, but were strong enough to crush all turbulence. At the same time Primus and Varus did not neglect to forward continual messages to Vitellius, offering him personal safety, the enjoyment of wealth, and a quiet retreat in Campania, provided he would lay down his arms and surrender himself and his children to Vespasian. Mucianus also wrote to him to the same effect, and Vitellius was often disposed to trust these overtures, and even discussed the number of his household and the choice of a residence on the coast. Such a lethargy had come over his spirit, that, had not others remembered he had been an Emperor, he would have himself forgotten it.[^13d5de2d9ecf4cf187a6fee9edbb9086]

Virgil departed from Narnia, intending to travel by road to Spoletium, a 22.863967316 mile journey. 

### A story about Spoletium



THE empire, which had been long thrown into a disturbed and unsettled state, by the rebellion and violent death of its three last rulers, was at length restored to peace and security by the Flavian family, whose descent was indeed obscure, and which boasted no ancestral honours; but the public had no cause to regret its elevation; though it is acknowledged that Domitian met with the just reward of his avarice and cruelty. Titus Flavius Petro, a townsman of Reate,^[Reate, the original seat of the Flavian family, was a city of the Sabines. Its present name is Rieti. ] whether a centurion or an _evocatus_^[It does not very clearly appear what rank in the Roman armies was held by the evocati. They are mentioned on three occasions by Suetonius, without affording us much assistance. Caesar, like our author, joins them with the centurions. See, in particular, De Bell. Civil. I. xvii. 4. ] of Pompey's party in the civil war, is uncertain, fled out of the battle of Pharsalia and went home; where, having at last obtained his pardon and discharge, he became a collector of the money raised by public sales in the way of auction. His son, surnamed Sabinus, was never engaged in the military service, though some say he was a centurion of the first order, and others, that whilst he held that rank, he was discharged on account of his bad state of health: this Sabinus, I say, was a republican, and received the tax of the fortieth penny in Asia. And there were remaining, at the time of the advancement of the family, several statues, which had been erected to him by the cities of that province, with this inscription: "To the honest Tax-farmer."^[The inscription was in Greek, \rendergreek{καλῶς τελωθήσαντι}] He afterwards turned usurer amongst the Helvetii, and there died, leaving behind him his wife, Vespasia Polla, and two sons by her; the elder of whom, Sabinus, came to be prefect of the city, and the younger, Vespasian, to be emperor. Polla, descended of a good family, at Nursia,^[In the ancient Umbria. afterwards the duchy of Spoleto; its modern name being Norcia.] had for her father Vespasius Pollio, thrice appointed military tribune, and at last prefect of the camp; and her brother was a senator of praetorian dignity. There is to this day, about six miles from Nursia, on the road to Spoletum, a place on the summit of a hill, called Vespasize, where are several monuments of the Vespasii, a sufficient proof of the splendour and antiquity of the family. I will not deny that some have pretended to say. that Petro's father was a native of Gallia Transpadana,^[Gaul beyond, north of, the Po, now Lombardy. ] whose employment was to hire work-people who used to emigrate every year from the country of the Umbria into that of the Sabines, to assist them in their husbandry;^[We find the annual migration of labourers in husbandry a very common practice in ancient as well as in modern times. At present, several thousand industrious labourers cross over every summer from the duchies of Parma and Modena, bordering on the district mentioned by Suetonius, to the island of Corsica; returning to the continent when the harvest is got in. ] but who settled at last in the town of Reate, and there married. But of this I have not been able to discover the least proof, upon the strictest inquiry.[^b25f10d12c434cbd870416da5a917816]

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, a 90.170252665 mile journey. 

### A story about Fanum Fortunae



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

10\. Thus the gable tops run in two directions, like the letter T, and give a beautiful effect to the outside and inside of the main roof. Further, by the omission of an ornamental entablature and of a line of screens and a second tier of columns, troublesome labour is saved and the total cost greatly diminished. On the other hand, the carrying of the columns themselves in unbroken height directly up to the beams that support the main roof, seems to add an air of sumptuousness and dignity to the work.[^c91b435061fd4275a051b6e818e7b6eb]

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ariminum, a 38.157771739 mile journey. 

### An extract from For Aulus Caecina by Cicero, Marcus Tullius



Since you make this statement, and lay down this principle, "that, if Caecina, when he was actually in his farm, had been driven from it, then it would have been right for him to be restored by means of this interdict; but now he can by no means be said to have been from a place where he has not been; and, therefore, we have gained nothing by this interdict;" I ask you, if, this day, when you are returning home, men collected in a body, and armed, not only prevent you from crossing the threshold and from coming under the roof of your own house, but keep you off from approaching it— from even entering the court yard,—what will you do? My friend Lucius Calpurnius reminds you to say the same thing that he said before, namely that you would bring an action for the injury. But what has this to do with possession? What has this to do with restoring a man who ought to be restored? or with the civil law? I will grant you even more. I will allow you not only to bring your action, but also to succeed in it. Will you be any the more in possession of your property for that? For an action for injury done does not carry with it, even if successful, any right of possession; but merely makes up to a man for the loss he sustains through the diminution of his liberty, by the trial and penalty imposed upon the offender.[^b109094a3271426caf56ddb1786cc26c]

Virgil departed from Ariminum, intending to travel by ship down the coast to Fanum Fortunae, a 38.157771739 mile journey. 

### A story about Fanum Fortunae



It was, by no means, a fair proposal, that Caesar should be obliged to quite Rimini and return to Gaul, while Pompey held provinces and legions that were none of his: that he should dismiss his army, whilst the other was levying troops: and, that only a general promise of going into Spain should be given, without fixing a day for his departure; by which evasion, was he to be found in Italy, even at the expiration of Caesar's consulship, he could not yet be charged with breach of faith. His forbearing too to appoint a time for a conference, and declining to approach nearer, gave little reason to hope for a peace. He therefore sent Antony to Arretium, with five cohorts; remained himself at Rimini, with two, where he resolved to levy troops; and seizing Pisaurum, Fanum, and Ancona, left a cohort in each for a garrison.[^6874be05b7b5462898f1b25c86e73143]

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ancona, a 42.411056234 mile journey. 

### A story about Ancona by Vitruvius Pollio



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

17\. The leaves of these trees are like those of the pine; timber from them comes in long lengths, is as easily wrought in joiner's work as is the clearwood of fir, and contains a liquid resin, of the colour of Attic honey, which is good for consumptives. With regard to the different kinds of timber, I have now explained of what natural properties they appear to be composed, and how they were produced. It remains to consider the question why the highland fir, as it is called in Rome, is inferior, while the lowland fir is extremely useful in buildings so far as durability is concerned; and further to explain how it is that their bad or good qualities seem to be due to the peculiarities of their neighbourhood, so that this subject may be clearer to those who examine it.[^42940c521cd8441a9ba46e16f23d08ec]

Virgil departed from Ancona, intending to travel by ship down the coast to Iader, a 107.75815881999999 mile journey. 

Virgil departed from Iader, intending to travel by ship down the coast to Titius (river), a 48.512298083 mile journey. 

Virgil departed from Titius (river), intending to travel by ship down the coast to Iader, a 48.512298083 mile journey. 

Virgil departed from Iader, intending to travel by road to Burnum, a 40.332570239000006 mile journey. 

Virgil departed from Burnum, intending to travel by road to Salona, a 50.36833326 mile journey. 

### An extract from Civil War by Julius Caesar



Caesar having landed his troops, sent the fleet back the same night to Brundusium, to bring over his other legions and cavalry. Fufius Kalenus, lieutenant-general, had the charge of this expedition, with orders to use the utmost despatch. But setting sail too late, he lost the benefit of the wind, which offered fair all night, and fell in with the enemy. For Bibulus hearing at Corcyra of Caesar's arrival, forthwith put to sea, in hopes of intercepting some of the transports; and meeting the fleet as it returned empty, took about thirty ships, which he immediately burned, with all that were on board; partly to satisfy his own vengeance for the disappointment he had received; partly to deter the rest of the troops from attempting the passage. He then stationed his fleet along the coast, from Salona to Oricum, guarded all places with extraordinary care, and even lay himself aboard, notwithstanding the rigour of the winter; declining no danger nor fatigue, and solely intent upon intercepting Caesar's supplies.[^7c7ef612b3a14fc2b625860e446e78fe]

Virgil departed from Salona, intending to travel by ship down the coast to Aternum, a 153.083445044 mile journey. 

Virgil departed from Aternum, intending to travel by ship down the coast to Castrum Truentinum, a 38.822017338 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a 17.434427518 mile journey. 

[^f119f8a329344fafa4de979f8a60d239]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.78} 


[^13d5de2d9ecf4cf187a6fee9edbb9086]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.63} 


[^b25f10d12c434cbd870416da5a917816]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie  Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo020.perseus-eng1:1} 


[^c91b435061fd4275a051b6e818e7b6eb]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:5.1} 


[^b109094a3271426caf56ddb1786cc26c]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi008.perseus-eng1:35} 


[^6874be05b7b5462898f1b25c86e73143]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.11} 


[^42940c521cd8441a9ba46e16f23d08ec]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:2.9} 


[^7c7ef612b3a14fc2b625860e446e78fe]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.8} 


