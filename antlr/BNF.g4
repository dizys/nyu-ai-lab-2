grammar BNF;

bnf: bnf_rule (NL+ bnf_rule)* NL* EOF;

bnf_rule: clause;

clause:
	ATOM
	| NOT clause
	| clause AND clause
	| clause OR clause
	| clause IMPLIES clause
	| clause IFF clause
	| LEFT_PAREN clause RIGHT_PAREN;

LEFT_PAREN: '(';
RIGHT_PAREN: ')';

AND: '&' | '∧' | '^';
OR: '|' | '∨';
NOT: '!' | '¬';

IFF: '<=>' | '⇔';
IMPLIES: '=>' | '⇒';

ATOM: [a-zA-Z0-9_]+;

NL: '\n';

WS: [ \t]+ -> skip;

ErrorCharacter: .;
