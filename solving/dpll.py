"""
DPLL Solver
"""

from typing import Dict, List, Tuple, Union, TypedDict

from .bnf import cnf_rep_to_text


def collect_atoms(cnf_rep: List[List[Tuple[str, bool]]]) -> List[str]:
    """
    Collects all the atoms in the CNF representation.

    :param cnf_rep: The CNF representation to collect atoms from.
    :return: The list of atoms in the CNF representation.
    """

    atoms = []
    for clause in cnf_rep:
        for atom in clause:
            if atom[0] not in atoms:
                atoms.append(atom[0])
    atoms.sort()
    return atoms


class DPLLStepState(TypedDict):
    """
    The state of a DPLL step.
    """
    type: str
    cnf_rep: List[List[Tuple[str, bool]]]
    atom_bounds: Dict[str, bool]
    decision_atom: Tuple[str, bool]


class DPLLException(Exception):
    """
    Exception for DPLL solver.
    """
    pass


class DPLL:
    """
    DPLL Solver
    """
    cnf_rep: List[List[Tuple[str, bool]]]
    atom_list: List[str]
    atom_bounds: Dict[str, bool]
    verbose: bool
    history: List[DPLLStepState]

    def __init__(self, cnf_rep: List[List[Tuple[str, bool]]], verbose=False):
        """
        Initializes the DPLL solver.
        """
        self.cnf_rep = cnf_rep
        self.atom_list = collect_atoms(cnf_rep)
        self.atom_bounds = {}
        self.verbose = verbose
        self.history = []

    def find_unit_clause(self) -> Union[Tuple[str, bool], None]:
        """
        Finds a single atom in a clause.
        """
        atoms: List[Tuple[str, bool]] = []
        for clause in self.cnf_rep:
            if len(clause) == 1:
                for atom_bound in clause:
                    atoms.append(atom_bound)
        atoms.sort(key=lambda x: x[0])
        if len(atoms) == 0:
            return None
        return atoms[0]

    def is_pure_literal(self, atom_str: str, true_literal: bool) -> bool:
        """
        Checks if a literal is pure.
        """
        result = True
        for clause in self.cnf_rep:
            for atom_bound in clause:
                if atom_bound[0] == atom_str and atom_bound[1] != true_literal:
                    result = False

        return result

    def is_atom_bound(self, atom_str: str) -> bool:
        """
        Checks if an atom is bound.
        """
        return atom_str in self.atom_bounds

    def find_pure_literal(self) -> Union[Tuple[str, bool], None]:
        """
        Finds a pure literal in the CNF representation.
        """
        for atom in self.atom_list:
            if self.is_atom_bound(atom):
                continue
            if self.is_pure_literal(atom, True):
                return atom, True
            if self.is_pure_literal(atom, False):
                return atom, False
        return None

    def find_easy_case(self) -> Union[Tuple[str, bool], None]:
        """
        Finds an easy case in the CNF representation.
        """
        result = self.find_unit_clause()

        if result is not None:
            return result

        result = self.find_pure_literal()

        return result

    def guess_atom(self, try_false=False) -> Union[Tuple[str, bool], None]:
        """
        Guess one atom in the CNF representation.
        """
        for atom in self.atom_list:
            if self.is_atom_bound(atom):
                continue
            return atom, not try_false

        return None

    def rewind_to_last_guess(self) -> bool:
        """
        Rewinds the CNF representation to the last guess.
        """
        if len(self.history) == 0:
            return False
        # Find the last history state that is a guess type
        while(self.history[-1]['type'] != 'guess'):
            self.history.pop()
            if len(self.history) == 0:
                return False

        state = self.history.pop()
        self.cnf_rep = state['cnf_rep']
        self.atom_bounds = state['atom_bounds']
        return True

    def eliminate_atom(self, atom: str, value: bool) -> bool:
        """
        Eliminates an atom from the CNF representation.
        """
        new_cnf_rep: List[List[Tuple[str, bool]]] = []
        legal = True
        for clause in self.cnf_rep:
            new_clause: List[Tuple[str, bool]] = []
            skip_clause = False
            for atom_bound in clause:
                if atom_bound[0] == atom and atom_bound[1] == value:
                    skip_clause = True
                    break
                if atom_bound[0] == atom and atom_bound[1] != value:
                    continue
                new_clause.append(atom_bound)
            if skip_clause:
                continue
            if len(new_clause) == 0:
                legal = False
            new_cnf_rep.append(new_clause)
        self.cnf_rep = new_cnf_rep
        return legal

    def is_finished(self) -> bool:
        """
        Checks if the CNF representation is finished.
        """
        return len(self.cnf_rep) == 0

    def is_legal(self) -> bool:
        """
        Checks if the CNF representation is legal.
        """
        for clause in self.cnf_rep:
            if len(clause) == 0:
                return False
        return True

    def print_step(self, step_type: str, legal: bool, atom_bound: Tuple[str, bool]):
        """
        Prints a step state in the CNF representation.
        """
        value_str = "true" if atom_bound[1] else "false"
        if step_type == 'easy':
            print(
                f'easyCase {atom_bound[0]} = {value_str}')
        elif step_type == 'guess':
            print(
                f'hard case, guess: {atom_bound[0]}={value_str}')
        else:
            print(
                f'fail|hard case, try: {atom_bound[0]}={value_str}')
        if not legal:
            print(
                f'{"!" if atom_bound[1] else ""}{atom_bound[0]} contradiction')

    def step(self):
        """
        Performs a single step in the DPLL algorithm.
        """
        if self.is_finished():
            return True
        legal = self.is_legal()
        easy_case = self.find_easy_case()
        guess = self.guess_atom()
        atom_bound: Union[Tuple[str, bool], None] = None
        if legal and easy_case:
            step_type = 'easy'
            atom_bound = easy_case
        elif legal and guess:
            step_type = 'guess'
            atom_bound = guess
        else:
            step_type = 'retry'
            if not self.rewind_to_last_guess():
                raise DPLLException('No more guesses')
            atom_bound = self.guess_atom(try_false=True)
        if atom_bound is None:
            raise DPLLException('Unexpected empty step atom bound')
        self.history.append({
            'type': step_type,
            'cnf_rep': self.cnf_rep.copy(),
            'atom_bounds': self.atom_bounds.copy(),
            'decision_atom': atom_bound
        })
        self.atom_bounds[atom_bound[0]] = atom_bound[1]
        legal = self.eliminate_atom(atom_bound[0], atom_bound[1])
        if self.verbose:
            self.print_step(step_type, legal, atom_bound)
        return legal

    def print_cnf(self):
        """
        Prints the current CNF representation.
        """
        print(cnf_rep_to_text(self.cnf_rep))

    def solve(self) -> Union[Dict[str, bool], None]:
        """
        Solves the CNF representation.
        """
        self.print_cnf()
        try:
            while not self.is_finished():
                legal = self.step()
                if legal and not self.is_finished():
                    self.print_cnf()
        except DPLLException:
            return None
        return self.atom_bounds

    def fill_unbounded_atoms(self, fill_with=False) -> bool:
        """
        Fills in the unbounded atoms in the CNF representation.
        """
        for atom in self.atom_list:
            if self.is_atom_bound(atom):
                continue
            self.atom_bounds[atom] = fill_with
            if self.verbose:
                print(
                    f'unbound {atom}={"true" if fill_with else "false"}')
        return self.atom_bounds
