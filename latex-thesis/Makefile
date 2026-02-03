all: main.pdf

main.pdf: main.tex references.bib $(wildcard latex-thesis-chapters/*.tex)
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.bcf *.xml *.pdf

.PHONY: all clean
