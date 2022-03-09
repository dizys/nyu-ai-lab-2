from distutils.command.build_scripts import first_line_re
from typing import Dict, List, Tuple


def text_to_cnf_rep(text: str) -> List[List[Tuple[str, bool]]]:
    """
    Converts a text to a CNF representation.

    :param text: The text to convert.
    :return: The CNF representation of the text.
    """

    lines = text.strip().split('\n')
    cnf_rep = []
    for line in lines:
        line = line.strip()
        clause: List[Tuple[str, bool]] = []
        atoms = line.split(' ')
        for atom in atoms:
            atom = atom.strip()
            if atom == '':
                continue
            if atom[0] == '!' or atom[0] == '~' or atom[0] == '¬':
                clause.append((atom[1:], False))
            else:
                clause.append((atom, True))
        clause.sort(key=lambda x: x[0])
        cnf_rep.append(clause)
    return cnf_rep


def cnf_rep_to_text(cnf_rep: List[List[Tuple[str, bool]]]) -> str:
    """
    Converts a CNF representation to a text.

    :param cnf_rep: The CNF representation to convert.
    :return: The text representation of the CNF.
    """

    lines = []
    for clause in cnf_rep:
        clause_str = ''
        first_in_clause = True
        for atom in clause:
            if first_in_clause:
                first_in_clause = False
            else:
                clause_str += ' '
            if atom[1]:
                clause_str += atom[0]
            else:
                clause_str += '!' + atom[0]
        lines.append(clause_str)
    return '\n'.join(lines)


def bnf_to_cnf_rep(bnf: str) -> List[List[Tuple[str, bool]]]:
    """
    Converts a BNF to a CNF representation.

    :param bnf: The BNF to convert.
    :return: The CNF representation of the BNF.
    """

    lexer = BNFLexer(InputStream(bnf))
    stream = CommonTokenStream(lexer)
    parser = BNFParser(stream)
    tree = parser.bnf()
    listener = BNFListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return []
