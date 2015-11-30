pandoc output.markdown -S --normalize --toc -o via_appia_test.pdf --latex-engine=xelatex --template novel_template.latex --variable otherlangs=polutonikogreek,greek --variable lang="english" -V geometry:paperwidth=6.0in  -V geometry:paperheight=9.0in -V geometry:inner=1.2in -V geometry:outer=0.8in -V geometry:margin=.9in -V fontfamily:"DejaVu Serif" -V linestretch:1.2 -V documentclass=book