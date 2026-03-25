# CV build targets
# Requires: pandoc, wkhtmltopdf or pandoc with pdf engine

SRC = README.md
NAME = brad-phelan-cv

.PHONY: all pdf html clean

all: pdf html

pdf:
	pandoc $(SRC) -o $(NAME).pdf \
		--pdf-engine=wkhtmltopdf \
		--css style.css \
		-V margin-top=20 \
		-V margin-bottom=20 \
		-V margin-left=25 \
		-V margin-right=25

html:
	pandoc $(SRC) -o $(NAME).html \
		--standalone \
		--css style.css

clean:
	rm -f $(NAME).pdf $(NAME).html
