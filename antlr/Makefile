ANTLR4_BIN = java org.antlr.v4.Tool
GRAMMAR_FILE = BNF.g4

.PHONY: java python go js ts clean

all: java python go js ts

java:
	$(ANTLR4_BIN) $(GRAMMAR_FILE) -o java

python:
	$(ANTLR4_BIN) -Dlanguage=Python3 $(GRAMMAR_FILE) -o python

go:
	$(ANTLR4_BIN) -Dlanguage=Go $(GRAMMAR_FILE) -o go/parser

js:
	$(ANTLR4_BIN) -Dlanguage=JavaScript $(GRAMMAR_FILE) -o js

ts:
	yarn install
	yarn antlr4ts -visitor $(GRAMMAR_FILE) -o ts

clean:
	rm -rf java python go js ts
