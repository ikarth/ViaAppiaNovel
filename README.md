# Via Appia Novel
Via Appia Novel Generator for NaNoGenMo 2015

## NaNoGenMo 20145
National Novel Generation Month Project 2015

[NaNoGenMo 2015](https://github.com/dariusk/NaNoGenMo-2015): It started as a joke on Twitter by Darius Kazemi and grew into an entire month of people creating novel-writing generators. This one is mine.

A [thread about its development can be found here](https://github.com/dariusk/NaNoGenMo-2015/issues/15).

The final NaNoGenMo edition of the novel is here: [Virgil's Commonplace Book](https://github.com/ikarth/ViaAppiaNovel/blob/master/via_appia_nanogenmo.pdf?raw=true)

This project and my [erat_viator](https://twitter.com/erat_viator) twitterbot project are conceptually linked.

## Previous projects

I've also done novel generators for all of the past NaNoGenMos:

For 2014, [The Infinite Garden of One Thousand and One Stories](https://github.com/ikarth/nonogen)

For 2013, [Gutenberg Shuffle](https://github.com/ikarth/nanogenmo)

## About the generator
The book generator is a Python program that outputs a Markdown text file designed to be converted into PDF form via Pandoc.

    pandoc output.markdown -S --normalize --toc \\
    -o via_appia_test.pdf --latex-engine=xelatex \\
    --template novel_template.latex \\
    --variable otherlangs=polutonikogreek,greek \\
    --variable lang="english" -V geometry:paperwidth=6in \\
    -V geometry:paperheight=9in -V geometry:margin=.9in \\
    -V fontfamily:"DejaVu Serif" -V linestretch:1.2 \\
    -V documentclass=book

Requirements.txt specifies an overkill of libraries because I used the same virtual environment to develop three separate procedural generation projects this month. You probably don't need two separate twitter libraries and NLTK to run this. Probably.

## License

Copyright © 2015 Isaac J. Karth

Distributed under the MIT License. See LICENSE for details.
