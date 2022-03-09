# BNF Parser in ANTLR4

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
