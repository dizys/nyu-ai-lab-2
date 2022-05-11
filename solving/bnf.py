from typing import Dict, List, Tuple

from .bnf_parser import bnf_text_to_trees, BNFParserError


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
        sentence: List[Tuple[str, bool]] = []
        atoms = line.split(' ')
        for atom in atoms:
            atom = atom.strip()
            if atom == '':
                continue
            if atom[0] == '!' or atom[0] == '~' or atom[0] == '¬':
                sentence.append((atom[1:], False))
            else:
                sentence.append((atom, True))
        sentence.sort(key=lambda x: x[0])
        cnf_rep.append(sentence)
    return cnf_rep


def cnf_rep_to_text(cnf_rep: List[List[Tuple[str, bool]]]) -> str:
    """
    Converts a CNF representation to a text.

    :param cnf_rep: The CNF representation to convert.
    :return: The text representation of the CNF.
    """

    lines = []
    for sentence in cnf_rep:
        sentence_str = ''
        first_in_clause = True
        for atom in sentence:
            if first_in_clause:
                first_in_clause = False
            else:
                sentence_str += ' '
            if atom[1]:
                sentence_str += atom[0]
            else:
                sentence_str += '!' + atom[0]
        lines.append(sentence_str)
    return '\n'.join(lines)


def print_rules(rules: List[List[Tuple[str, bool]]]):
    for rule in rules:
        print("  - ", rule)


def remove_sentence_with_atom_and_its_negation(cnf_rep: List[List[Tuple[str, bool]]]) -> List[List[Tuple[str, bool]]]:
    result: List[List[Tuple[str, bool]]] = []
    for sentence in cnf_rep:
        atom_dict: Dict[str, bool] = {}
        is_sentence_valid = True
        for atom_bound in sentence:
            atom = atom_bound[0]
            bound = atom_bound[1]
            if atom in atom_dict:
                if atom_dict[atom] != bound:
                    is_sentence_valid = False
                    break
            else:
                atom_dict[atom] = bound
        if is_sentence_valid:
            result.append(sentence)
    return result


def print_cnf_rep(cnf_rep: List[List[Tuple[str, bool]]]):
    for sentence in cnf_rep:
        sentence_rep = []
        for atom in sentence:
            atom_rep = atom[0]
            if not atom[1]:
                atom_rep = '¬' + atom_rep
            sentence_rep.append(atom_rep)
        print('  - ', " ".join(sentence_rep))


def bnf_to_cnf_rep(bnf: str, verbose=False) -> List[List[Tuple[str, bool]]]:
    """
    Converts a BNF to a CNF representation.

    :param bnf: The BNF to convert.
    :return: The CNF representation of the BNF.
    """
    rules = bnf_text_to_trees(bnf)
    if verbose:
        print('Parsed rules:')
        print_rules(rules)

    for rule in rules:
        rule.eliminate_iff()
    if verbose:
        print('\nStep 1. Eliminating IFF "<=>":')
        print_rules(rules)

    for rule in rules:
        rule.eliminate_implies()
    if verbose:
        print('\nStep 2. Eliminating IMPLIES "=>":')
        print_rules(rules)

    for rule in rules:
        rule.push_not_to_atom_level()
    if verbose:
        print('\nStep 3. Pushing NOT to atom level:')
        print_rules(rules)

    for rule in rules:
        rule.apply_distribution_rule()
    if verbose:
        print('\nStep 4. Applying distribution rule:')
        print_rules(rules)

    cnf_rep: List[List[Tuple[str, bool]]] = []
    for rule in rules:
        rule_cnf_rep = rule.to_cnf_rep()
        cnf_rep.extend(rule_cnf_rep)
    if verbose:
        print('\nStep 5. Separate top-level conjunctions and convert to CNF:')
        print_cnf_rep(cnf_rep)

    cnf_rep = remove_sentence_with_atom_and_its_negation(cnf_rep)
    if verbose:
        print('\nStep 6. Remove any sentence that includes an atom and its negation:')
        print_cnf_rep(cnf_rep)
    return cnf_rep
