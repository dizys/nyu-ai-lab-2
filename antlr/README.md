# BNF Parser in ANTLR4

[ANTLR4](https://www.antlr.org/) grammar rules for BNF. Includes the Makefile to build parsers in Java, Python, Golang, JavaScript and TypeScript.

## Prerequisites

-   Java 1.7+
-   Python 3.5+
-   Golang 1.5+
-   Node.js 14+
-   GNU make

## Development guide

**1. Installing ANTLR4**

Official guidance: [read](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md)

**2. Get the Python3 ANTLR runtime**

From the [official guidance](https://github.com/antlr/antlr4/blob/master/doc/python-target.mdd):

```bash
pip install antlr4-python3-runtime
```

**3. Generate parsers for different runtimes**

```bash
make
```

The source of the parsers will be available at folder `java`, `python`, `go` and `js` respectively.

**4. Test your Java parser**

Run the parser with the analysis tool `grun`:

```bash
cd java
javac *.java
grun BNF bnf -tree
```

Input your rule and press `Ctrl` + `D` to end the input stream. The parse tree (AST) will be displayed.

## Grammar

Parser rules (precedence of the operators are as in the order they appear):

```EBNF
<BNF> ::= <BNF_RULE> (nl <BNF_RULE>)*
<BNF_RULE> ::= <CLAUSE>
<CLAUSE> ::= atom
            | not <CLAUSE>
            | <CLAUSE> and <CLAUSE>
            | <CLAUSE> or <CLAUSE>
            | <CLAUSE> implies <CLAUSE>
            | <CLAUSE> iff <CLAUSE>
            | left_paren <CLAUSE> right_paren
```

Tokens (terminals):

```yml
left_paren: '('
right_paren: ')'

and: '&' | '∧'
or: '|'| '∨'
not: '!' | '¬'

iff: '<=>'
implies: '=>'

atom: [a-zA-Z0-9]+

nl: '\n'
```

ANTLR4 grammar file at [BNF.g4](./BNF.g4).
