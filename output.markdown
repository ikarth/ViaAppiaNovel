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

### An account of Ocriculum



While these successes were being achieved on the side of Vitellius, the army of Vespasian had left Narnia, and was passing the holiday of the Saturnalia in idleness at Ocriculum. The reason alleged for so injurious a delay was that they might wait for Mucianus. Some persons indeed there were who assailed Antonius with insinuations, that he lingered with treacherous intent, after receiving private letters from Vitellius, which conveyed to him the offer of the consulship and of the Emperor's daughter in marriage with a vast dowry, as the price of treason. Others asserted that this was all a fiction, invented to please Mucianus. Some again alleged that the policy agreed upon by all the generals was to threaten rather than actually to attack the capital, as Vitellius' strongest cohorts had revolted from him, and it seemed likely that, deprived of all support, he would abdicate the throne, but that the whole plan was ruined by the impatience and subsequent cowardice of Sabinus, who, after rashly taking up arms, had not been able to defend against three cohorts the great stronghold of the Capitol, which might have defied even the mightiest armies. One cannot, however, easily fix upon one man the blame which belongs to all. Mucianus did in fact delay the conquerors by ambig- uously-worded dispatches; Antonius, by a perverse acquiescence, or by an attempt to throw the odium upon another, laid himself open to blame; the other generals, by imagining that the war was over, contrived a distinction for its closing scene. Even Petilius Cerialis, though he had been sent on with a thousand cavalry by cross roads through the Sabine district so as to enter Rome by the Via Salaria, had not been sufficiently prompt in his movements, when the report of the siege of the Capitol put all alike on the alert.[^819c88b57f394bee9ca395402576b32c]

Virgil departed from Ocriculum, intending to travel by road to Narnia, a 8.118212115 mile journey. 

### A story about Narnia by Cornelius Tacitus



Antonius marched by the Via Flaminia, and arrived at Saxa Rubra, when the night was far spent, too late to give any help. There he received nothing but gloomy intelligence, that Sabinus was dead, that the Capitol had been burnt to the ground, that Rome was in consternation, and also that the populace and the slaves were arming themselves for Vitellius. And Petilius Cerialis had been defeated in a cavalry skirmish. While he was hurrying on without caution, as against a vanquished enemy, the Vitellianists, who had disposed some infantry among their cavalry, met him. The conflict took place not far from the city among buildings, gardens, and winding lanes, which were well known to the Vitellianists, but disconcerting to their opponents, to whom they were strange. Nor indeed were all the cavalry one in heart, for there were with them some who had lately capitulated at Narnia, and who were anxiously watching the fortunes of the rival parties. Tullius Flavianus, commanding a squadron, was taken prisoner; the rest fled in disgraceful confusion, but the victors did not continue the pursuit beyond Fidenæ.[^a3e0b53dfdd7443080337ee6ae04e4c4]

Virgil departed from Narnia, intending to travel by road to Spoletium, a 22.863967316 mile journey. 

### A story about Spoletium by Suetonius ca. 69-ca. 122



THE empire, which had been long thrown into a disturbed and unsettled state, by the rebellion and violent death of its three last rulers, was at length restored to peace and security by the Flavian family, whose descent was indeed obscure, and which boasted no ancestral honours; but the public had no cause to regret its elevation; though it is acknowledged that Domitian met with the just reward of his avarice and cruelty. Titus Flavius Petro, a townsman of Reate,^[Reate, the original seat of the Flavian family, was a city of the Sabines. Its present name is Rieti. ] whether a centurion or an _evocatus_^[It does not very clearly appear what rank in the Roman armies was held by the evocati. They are mentioned on three occasions by Suetonius, without affording us much assistance. Caesar, like our author, joins them with the centurions. See, in particular, De Bell. Civil. I. xvii. 4. ] of Pompey's party in the civil war, is uncertain, fled out of the battle of Pharsalia and went home; where, having at last obtained his pardon and discharge, he became a collector of the money raised by public sales in the way of auction. His son, surnamed Sabinus, was never engaged in the military service, though some say he was a centurion of the first order, and others, that whilst he held that rank, he was discharged on account of his bad state of health: this Sabinus, I say, was a republican, and received the tax of the fortieth penny in Asia. And there were remaining, at the time of the advancement of the family, several statues, which had been erected to him by the cities of that province, with this inscription: "To the honest Tax-farmer."^[The inscription was in Greek, \rendergreek{καλῶς τελωθήσαντι}] He afterwards turned usurer amongst the Helvetii, and there died, leaving behind him his wife, Vespasia Polla, and two sons by her; the elder of whom, Sabinus, came to be prefect of the city, and the younger, Vespasian, to be emperor. Polla, descended of a good family, at Nursia,^[In the ancient Umbria. afterwards the duchy of Spoleto; its modern name being Norcia.] had for her father Vespasius Pollio, thrice appointed military tribune, and at last prefect of the camp; and her brother was a senator of praetorian dignity. There is to this day, about six miles from Nursia, on the road to Spoletum, a place on the summit of a hill, called Vespasize, where are several monuments of the Vespasii, a sufficient proof of the splendour and antiquity of the family. I will not deny that some have pretended to say. that Petro's father was a native of Gallia Transpadana,^[Gaul beyond, north of, the Po, now Lombardy. ] whose employment was to hire work-people who used to emigrate every year from the country of the Umbria into that of the Sabines, to assist them in their husbandry;^[We find the annual migration of labourers in husbandry a very common practice in ancient as well as in modern times. At present, several thousand industrious labourers cross over every summer from the duchies of Parma and Modena, bordering on the district mentioned by Suetonius, to the island of Corsica; returning to the continent when the harvest is got in. ] but who settled at last in the town of Reate, and there married. But of this I have not been able to discover the least proof, upon the strictest inquiry.[^aee569ab52c1454d9e0ef568a8ef8f4c]

Virgil departed from Spoletium, intending to travel by road to Fanum Fortunae, a 90.170252665 mile journey. 

### The story of Fanum Fortunae



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

10\. Thus the gable tops run in two directions, like the letter T, and give a beautiful effect to the outside and inside of the main roof. Further, by the omission of an ornamental entablature and of a line of screens and a second tier of columns, troublesome labour is saved and the total cost greatly diminished. On the other hand, the carrying of the columns themselves in unbroken height directly up to the beams that support the main roof, seems to add an air of sumptuousness and dignity to the work.[^9eb46fe6b5e141758a35e09ed9be95c7]

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ariminum, a 38.157771739 mile journey. 

### The story of Ariminum



  
Such were the hidden motives of the chiefs;  
But in the public life the seeds of war  
Their hold had taken, such as are the doom  
Of potent nations: and when fortune poured  
Through Roman gates the booty of a world,  
The curse of luxury, chief bane of states,  
Fell on her sons. Farewell the ancient ways!  
Behold the pomp profuse, the houses decked  
With ornament; their hunger loathed the food  
Of former days; men wore attire for dames  
Scarce fitly fashioned; poverty was scorned,  
Fruitful of warriors; and from all the world  
Came that which ruins nations; while the fields  
Furrowed of yore by great Camillus' plough,  
Or by the mattock which a Curius held,  
Lost their once narrow bounds, and widening tracts  
By hinds unknown were tilled. No nation this  
To sheathe the sword, with tranquil peace content  
And with her liberties; but prone to ire;  
Crime holding light as though by want compelled:  
Great was the glory in the minds of men,  
Ambition lawful even at point of sword,  
To rise above their country: might their law:  
Decrees were forced from Senate and from Plebs:  
Consul and Tribune broke the laws alike:  
Bought were the fasces, and the people sold  
For gain their favour: bribery's fatal curse  
Stained every yearly contest of the Field.  
Then covetous usury rose, and interest  
Was greedier with the seasons; and all trust  
Was crushed; and many found a boon in war.  
Caesar has crossed the Alps, his mighty soul  
Great tumults pondering and the coming shock.  
Now on the marge of Rubicon, he saw,  
In face most sorrowful and ghostly guise,  
His trembling country's image; huge it seemed  
Through mists of night obscure; and hoary hair  
Streamed from the lofty front with turrets crowned:  
Torn were her locks and naked were her arms.  
Then thus, with broken sighs the Vision spake:  
What seek ye, men of Rome? and whither hence  
Bear ye my standards? If by right ye come,  
My citizens, stay here; these are the bounds;  
No further dare.' But Caesar's hair was stiff  
With horror as he gazed, and ghastly dread  
Restrained his footsteps on the further bank.  
Then spake he, ' Thunderer, who from the rock  
Tarpeian seest the wall of mighty Rome;  
Gods of my race who watched o'er Troy of old;  
Thou Jove of Alba's height, and Vestal fires,  
And rites of Romulus erst rapt to heaven,  
And God-like Rome; be friendly to my quest.  
Not with offence or hostile arms I come,  
Thy Caesar, conqueror by land and sea,  
Thy soldier here and wheresoe'er thou wilt:  
No other's; his, his only be the guilt  
Whose acts make me thy foe.' He gives the word  
And bids his standards cross the swollen stream.  
So in the wastes of Afric's burning clime  
The lion crouches as his foes draw near,  
Feeding his wrath the while, his lashing tail  
Provokes his fury; stiff upon his neck  
Bristles his mane: deep from his gaping jaws  
Resounds the muttered growl, and should a lance  
Or javelin reach him from the hunter's ring,  
Scorning the puny scratch he bounds afield.  
From modest fountain blood-red Rubicon  
In summer's heat flows on; his pigmy tide  
Creeps through the valleys and with slender marge  
Divides the Italian peasant from the Gaul.  
Then winter gave him strength, and fraught with rain  
The third day's crescent moon; while Eastern winds  
Thawed from the Alpine slopes the yielding snow.  
The cavalry first form across the stream  
To break the torrent's force; the rest with ease  
Beneath their shelter gain the further bank.  
When Caesar crossed and trod beneath his feet  
The soil of Italy's forbidden fields,  
Here,' spake he, 'peace, here broken laws be left;  
Farewell to treaties. Fortune, lead me on;  
War is our judge, and in the fates our trust.'  
Then in the shades of night he leads the troops  
Swifter than Balearic sling or shaft  
Winged by retreating Parthian, to the walls  
Of threatened Rimini, while fled the stars,  
Save Lucifer, before the coming sun,  
Whose fires were veiled in clouds, by south wind driven,  
Or else at heaven's command: and thus drew on  
The first dark morning of the civil war.  
Now stood the troops within the captured town,  
Their standards planted; and the trumpet clang  
Rang forth in harsh alarums, giving note  
Of impious strife: roused from their sleep the men  
Rushed to the hall and snatched the ancient arms  
Long hanging through the years of peace; the shield  
With crumbling frame; dark with the tooth of rust  
Their swords;^[Marlowe has it: ' ... And swords With ugly teeth of black rust foully scarred.'] and javelins with blunted point.  
' ... And swords  
With ugly teeth of black rust foully scarred.'  
But when the well-known signs and eagles shone,  
And Caesar towering o'er the throng was seen,  
They shook for terror, fear possessed their limbs,  
And thoughts unuttered stirred within their souls.  
O miserable those to whom their home  
Denies the peace that all men else enjoy!  
Placed as we are beside the Northern bounds  
And scarce a footstep from the restless Gaul,  
We fall the first; would that our lot had been  
Beneath the Eastern sky, or frozen North,  
To lead a wandering life, rather than keep  
' The gates of Latium. Brennus sacked the town  
' And Hannibal, and all the Teuton hosts.  
' This is the path when Rome's the prize of war.'  
Deep in their breasts they breathed the silent moan;  
But dared not speak their sorrow nor their fear.  
As when in winter all the fields are still,  
And birds are voiceless, and no murmured sound  
Breaks on the silence of the central sea;  
So deep the stillness. But when through the shades  
The day had broken, lo! the torch of war!  
For by the hand of Fate is swift dispersed  
All Caesar's shame of battle, and his mind  
Scarce doubted more; and Fortune toiled to make  
His action just and give him cause for arms.  
For while Rome wavered and her patriots' names  
Were loud and frequent in the mouths of men,  
The Senate angered and in scorn of right^[In the Senate, Curio had proposed and carried a resolution that Pompeius and Caesar should lay their arms down simultaneously: but this was resisted by the Oligarchal party, who endeavoured, though unsuccessfully, to expel Curio from the Senate, and who placed Pompeius in command of the legions at Capua. This was in effect a declaration of war; and Curio, after a last attempt at resistance, left the city, and betook himself to Caesar. (See the close of Book IV.)]  
Drove out the Tribunes who withstood their will.  
To Caesar's troops already on the march  
They haste with Curio, who in former days  
With bold and venal tongue had dared to speak  
For Freedom, and to voice the people's wrongs,  
And summon to their side the chiefs in arms.  
Who, when he saw that Caesar doubted still,  
Spake out; ' So long as I the rostrum held  
' By this my voice against the Senate's will  
' Was thy command prolonged, and to thy side  
' By me were drawn the wavering men of Rome.  
' Mute now are laws in war; we from our hearths  
Are driven, yet willing exiles; for thine arms  
Shall make us citizens of Rome again.  
'Strike;^['Strike.' Dante places Curio in the ninth gulf of hell, 'from whose throat was cut the tongue which spake that hardy word.'-' Inferno,' xxviii.98 (Cary).] for no strength as yet the foe hath gained.  
'To pause when ready is to court defeat:  
'Like risk, like labour, thou hast known before,  
'But never such reward. Could Gallia hold  
'Thine armies ten long years ere victory came,  
'That little nook of earth? One paltry fight  
'Or twain, fought out by thy resistless hand,  
'And Rome for thee shall have subdued the world:  
'Tis true no triumph now would bring thee home;  
'No captive tribes would grace thy chariot wheels  
'Winding in pomp around the ancient hill:  
'Spite, gnawing spite, denies thee all thy due;  
For all thy conquests, for a world well won  
'Scarce shalt thou go unpunished. Yet 'tis fate  
'Thou should'st subdue thy kinsman: share the world  
'With him thou canst not; rule thou canst, alone.'  
[^b74f5ea9089d417c9a622abfb7a25bbd]

Virgil departed from Ariminum, intending to travel by ship down the coast to Fanum Fortunae, a 38.157771739 mile journey. 

### A story about Fanum Fortunae



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

17\. The leaves of these trees are like those of the pine; timber from them comes in long lengths, is as easily wrought in joiner's work as is the clearwood of fir, and contains a liquid resin, of the colour of Attic honey, which is good for consumptives. With regard to the different kinds of timber, I have now explained of what natural properties they appear to be composed, and how they were produced. It remains to consider the question why the highland fir, as it is called in Rome, is inferior, while the lowland fir is extremely useful in buildings so far as durability is concerned; and further to explain how it is that their bad or good qualities seem to be due to the peculiarities of their neighbourhood, so that this subject may be clearer to those who examine it.[^54d888bdd7bd4a51b335b421f7a0554d]

Virgil departed from Fanum Fortunae, intending to travel by ship down the coast to Ancona, a 42.411056234 mile journey. 

### The story of Ancona



  
Soon as the sun dispelled the chilly night,  
The sounding doors flew wide, and from the tomb  
Of dead Hortensius grieving Marcia came.^[Marcia was first married to Cato, and bore him three sons; he then yielded her to Hortensius. On his death she returned to Cato. (Plutarch, 'Cato,' 25, 52.) It was in reference to this that Caesar charged him with making a traffic of his marriage; but Plutarch says 'to accuse Cato of filthy lucre is like upbraiding Hercules with cowardice.' After the marriage Marcia remained at Rome while Cato hurried after Pompeius.]  
First joined in wedlock to a greater man  
Three children did she bear to grace his home:  
Then Cato to Hortensius gave the dame  
To be a fruitful mother of his sons  
And join their houses in a closer tie.  
And now the last sad offices were done  
She came with hair dishevelled, beaten breast,  
And ashes on her brow, and features worn  
With grief; thus only pleasing to the man.  
' When youth was in me and maternal power  
' I did thy bidding, Cato, and received  
' A second husband: now in years grown old  
' Ne'er to be parted I return to thee.  
' Renew our former pledges undefiled:  
' Give back the name of wife: upon my tomb  
' Let " Marcia, spouse to Cato," be engraved.  
' Nor let men question in the time to come,  
' Didst thou compel, or did I willing leave  
' My first espousals. Not in happy times,  
' Partner of joys, I come; but days of care  
' And labour shall be mine to share with thee.  
' Nor leave me here, but take me to the camp,  
' Thy fond companion: why should Magnus' wife  
' Be nearer, Cato, to the wars than thine?'  
Although the times were warlike and the fates  
Called to the fray, he lent a willing ear.  
Yet must they plight their faith in simple form  
Of law; their witnesses the gods alone.  
No festal wreath of flowers crowned the gate  
Nor glittering fillet on each post entwined;  
No flaming torch was there, nor ivory steps,  
No couch with robes of broidered gold adorned;  
No comely matron placed upon her brow  
The bridal garland, or forbad the foot^[The bride was carried over the threshold of her new home, for to stumble on it would be of evil omen. Plutarch ('Romulus') refers this custom to the rape of the Sabine women, who were 'so lift up and carried away by force.' (North, volume i., p. 88, Edition by Windham.) I have read vetuit in this passage, though vitat appears to be a better variation according to the manuscripts.]  
To touch the threshold stone; no saffron veil  
Concealed the timid blushes of the bride;  
No jewelled belt confined her flowing robe^[The bride was dressed in a long white robe, bound round the waist with a girdle. She had a veil of bright yellow colour. ('Dict. Antiq.')]  
Nor modest circle bound her neck; no scarf  
Hung lightly on the snowy shoulder's edge  
Around the naked arm. Just as she came,  
Wearing the garb of sorrow, while the wool  
Covered the purple border of her robe,  
Thus was she wedded. As she greets her sons  
She greets her husband. Nor, in Sabine use  
Did mournful Cato share the festal taunt:  
Nor friend nor foe was bidden : silent both  
They joined in marriage, yet content, unseen  
By any save by Brutus. Sad and stern  
On Cato's lineaments the marks of grief  
Were still unsoftened, and the hoary hair  
Hung o'er his reverend visage; for since first  
Men flew to arms, his locks were left unkempt  
To stream upon his brow, and on his chin  
His beard untended grew. 'Twas his alone  
Who hated not, nor loved, for all mankind  
To mourn alike. Nor did their former couch  
Again receive them, for his lofty soul  
E'en lawful love resisted. 'Twas his rule^['I know not three wiser precepts for the conduct either of princes or private men.' Sir W. Temple, i. 184, quoting this passage.]  
Inflexible, to keep the middle path  
Marked out and bounded; to observe the laws  
Of natural right; and for his country's sake  
To risk his life, his all, as not for self  
Brought into being, but for all the world:  
Such was his creed. To him a sumptuous feast  
Was hunger conquered, and the lowly hut,  
Which scarce kept out the winter, was a home  
Equal to palaces: a robe of price  
Such hairy garments as were worn of old:  
The end of marriage, offspring. To the State  
Father alike and husband, right and law  
He ever followed with unswerving step:  
No thought of selfish pleasure turned the scale  
In Cato's acts, or swayed his upright soul.  
Meanwhile Pompeius led his trembling host  
To fields Campanian, and held the walls  
First founded by the chief of Trojan race.  
These chose he for the central seat of war,  
Some troops despatching who might meet the foe  
Where shady Apennine lifts up the ridge  
Of mid Italia; nearest to the sky  
Upsoaring, with the seas on either hand,  
The upper and the lower. Pisa's sands  
Breaking the margin of the Tuscan deep,  
Here bound his mountains: there Ancona's towers  
Laved by Dalmatian waves. Rivers immense,  
In his recesses born, pass on their course,  
To either sea diverging. To the left  
Metaurus and Crustumium's torrent fall  
And Sena's streams and Aufidus who bursts  
On Adrian billows; and that mighty flood  
Which, more than all the rivers of the earth,  
Sweeps down the soil and tears the woods away  
And drains Hesperia's springs. In fabled lore  
His banks were first by poplar shade enclosed:^[Phaethon's sisters, who yoked the horses of the Sun to the chariot for their brother, were turned into poplars. Phaethon was flung by Jupiter into the river Po.]  
And when by Phaethon the waning day  
Was drawn in path transverse, and all the heaven  
Blazed with his car aflame, and from the depths  
Of inmost earth were rapt all other floods,  
Padus still rolled in pride of stream along.  
Nile were no larger, but that o'er the sand  
Of level Egypt he spreads out his waves;  
Nor Ister, if he sought the Scythian main  
Unhelped upon his journey through the world  
By tributary waters not his own.  
But on the right hand Tiber has his source,  
Deep-flowing Rutuba, Vulturnus swift,  
And Sarnus breathing vapours of the night^[Sarnus, site of the battle in which Narses defeated Teias, the last of the Ostrogoths, in 553 A.D.]  
Rise there, and Liris with Vestinian wave  
Still gliding through Marica's shady grove,  
And Siler flowing through Salernian meads:  
And Macra's swift unnavigable stream  
Near Luna rests in Ocean. On the Alps  
Whose spurs strike plainwards, and on fields of Gaul  
The cloudy heights of Apennine look down  
In further distance: on his nearer slopes  
The Sabine turns the ploughshare; Umbrian kine  
And Marsian fatten; with his pineclad rocks  
He girds the tribes of Latium, nor leaves  
Hesperia's soil until the waves that beat  
On Scylla's cave compel. His southern spurs  
Extend to Juno's temple, and of old  
Stretched further than Italia, till the main  
O'erstepped his limits and the lands repelled.  
But, when the seas were joined, Pelorus claimed  
His latest summits for Sicilia's isle.  
[^86b1b0349f604b65a955ea8cb3bde597]

Virgil departed from Ancona, intending to travel by ship down the coast to Iader, a 107.75815881999999 mile journey. 

### On the subject of the countryside near that place



But why do I wonder? when, having taken a bribe, you ravaged Pessinus itself, the habitation and home of the mother of the gods, and sold to Brogitarus—a fellow half Gaul, half Greek, a profligate and impious man, whose agents, while you were tribune, used to pay you the money for your share of the work in the temple of Castor—the whole of that place and the temple; when you dragged the priest from the very altar and cushion of the goddess; when you perverted those omens which all antiquity, which Persians, and Syrians, and all kings who have ever reigned in Europe and Asia have always venerated with the greatest piety; which, last of all; our own ancestors considered so sacred, that though we had the city and all Italy crowded with temples, still our generals in our most important and most perilous wars used to offer their vows to this goddess, and to pay them in Pessinus itself, at that identical principal altar and on that spot and in that temple.

[^bf0bf1b9e5d24c15931f1fdc24d464c1]

Virgil departed from Iader, intending to travel by ship down the coast to Titius (river), a 48.512298083 mile journey. 

### A story about Salona



  
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
[^9d9abfdddf114d17bfa7364da69f0be6]

Virgil departed from Titius (river), intending to travel by ship down the coast to Iader, a 48.512298083 mile journey. 

### On the subject of Salona



Caesar having landed his troops, sent the fleet back the same night to Brundusium, to bring over his other legions and cavalry. Fufius Kalenus, lieutenant-general, had the charge of this expedition, with orders to use the utmost despatch. But setting sail too late, he lost the benefit of the wind, which offered fair all night, and fell in with the enemy. For Bibulus hearing at Corcyra of Caesar's arrival, forthwith put to sea, in hopes of intercepting some of the transports; and meeting the fleet as it returned empty, took about thirty ships, which he immediately burned, with all that were on board; partly to satisfy his own vengeance for the disappointment he had received; partly to deter the rest of the troops from attempting the passage. He then stationed his fleet along the coast, from Salona to Oricum, guarded all places with extraordinary care, and even lay himself aboard, notwithstanding the rigour of the winter; declining no danger nor fatigue, and solely intent upon intercepting Caesar's supplies.[^0d31b69a9e3e4ef9a3f676ed61aa0993]

Virgil departed from Iader, intending to travel by road to Burnum, a 40.332570239000006 mile journey. 

### On the subject of Salona



After the mouth of the Silaris one comes to Leucania, and to the temple of the Argoan Hera, built by Jason, and near by, within fifty stadia, to Poseidonia. Thence, sailing out past the gulf, one comes to Leucosia,^[Now Licosa.] an island, from which it is only a short voyage across to the continent. The island is named after one of the Sirens, who was cast ashore here after the Sirens had flung themselves, as the myth has it, into the depths of the sea. In front of the island lies that promontory^[Poseidium, now Punta Della Licosa.] which is opposite the Sirenussae and with them forms the Poseidonian Gulf. On doubling this promontory one comes immediately to another gulf, in which there is a city which was called "Hyele" by the Phocaeans who founded it, and by others "Ele," after a certain spring, but is called by the men of today "Elea." This is the native city of Parmenides and Zeno, the Pythagorean philosophers. It is my opinion that not only through the influence of these men but also in still earlier times the city was well governed; and it was because of this good government that the people not only held their own against the Leucani and the Poseidoniatae, but even returned victorious, although they were inferior to them both in extent of territory and in population. At any rate, they are compelled, on account of the poverty of their soil, to busy themselves mostly with the sea and to establish factories for the salting of fish, and other such industries. According to Antiochus,^[Antiochus Syracusanus, the historian. Cp. Hdt. 1.167] after the capture of Phocaea by Harpagus, the general of Cyrus, all the Phocaeans who could do so embarked with their entire families on their light boats and, under the leadership of Creontiades, sailed first to Cyrnus and Massalia, but when they were beaten off from those places founded Elea. Some, however, say that the city took its name from the River Elees.^[The Latin form is "Hales" (now the Alento).] It is about two hundred stadia distant from Poseidonia. After Elea comes the promontory of Palinurus. Off the territory of Elea are two islands, the Oenotrides, which have anchoring-places. After Palinurus comes Pyxus—a cape, harbor, and river, for all three have the same name. Pyxus was peopled with new settlers by Micythus, the ruler of the Messene in Sicily, but all the settlers except a few sailed away again. After Pyxus comes another gulf, and also Laüs—a river and city; it is the last of the Leucanian cities, lying only a short distance above the sea, is a colony of the Sybaritae, and the distance thither from Ele is four hundred stadia. The whole voyage along the coast of Leucania is six hundred and fifty stadia. Near Laüs is the hero-temple of Draco, one of the companions of Odysseus, in regard to which the following oracle was given out to the Italiotes:^[The Greek inhabitants of Italy were called "Italiotes."] Much people will one day perish about Laïan Draco.^[There is a word-play here which cannot be brought out in translation: the word for "people" in Greek is "laos."] And the oracle came true, for, deceived by it, the peoples^[Literally, "laoi."] who made campaigns against Laüs, that is, the Greek inhabitants of Italy, met disaster at the hands of the Leucani. These, then, are the places on the Tyrrhenian seaboard that belong to the Leucani. As for the other sea,^[The Adriatic.] they could not reach it at first; in fact, the Greeks who held the Gulf of Tarentum were in control there. Before the Greeks came, however, the Leucani were as yet not even in existence, and the regions were occupied by the Chones and the Oenotri. But after the Samnitae had grown considerably in power, and had ejected the Chones and the Oenotri, and had settled a colony of Leucani in this portion of Italy, while at the same time the Greeks were holding possession of both seaboards as far as the Strait, the Greeks and the barbarians carried on war with one another for a long time. Then the tyrants of Sicily, and afterwards the Carthaginians, at one time at war with the Romans for the possession of Sicily and at another for the possession of Italy itself, maltreated all the peoples in this part of the world, but especially the Greeks. Later on, beginning from the time of the Trojan war, the Greeks had taken away from the earlier inhabitants much of the interior country also, and indeed had increased in power to such an extent that they called this part of Italy, together with Sicily, Magna Graecia. But today all parts of it, except Taras,^[The old name of Tarentum.] Rhegium, and Neapolis, have become completely barbarized,^["Barbarized," in the sense of "non-Greek" (cp. 5. 4. 4 and 5. 4. 7).] and some parts have been taken and are held by the Leucani and the Brettii, and others by the Campani—that is, nominally by the Campani but in truth by the Romans, since the Campani themselves have become Romans. However, the man who busies himself with the description of the earth must needs speak, not only of the facts of the present, but also sometimes of the facts of the past, especially when they are notable. As for the Leucani, I have already spoken of those whose territory borders on the Tyrrhenian Sea, while those who hold the interior are the people who live above the Gulf of Tarentum. But the latter, and the Brettii, and the Samnitae themselves (the progenitors of these peoples) have so utterly deteriorated that it is difficult even to distinguish their several settlements; and the reason is that no common organization longer endures in any one of the separate tribes; and their characteristic differences in language, armor, dress, and the like, have completely disappeared; and, besides, their settlements, severally and in detail, are wholly without repute. Accordingly, without making distinctions between them, I shall only tell in a general way what I have learned about the peoples who live in the interior, I mean the Leucani and such of the Samnitae as are their next neighbors. Petelia, then, is regarded as the metropolis of the Chones, and has been rather populous down to the present day. It was founded by Philoctetes after he, as the result of a political quarrel, had fled from Meliboea. It has so strong a position by nature that the Samnitae once fortified it against the Thurii. And the old Crimissa, which is near the same regions, was also founded by Philoctetes. Apollodorus, in his work On Ships,^[That is, his work entitled "On the (Homeric) Catalogue of Ships" (cp. 1. 2. 24).] in mentioning Philoctetes, says that, according to some, when Philoctetes arrived at the territory of Croton, he colonized the promontory Crimissa, and, in the interior above it, the city Chone, from which the Chonians of that district took their name, and that some of his companions whom he had sent forth with Aegestes the Trojan to the region of Eryx in Sicily fortified Aegesta.^[Also spelled Segesta and Egesta.] Moreover, Grumentum and Vertinae are in the interior, and so are Calasarna and some other small settlements, until we arrive at Venusia, a notable city; but I think that this city and those that follow in order after it as one goes towards Campania are Samnite cities. Beyond Thurii lies also the country that is called Tauriana. The Leucani are Samnite in race, but upon mastering the Poseidoniatae and their allies in war they took possession of their cities. At all other times, it is true, their government was democratic, but in times of war they were wont to choose a king from those who held magisterial offices. But now they are Romans. The seaboard that comes next after Leucania, as far as the Sicilian Strait and for a distance of thirteen hundred and fifty stadia, is occupied by the Brettii. According to Antiochus, in his treatise On Italy, this territory (and this is the territory which he says he is describing) was once called Italy, although in earlier times it was called Oenotria. And he designates as its boundaries, first, on the Tyrrhenian Sea, the same boundary that I have assigned to the country of the Brettii—the River Laüs; and secondly, on the Sicilian Sea, Metapontium. But as for the country of the Tarantini, which borders on Metapontium, he names it as outside of Italy, and calls its inhabitants Iapyges. And at a time more remote, according to him, the names "Italians" and "Oenotrians" were applied only to the people who lived this side the isthmus in the country that slopes toward the Sicilian Strait. The isthmus itself, one hundred and sixty stadia in width, lies between two gulfs—the Hipponiate (which Antiochus has called Napetine) and the Scylletic. The coasting-voyage round the country comprised between the isthmus and the Strait is two thousand stadia. But after that, he says, the name of "Italy" and that of the "Oenotrians" was further extended as far as the territory of Metapontium and that of Seiris, for, he adds, the Chones, a well-regulated Oenotrian tribe, had taken up their abode in these regions and had called the land Chone. Now Antiochus had spoken only in a rather simple and antiquated way, without making any distinctions between the Leucani and the Brettii. In the first place, Leucania lies between the Tyrrhenian and Sicilian coastlines,^[Between the coastlines on the Tyrrhenian and Sicilian Seas.] the former coastline from the River Silaris as far as Laüs, and the latter, from Metapontium as far as Thurii; in the second place, on the mainland, from the country of the Samnitae as far as the isthmus which extends from Thurii to Cerilli (a city near Laüs), the isthmus is three hundred stadia in width. But the Brettii are situated beyond the Leucani; they live on a peninsula, but this peninsula includes another peninsula which has the isthmus that extends from Scylletium to the Hipponiate Gulf. The name of the tribe was given to it by the Leucani, for the Leucani call all revolters "brettii." The Brettii revolted, so it is said (at first they merely tended flocks for the Leucani, and then, by reason of the indulgence of their masters, began to act as free men), at the time when Rio made his expedition against Dionysius and aroused all peoples against all others. So much, then, for my general description of the Leucani and the Brettii. The next city after Laüs belongs to Brettium, and is named Temesa, though the men of today call it Tempsa; it was founded by the Ausones, but later on was settled also by the Aetolians under the leadership of Thoas; but the Aetolians were ejected by the Brettii, and then the Brettii were crushed by Hannibal and by the Romans. Near Temesa, and thickly shaded with wild olive trees, is the hero-temple of Polites, one of the companions of Odysseus, who was treacherously slain by the barbarians, and for that reason became so exceedingly wroth against the country that, in accordance with an oracle, the people of the neighborhood collected tribute^[According to Paus. 6.6.2 the oracle bade the people annually to give the hero to wife the fairest maiden in Temesa.] for him; and hence, also, the popular saying applied to those who are merciless,^["Merciless" is an emendation. Some read "disagreeable." According to Aelian Var. Hist. 8.18, the popular saying was applied to those who in pursuit of profit overreached themselves (so Plutarch Prov. 31). But Eustathius (note on Iliad 1.185) quotes "the geographer" (i.e., Strabo; see note 1, p. 320) as making the saying apply to "those who are unduly wroth, or very severe when they should not be."] that they are "beset by the hero of Temesa." But when the Epizephyrian Locrians captured the city, Euthymus, the pugilist, so the story goes, entered the lists against Polites, defeated him in the fight and forced him to release the natives from the tribute. People say that Homer has in mind this Temesa, not the Tamassus in Cyprus (the name is spelled both ways), when he says "to Temesa, in quest of copper."^[Hom. Od. 1.184] And in fact copper mines are to be seen in the neighborhood, although now they have been abandoned. Near Temesa is Terina, which Hannibal destroyed, because he was unable to guard it, at the time when he had taken refuge in Brettium itself. Then comes Consentia, the metropolis of the Brettii; and a little above this city is Pandosia, a strong fortress, near which Alexander the Molossian^[Cp. 6. 3. 4 and footnote.] was killed. He, too, was deceived by the oracle^[The oracle, quoted by Casaubon from some source unknown to subsequent editors was:\rendergreek{Αἰακίδη, προφύλαξο μολεῖν Α᾿χερούσιον ὕδωρ}\rendergreek{Πανδοσίην δ᾽ ὅθι τοι θάνατος πεπρωμένος ἐστί}Source unknown. "Son of Aeacus, beware to go to the Acherusian water and Pandosia, where it is fated you will die."] at Dodona, which bade him be on his guard against Acheron and Pandosia; for places which bore these names were pointed out to him in Thesprotia, but he came to his end here in Brettium. Now the fortress has three summits, and the River Acheron flows past it. And there was another oracle that helped to deceive him: Three-hilled Pandosia, much people shalt thou kill one day; for he thought that the oracle clearly meant the destruction of the enemy, not of his own people. It is said that Pandosia was once the capital of the Oenotrian Kings. After Consentia comes Hipponium, which was founded by the Locrians. Later on, the Brettii were in possession of Hipponium, but the Romans took it away from them and changed its name to Vibo Valentia. And because the country round about Hipponium has luxuriant meadows abounding in flowers, people have believed that Core^[i.e., Persephone.] used to come hither from Sicily to gather flowers; and consequently it has become the custom among the women of Hipponium to gather flowers and to weave them into garlands, so that on festival days it is disgraceful to wear bought garlands. Hipponium has also a naval station, which was built long ago by Agathocles, the tyrant of the Siciliotes,^[The "Siciliotes" were Sicilian Greeks, as distinguished from native Sicilians.] when he made himself master of the city. Thence one sails to the Harbor of Heracles,^[Now Tropea. But in fact the turn towards the west begins immediately after Hipponium.] which is the point where the headlands of Italy near the Strait begin to turn towards the west. And on this voyage one passes Medma, a city of the same Locrians aforementioned, which has the same name as a great fountain there, and possesses a naval station near by, called Emporium. Near it is also the Metaurus River, and a mooring-place bearing the same name. Off this coast lie the islands of the Liparaei, at a distance of two hundred stadia from the Strait. According to some, they are the islands of Aeolus, of whom the Poet makes mention in the Odyssey.^[Hom. Od. 10.2ff] They are seven in number and are all within view both from Sicily and from the continent near Medma. But I shall tell about them when I discuss Sicily. After the Metaurus River comes a second Metaurus.^[Strabo's "Metaurus" and "second Metaurus" are confusing. Kramer, Meineke, and others wish to emend the text so as to make the "second" river refer to Crataeis or some other river. But we should have expected Strabo to mention first the Medma (now the Mesima), which was much closer to Medma than the Metaurus (now the Marro), and to which he does not refer at all. Possibly he thought both rivers were called Metaurus (cp. Müller, Ind. Var. Lectionis, p. 975), in which case "the second Metaurus" is the Metaurus proper. The present translator, however, believes that Strabo, when he says "second Metaurus," alludes to the Umbrian Metaurus (5. 2. 10) as the first, and that the copyist, unaware of this fact, deliberately changed "Medma" to Metaurus" in the two previous instances.] Next after this river comes Scyllaeum, a lofty rock which forms a peninsula, its isthmus being low and affording access to ships on both sides. This isthmus Anaxilaüs, the tyrant of the Rhegini, fortified against the Tyrrheni, building a naval station there, and thus deprived the pirates of their passage through the strait. For Caenys,^[Now Cape Cavallo.] too, is near by, being two hundred and fifty stadia distant from Medma; it is the last cape, and with the cape on the Sicilian side, Pelorias, forms the narrows of the Strait. Cape Pelorias is one of the three capes that make the island triangular, and it bends towards the summer sunrise,^[North-east (cp. 1. 2. 21).] just as Caenys bends towards the west, each one thus turning away from the other in the opposite direction. Now the length of the narrow passage of the Strait from Caenys as far as the Poseidonium,^[Altar or temple of Poseidon.] or the Columna Rheginorum, is about six stadia, while the shortest passage across is slightly more; and the distance is one hundred stadia from the Columna to Rhegium, where the Strait begins to widen out, as one proceeds towards the east, towards the outer sea, the sea which is called the Sicilian Sea. Rhegium was founded by the Chalcidians who, it is said, in accordance with an oracle, were dedicated, one man out of every ten Chalcidians, to Apollo,^[Cp. 6. 1. 9.] because of a dearth of crops, but later on emigrated hither from Delphi, taking with them still others from their home. But according to Antiochus, the Zanclaeans sent for the Chalcidians and appointed Antimnestus their founder-in-chief.^[Zancle was the original name of Messana (now Messina) in Sicily. It was colonized and named Messana by the Peloponnesian Messenians (6. 2. 3).] To this colony also belonged the refugees of the Peloponnesian Messenians who had been defeated by the men of the opposing faction. These men were unwilling to be punished by the Lacedaemonians for the violation of the maidens^[Cp. 6. 3. 3. and 8. 4. 9.] which took place at Limnae, though they were themselves guilty of the outrage done to the maidens, who had been sent there for a religious rite and had also killed those who came to their aid.^[Cp. Paus. 4.4.1] So the refugees, after withdrawing to Macistus, sent a deputation to the oracle of the god to find fault with Apollo and Artemis if such was to be their fate in return for their trying to avenge those gods, and also to enquire how they, now utterly ruined, might be saved. Apollo bade them go forth with the Chalcidians to Rhegium, and to be grateful to his sister; for, he added, they were not ruined, but saved, inasmuch as they were surely not to perish along with their native land, which would be captured a little later by the Spartans. They obeyed; and therefore the rulers of the Rhegini down to Anaxilas^[Anaxilas (also spelled Anaxilaüs) was ruler of Rhegium from 494 to 476 B.C. (Diod. Sic. 11.48).] were always appointed from the stock of the Messenians. According to Antiochus, the Siceli and Morgetes had in early times inhabited the whole of this region, but later on, being ejected by the Oenotrians, had crossed over into Sicily. According to some, Morgantium also took its name from the Morgetes of Rhegium.^[Cp. 6. 2. 4. The Latin name of this Sicilian city was "Murgantia." Livy 10.17 refers to another Murgantia in Samnium.] The city of Rhegium was once very powerful and had many dependencies in the neighborhood; and it was always a fortified outpost threatening the island, not only in earlier times but also recently, in our own times, when Sextus Pompeius caused Sicily to revolt. It was named Rhegium, either, as Aeschylus says, because of the calamity that had befallen this region, for, as both he and others state, Sicily was once "rent"^[Cp. 1. 3. 19 and the footnote on "rent."] from the continent by earthquakes, "and so from this fact," he adds, "it is called Rhegium." They infer from the occurrences about Aetna and in other parts of Sicily, and in Lipara and in the islands about it, and also in the Pithecussae and the whole of the coast of the adjacent continent, that it is not unreasonable to suppose that the rending actually took place. Now at the present time the earth about the Strait, they say, is but seldom shaken by earthquakes, because the orifices there, through which the fire is blown up and the red-hot masses and the waters are ejected, are open. At that time, however, the fire that was smouldering beneath the earth, together with the wind, produced violent earthquakes, because the passages to the surface were all blocked up, and the regions thus heaved up yielded at last to the force of the blasts of wind, were rent asunder, and then received the sea that was on either side, both here^[At the Strait.] and between the other islands in that region.^[Cp. 1. 3. 10 and the footnote.] And, in fact, Prochyte and the Pithecussae are fragments broken off from the continent, as also Capreae, Leucosia, the Sirenes, and the Oenotrides. Again, there are islands which have arisen from the high seas, a thing that even now happens in many places; for it is more plausible that the islands in the high seas were heaved up from the deeps, whereas it is more reasonable to think that those lying off the promontories and separated merely by a strait from the mainland have been rent therefrom. However, the question which of the two explanations is true, whether Rhegium got its name on account of this or on account of its fame (for the Samnitae might have called it by the Latin word for "royal,"^[Regium.] because their progenitors had shared in the government with the Romans and used the Latin language to a considerable extent), is open to investigation. Be this as it may, it was a famous city, and not only founded many cities but also produced many notable men, some notable for their excellence as statesmen and others for their learning; nevertheless, Dionysius^[Dionysius the Elder (b. about 432 B.C., d. 367 B.C.)] demolished it, they say, on the charge that when he asked for a girl in marriage they proffered the daughter of the public executioner;^[Diod. Sic. 14.44 merely says that the Assembly of the Rhegini refused him a wife.] but his son restored a part of the old city and called it Phoebia.^[Apparently in honor of Phoebus (Apollo); for, according to Plut. De Alexandri Virtute, (338) Dionysius the Younger called himself the son of Apollo, "offspring of his mother Doris by Phoebus."] Now in the time of Pyrrhus the garrison of the Campani broke the treaty and destroyed most of the inhabitants, and shortly before the Marsic war much of the settlement was laid in ruins by earthquakes; but Augustus Caesar, after ejecting Pompeius from Sicily, seeing that the city was in want of population, gave it some men from his expeditionary forces as new settlers, and it is now fairly populous. As one sails from Rhegium towards the east, and at a distance of fifty stadia, one comes to Cape Leucopetra^[Literally, "White Rock."] (so called from its color), in which, it is said, the Apennine Mountain terminates. Then comes Heracleium, which is the last cape of Italy and inclines towards the south; for on doubling it one immediately sails with the southwest wind as far as Cape Iapygia, and then veers off, always more and more, towards the northwest in the direction of the Ionian Gulf.^[The "Ionian Gulf" was the southern "part of what is now called the Adriatic Sea" (2. 5. 20); see 7. 5. 8-9.] After Heracleium comes a cape belonging to Locris, which is called Zephyrium; its harbor is exposed to the winds that blow from the west, and hence the name. Then comes the city Locri Epizephyrii,^[Literally, the "western Locrians," both city and inhabitants having the same name.] a colony of the Locri who live on the Crisaean Gulf,^[Now the Gulf of Salona in the Gulf of Corinth.] which was led out by Evanthes only a little while after the founding of Croton and Syracuse.^[Croton and Syracuse were founded, respectively, in 710 and 734 B.C. According to Diod. Sic. 4.24, Heracles had unintentionally killed Croton and had foretold the founding of a famous city on the site, the same to be named after Croton.] Ephorus is wrong in calling it a colony of the Locri Opuntii. However, they lived only three or four years at Zephyrium, and then moved the city to its present site, with the cooperation of Syracusans [for at the same time the latter, among whom . . .]^[The Greek text, here translated as it stands, is corrupt. The emendations thus far offered yield (instead of the nine English words of the above rendering) either (1) "for the latter were living" (or "had taken up their abode") "there at the same time" or (2) "together with the Tarantini." There seems to be no definite corroborative evidence for either interpretation; but according to Pausanias, "colonies were sent to Croton, and to Locri at Cape Zephyrium, by the Lacedaemonians" (3.3); and "Tarentum is a Lacedaemonian colony" (10. 10). Cp. the reference to the Tarantini in Strabo's next paragraph.] And at Zephyrium there is a spring, called Locria, where the Locri first pitched camp. The distance from Rhegium to Locri is six hundred stadia. The city is situated on the brow of a hill called Epopis. The Locri Epizephyrii are believed to have been the first people to use written laws. After they had lived under good laws for a very long time, Dionysius, on being banished from the country of the Syracusans,^[Dionysius the Younger was banished thence in 357 B.C.] abused them most lawlessly of all men. For he would sneak into the bed-chambers of the girls after they had been dressed up for their wedding, and lie with them before their marriage; and he would gather together the girls who were ripe for marriage, let loose doves with cropped wings upon them in the midst of the banquets, and then bid the girls waltz around unclad, and also bid some of them, shod with sandals that were not mates (one high and the other low), chase the doves around—all for the sheer indecency of it. However, he paid the penalty after he went back to Sicily again to resume his government; for the Locri broke up his garrison, set themselves free, and thus became masters of his wife and children. These children were his two daughters, and the younger of his two sons (who was already a lad), for the other, Apollocrates, was helping his father to effect his return to Sicily by force of arms. And although Dionysius—both himself and the Tarantini on his behalf—earnestly begged the Locri to release the prisoners on any terms they wished, they would not give them up; instead, they endured a siege and a devastation of their country. But they poured out most of their wrath upon his daughters, for they first made them prostitutes and then strangled them, and then, after burning their bodies, ground up the bones and sank them in the sea. Now Ephorus, in his mention of the written legislation of the Locri which was drawn up by Zaleucus from the Cretan, the Laconian, and the Areopagite usages, says that Zaleucus was among the first to make the following innovation—that whereas before his time it had been left to the judges to determine the penalties for the several crimes, he defined them in the laws, because he held that the opinions of the judges about the same crimes would not be the same, although they ought to be the same. And Ephorus goes on to commend Zaleucus for drawing up the laws on contracts in simpler language. And he says that the Thurii, who later on wished to excel the Locri in precision, became more famous, to be sure, but morally inferior; for, he adds, it is not those who in their laws guard against all the wiles of false accusers that have good laws, but those who abide by laws that are laid down in simple language. And Plato has said as much—that where there are very many laws, there are also very many lawsuits and corrupt practices, just as where there are many physicians, there are also likely to be many diseases.^[This appears to be an exact quotation, but the translator has been unable to find the reference in extant works. Plato utters a somewhat similar sentiment, however, in the Plat. Rep. 404e-405a] The Halex River, which marks the boundary between the Rhegian and the Locrian territories, passes out through a deep ravine; and a peculiar thing happens there in connection with the grasshoppers, that although those on the Locrian bank sing, the others remain mute. As for the cause of this, it is conjectured that on the latter side the region is so densely shaded that the grasshoppers, being wet with dew, cannot expand their membranes, whereas those on the sunny side have dry and horn-like membranes and therefore can easily produce their song. And people used to show in Locri a statue of Eunomus, the cithara-bard, with a locust seated on the cithara. Timaeus says that Eunomus and Ariston of Rhegium were once contesting with each other at the Pythian games and fell to quarrelling about the casting of the lots;^[Apparently as to which should perform first.] so Ariston begged the Delphians to cooperate with him, for the reason that his ancestors belonged^[Cp. 6. 1. 6.] to the god and that the colony had been sent forth from there;^[From Delphi to Rhegium.] and although Eunomus said that the Rhegini had absolutely no right even to participate in the vocal contests, since in their country even the grasshoppers, the sweetest-voiced of all creatures, were mute, Ariston was none the less held in favor and hoped for the victory; and yet Eunomus gained the victory and set up the aforesaid image in his native land, because during the contest, when one of the chords broke, a grasshopper lit on his cithara and supplied the missing sound. The interior above these cities is held by the Brettii; here is the city Mamertium, and also the forest that produces the best pitch, the Brettian. This forest is called Sila, is both well wooded and well watered, and is seven hundred stadia in length. After Locri comes the Sagra, a river which has a feminine name. On its banks are the altars of the Dioscuri, near which ten thousand Locri, with Rhegini,^[The Greek, as the English, leaves one uncertain whether merely the Locrian or the combined army amounted to 10,000 men. Justin 20.3 gives the number of the Locrian army as 15,000, not mentioning the Rhegini; hence one might infer that there were 5,000 Rhegini, and Strabo might have so written, for the Greek symbol for 5,000 (\rendergreek{,ε}), might have fallen out of the text.] clashed with one hundred and thirty thousand Crotoniates and gained the victory—an occurrence which gave rise, it is said, to the proverb we use with incredulous people, "Truer than the result at Sagra." And some have gone on to add the fable that the news of the result was reported on the same day^[Cicero De Natura Deorum 2.2 refers to this tradition.] to the people at the Olympia when the games were in progress, and that the speed with which the news had come was afterwards verified. This misfortune of the Crotoniates is said to be the reason why their city did not endure much longer, so great was the multitude of men who fell in the battle. After the Sagra comes a city founded by the Achaeans, Caulonia, formerly called Aulonia, because of the glen^["Aulon."] which lies in front of it. It is deserted, however, for those who held it were driven out by the barbarians to Sicily and founded the Caulonia there. After this city comes Scylletium, a colony of the Athenians who were with Menestheus (and now called Scylacium).^[Cp. Vergil Aen. 3.552] Though the Crotoniates held it, Dionysius included it within the boundaries of the Locri. The Scylletic Gulf, which, with the Hipponiate Gulf forms the aforementioned isthmus,^[6. 1. 4.] is named after the city. Dionysius undertook also to build a wall across the isthmus when he made war upon the Leucani, on the pretext, indeed, that it would afford security to the people inside the isthmus from the barbarians outside, but in truth because he wished to break the alliance which the Greeks had with one another, and thus command with impunity the people inside; but the people outside came in and prevented the undertaking. After Scylletium comes the territory of the Crotoniates, and three capes of the Iapyges; and after these, the Lacinium,^[The Lacinium derived its name from Cape Lacinium (now Cape Nao), on which it was situated. According to Diod. Sic. 4.24, Heracles, when in this region, put to death a cattle-thief named Lacinius. Hence the name of the cape.] a temple of Hera, which at one time was rich and full of dedicated offerings. As for the distances by sea, writers give them without satisfactory clearness, except that, in a general way, Polybius gives the distance from the strait to Lacinium as two thousand three hundred stadia,^[Strabo probably wrote "two thousand" and not "one thousand" (see Manner, t. 9. 9, p. 202), and so read Gosselin, Groskurd, Forbiger, Müller-Dübner, and Meineke. Compare Strabo's other quotation (5. 1. 3) from Polybius on this subject. There, as here, unfortunately, the figures ascribed to Polybius cannot be compared with his original statement, which is now lost.] and the distance thence across to Cape Iapygia as seven hundred. This point is called the mouth of the Tarantine Gulf. As for the gulf itself, the distance around it by sea is of considerable length, two hundred and forty miles,^[240 Roman miles=1,920, or 2,000 (see 7. 7. 4), stadia.] as the Chorographer^[See 5. 2. 7, and the footnote.] says, but Artemidorus says three hundred and eighty for a man well-girded, although he falls short of the real breadth of the mouth of the gulf by as much.^[This passage ("although . . . much") is merely an attempt to translate the Greek of the manuscripts. The only variant in the manuscripts is that of "ungirded" for "well-girded." If Strabo wrote either, which is extremely doubtful, we must infer that Artemidorus' figure, whatever it was pertained to the number of days it would take a pedestrian, at the rate, say of 160 stadia (20 Roman miles) per day, to make the journey around the gulf by land. Most of the editors (including Meineke) dismiss the passage as hopeless by merely indicating gaps in the text. Groskurd and C. Müller not only emend words of the text but also fill in the supposed gaps with seventeen and nine words, respectively. Groskurd makes Artemidorus say that a well-girded pedestrian can complete the journey around the gulf in twelve days, that the coasting-voyage around it is 2,000 stadia, and that he leaves for the mouth the same number (700) of stadia assigned by Polybius to the breadth of the mouth of the gulf. But C. Müller writes: "Some make it less, saying 1,380 stadia, whereas Artemidorus makes it as many plus 30 (1,410), in speaking of the breadth of the mouth of the gulf." But the present translator, by making very simple emendations (see critical note 2 on page 38), arrives at the following: Artemidorus says eighty stadia longer (i.e., 2,000) although he falls short of the breadth of the mouth of the gulf by as much (i.e., 700 - 80 = 620). It should be noted that Artemidorus, as quoted by Strabo, always gives distances in terms of stadia, not miles (e.g., 3. 2. 11, 8. 2. 1, 14. 2. 29, et passim), and that his figures at times differ considerably from those of the Chorographer (cp. 6. 3. 10).] The gulf faces the winter-sunrise;^[i.e., south-east.] and it begins at Cape Lacinium, for, on doubling it, one immediately comes to the cities^[As often Strabo refers to sites of perished cities as cities.] of the Achaeans, which, except that of the Tarantini, no longer exist, and yet, because of the fame of some of them, are worthy of rather extended mention. The first city is Croton, within one hundred and fifty stadia from the Lacinium; and then comes the River Aesarus, and a harbor, and another river, the Neaethus. The Neaethus got its name, it is said, from what occurred there: Certain of the Achaeans who had strayed from the Trojan fleet put in there and disembarked for an inspection of the region, and when the Trojan women who were sailing with them learned that the boats were empty of men, they set fire to the boats, for they were weary of the voyage, so that the men remained there of necessity, although they at the same time noticed that the soil was very fertile. And immediately several other groups, on the strength of their racial kinship, came and imitated them, and thus arose many settlements, most of which took their names from the Trojans; and also a river, the Neaethus, took its appellation from the aforementioned occurrence.^[The Greek "Neas aethein" means "to burn ships."] According to Antiochus, when the god told the Achaeans to found Croton, Myscellus departed to inspect the place, but when he saw that Sybaris was already founded—having the same name as the river near by—he judged that Sybaris was better; at all events, he questioned the god again when he returned whether it would be better to found this instead of Croton, and the god replied to him (Myscellus^[Ovid Met. 15.20 spells the name "Myscelus," and perhaps rightly; that is, "Mouse-leg" (?).] was a hunchback as it happened): "Myscellus, short of back, in searching else outside thy track, thou hunt'st for morsels only; 'tis right that what one giveth thee thou do approve;"^[For a fuller account, see Diod. Sic. 8. 17 His version of the oracle is: "Myscellus, short of back, in searching other things apart from god, thou searchest only after tears; what gift god giveth thee, do thou approve."] and Myscellus came back and founded Croton, having as an associate Archias, the founder of Syracuse, who happened to sail up while on his way to found Syracuse.^[The generally accepted dates for the founding of Croton and Syracuse are, respectively, 710 B.C. and 734 B.C. But Strabo's account here seems to mean that Syracuse was founded immediately after Croton (cp. 6. 2. 4). Cp. also Thucydides 6. 3. 2] The Iapyges used to live at Croton in earlier times, as Ephorus says. And the city is reputed to have cultivated warfare and athletics; at any rate, in one Olympian festival the seven men who took the lead over all others in the stadium-race were all Crotoniates, and therefore the saying "The last of the Crotoniates was the first among all other Greeks" seems reasonable. And this, it is said, is what gave rise to the other proverb, "more healthful than Croton," the belief being that the place contains something that tends to health and bodily vigor, to judge by the multitude of its athletes. Accordingly, it had a very large number of Olympic victors, although it did not remain inhabited a long time, on account of the ruinous loss of its citizens who fell in such great numbers^[Cp. 6. 1 10.] at the River Sagra. And its fame was increased by the large number of its Pythagorean philosophers, and by Milo, who was the most illustrious of athletes, and also a companion of Pythagoras, who spent a long time in the city. It is said that once, at the common mess of the philosophers, when a pillar began to give way, Milo slipped in under the burden and saved them all, and then drew himself from under it and escaped. And it is probably because he relied upon this same strength that he brought on himself the end of his life as reported by some writers; at any rate, the story is told that once, when he was travelling through a deep forest, he strayed rather far from the road, and then, on finding a large log cleft with wedges, thrust his hands and feet at the same time into the cleft and strained to split the log completely asunder; but he was only strong enough to make the wedges fall out, whereupon the two parts of the log instantly snapped together; and caught in such a trap as that, he became food for wild beasts. Next in order, at a distance of two hundred stadia, comes Sybaris, founded by the Achaeans; it is between two rivers, the Crathis and the Sybaris. Its founder was Is of Helice.^[The reading, "Is of Helice," is doubtful. On Helice, see 1. 3. 18 and 8. 7. 2.] In early times this city was so superior in its good fortune that it ruled over four tribes in the neighborhood, had twenty- five subject cities, made the campaign against the Crotoniates with three hundred thousand men, and its inhabitants on the Crathis alone completely filled up a circuit of fifty stadia. However, by reason of luxury^[Cp. "Sybarite."] and insolence they were deprived of all their felicity by the Crotoniates within seventy days; for on taking the city these conducted the river over it and submerged it. Later on, the survivors, only a few, came together and were making it their home again, but in time these too were destroyed by Athenians and other Greeks, who, although they came there to live with them, conceived such a contempt for them that they not only slew them but removed the city to another place near by and named it Thurii, after a spring of that name. Now the Sybaris River makes the horses that drink from it timid, and therefore all herds are kept away from it; whereas the Crathis makes the hair of persons who bathe in it yellow or white, and besides it cures many afflictions. Now after the Thurii had prospered for a long time, they were enslaved by the Leucani, and when they were taken away from the Leucani by the Tarantini, they took refuge in Rome, and the Romans sent colonists to supplement them, since their population was reduced, and changed the name of the city to Copiae. After Thurii comes Lagaria, a stronghold, bounded by Epeius and the Phocaeans; thence comes the Lagaritan wine, which is sweet, mild, and extremely well thought of among physicians. That of Thurii, too, is one of the famous wines. Then comes the city Heracleia, a short distance above the sea; and two navigable rivers, the Aciris and the Siris. On the Siris there used to be a Trojan city of the same name, but in time, when Heracleia was colonized thence by the Tarantini, it became the port of the Heracleotes. It is Twenty-four stadia distant from Heracleia and about three hundred and thirty from Thurii. Writers produce as proof of its settlement by the Trojans the wooden image of the Trojan Athene which is set up there—the image that closed its eyes, the fable goes, when the suppliants were dragged away by the Ionians who captured the city; for these Ionians came there as colonists when in flight from the dominion of the Lydians, and by force took the city, which belonged to the Chones,^[Cp. 6. 1. 2.] and called it Polieium; and the image even now can be seen closing its eyes. It is a bold thing, to be sure, to tell such a fable and to say that the image not only closed its eyes (just as they say the image in Troy turned away at the time Cassandra was violated) but can also be seen closing its eyes; and yet it is much bolder to represent as brought from Troy all those images which the historians say were brought from there; for not only in the territory of Siris, but also at Rome, at Lavinium, and at Luceria, Athene is called "Trojan Athena," as though brought from Troy. And further, the daring deed of the Trojan women is current in numerous places, and appears incredible, although it is possible. According to some, however, both Siris and the Sybaris which is on the Teuthras^[The "Teuthras" is otherwise unknown, except that there was a small river of that name, which cannot be identified, near Cumae (see Propertius 1. 11.11 and Silius Italicus 11.288). The river was probably named after Teuthras, king of Teuthrania in Mysia (see 12. 8. 2). But there seems to be no evidence of Sybarites in that region. Meineke and others are probably right in emending to the "Trais" (now the Trionto), on which, according to Diod. Sic. 12.22, certain Sybarites took up their abode in 445 B.C.] were founded by the Rhodians. According to Antiochus, when the Tarantini were at war with the Thurii and their general Cleandridas, an exile from Lacedaemon, for the possession of the territory of Siris, they made a compromise and peopled Siris jointly, although it was adjudged the colony of the Tarantini; but later on it was called Heracleia, its site as well as its name being changed. Next in order comes Metapontium, which is one hundred and forty stadia from the naval station of Heracleia. It is said to have been founded by the Pylians who sailed from Troy with Nestor; and they so prospered from farming, it is said, that they dedicated a golden harvest^[An ear, or sheaf, of grain made of gold, apparently.] at Delphi. And writers produce as a sign of its having been founded by the Pylians the sacrifice to the shades of the sons of Neleus.^[Neleus had twelve sons, including Nestor. All but Nestor were slain by Heracles.] However, the city was wiped out by the Samnitae. According to Antiochus: Certain of the Achaeans were sent for by the Achaeans in Sybaris and resettled the place, then forsaken, but they were summoned only because of a hatred which the Achaeans who had been banished from Laconia had for the Tarantini, in order that the neighboring Tarantini might not pounce upon the place; there were two cities, but since, of the two, Metapontium was nearer^[The other, of course, was Siris.] to Taras,^[The old name of Tarentum.] the newcomers were persuaded by the Sybarites to take Metapontium and hold it, for, if they held this, they would also hold the territory of Siris, whereas, if they turned to the territory of Siris, they would add Metapontium to the territory of the Tarantini, which latter was on the very flank of Metapontium; and when, later on, the Metapontians were at war with the Tarantini and the Oenotrians of the interior, a reconciliation was effected in regard to a portion of the land—that portion, indeed, which marked the boundary between the Italy of that time and Iapygia.^[i.e., the Metapontians gained undisputed control of their city and its territory, which Antiochus speaks of as a "boundary" (cp. 6. 1. 4 and 6. 3. 1).] Here, too, the fabulous accounts place Metapontus,^[The son of Sisyphus. His "barbarian name," according to Stephanus Byzantinus and Eustathius, was Metabus.] and also Melanippe the prisoner and her son Boeotus.^[One of Euripides' tragedies was entitled Melanippe the Prisoner; only fragments are preserved. She was the mother of Boeotus by Poseidon.] In the opinion of Antiochus, the city Metapontium was first called Metabum and later on its name was slightly altered, and further, Melanippe was brought, not to Metabus, but to Dius,^[A Metapontian.] as is proved by a hero-temple of Metabus, and also by Asius the poet, when he says that Boeotus was brought forth "in the halls of Dius by shapely Melanippe,"^[Asius Fr.] meaning that Melanippe was brought to Dius, not to Metabus. But, as Ephorus says, the colonizer of Metapontium was Daulius, the tyrant of the Crisa which is near Delphi. And there is this further account, that the man who was sent by the Achaeans to help colonize it was Leucippus, and that after procuring the use of the place from the Tarantini for only a day and night he would not give it back, replying by day to those who asked it back that he had asked and taken it for the next night also, and by night that he had taken and asked it also for the next day.Next in order comes Taras and Iapygia; but before discussing them I shall, in accordance with my original purpose, give a general description of the islands that lie in front of Italy; for as from time to time I have named also the islands which neighbor upon the several tribes, so now, since I have traversed Oenotria from beginning to end, which alone the people of earlier times called Italy, it is right that I should preserve the same order in traversing Sicily and the islands round about it.[^2da2531430bd480999fcb8b47d09a628]

Virgil departed from Burnum, intending to travel by road to Salona, a 50.36833326 mile journey. 

### Salona in Civil War



After the departure of the Liburnian his command, sailed from Illyricum, and came before Salona. Having spirited up the Dalmatians, and other barbarous nations in those parts, he drew Issa to revolt from Caesar. But finding that the council of Salona was neither to be moved by promises nor threats, he resolved to invest the town. Salona is built upon a hill, and advantageously situated for defence; but as the fortifications were very inconsiderable, the Roman citizens, residing there, immediately surrounded the place with wooden towers; and finding themselves too few to resist the attacks of the enemy, who soon overwhelmed them with wounds, betook themselves to their last refuge, by granting liberty to all slaves capable of bearing arms, and cutting off the women's hair, to make cords for their engines. Octavius perceiving their obstinacy, formed five different camps round the town, that they might at once suffer all the inconveniences of a siege, and be exposed to frequent attacks. The Salonians, determined to endure any thing, found themselves most pressed for want of corn; and therefore sent deputies to Caesar to solicit a supply, patiently submitting to all the other hardships they laboured under. When the siege had now continued a considerable time, and the Octavians began to be off their guard, the Salonians, finding the opportunity favourable, about noon, when the enemy were dispersed, disposed their wives and children upon the walls, that every thing might have its wonted appearance; and sallying in a body with their enfranchised slaves, attacked the nearest quarters of Octavius. Having soon forced these, they advanced to the next; thence to a third, a fourth, and so on through the rest; till having driven the enemy from every post, and made great slaughter of their men, they at length compelled them, and Octavius their leader, to betake themselves to their ships. Such was the issue of the siege. As winter now approached, and the loss had been very considerable; Octavius, despairing to reduce the place, retired to Dyrrhachium, and joined Pompey.[^f0b72bf41e6849f395c72559a466998f]

Virgil departed from Salona, intending to travel by ship down the coast to Aternum, a 153.083445044 mile journey. 

### What Julius Caesar once said about the countryside near that place



On entering Pompey's camp, we found tables ready-covered, sideboards loaded with plate, and tents adorned with branches of myrtle; that of L. Lentulus, with some others, was shaded with ivy. Every thing gave proofs of the highest luxury, and an assured expectation of victory; whence it was easy to see, that they little dreamed of the issue of that day, since, intent only on voluptuous refinements, they pretended, with troops immersed in luxury, to oppose Caesar's army accustomed to fatigue, and inured to the want of necessaries.

Pompey finding our men had forced his intrenchments, mounted his horse, quitted his armour for a habit more suitable to his ill fortune, and withdrawing by the Decuman port, rode full speed to Larissa. Nor did he stop there; but continuing his flight day and night, without intermission, he arrived at the sea-side, with thirty horse, and went on board a little bark; often complaining, "That he had been so far deceived in his opinion of his followers, as to see those very men, from whom he expected victory, the first to fly, and in a manner betray him into the hands of his enemies."[^e26de4ab4a5f4b35b3358b1f7d00aab5]

Virgil departed from Aternum, intending to travel by ship down the coast to Castrum Truentinum, a 38.822017338 mile journey. 

### A story about Formiae



He was sent by Galba into Lower Germany,^[A.U.C. 821] contrary to his expectation. It is supposed that he was assisted in procuring this appointment by the interest of Titus Junius, a man of great influence at that time; whose friendship he had long before gained by favouring the same set of charioteers with him in the Circensian games. But Galba openly declared that none were less to be feared than those who only cared for their bellies, and that even his enormous appetite must be satisfied with the plenty of that province; so that it is evident he was selected for that government more out of contempt than kindness. It is certain, that when he was to set out, he had not money for the expenses of his journey; he being at that time so much straitened in his circumstances, that he was obliged to put his wife and children, whom he left at Rome, into a poor lodging which he hired for them, in order that he might let his own house for the remainder of the year; and he pawned a pearl taken from his mother's ear-ring, to defray his expenses on the road. A crowd of creditors who were waiting to stop him, and amongst them the people of Sineussa and Formia, whose taxes he had converted to his own use, he eluded, by alarming them with the apprehension of false accusations. He had, however, sued a certain freedman, who was clamorous in demanding a debt of him, under pretence that he had kicked him; which action he would not withdraw, until he had wrung from the freedman fifty thousand sesterces. Upon his arrival in the province, the army, which was disaffected to Galba, and ripe for insurrection, received him with open arms, as if he had been sent them from heaven. It was no small recommendation to their favour, that he was the son of a man who had been thrice consul, was in the prime of life, and of an easy, prodigal disposition. This opinion, which had been long entertained of him, Vitellius confirmed by some late practices; having kissed all the common soldiers whom he met with upon the road, and been excessively complaisant in the inns and stables to the muleteers and travellers; asking them in a morning, if they had got their breakfasts, and letting them see, by belching, that he had eaten his.[^6828139e3b95451a9639dd1fd0da81bf]

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a 17.434427518 mile journey. 

### A story about Tibur



"Two brothers, Catillus and Coras, come from Tibur."[^a580534fece147cdbebb3be9ad0201f5]

[^819c88b57f394bee9ca395402576b32c]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.78} 


[^a3e0b53dfdd7443080337ee6ae04e4c4]: From the Perseus Digital Library:      Complete Works of Tacitus. Tacitus. Alfred John Church. William Jackson Brodribb. Sara Bryant. edited for Perseus. New York. : Random House, Inc. Random House, Inc. 1873. reprinted 1942. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1351.phi004.perseus-eng1:3.79} 


[^aee569ab52c1454d9e0ef568a8ef8f4c]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie  Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo020.perseus-eng1:1} 


[^9eb46fe6b5e141758a35e09ed9be95c7]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:5.1} 


[^b74f5ea9089d417c9a622abfb7a25bbd]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:1.158} 


[^54d888bdd7bd4a51b335b421f7a0554d]: From the Perseus Digital Library:      Vitruvius: The Ten Books on Architecture. Vitruvius. Morris Hicky Morgan. Cambridge: Harvard University Press. London: Humphrey Milford. Oxford University Press. 1914. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1056.phi001.perseus-eng1:2.9} 


[^86b1b0349f604b65a955ea8cb3bde597]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:2.326} 


[^bf0bf1b9e5d24c15931f1fdc24d464c1]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. George Bell & Sons, York Street, Covent Garden. 1891. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi021.perseus-eng1:28} 


[^9d9abfdddf114d17bfa7364da69f0be6]: From the Perseus Digital Library:      Pharsalia. M. Annaeus Lucanus. Sir Edward Ridley. London. Longmans, Green, and Co. 1905. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0917.phi001.perseus-eng1:4.402} 


[^0d31b69a9e3e4ef9a3f676ed61aa0993]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.8} 


[^2da2531430bd480999fcb8b47d09a628]: From the Perseus Digital Library:      Strabo. ed. H. L. Jones, The Geography of Strabo. Cambridge, Mass.: Harvard University Press; London: William Heinemann, Ltd. 1924. \url{http://data.perseus.org/citations/urn:cts:greekLit:tlg0099.tlg001.perseus-eng1:6.1} 


[^f0b72bf41e6849f395c72559a466998f]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.9} 


[^e26de4ab4a5f4b35b3358b1f7d00aab5]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:3.96} 


[^6828139e3b95451a9639dd1fd0da81bf]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889. \url{http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo019.perseus-eng1:7} 


[^a580534fece147cdbebb3be9ad0201f5]: From the Perseus Digital Library: Perseus Digital Library \url{http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0051:book=7:commline=670-677} 


