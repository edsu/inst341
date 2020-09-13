all: index slides.html

index:
	pandoc -o index.html README.md

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md
