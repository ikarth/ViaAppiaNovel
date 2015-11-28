% Virgil's Commonplace Book
% Isaac Karth
% November 26, 2015
\newpage


\newpage
# Virgil's Commonplace Book
\newpage
&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


Virgil's Commonplace Book

2015


This work includes extracts from texts provided by the Perseus Digital Library under a Creative Commons Attribution-ShareAlike 3.0 United States License


\newpage

## Introduction
It has long been a common practice to incorporate the works of earlier writers into new books. Indeed, many commonplace books consist of nothing _but_ quotations and similar notes. We have many surviving examples from the Roman Empire, such as Aulus Gellius' _Attic Nights_. These texts were not always attributed to the original source. Lacking the modern concept of plagiarism (and our post-printing-press system of uniform citations) writers sometimes come off as careless to modern sensibilities. Quotes could be paraphrased and rather vague citations were the norm. Indeed, some authors committed a kind of reverse plagiarism, [pseudepigraphically](https://en.wikipedia.org/wiki/Pseudepigrapha) attributing their work to an earlier, more famous author.
 
In a way, this reuse is fortunate: many texts from the Classical period only exist in fragments quoted in other documents. Some works survive in [epitome](https://en.wikipedia.org/wiki/Epitome), distilled versions that summarized the text; for others we have fragments that later writers quoted or abridged as they wrote their compilations.

Artists, of course, have been far looser with their borrowings than writers of mere facts, placing the present work solidly within a long tradition. The closest literary ancedents of NaNoGenMo--Dada and Oulipo--have often explored similar sampling approaches. Kathryn Hume has suggested that technical constratints have lead NaNoGenMo to "align itself with poetics of recontextualization and reassembly." While I'd point out that NaNoGenMo also exhibits other aspects, such as the concrete poetry in thricedotted's _The Seeker_, or the way structurally-plotted works like _Hannah and The Twelve-Disk Tower of Hanoi_ evoke the chessboard constraints of _Life a User's Manual_ or _Through the Looking Glass_, there is an undeniable strand of appropreation as we teach our machines to imitate their human creators. Still, that's no reason to neglect giving credit, so this book attempts to cite the sources for the texts it borrows.

In this work, that deliberate borrowing is the intent. Unlike an age of precious codices, the information age is a time of entirely too much to read. Search engines can find anything you ask for but, like a fairy-tale mirror, can only answer the questions you know enough to ask in the first place. The serendipity of browsing through a library is lost. Extracting the stories and arranging them in a new pattern presents a new angle. Rather than an exhaustive view of the forest, it picks out one or two trees you might have otherwise overlooked.

I chose Virgil as the protagonist for three reasons: first, his works are among the source texts in the Perseus Digital Library used for much of the text here. His _Aeneid_ builds on earlier traditions, recast in a founding epic for a new age: appropriate for a work themed around appropriation and reuse in this new information age. This would not be enough to recommend him on its own: there are other authors whose works were much closer to the kind of copying and summarizing going on here. And _The Golden Ass_ by Apuleius, one of the earliest surviving novels, is closer in form to the travel tale that structures this generated novel. 

But there was also a tradition that linked Virgil and his poetry with magic and prophecy. It was no accident that Dante chose Virgil to be his guide through the _Inferno_. That touch of magic, a magic intimately linked with words and poetry. And, as Jeff Howard has pointed out,^[in _Game Magic_] programming is a form of magic. A magician-protagonist is entirely appropreate.

Lastly, that tradition of magic lead the much-neglected Avram Davidson to pen a novel with Vergil Magus as the magician-protagonist. My own pseudo-Virgil is a humble tribute, a machine homunculus librarian to forgotten texts.

--Isaac Karth 

2015-11-27 

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
    Virgil departed from Roma, intending to travel on a military boat downstream to the countryside, a 17.017487577 mile journey. 

Virgil departed from the countryside, intending to travel on a boat heading upstream to Roma, a 17.017487577 mile journey. 

### A story by Titus Livius (Livy) about Roma from The History of Rome, Book 1



There^[The Combat of the Horatii and Curiatii.] happened to be in each of the armies a triplet of brothers, fairly matched in years and strength. It is generally agreed that they were called Horatii and Curiatii. Few incidents in antiquity have been more widely celebrated, yet in spite of its celebrity there is a discrepancy in the accounts as to which nation each belonged. There are authorities on both sides, but I find that the majority give the name of Horatii to the Romans, and my sympathies lead me to follow them.

The kings suggested to them that they should each fight on behalf of their country, and where victory rested, there should be the sovereignty. They raised no objection; so the time and place were fixed. But before they engaged a treaty was concluded between the Romans and the Albans, providing that the nation whose representatives proved victorious should receive the peaceable submission of the other.

This is the earliest treaty recorded, and as all treaties, however different the conditions they contain, are concluded with the same forms, I will describe the forms with which this one was concluded as handed down by tradition. The Fetial put the formal question to Tullus: "Do you, King, order me to make a treaty with the _Pater Patratus_ of the Alban nation?" On the king replying in the affirmative, the Fetial said: "I demand of thee, King, some tufts of grass." The king replied: "Take those that are pure." The Fetial brought pure grass from the Citadel. Then he asked the king: "Do you constitute me the plenipotentiary of the People of Rome, the Quirites, sanctioning also my vessels and comrades?" To which the king replied: "So far as may be without hurt to myself and the People of Rome, the Quirites, I do." The Fetial was M. Valerius. He made Spurius Furius the Pater Patratus by touching his head and hair with the grass. Then the Pater Patratus, who is constituted for the purpose of giving the treaty the religious sanction of an oath, did so by a long formula in verse, which it is not worth while to quote. After reciting the conditions he said: "Hear, 0 Jupiter, hear! thou Pater Patratus of the people of Alba! Hear ye, too, people of Alba! As these conditions have been publicly rehearsed from first to last, from these tablets, in perfect good faith, and inasmuch as they have here and now been most clearly understood, so these conditions the People of Rome will not be the first to go back from. If they shall, in their national council, with false and malicious intent be the first to go back, then do thou, Jupiter, on that day, so smite the People of Rome, even as I here and now shall smite this swine, and smite them so much the more heavily, as thou art greater in power and might." With these words he struck the swine with a flint. In similar wise the Albans recited their oath and formularies through their own dictator and their priests.[^03327f494118404583fd5a919e2d5d65]

Virgil departed from Roma, intending to travel by road to Volsinii, a 62.636682284 mile journey. 

Virgil departed from Volsinii, intending to travel by road to Roma, a 62.636682284 mile journey. 

### A story by Polybius about Roma from Histories



It was in the nineteenth year after the sea-fight at^[B. C. 387-386. The rise of the Roman dominion may be traced from the retirement of the Gauls from the city. From that time one nation after another in Italy fell into their hands.] Aegospotami, and the sixteenth before the battle at Leuctra; the year in which the Lacedaemonians made what is called the Peace of Antalcidas with the King of Persia; the year in which the elder Dionysius was besieging Rhegium after beating the Italian Greeks on the river Elleporus; and in which the Gauls took Rome itself by storm and were occupying the whole of it except the Capitol. With these Gauls the Romans made a treaty and settlement which they were content to accept: and having thus become beyond all expectation once more masters of their own country, they made a start in their career of expansion; and in the succeeding period engaged in various wars with their neighbours.^[The Latini.] First, by dint of valour, and the good fortune which attended them in the field, they mastered all the Latini; then they went to war with the Etruscans; then with the Celts; and next with the Samnites, who lived on the eastern and northern frontiers of Latium.^[The Etruscans, Gauls, and Samnites.] Some time after this the Tarentines insulted the ambassadors of Rome, and, in fear of the consequences, invited and obtained the assistance of Pyrrhus.^[Pyrrhus, B. C. 280.] This happened in the year before the Gauls invaded Greece, some of whom perished near Delphi, while others crossed into Asia. Then it was that the Romans—having reduced the Etruscans and Samnites to obedience, and conquered the Italian Celts in many battles—attempted for the first time the reduction of the rest of Italy.^[Southern Italy.] The nations for whose possessions they were about to fight they affected to regard, not in the light of foreigners, but as already for the most part belonging and pertaining to themselves. The experience gained from their contests with the Samnites and the Celts had served as a genuine training in the art of war.^[Pyrrhus finally quits Italy, B. C. 274.] Accordingly, they entered upon the war with spirit, drove Pyrrhus from Italy, and then undertook to fight with and subdue those who had taken part with him. They succeeded everywhere to a marvel, and reduced to obedience all the tribes inhabiting Italy except the Celts; after which they undertook to besiege some of their own citizens, who at that time were occupying Rhegium.[^4efc643811af4e329882b9090e7d139a]

Virgil departed from Roma, intending to travel by road to Tibur, a 17.629538012 mile journey. 

### A story by Polybius about Tibur from Histories



After this one would naturally be inclined to ask what part is left for the people in the constitution, when the Senate has these various functions, especially the control of the receipts and expenditure of the exchequer; and when the Consuls, again, have absolute power over the details of military preparation, and an absolute authority in the field? There is, however, a part left the people, and it is a most important one. For the people is the sole fountain of honour and of punishment; and it is by these two things and these alone that dynasties and constitutions and, in a word, human society are held together: for where the distinction between them is not sharply drawn both in theory and practice, there no undertaking can be properly administered,—as indeed we might expect when good and bad are held in exactly the same honour. The people then are the only court to decide matters of life and death; and even in-cases where the penalty is money, if the sum to be assessed is sufficiently serious, and especially when the accused have held the higher magistracies. And in regard to this arrangement there is one point deserving especial commendation and record. Men who are on trial for their lives at Rome, while sentence is in process of being voted,—if even only one of the tribes whose votes are needed to ratify the sentence has not voted,—have the privilege at Rome of openly departing and condemning themselves to a voluntary exile. Such men are safe at Naples or Praeneste or at Tibur, and at other towns with which this arrangement has been duly ratified on oath.

Again, it is the people who bestow offices on the deserving, which are the most honourable rewards of virtue. It has also the absolute power of passing or repealing laws; and, most important of all, it is the people who deliberate on the question of peace or war. And when provisional terms are made for alliance, suspension of hostilities, or treaties, it is the people who ratify them or the reverse.

These considerations again would lead one to say that the chief power in the state was the people's, and that the constitution was a democracy.[^e2ae9f50109149f78e488529b8ff0400]

Virgil departed from Tibur, intending to travel by road to Alba Fucens, a 39.645955284 mile journey. 

Virgil departed from Alba Fucens, intending to travel by road to Tibur, a 39.645955284 mile journey. 

### A story by Virgil about Tibur from Aeneid



A solemn custom was observ'd of old,  
Which Latium held, and now the Romans hold,  
Their standard when in fighting fields they rear  
Against the fierce Hyrcanians, or declare  
The Scythian, Indian, or Arabian war;  
Or from the boasting Parthians would regain  
Their eagles, lost in Carrhae's bloody plain.  
Two gates of steel (the name of Mars they bear,  
And still are worship'd with religious fear)  
Before his temple stand: the dire abode,  
And the fear'd issues of the furious god,  
Are fenc'd with brazen bolts; without the gates,  
The wary guardian Janus doubly waits.  
Then, when the sacred senate votes the wars,  
The Roman consul their decree declares,  
And in his robes the sounding gates unbars.  
The youth in military shouts arise,  
And the loud trumpets break the yielding skies.  
These rites, of old by sov'reign princes us'd,  
Were the king's office; but the king refus'd,  
Deaf to their cries, nor would the gates unbar  
Of sacred peace, or loose th' imprison'd war;  
But hid his head, and, safe from loud alarms,  
Abhorr'd the wicked ministry of arms.  
Then heav'n's imperious queen shot down from high:  
At her approach the brazen hinges fly;  
The gates are forc'd, and ev'ry falling bar;  
And, like a tempest, issues out the war.  
  
The peaceful cities of th' Ausonian shore,  
Lull'd in their ease, and undisturb'd before,  
Are all on fire; and some, with studious care,  
Their restiff steeds in sandy plains prepare;  
Some their soft limbs in painful marches try,  
And war is all their wish, and arms the gen'ral cry.  
Part scour the rusty shields with seam; and part  
New grind the blunted ax, and point the dart:  
With joy they view the waving ensigns fly,  
And hear the trumpet's clangor pierce the sky.  
Five cities forge their arms: th' Atinian pow'rs,  
Antemnae, Tibur with her lofty tow'rs,  
Ardea the proud, the Crustumerian town:  
All these of old were places of renown.  
Some hammer helmets for the fighting field;  
Some twine young sallows to support the shield;  
The croslet some, and some the cuishes mold,  
With silver plated, and with ductile gold.  
The rustic honors of the scythe and share  
Give place to swords and plumes, the pride of war.  
Old fauchions are new temper'd in the fires;  
The sounding trumpet ev'ry soul inspires.  
The word is giv'n; with eager speed they lace  
The shining headpiece, and the shield embrace.  
The neighing steeds are to the chariot tied;  
The trusty weapon sits on ev'ry side.  
  
[^c6fe8baaf1374ae58104067ba8dc3985]

Virgil departed from Tibur, intending to travel by road to Alba Fucens, a 39.645955284 mile journey. 

Virgil departed from Alba Fucens, intending to travel by road to Tibur, a 39.645955284 mile journey. 

### A story by Suetonius ca. 69-ca. 122 about Tibur from Caligula



He completed the works which were left unfinished by Tiberius, namely, the temple of Augustus, and the theatre of Pompey.^[See TIBERIUS, c. xlvii. and AUGUSTUS, c. xxxi.] He began, likewise, the aqueduct from the neighbourhood of Tibur,^[This aqueduct, commenced by Caligula and completed by Claudian, a truly imperial work, conveyed the waters of two streams to Rome, following the valley of the Anio from above Tivoli. The course of one of these rivulets was forty miles, and it was carried on arches, immediately after quitting its source, for a distance of three miles. The other, the Anio Novus, also began on arches, which continued for upwards of twelve miles. After this, both were conveyed under ground; but at the distance of six miles from the city, they were united, and carried upon arches all the rest of the way. This is the most perfect of all the ancient aqueducts; and it has been repaired, so as to convey the Acqua Felice, one of the three streams which now supply Rome. See CLAUDIUS, c. XX. ] and an amphitheatre near the Septa;^[By Septa, Suetonius here means the huts or barracks of the pretorian camp, which was a permanent and fortified station. It stood to the east of the Viminal and Quirinal hills, between the present Porta Pia and S. Lorenzo, where these is a quadrangular projection in the city walls marking the site. The remains of the Amphitheatrum Castrense stand between the Porta Maggiore and S. Giovanni, formerly without the ancient walls, but now included in the line. It is all of brick, even the Corinthian pillars, and seems to have been but a rude structure, suited to the purpose for which it was built, the amusement of the soldiers, and gymnastic exercises. For this purpose they were used to construct temporary amphitheatres near the stations in the distant provinces, which were not built of stone or brick, but hollow circular spots dug in the ground, round which the spectators sat on the declivity, on ranges of seats cut in the sod. Many vestiges of this kind have been traced in Britain. ] of which works, one was completed by his successor Claudius, and the other remained as he left it. The walls of Syracuse, which had fallen to decay by length of time, he repaired, as he likewise did the temples of the gods. He formed plans for rebuilding the palace of Polycrates at Samos, finishing the temple of the Didymaean Apollo at Miletus, and building a town on a ridge of the Alps; but, above all, for cutting through the isthmus in Achaia^[The Isthmus of Corinth; an enterprize which had formerly been attempted by Demetrius, and which was also projected by Julius Caesar, c. xliv., and Nero, c. xix.; but they all failed of accomplishing it.] and even sent a centurion of the first rank to measure out the work.[^28715070ddcf483f8c0815666c9904ed]

Virgil departed from Tibur, intending to travel by road to Roma, a 17.629538012 mile journey. 

### A story by Cicero, Marcus Tullius about Roma from Philippics



Therefore, if when we have received those men we can still be free, let us subdue our hatred to them, and endure peace; but if there can be no tranquillity while those men are in safety, then let us rejoice that an opportunity of fighting them is put in our power. For so, either (these men being conquered) we shall enjoy the republic victorious, or, if we be defeated, (but may Jupiter avert that disaster), we shall live, if not with an actual breath, at all events in the renown of our valor.[^226a815df2c54c3f8691a05a4bced9d9]

Virgil departed from Roma, intending to travel by road to Tibur, a 17.629538012 mile journey. 

### A story by Cicero, Marcus Tullius about Tibur from Philippics



Marcus Lepidus is desirous of peace. He does well especially if he can make such a peace as he made lately, owing to which the republic will behold the son of Cnaeus Pompeius, and will receive him in her bosom and embrace; and will think, that not he alone, but that she also is restored to herself with him. This was the reason why you decreed to him a statue in the rostra with an honorable inscription, and why you voted him a triumph in his absence. For although he had performed great exploits in war, and such as well deserved a triumph, still for that he might not have had that given to him which was not given to Lucius Aemilius, nor to Aemilianus Scipio, nor to the former Africanus, nor to Marius, nor to Pompeius, who had the conduct of greater wars than he had, but because he had put an end to a civil war in perfect silence, the first moment that it was in his power, on that account you conferred on him the greatest honors.[^b7200a34f3b54ed6aac19ec24265cf7a]

Virgil departed from Tibur, intending to travel by road to Alba Fucens, a 39.645955284 mile journey. 

Virgil departed from Alba Fucens, intending to travel by road to Corfinium, a 24.140884721 mile journey. 

### A story by Julius Caesar about Corfinium from Civil War



Pompey, having intelligence of what passed at Corfinium, retreated from Luceria to Canusium, and from thence to Brundusium. He ordered all the new levies to join him, armed the shepherds and slaves, furnished them with horses, and formed a body of about three hundred cavalry. Meanwhile the pretor L. Manlius flying from Alba, with six cohorts; and the pretor Rutilus Lupus, from Tarracina, with three; saw Caesar's cavalry at a distance, commanded by Bivius Curius: upon which, the soldiers immediately abandoned the two pretors, and joined the troops under the conduct of Curius. Several other parties, flying different ways, fell in, some with the foot,otherswith the horse. Cn. Magius of Cremona, Pompey's chief engineer, being taken on his way to Brundusium, was brought to Caesar, who sent him back to Pompey with this message: "That as he had not yet obtained an interview, his design was to come to Brundusium, there to confer with him in relation to the common safety; because they soon would be able to despatch, in a personal treaty, what, if managed by the intervention of others, could not be hindered from running into a tedious negotiation."[^6db459e000c34fc1ae92f4fd96b10c2d]

Virgil departed from Corfinium, intending to travel by road to Aesernia, a 43.612787748 mile journey. 

Virgil departed from Aesernia, intending to travel by road to Corfinium, a 43.612787748 mile journey. 

### A story by Julius Caesar about Corfinium from Civil War



Pompey, having intelligence of what passed at Corfinium, retreated from Luceria to Canusium, and from thence to Brundusium. He ordered all the new levies to join him, armed the shepherds and slaves, furnished them with horses, and formed a body of about three hundred cavalry. Meanwhile the pretor L. Manlius flying from Alba, with six cohorts; and the pretor Rutilus Lupus, from Tarracina, with three; saw Caesar's cavalry at a distance, commanded by Bivius Curius: upon which, the soldiers immediately abandoned the two pretors, and joined the troops under the conduct of Curius. Several other parties, flying different ways, fell in, some with the foot,otherswith the horse. Cn. Magius of Cremona, Pompey's chief engineer, being taken on his way to Brundusium, was brought to Caesar, who sent him back to Pompey with this message: "That as he had not yet obtained an interview, his design was to come to Brundusium, there to confer with him in relation to the common safety; because they soon would be able to despatch, in a personal treaty, what, if managed by the intervention of others, could not be hindered from running into a tedious negotiation."[^36bd4d688a07416e908f3af20bc69476]

Virgil departed from Corfinium, intending to travel by road to Aesernia, a 43.612787748 mile journey. 

Virgil departed from Aesernia, intending to travel by road to Corfinium, a 43.612787748 mile journey. 

### A story by Julius Caesar about Corfinium from Civil War



Caesar having made himself master of Asculum, and obliged Lentulus to retire, ordered the soldiers who had deserted him, to be sought after, and new levies to be made. He remained only one day there, to settle what related to provisions, and then pursued his march to Corfinium. Upon his arrival there, he found five cohorts, whom Domitius had detached from the garrison, employed in breaking down a bridge about three miles distant from the town. But Caesar's advanced parties attacking them, they quickly abandoned the bridge, and retired to Corfinium. Caesar having passed with his legions, halted before the town, and encamped under the walls.[^351eb04f08944136aede2d521ee57bd6]

Virgil departed from Corfinium, intending to travel by road to Aesernia, a 43.612787748 mile journey. 

Virgil departed from Aesernia, intending to travel by road to Bovianum, a 15.321766118000001 mile journey. 

### A story by Cicero, Marcus Tullius about Bovianum from For Aulus Cluentius



Oppianicus began to entreat the man to show him some method of corrupting the tribunal But he, as was afterwards heard from Oppianicus himself, said that there was no one in the city except himself who could do this. But at first he began to make objections, because he said that he was a candidate for the aedileship with men of the highest rank, and that he was afraid of incurring unpopularity and of giving offence. Afterwards, being prevailed on, he required at first a large sum of money. At last, he came down to what could be managed, and desired six hundred and forty thousand sesterces to be sent to his house. And as soon as this money was brought to him, that most worthless man immediately began to form and adopt the following idea,—that nothing could be more advantageous for his interests than for Oppianicus to be condemned; because, if he were acquitted, he must either distribute the money among the judges, or else restore it to him: but if he were condemned, there would be no one to reclaim it.[^4fca525b8ff447f8aa78137fdbbf1b6b]

Virgil departed from Bovianum, intending to travel by road to Aequum Tuticum, a 38.820774596 mile journey. 

Virgil departed from Aequum Tuticum, intending to travel by road to Bovianum, a 38.820774596 mile journey. 

### A story by Cicero, Marcus Tullius about Bovianum from For Aulus Cluentius



Oppianicus began to entreat the man to show him some method of corrupting the tribunal But he, as was afterwards heard from Oppianicus himself, said that there was no one in the city except himself who could do this. But at first he began to make objections, because he said that he was a candidate for the aedileship with men of the highest rank, and that he was afraid of incurring unpopularity and of giving offence. Afterwards, being prevailed on, he required at first a large sum of money. At last, he came down to what could be managed, and desired six hundred and forty thousand sesterces to be sent to his house. And as soon as this money was brought to him, that most worthless man immediately began to form and adopt the following idea,—that nothing could be more advantageous for his interests than for Oppianicus to be condemned; because, if he were acquitted, he must either distribute the money among the judges, or else restore it to him: but if he were condemned, there would be no one to reclaim it.[^e3fc1141f9ce44c0aeaf43224b2df728]

Virgil departed from Bovianum, intending to travel by road to Aequum Tuticum, a 38.820774596 mile journey. 

Virgil departed from Aequum Tuticum, intending to travel by road to Herdoniae, a 31.343195982 mile journey. 

Virgil departed from Herdoniae, intending to travel by road to Canusium, a 24.347179893 mile journey. 

### A story by Strabo about Canusium from Geography



Now that I have traversed the regions of Old Italy^[i.e., Oenotria (see 6. 1. 15 and 5. 1. 1).] as far as Metapontium, I must speak of those that border on them. And Iapygia borders on them. The Greeks call it Messapia, also, but the natives, dividing it into two parts, call one part (that about the Iapygian Cape)^[Cape Leuca.] the country of the Salentini, and the other the country of the Calabri. Above these latter, on the north, are the Peucetii and also those people who in the Greek language are called Daunii, but the natives give the name Apulia to the whole country that comes after that of the Calabri, though some of them, particularly the Peucetii, are called Poedicli also. Messapia forms a sort of peninsula, since it is enclosed by the isthmus that extends from Brentesium^[See 5. 3. 6 and footnote.] as far as Taras, three hundred and ten stadia. And the voyage thither^[From Brentesium to Taras.] around the Iapygian Cape is, all told, about four hundred^[This figure is wrong. Strabo probably wrote 1,200; Groskurd thinks that he wrote 1,400, but in section 5 (below) the figures for the intervals of the same voyage total 1,220 stadia.] stadia. The distance from Metapontium^[To Taras.] is about two hundred and twenty stadia, and the voyage to it is towards the rising sun. But though the whole Tarantine Gulf, generally speaking, is harborless, yet at the city there is a very large and beautiful harbor,^[Mare Piccolo.] which is enclosed by a large bridge and is one hundred stadia in circumference. In that part of the harbor which lies towards the innermost recess,^[i.e., the part that is immediately to the east of the city, as Tozer (op. cit., p. 183) points out.] the harbor, with the outer sea, forms an isthmus, and therefore the city is situated on a peninsula; and since the neck of land is low-lying, the ships are easily hauled overland from either side. The ground of the city, too, is low-lying, but still it is slightly elevated where the acropolis is. The old wall has a large circuit, but at the present time the greater part of the city—the part that is near the isthmus—has been forsaken, but the part that is near the mouth of the harbor, where the acropolis is, still endures and makes up a city of noteworthy size. And it has a very beautiful gymnasium, and also a spacious market-place, in which is situated the bronze colossus of Zeus, the largest in the world except the one that belongs to the Rhodians. Between the marketplace and the mouth of the harbor is the acropolis, which has but few remnants of the dedicated objects that in early times adorned it, for most of them were either destroyed by the Carthaginians when they took the city or carried off as booty by the Romans when they took the place by storm.^[Tarentum revolted from Rome to Hannibal during the Second Punic War, but was recaptured (209 B.C.) and severely dealt with.] Among this booty is the Heracles in the Capitol, a colossal bronze statue, the work of Lysippus, dedicated by Maximus Fabius, who captured the city. In speaking of the founding of Taras, Antiochus says: After the Messenian war^[743-723 B.C.] broke out, those of the Lacedaemonians who did not take part in the expedition were adjudged slaves and were named Helots,^[On the name and its origin, see 8. 5. 4; also Pauly-Wissowa, Real-Encycl. s.v. "Heloten."] and all children who were born in the time of the expedition were called Partheniae^["Children of Virgins."] and judicially deprived of the rights of citizenship, but they would not tolerate this, and since they were numerous formed a plot against the free citizens; and when the latter learned of the plot they sent secretly certain men who, through a pretence of friendship, were to report what manner of plot it was; among these was Phalanthus, who was reputed to be their champion, but he was not pleased, in general, with those who had been named to take part in the council. It was agreed, however, that the attack should be made at the Hyacinthian festival in the Amyclaeum^[The temple of Amyclaean Apollo.] when the games were being celebrated, at the moment when Phalanthus should put on his leather cap (the free citizens were recognizable by their hair^[i.e., by the length of it. According to Plut. Lys. 1 the wearing of long hair by the Spartans dated back to Lycurgus (the ninth century B.C.), but according to Hdt. 1.82 they wore their hair short till the battle of Thyrea (in the sixth century B.C.), when by legal enactment they began to wear it long.]); but when Phalanthus and his men had secretly reported the agreement, and when the games were in progress, the herald came forward and forbade Phalanthus to put on a leather cap; and when the plotters perceived that the plot had been revealed, some of them began to run away and others to beg for mercy; but they were bidden to be of good cheer and were given over to custody; Phalanthus, however, was sent to the temple of the god^[At Delphi.] to consult with reference to founding a colony; and the god responded, "I give to thee Satyrium, both to take up thine abode in the rich land of Taras and to become a bane to the Iapygians." Accordingly, the Partheniae went thither with Phalanthus, and they were welcomed by both the barbarians and the Cretans who had previously taken possession of the place. These latter, it is said, are the people who sailed with Minos to Sicily, and, after his death, which occurred at the home of Cocalus in Camici,^[Cp. 6. 2. 6.] set sail from Sicily; but on the voyage back^[Back to Crete.] they were driven out of their course to Taras, although later some of them went afoot around the Adrias^[The Adriatic.] as far as Macedonia and were called Bottiaeans. But all the people as far as Daunia, it is said, were called Iapyges, after Iapyx, who is said to have been the son of Daedalus by a Cretan woman and to have been the leader of the Cretans. The city of Taras, however, was named after some hero. But Ephorus describes the founding of the city thus: The Lacedaemonians were at war with the Messenians because the latter had killed their king Teleclus when he went to Messene to offer sacrifice, and they swore that they would not return home again until they either destroyed Messene or were all killed; and when they set out on the expedition, they left behind the youngest and the oldest of the citizens to guard the city; but later on, in the tenth year of the war, the Lacedaemonian women met together and sent certain of their own number to make complaint to their husbands that they were carrying on the war with the Messenians on unequal terms, for the Messenians, staying in their own country, were begetting children, whereas they, having abandoned their wives to widowhood, were on an expedition in the country of the enemy, and they complained that the fatherland was in danger of being in want of men; and the Lacedaemonians, both keeping their oath and at the same time bearing in mind the argument of the women, sent the men who were most vigorous and at the same time youngest, for they knew that these had not taken part in the oaths, because they were still children when they went out to war along with the men who were of military age; and they ordered them to cohabit with the maidens, every man with every maiden, thinking that thus the maidens would bear many more children; and when this was done, the children were named Partheniae. But as for Messene, it was captured after a war of nineteen years, as Tyrtaeus says: "About it they fought for nineteen years, relentlessly, with heart ever steadfast, did the fathers of our fathers, spearmen they; and in the twentieth the people forsook their fertile farms and fled from the great mountains of Ithome." Now the Lacedaemonians divided up Messenia among themselves, but when they came on back home they would not honor the Partheniae with civic rights like the rest, on the ground that they had been born out of wedlock; and the Partheniae, leaguing with the Helots, formed a plot against the Lacedaemonians and agreed to raise a Laconian cap in the market-place as a signal for the attack. But though some of the Helots had revealed the plot, the Lacedaemonians decided that it would be difficult to make a counter-attack against them, for the Helots were not only numerous but were all of one mind, regarding themselves as virtually brothers of one another, and merely charged those who were about to raise the signal to go away from the marketplace. So the plotters, on learning that the undertaking had been betrayed, held back, and the Lacedaemonians persuaded them, through the influence of their fathers, to go forth and found a colony, and if the place they took possession of sufficed them, to stay there, but if not, to come on back and divide among themselves the fifth part of Messenia. And they, thus sent forth, found the Achaeans at war with the barbarians, took part in their perils, and founded Taras. At one time the Tarantini were exceedingly powerful, that is, when they enjoyed a democratic government; for they not only had acquired the largest fleet of all peoples in that part of the world but were wont to send forth an army of thirty thousand infantry, three thousand cavalry, and one thousand commanders of cavalry. Moreover, the Pythagorean philosophy was embraced by them, but especially by Archytas,^[Archytas (about 427-347 B.C.), besides being chosen seven times as chief magistrate ("strategus") of Tarentum, was famous as general, Pythagorean philosopher, mathematician, and author. Aristotle and Aristoxenus wrote works on his life and writings, but both of these works are now lost.] who presided over the city for a considerable time. But later, because of their prosperity, luxury prevailed to such an extent that the public festivals celebrated among them every year were more in number than the days of the year; and in consequence of this they also were poorly governed. One evidence of their bad policies is the fact that they employed foreign generals; for they sent for Alexander^[Alexander I was appointed king of Epeirus by Philip of Macedonia about 342 B.C., and was killed by a Luecanian about 330 B.C. (cp. 6. 1. 5).] the Molossian to lead them in their war against the Messapians and Leucanians, and, still before that, for Archidamus,^[Archidamus III, king of Sparta, was born about 400 B.C. and lost his life in 338 B.C. in this war.] the son of Agesilaüs, and, later on, for Cleonymus,^[Little is know of this Cleonymus, save that he was the son of Cleomenes II, who reigned at Sparta 370-309 B.C.] and Agathocles,^[Agathocles (b. about 361 B.C.—d. 289 B.C.) was a tyrant of Syracuse. He appears to have led the Tarantini about 300 B.C.] and then for Pyrrhus,^[Pyrrhus (about 318-272 B.C.), king of Epeirus, accepted the invitation of Tarentum in 281 B.C.] at the time when they formed a league with him against the Romans. And yet even to those whom they called in they could not yield a ready obedience, and would set them at enmity. At all events, it was out of enmity that Alexander tried to transfer to Thurian territory the general festival assembly of all Greek peoples in that part of the world—the assembly which was wont to meet at Heracleia in Tarantine territory, and that he began to urge that a place for the meetings be fortified on the Acalandrus River. Furthermore, it is said that the unhappy end which befell him^[6. 1. 5.] was the result of their ingratitude. Again, about the time of the wars with Hannibal, they were deprived of their freedom, although later they received a colony of Romans, and are now living at peace and better than before. In their war against the Messapians for the possession of Heracleia, they had the co-operation of the king of the Daunians and the king of the Peucetians. That part of the country of the Iapygians which comes next is fine, though in an unexpected way; for although on the surface it appears rough, it is found to be deep-soiled when ploughed, and although it is rather lacking in water, it is manifestly none the less good for pasturage and for trees. The whole of this district was once extremely populous; and it also had thirteen cities; but now, with the exception of Taras and Brentesium, all of them are so worn out by war that they are merely small towns. The Salentini are said to be a colony of the Cretans. The temple of Athene, once so rich, is in their territory, as also the look-out-rock called Cape Iapygia, a huge rock which extends out into the sea towards the winter sunrise,^[i.e., south-east.] though it bends approximately towards the Lacinium, which rises opposite to it on the west and with it bars the mouth of the Tarantine Gulf. And with it the Ceraunian Mountains, likewise, bar the mouth of the Ionian Gulf; the passage across from it both to the Ceraunian Mountains and to the Lacinium is about seven hundred stadia. But the distance by sea from Taras around to Brentesium is as follows: First, to the small town of Baris, six hundred stadia; Baris is called by the people of today Veretum, is situated at the edge of the Salentine territory, and the trip thither from Taras is for the most part easier to make on foot than by sailing. Thence to Leuca eighty stadia; this, too, is a small town, and in it is to be seen a fountain of malodorous water; the mythical story is told that those of the Giants who survived at the Campanian Phlegra^[See 5. 4. 4 and 5. 4. 6.] and are called the Leuternian Giants were driven out by Heracles, and on fleeing hither for refuge were shrouded by Mother Earth, and the fountain gets its malodorous stream from the ichor of their bodies; and for this reason, also, the seaboard here is called Leuternia. Again, from Leuca to Hydrus,^[Also called Hydruntum; now Otranto.] a small town, one hundred and fifty stadia. Thence to Brentesium four hundred; and it is an equal distance to the island Sason,^[Now Sasena.] which is situated about midway of the distance across from Epeirus to Brentesium. And therefore those who cannot accomplish the straight voyage sail to the left of Sason and put in at Hydrus; and then, watching for a favorable wind, they hold their course towards the harbors of the Brentesini, although if they disembark, they go afoot by a shorter route by way of Rodiae,^[Also called Rudiae; now Rugge.] a Greek city, where the poet Ennius was born. So then, the district one sails around in going from Taras to Brentesium resembles a peninsula, and the overland journey from Brentesium to Taras, which is only a one day's journey for a man well-girt, forms the isthmus of the aforesaid peninsula;^[6. 3. 1.] and this peninsula most people call by one general name Messapia, or Iapygia, or Calabria, or Salentina, although some divide it up, as I have said before.^[6. 3. 1.] So much, then, for the towns on the seacoast. In the interior are Rodiae and Lupiae, and, slightly above the sea, Aletia; and at the middle of the isthmus, Uria, in which is still to be seen the palace of one of the chieftains. When Herodotus^[7. 170.] states that Hyria is in Iapygia and was founded by the Cretans who strayed from the fleet of Minos when on its way to Sicily,^[Cp. 6. 3. 2.] we must understand Hyria to be either Uria or Veretum. Brentesium, they say, was further colonized by the Cretans, whether by those who came over with Theseus from Cnossus or by those who set sail from Sicily with Iapyx (the story is told both ways), although they did not stay together there, it is said, but went off to Bottiaea.^[Cp. 6. 3. 2, where Antiochus says that some of them went to Bottiaea.] Later on, however, when ruled by kings, the city lost much of its country to the Lacedaemonians who were under the leadership of Phalanthus; but still, when he was ejected from Taras, he was admitted by the Brentesini, and when he died was counted by them worthy of a splendid burial. Their country is better than that of the Tarantini, for, though the soil is thin, it produces good fruits, and its honey and wool are among those that are strongly commended. Brentesium is also better supplied with harbors; for here many harbors are closed in by one mouth; and they are sheltered from the waves, because bays are formed inside in such a way as to resemble in shape a stag's horns;^[So, too, the gulf, or bay, at Byzantium resembles a stag's horn (7. 6. 2).] and hence the name, for, along with the city, the place very much resembles a stag's head, and in the Messapian language the head of the stag is called "brentesium."^[Stephanus Byzantinus says: "According to Seleucus, in his second book on Languages, 'brentium' is the Messapian word for 'the head of the stag.'" Hence the editors who emend "brentesium" to "brentium" are almost certainly correct.] But the Tarantine harbor, because of its wide expanse, is not wholly sheltered from the waves; and besides there are some shallows in the innermost part of it.^[Here, as in 6. 3. 1., Strabo is speaking of the inner harbor (Mare Piccolo), not the outer, of which, as Tozer (p. 184) says, Strabo takes no account.] In the case of those who sail across from Greece or Asia, the more direct route is to Brentesium, and, in fact, all who propose to go to Rome by land put into port here. There are two roads^[On these roads see Ashby and Gardner, The Via Trajana, Paper of the British School at Rome, 1916, Vol.VIII, No. 5, pp. 107 ff.] from here: one, a mule-road through the countries of the Peucetii (who are called Poedicli),^[Cp. 6. 3. 1.] the Daunii, and the Samnitae as far as Beneventum; on this road is the city of Egnatia,^[Also spelled Gnathia, Gnatia, and Ignatia; now Torre d'Agnazzo.] and then, Celia,^[Also spelled Caelia; now Ceglie di Bari.] Netium,^[Now Noja.] Canusium, and Herdonia.^[Now Ordona.] But the road by way of Taras, lying slightly to the left of the other, though as much as one day's journey out of the way when one has made the circuit,^[i.e., to the point where it meets the other road, near Beneventum.] what is called the Appian Way, is better for carriages. On this road are the cities of Uria and Venusia, the former between Taras and Brentesium and the latter on the confines of the Samnitae and the Leucani. Both the roads from Brentesium meet near Beneventum and Campania. And the common road from here on, as far as Rome, is called the Appian Way, and passes through Caudium,^[Now Montesarchio.] Calatia,^[Now Galazze.] Capua,^[The old Santa Maria di Capua, now in ruins; not the Capua of today, which is on the site of Casilinum.] and Casilinum to Sinuessa.^[Now Mondragone.] And the places from there on I have already mentioned. The total length of the road from Rome to Brentesium is three hundred and sixty miles. But there is also a third road, which runs from Rhegium through the countries of the Brettii, the Leucani, and the Samnitae into Campania, where it joins the Appian Way; it passes through the Apennine Mountains and it requires three or four days more than the road from Brentesium. The voyage from Brentesium to the opposite mainland is made either to the Ceraunian Mountains and those parts of the seaboard of Epeirus and of Greece which come next to them, or else to Epidamnus; the latter is longer than the former, for it is one thousand eight hundred stadia.^[Strabo has already said the the voyage from Brentesium to Epeirus by way of Sason (Saseno) was about 800 stadia (6. 3. 5). But Strabo was much out of the way, and apparently was not on the regular route. Again, Epidamnus (now Durazzo) is in fact only about 800 stadia distant, not 1,800 as the text makes Strabo say. It is probable, therefore, that Strabo said either simply " for it is 800 stadia," or "for it is 1,000 stadia, while the former is 800.] And yet the latter is the usual route, because the city has a good position with reference both to the tribes of the Illyrians and to those of the Macedonians. As one sails from Brentesium along the Adriatic seaboard, one comes to the city of Egnatia, which is the common stopping-place for people who are travelling either by sea or land to Barium;^[Now Bari.] and the voyage is made with the south wind. The country of the Peucetii extends only thus far^[To Barium.] on the sea, but in the interior as far as Silvium.^[Silvium appears to have been on the site of what is now Garagone.] All of it is rugged and mountainous, since it embraces a large portion of the Apennine Mountains; and it is thought to have admitted Arcadians as colonists. From Brentesium to Barium is about seven hundred stadia, and Taras is about an equal distance from each. The adjacent country is inhabited by the Daunii; and then come the Apuli, whose country extends as far as that of the Frentani. But since the terms "Peucetii" and "Daunii" are not at all used by the native inhabitants, except in early times, and since this country as a whole is now called Apulia, necessarily the boundaries of these tribes cannot be told to a nicety either, and for this reason neither should I myself make positive assertions about them. From Barium to the Aufidus River, on which is the Emporium of the Canusitae^[This Emporium should probably be identified with the Canne of today (see Ashby and Gardner, op. cit., p. 156).] is four hundred stadia and the voyage inland to Emporium is ninety. Near by is also Salapia,^[Now Salpi.] the seaport of the Argyrippini. For not far above the sea (in the plain, at all events) are situated two cities, Canusium^[Now Canosa.] and Argyrippa,^[Now Arpino.] which in earlier times were the largest of the Italiote cities, as is clear from the circuits of their walls. Now, however, Argyrippa is smaller; it was called Argos Hippium at first, then Argyrippa, and then by the present name Arpi. Both are said to have been founded by Diomedes.^[Cp. 5. 1. 9.] And as signs of the dominion of Diomedes in these regions are to be seen the Plain of Diomedes and many other things, among which are the old votive offerings in the temple of Athene at Luceria—a place which likewise was in ancient times a city of the Daunii, but is now reduced—and, in the sea near by, two islands that are called the Islands of Diomedes, of which one is inhabited, while the other, it is said, is desert; on the latter, according to certain narrators of myths, Diomedes was caused to disappear, and his companions were changed to birds, and to this day, in fact, remain tame and live a sort of human life, not only in their orderly ways but also in their tameness towards honorable men and in their flight from wicked and knavish men. But I have already mentioned the stories constantly told among the Heneti about this hero and the rites which are observed in his honor.^[Cp. 5. 1. 9.] It is thought that Sipus^[In Latin, Sipontum; now in ruins, near Santa Maria di Siponto.] also was founded by Diomedes, which is about one hundred and forty stadia distant from Salapia; at any rate it was named "Sepius" in Greek after the "sepia"^[Cuttle-fish.] that are cast ashore by the waves. Between Salapia and Sinus is a navigable river, and also a large lake that opens into the sea; and the merchandise from Sipus, particularly grain, is brought down on both. In Daunia, on a hill by the name of Drium, are to be seen two hero-temples: one, to Calchas, on the very summit, where those who consult the oracle sacrifice to his shade a black ram and sleep in the hide, and the other, to Podaleirius, down near the base of the hill, this temple being about one hundred stadia distant from the sea; and from it flows a stream which is a cure-all for diseases of animals. In front of this gulf is a promontory, Garganum, which extends towards the east for a distance of three hundred stadia into the high sea; doubling the headland, one comes to a small town, Urium, and off the headland are to be seen the Islands of Diomedes. This whole country produces everything in great quantity, and is excellent for horses and sheep; but though the wool is softer than the Tarantine, it is not so glossy. And the country is well sheltered, because the plains lie in hollows. According to some, Diomedes even tried to cut a canal as far as the sea, but left behind both this and the rest of his undertakings only half-finished, because he was summoned home and there ended his life. This is one account of him; but there is also a second, that he stayed here till the end of his life; and a third, the aforesaid mythical account, which tells of his disappearance in the island; and as a fourth one might set down the account of the Heneti, for they too tell a mythical story of how he in some way came to his end in their country, and they call it his apotheosis. Now the above distances are put down in accordance with the data of Artemidorus;^[Artemidorus (flourished about 100 B.C.), of Ephesus, was an extensive traveller and a geographer of great importance. He wrote a geography of the inhabited world in eleven books, a Periplus of the Mediterranean, and Ionian Historical Sketches. But his works, except numerous fragments preserved in other authors, are now lost.] but according to the Chorographer,^[See 5. 2. 7 and footnote.] the distances from Brentesium as far as Garganum^[Monte Gargano.] amount to one hundred and sixty-five miles, whereas according to Artemidorus they amount to more; and thence to Ancona two hundred and fifty-four miles according to the former, whereas according to Artemidorus the distance to the Aesis River, which is near Ancona, is one thousand two hundred and fifty stadia, a much shorter distance. Polybius states that the distance from Iapygia has been marked out by miles, and that the distance to the city of Sena^[Sena Gallica; now Sinigaglia.] is five hundred and sixty-two miles, and thence to Aquileia one hundred and seventy-eight. And they do not agree with the commonly accepted distance along the Illyrian coastline, from the Ceraunian Mountains to the recess of the Adrias,^[The Adriatic.] since they represent this latter coasting voyage as over six thousand stadia,^[Polybius here gives the total length of the coastline on the Italian side as 740 miles, or 6,166 stadia (8 1/3 stadia to the mile; see 7. 7. 4), and elsewhere (2. 4. 3) Strabo quotes him as reckoning the length of the Illyrian coastline from the Ceraunian Mts. only to Iapygia (not including Istria) as 6,150 stadia. Cp. also 7. 5. 3, 4, 10.] thus making it even longer than the former, although it is much shorter. However, every writer does not agree with every other, particularly about the distances, as I often say.^[Cp. 1. 2. 13; 2. 1. 7-8, and 2. 4. 3.] As for myself, where it is possible to reach a decision, I set forth my opinion, but where it is not, I think that I should make known the opinions of others. And when I have no opinion of theirs, there is no occasion for surprise if I too have passed something by, especially when one considers the character of my subject; for I would not pass by anything important, while as for little things, not only do they profit one but slightly if known, but their omission escapes unnoticed, and detracts not at all, or else not much, from the completeness of the work.^[Cp. 1. 1. 23.] The intervening space, immediately after Cape Garganum, is taken up by a deep gulf; the people who live around it are called by the special name of Apuli, although they speak the same language as the Daunii and the Peucetii, and do not differ from them in any other respect either, at the present time at least, although it is reasonable to suppose that in early times they differed and that this is the source of the three diverse names for them that are now prevalent. In earlier times this whole country was prosperous, but it was laid waste by Hannibal and the later wars. And here too occurred the battle of Cannae, in which the Romans and their allies suffered a very great loss of life. On the gulf is a lake; and above the lake, in the interior, is Teanum Apulum,^[Passo di Civita.] which has the same name as Teanum Sidicinum. At this point the breadth of Italy seems to be considerably contracted, since from here to the region of Dicaearcheia^[Puteoli.] an isthmus is left of less than one thousand stadia from sea to sea. After the lake comes the voyage along the coast to the country of the Frentani and to Buca;^[Now Termoli.] and the distance from the lake either to Buca or to Cape Garganum is two hundred stadia. As for the places that come next after Buca, I have already mentioned them.^[5. 4. 2.][^93f0150da5924654833de13d95eeb841]

Virgil departed from Canusium, intending to travel by road to Barium, a 44.372724481 mile journey. 

### A story by Flavius Josephus about Barium from Jewish Antiquities



Now all the writers of barbarian histories make mention of this flood, and of this ark; among whom is Berosus the Chaldean. For when he is describing the circumstances of the flood, he goes on thus: "It is said there is still some part of this ship in Armenia, at the mountain of the Cordyaeans; and that some people carry off pieces of the bitumen, which they take away, and use chiefly as amulets for the averting of mischiefs." Hieronymus the Egyptian also, who wrote the Phoenician Antiquities, and Mnaseas, and a great many more, make mention of the same. Nay, Nicolaus of Damascus, in his ninety-sixth book, hath a particular relation about them; where he speaks thus: "There is a great mountain in Armenia, over Minyas, called Baris, upon which it is reported that many who fled at the time of the Deluge were saved; and that one who was carried in an ark came on shore upon the top of it; and that the remains of the timber were a great while preserved. This might be the man about whom Moses the legislator of the Jews wrote."[^6a6323cac2d84299830e5717e09b9376]

Virgil departed from Barium, intending to travel by ship, down the coast to Ancona, a 262.95799349 mile journey. 

### A story by E. T. Merrill about Ancona from Commentary on Catullus



Catullus calls upon the Annals of Volusius to aid him in the discharge of a vow made by Lesbia, invokes Venus to recognize the payment, and with the word throws the Annals into the fire.—The poem was evidently written ahout 59 or 58 B.C., in the short period of reconciliation after the temporary coolness marked by Catul. 8.1ff.; cf. Intr. 19f.—Meter, Phalaecean.

annales: probably chronicles in verse, after the fashion of the famous Annals of Ennius.

Volusi: cf. Intr. 75.

cacata charta: defiled sheets; the verses were so wretched that they but spoiled good paper.

mea puella: i.e. Lesbia; cf. Catul. 3.3n.

sanctae: divine; cf. Catul. 68.5 sancta Venus ; Catul. 64.95 sancte puer [Cupido] ; Catul. 64.298 pater divum sancta cum coniuge ; Catul. 64.268 sanctis divis.

Veneri Cupidinique: cf. Catul. 3.1n.

truces iambos: the traditional weapons of satire since the time of Archilochus; cf. Catul. 12.10n.; Hor. Carm. 1.16.22 me quoque pectoris fervor in celeres iambos misit furentem ; Hor. AP 79 Archilochum proprio rabies armavit iambo : the poems here meant are Catul. 8.1ff. and, perhaps, Catul. 37.1ff., possibly with others not included in the final _liber Catulli._

electissima: choicest from their badness, the worst; with the frony of meaning cf. Catul. 33.1 optime ; Catul. 37.14 boni beatique

pessimi poetae: so Lesbia had in a pet called Catullus, in that he made her uncomfortable by his _truces iambi_; and she would, of course, dedicate to Vulcan not the bad poetry of some undetermined poetaster, but the particular verses that had stung her, which would naturally be destroyed after a reconciliation as painful memorials (cf. Hor. Carm. 1.16 on a similar occasion). Catullus now playfully ignores the real meaning of her words, and pitches upon Volusius as the _pessimus poeta_ of his acquaintance, whose works are therefore due to Vulcan.

tardipedi deo: i.e. Vulcan, who was lamed by the fall from heaven to Lemnos (Hom. Il. 1.586ff.); cf. Tib. 1.9.49 illa velim rapida Volcanus carmina flamma torreat ; Quint. 8.6.24 Vulcanum pro igne vulgo audimus.

infelicibus lignis: cf. Macrob. 3.20.3 arbores quae inferum deorum avertentiumque in tutela sunt, eas infelices nominant … quibus portenta prodigiaque mala comburi iubere oportet ; Legg. Regg. ap. Liv. 1.26 infelici arbori reste suspendito [perduellionem].

hoc: sc. _votum_.

pessima puella: spoken jestingly (cf. Catul. 55.10), but in reminiscence of the same term applied by her to him (v. 6), which he now attempts to pass on to the unfortunate Volusius.

iocose lepide: Catullus asserts (of course without foundation) that the vow was made sportively in the sense in which he has just interpreted it.

nunc: the moment of consummation of the vow has come, and the poet as officiating priest stands ready with the offering, and begins the final prayer.

caeruleo creata ponto: by early tradition Aphrodite was born of the sea-foam: cf. Hes. Theog. 195; Anacr. 54, etc. Note the solemn effect of the manifold address, with which cf. the prayer of Chryses to Phoebus, Hom. Il. 1.37ff., etc.

Idalium: a town and wooded mountain of Cyprus, whereon stood a renowned temple of Aphrodite; cf. Catul. 61.17; Catul. 64.96; Verg. A. 1.680 hunc super alta Cythera aut super Idalium recondam ; Verg. A. 1.692 in altos Idaliae lucos.

Urios: apparently an otherwise unknown parallel form for _Urium_ (Ptol. 3.1.17; Strab. VI. 3.9.), the name of a town which lay at the foot of Mons Garganus in Apulia, on the bay of Urias (Mela 2.4.66). Its connection with the worship of Venus is unknown, though Ellis ascribes it to the association of this district with Diomedes (Verg. A. 8.9), who founded cities (e.g. Venusia) and temples in honor of Aphrodite (Serv. on Verg. A. 11.246).

apertos, storm-beaten; Mela says the bay was _pleraque asper accessu._

Ancona (from the Greek form \rendergreek{Ἀγκών}): this well-known city of Picenum contained a temple of Venus Marina; cf. Juv. 4.40 domum Veneris, quam Dorica sustinet Ancon.

Cnidum: in this famous city at the extremity of the Cnidian Chersonese in Caria were several temples of Aphrodite, and the renowned statue of the goddess by Praxiteles.

harundinosam: the reeds of Cnidus were a great article of export on account of their excellence for manufacture into paper; cf. Plin. NH 16.157; Aus. Ep. 7.49 nec iam fissipedis per calami vias grassetur Cnidiae sulcus harundinis.

Amathunta: a seaport town of southern Cyprus, where the Adonis cult was especially carried on; cf. Catul. 68.51 duplex Amathusia (of Venus).

Golgos: this town of Cyprus held, according to Paus. 8.5.2, the oldest shrine of Aphrodite; cf. Theocr. 15.100 δέσποιν᾽ ἃ Γολγώς τε καὶ Ἰδάλιον ἐφίλασας .

Durrachium: formerly called Epidamnus, a seaport in southern Illyria, and the common port of arrival and departure for the passenger traffic between Italy and the East; hence _Hadriae tabernam._

acceptum face: i.e. discharge the account, now that the vow is to be paid; cf. the commercial term in Cic. Rosc. Com. 1.4 in codice accepti . On _face_ see Catul. 34.8n.

Si: etc. cf. Catul. 6.2 and Catul. 10.4; if Catullus had not departed from the strict form of the vow by offering a witty equivalent for the forfeited pledge, there would be no point to the _si_-clause. With _si_ in this sense, putting deferentially a fact that must be generally conceded (= _si quidem_), cf. Catul. 76.19.

at: turning from the previous thought and beginning the final malediction, as in Catul. 3.13; Catul. 27.5; Catul. 28.14.

interea: cf. Catul. 14.21n.

pleni ruris: etc. cf. Catul. 22.14n.

annales: etc. with the repetition of the opening verse cf. Catul. 16.1ff., Catul. 52.1ff., and Catul. 57.1ff.[^4081644764414708ae3ade45710bf300]

Virgil departed from Ancona, intending to travel by ship, down the coast to Pola, a 99.776648325 mile journey. 

Virgil departed from Pola, intending to travel by ship, down the coast to Ancona, a 99.776648325 mile journey. 

### A story by Cicero, Marcus Tullius about Ancona from Philippics



For what can be more unreasonable than for us to pass resolutions about peace without the knowledge of those men who wage the war! And not only without their knowledge, but even against their will? Do you think that Aulus Hirtius, that most illustrious consul, and that Caius Caesar, a man born by the especial kindness of the gods for this especial crisis, whose letters, announcing their hope of victory, I hold in my hand, are desirous of peace? They are anxious to conquer; and they wish to obtain that most delightful and beautiful condition of peace, as the consequence of victory, not of some agreement. What more? With what feelings do you think that Gaul will hear of this proceeding? For that province performs the chief part in repelling, and managing, and supporting this war. Gaul, following the mere nod, for I need not say the command of Decimus Brutus, has strengthened the beginning of the war with her arms, her men, and her treasures: she has exposed the whole of her body to the cruelty of Marcus Antonius: she is drained, laid waste, attacked with fire and sword. She is enduring all the injuries of war with equanimity, contented as long as she can ward off the danger of slavery.[^a2d318b8d42b464989053685b6e5eb50]

Virgil departed from Ancona, intending to travel by ship, down the coast to Castrum Truentinum, a 60.742743476 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by ship, down the coast to Ancona, a 60.742743476 mile journey. 

### A story by E. T. Merrill about Ancona from Commentary on Catullus



On Mentula as a 'land-poor' property owner. On the identity of Mentula with Mamurra see Intr. 73. The next poem speaks of the same estate as this.

Firmanus: Firmum, now Fermo, was a town in Picenum, about forty miles south of Ancona.

saltu: the word denoted first uncultivated land (cf. Fest. p. 302 sallus est ubi silvae et pastiones sunt, quarum causa casae quoque ), and then a measure of 800 _iugera_ as a single grant of such land by the land-commissions (Varr. R. R. 1.10.2), and then the grant in general, an 'estate,' even though comprising, as here, some arable land (cf. Fest. l.c. _si qua particula in eo saltu pastorum aut custodum causa aratur, ea res non peremit nomen saltui_).

tot res egregias: spoken ironically, like _non fulso_ in v. 1, for Catul. 115.1ff. shows that the fine things specified in Catul. 114.3 are but supposed attractions of the estate, which is really a small and worthless affair.

omne genus: accusative of specification.

exsuperat: sc. probably _saltus_ as subject; the estate is good for nothing, and its necessary expenses more than eat up the income from it.

concedo: etc. i. e. I grant, then, that he is rich, if a man can be rich who hasn't a cent to his name.

laudemus: etc. i. e. let us praise the estate, if praise can mean anything when the owner hasn't a roof over his head.

domo: with hiatus; see Intr. 86d.

ipse: the owner; cf. Catul. 64.43n.[^f76724f9e9e145aaaf465f1560779eef]

Virgil departed from Ancona, intending to travel by ship, down the coast to Castrum Truentinum, a 60.742743476 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by ship, down the coast to Aternum, a 38.822017338 mile journey. 

Virgil departed from Aternum, intending to travel by road to Larinum, a 63.420852486 mile journey. 

### A story by Cicero, Marcus Tullius about Larinum from For Aulus Cluentius



I, O judges, am thoroughly aware that I am under taking a cause which has now for eight years together been constantly discussed in a spirit opposed to the interests of my client, and which has been almost convicted and condemned by the silent opinion of men; but if any god will only incline your good-will to listen to me patiently, I will show you that there is nothing which a man has so much reason to dread as envy,—that when he has incurred envy, there is nothing so much to be desired by an innocent man as an impartial tribunal, because in this alone can any end and termination be found at last to undeserved disgrace. Wherefore, I am in very great hope, if I am able fully to unravel all the circumstances of this case, and to effect all that I wish by my speech, that this place, and this bench of judges before whom I am pleading, which the other side has expected to be most terrible and formidable to Aulus Cluentius, will be to him a harbour at last, and a refuge for the hitherto miserable and tempest-tossed bark of his fortunes.[^b29abcf9e90d4a38bbba6c2fcedd19b9]

Virgil departed from Larinum, intending to travel by road to Aternum, a 63.420852486 mile journey. 

Virgil departed from Aternum, intending to travel by ship, down the coast to Castrum Truentinum, a 38.822017338 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by ship, down the coast to Aternum, a 38.822017338 mile journey. 

Virgil departed from Aternum, intending to travel by ship, down the coast to Castrum Truentinum, a 38.822017338 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a 17.434427518 mile journey. 

Virgil departed from Asculum, intending to travel by road to Castrum Truentinum, a 17.434427518 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a 17.434427518 mile journey. 

Virgil departed from Asculum, intending to travel by road to Castrum Truentinum, a 17.434427518 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by ship, down the coast to Ancona, a 60.742743476 mile journey. 

### A story by Cicero, Marcus Tullius about Ancona from Philippics



For what can be more unreasonable than for us to pass resolutions about peace without the knowledge of those men who wage the war! And not only without their knowledge, but even against their will? Do you think that Aulus Hirtius, that most illustrious consul, and that Caius Caesar, a man born by the especial kindness of the gods for this especial crisis, whose letters, announcing their hope of victory, I hold in my hand, are desirous of peace? They are anxious to conquer; and they wish to obtain that most delightful and beautiful condition of peace, as the consequence of victory, not of some agreement. What more? With what feelings do you think that Gaul will hear of this proceeding? For that province performs the chief part in repelling, and managing, and supporting this war. Gaul, following the mere nod, for I need not say the command of Decimus Brutus, has strengthened the beginning of the war with her arms, her men, and her treasures: she has exposed the whole of her body to the cruelty of Marcus Antonius: she is drained, laid waste, attacked with fire and sword. She is enduring all the injuries of war with equanimity, contented as long as she can ward off the danger of slavery.[^cc14917553db4e47850ff9916cbe27e2]

Virgil departed from Ancona, intending to travel by ship, down the coast to Castrum Truentinum, a 60.742743476 mile journey. 

Virgil departed from Castrum Truentinum, intending to travel by road to Asculum, a 17.434427518 mile journey. 

Virgil departed from Asculum, intending to travel by road to Reate, a 59.120965166 mile journey. 

### A story by Suetonius ca. 69-ca. 122 about Reate from Divus Vespasianus



Vespasian was born in the country of the Sabines, between the Reate, and a little country-seat called Phalacrine, upon the fifth of the calends of December [27th November], in the evening, in the consulship of Quintus Sulpicius Camerinus and Caius Poppaeus Sabinus, five years before the death of Augustus;^[A.U.C. 762. A.D. 10] and was educated under the care of Tertulla, his grandmother by the father's side, upon an estate belonging to the family, at Cosa.^[Cosa was a place in the Volscian territory; of which Anagni was probably the chief town. It lies about forty miles to the north-east of Rome.] After his advancement to the empire, he used frequently to visit the place where he had spent his infancy; and the villa was continued in the same condition, that he might see every thing about him just as he had been used to do. And he had so great a regard for the memory of his grandmother, that, upon solemn occasions and festival days, he constantly drank out of a silver cup which she had been accustomed to use. After assuming the manly habit, he had a long time a distaste for the senatorian toga, though his brother had obtained it- nor could he be persuaded by any one but his mother to sue for that badge of honour. She at length drove him to it, more by taunts and reproaches, than by entreaties and authority, calling him now and then, by way of reproach, his brother's footman. He served as military tribune in Thrace. When made quaestor, the province of Crete and Cyrene fell to him by lot. He was candidate for the aedileship, and soon after for the praetorship, but met with a repulse in the former case; though at last, with much difficulty, he came in sixth on the poll-books. But the office of praetor he carried upon his first canvass, standing amongst the highest at the poll. Being incensed against the senate, and desirous to gain, by all possible means, the good graces of Caius,^[Caligula] he obtained leave to exhibit extraordinary^[These games were extraordinary, as being out of the usual course of those given by praetors. ] games for the emperor's victory in Germany, and advised them to increase the punishment of the conspirators against his life, by exposing their corpses unburied. He likewise gave him thanks in that august assembly for the honour of being admitted to his table.[^a929b0124cfd480fba1e9926ce0a981f]

[^03327f494118404583fd5a919e2d5d65]: From the Perseus Digital Library:      Livy. History of Rome. English Translation by. Rev. Canon Roberts. New York, New York. E. P. Dutton and Co. 1912. 1. Livy. History of Rome. English Translation. Rev. Canon Roberts. New York, New York. E. P. Dutton and Co. 1912. 2.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0914.phi0011.perseus-eng3:24> }  



[^4efc643811af4e329882b9090e7d139a]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962.

    \tiny{ <http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:1.6> }  



[^e2ae9f50109149f78e488529b8ff0400]: From the Perseus Digital Library:      Histories. Polybius. Evelyn S. Shuckburgh. translator. London, New York. Macmillan. 1889. Reprint Bloomington 1962.

    \tiny{ <http://data.perseus.org/citations/urn:cts:greekLit:tlg0543.tlg001.perseus-eng1:6.14> }  



[^c6fe8baaf1374ae58104067ba8dc3985]: From the Perseus Digital Library:      Vergil. Aeneid. John Dryden. trans. XXX. XXX. XXX.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0690.phi003.perseus-eng1:7.601> }  



[^28715070ddcf483f8c0815666c9904ed]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo014.perseus-eng1:21> }  



[^226a815df2c54c3f8691a05a4bced9d9]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi035.perseus-eng1:13.7> }  



[^b7200a34f3b54ed6aac19ec24265cf7a]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi035.perseus-eng1:13.9> }  



[^6db459e000c34fc1ae92f4fd96b10c2d]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.24> }  



[^36bd4d688a07416e908f3af20bc69476]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.24> }  



[^351eb04f08944136aede2d521ee57bd6]: From the Perseus Digital Library:      C. Julius Caesar. The Commentaries of Caesar. William Duncan. St. Louis. Edwards and Bushnell. 1856.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0448.phi002.perseus-eng1:1.16> }  



[^4fca525b8ff447f8aa78137fdbbf1b6b]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi010.perseus-eng1:69> }  



[^e3fc1141f9ce44c0aeaf43224b2df728]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi010.perseus-eng1:69> }  



[^93f0150da5924654833de13d95eeb841]: From the Perseus Digital Library:      Strabo. ed. H. L. Jones, The Geography of Strabo. Cambridge, Mass.: Harvard University Press; London: William Heinemann, Ltd. 1924.

    \tiny{ <http://data.perseus.org/citations/urn:cts:greekLit:tlg0099.tlg001.perseus-eng1:6.3> }  



[^6a6323cac2d84299830e5717e09b9376]: From the Perseus Digital Library:      Flavius Josephus. The Works of Flavius Josephus. Translated by. William Whiston, A.M. Auburn and Buffalo. John E. Beardsley. 1895.

    \tiny{ <http://data.perseus.org/citations/urn:cts:greekLit:tlg0526.tlg001.perseus-eng1:1.93> }  



[^4081644764414708ae3ade45710bf300]: From the Perseus Digital Library: Perseus Digital Library

    \tiny{ <http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=36> } 



[^a2d318b8d42b464989053685b6e5eb50]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi035.perseus-eng1:12.9> }  



[^f76724f9e9e145aaaf465f1560779eef]: From the Perseus Digital Library: Perseus Digital Library

    \tiny{ <http://www.perseus.tufts.edu/hopper/xmlchunk?doc=Perseus:text:1999.02.0004:text=comm:poem=114> } 



[^b29abcf9e90d4a38bbba6c2fcedd19b9]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge, B. A. London. Henry G. Bohn, York Street, Covent Garden. 1856.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi010.perseus-eng1:7> }  



[^cc14917553db4e47850ff9916cbe27e2]: From the Perseus Digital Library:      M. Tullius Cicero. The Orations of Marcus Tullius Cicero, literally translated by C. D. Yonge. London. George Bell & Sons. 1903.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi0474.phi035.perseus-eng1:12.9> }  



[^a929b0124cfd480fba1e9926ce0a981f]: From the Perseus Digital Library:      Suetonius: The Lives of the Twelve Caesars; An English Translation, Augmented with the Biographies of Contemporary Statesmen, Orators, Poets, and Other Associates. Suetonius. Publishing Editor. J. Eugene Reed. Alexander Thomson. Philadelphia. Gebbie & Co. 1889.

    \tiny{ <http://data.perseus.org/citations/urn:cts:latinLit:phi1348.abo020.perseus-eng1:2> }  



