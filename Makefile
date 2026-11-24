PYTHON ?= python3

.PHONY: all pdf review abstract watch clean

all: pdf

pdf: abstract.txt
	latexmk main.tex

review: abstract.txt
	latexmk -outdir=build/review review.tex

abstract: abstract.txt

abstract.txt: sections/abstract.tex scripts/abstract-text.py
	$(PYTHON) scripts/abstract-text.py $< $@

watch: abstract.txt
	latexmk -pvc -view=none main.tex

clean:
	latexmk -C main.tex
	latexmk -outdir=build/review -C review.tex
	rm -f abstract.txt
