.PHONY: all pdf watch clean

all: pdf

pdf:
	latexmk main.tex

watch:
	latexmk -pvc -view=none main.tex

clean:
	latexmk -C main.tex
