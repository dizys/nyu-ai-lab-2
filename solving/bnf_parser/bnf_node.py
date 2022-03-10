from typing import Union, Tuple, List


class BNFNode:
    ATOM = 1
    NOT = 2
    BINARY_CLAUSE = 3
    GROUPED = 4

    AND = '&'
    OR = '|'
    IMPLIES = '=>'
    IFF = '<=>'

    type: int
    operator: Union[str, None]
    left_child: Union["BNFNode", Tuple[str, bool], None]
    right_child: Union["BNFNode", Tuple[str, bool], None]

    def operator_val_to_name(self, operator_val: int) -> str:
        if operator_val == BNFNode.AND:
            return "AND"
        elif operator_val == BNFNode.OR:
            return "OR"
        elif operator_val == BNFNode.IMPLIES:
            return "IMPLIES"
        elif operator_val == BNFNode.IFF:
            return "IFF"
        else:
            return "UNKNOWN"

    def __init__(self, type: int, operator: Union[str, None] = None, left_child: Union["BNFNode", Tuple[str, bool], None] = None,  right_child: Union["BNFNode", Tuple[str, bool], None] = None):
        self.type = type
        self.operator = operator
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        result = ""
        if self.type == BNFNode.ATOM:
            result = f"(ATOM {self.left_child})"
        elif self.type == BNFNode.NOT:
            result = f"(NOT {self.left_child.__str__()})"
        elif self.type == BNFNode.BINARY_CLAUSE:
            result = f"({self.operator_val_to_name(self.operator)} {self.left_child.__str__()}  {self.right_child.__str__()})"
        elif self.type == BNFNode.GROUPED:
            result = f"(GROUP {self.left_child.__str__()})"
        else:
            result = f"Unknown node type: {self.type}"
        return result

    def print(self) -> None:
        print(self.__str__())

    def eliminate_iff(self):
        if isinstance(self.left_child, BNFNode):
            self.left_child.eliminate_iff()
        if isinstance(self.right_child, BNFNode):
            self.right_child.eliminate_iff()
        if self.type == BNFNode.BINARY_CLAUSE and self.operator == BNFNode.IFF:
            self.type = BNFNode.BINARY_CLAUSE
            self.operator = BNFNode.AND
            new_left_child = BNFNode(BNFNode.BINARY_CLAUSE,
                                     BNFNode.IMPLIES, self.left_child, self.right_child)
            new_right_child = BNFNode(BNFNode.BINARY_CLAUSE,
                                      BNFNode.IMPLIES, self.right_child, self.left_child)
            self.left_child = new_left_child
            self.right_child = new_right_child

    def eliminate_implies(self):
        if isinstance(self.left_child, BNFNode):
            self.left_child.eliminate_implies()
        if isinstance(self.right_child, BNFNode):
            self.right_child.eliminate_implies()
        if self.type == BNFNode.BINARY_CLAUSE and self.operator == BNFNode.IMPLIES:
            self.type = BNFNode.BINARY_CLAUSE
            self.operator = BNFNode.OR
            self.left_child = BNFNode(BNFNode.NOT, None, self.left_child)

    def _push_not_to_atom_level(self):
        if self.type == BNFNode.NOT:
            if isinstance(self.left_child, Tuple):
                self.type = BNFNode.ATOM
                self.operator = None
                self.left_child = (self.left_child[0], not self.left_child[1])
                self.right_child = None
            elif isinstance(self.left_child, BNFNode) and self.left_child.type == BNFNode.ATOM:
                node_to_become_inverted = self.left_child
                self.type = BNFNode.ATOM
                self.operator = None
                self.left_child = (
                    node_to_become_inverted.left_child[0], not node_to_become_inverted.left_child[1])
                self.right_child = None
            elif isinstance(self.left_child, BNFNode) and self.left_child.type == BNFNode.NOT:
                node_to_become = self.left_child.left_child
                self.type = node_to_become.type
                self.operator = node_to_become.operator
                self.left_child = node_to_become.left_child
                self.right_child = node_to_become.right_child
            elif isinstance(self.left_child, BNFNode) and self.left_child.type == BNFNode.BINARY_CLAUSE:
                if self.left_child.operator == BNFNode.AND:
                    self.type = BNFNode.BINARY_CLAUSE
                    self.operator = BNFNode.OR
                    new_left_child = BNFNode(
                        BNFNode.NOT, None, self.left_child.left_child)
                    new_right_child = BNFNode(
                        BNFNode.NOT, None, self.left_child.right_child)
                    self.left_child = new_left_child
                    self.right_child = new_right_child
                elif self.left_child.operator == BNFNode.OR:
                    self.type = BNFNode.BINARY_CLAUSE
                    self.operator = BNFNode.AND
                    new_left_child = BNFNode(
                        BNFNode.NOT, None, self.left_child.left_child)
                    new_right_child = BNFNode(
                        BNFNode.NOT, None, self.left_child.right_child)
                    self.left_child = new_left_child
                    self.right_child = new_right_child
        if isinstance(self.left_child, BNFNode):
            self.left_child._push_not_to_atom_level()
        if isinstance(self.right_child, BNFNode):
            self.right_child._push_not_to_atom_level()

    def has_not_node(self):
        if self.type == BNFNode.NOT:
            return True
        if isinstance(self.left_child, BNFNode) and self.left_child.has_not_node():
            return True
        if isinstance(self.right_child, BNFNode) and self.right_child.has_not_node():
            return True
        return False

    def push_not_to_atom_level(self):
        while self.has_not_node():
            self._push_not_to_atom_level()

    def _apply_distribution_rule(self):
        if self.type == BNFNode.BINARY_CLAUSE and self.operator == BNFNode.OR:
            if isinstance(self.left_child, BNFNode) and self.left_child.type == BNFNode.BINARY_CLAUSE and self.left_child.operator == BNFNode.AND:
                self.type = BNFNode.BINARY_CLAUSE
                self.operator = BNFNode.AND
                new_left_child = BNFNode(
                    BNFNode.BINARY_CLAUSE, BNFNode.OR, self.left_child.left_child, self.right_child)
                new_right_child = BNFNode(
                    BNFNode.BINARY_CLAUSE, BNFNode.OR, self.left_child.right_child, self.right_child)
                self.left_child = new_left_child
                self.right_child = new_right_child
            elif isinstance(self.right_child, BNFNode) and self.right_child.type == BNFNode.BINARY_CLAUSE and self.right_child.operator == BNFNode.AND:
                self.type = BNFNode.BINARY_CLAUSE
                self.operator = BNFNode.AND
                new_left_child = BNFNode(
                    BNFNode.BINARY_CLAUSE, BNFNode.OR, self.left_child, self.right_child.left_child)
                new_right_child = BNFNode(
                    BNFNode.BINARY_CLAUSE, BNFNode.OR, self.left_child, self.right_child.right_child)
                self.left_child = new_left_child
                self.right_child = new_right_child
        if isinstance(self.left_child, BNFNode):
            self.left_child._apply_distribution_rule()
        if isinstance(self.right_child, BNFNode):
            self.right_child._apply_distribution_rule()

    def are_all_ors_under_ands(self, and_level=True):
        if self.type == BNFNode.BINARY_CLAUSE and self.operator == BNFNode.AND:
            if not and_level:
                return False
            else:
                return self.left_child.are_all_ors_under_ands(True) and self.right_child.are_all_ors_under_ands(True)
        elif self.type == BNFNode.BINARY_CLAUSE and self.operator == BNFNode.OR:
            return self.left_child.are_all_ors_under_ands(False) and self.right_child.are_all_ors_under_ands(False)
        else:
            return True

    def apply_distribution_rule(self):
        while(not self.are_all_ors_under_ands()):
            self._apply_distribution_rule()

    def _to_cnf_rep(self) -> Union[List[List[Tuple[str, bool]]], List[Tuple[str, bool]], Tuple[str, bool]]:
        if self.type == BNFNode.BINARY_CLAUSE:
            if self.operator == BNFNode.AND:
                result: List[List[Tuple[str, bool]]] = []

                def add_to_result(item: Union[List[List[Tuple[str, bool]]], List[Tuple[str, bool]], Tuple[str, bool]]):
                    if isinstance(item, tuple):
                        result.append([item])
                    elif isinstance(item, list) and len(item) > 0:
                        if isinstance(item[0], list):
                            result.extend(item)
                        else:
                            result.append(item)
                if isinstance(self.left_child, BNFNode):
                    add_to_result(self.left_child._to_cnf_rep())
                if isinstance(self.right_child, BNFNode):
                    add_to_result(self.right_child._to_cnf_rep())
                return result
            elif self.operator == BNFNode.OR:
                result: List[Tuple[str, bool]] = []

                def add_to_result(item: Union[List[Tuple[str, bool]], Tuple[str, bool]]):
                    if isinstance(item, tuple):
                        result.append(item)
                    elif isinstance(item, list) and len(item) > 0:
                        result.extend(item)
                if isinstance(self.left_child, BNFNode):
                    add_to_result(self.left_child._to_cnf_rep())
                if isinstance(self.right_child, BNFNode):
                    add_to_result(self.right_child._to_cnf_rep())
                return result
        else:
            return self.left_child

    def to_cnf_rep(self) -> List[List[Tuple[str, bool]]]:
        raw_cnf_rep = self._to_cnf_rep()
        result: List[List[Tuple[str, bool]]] = []
        if isinstance(raw_cnf_rep, list) and len(raw_cnf_rep) > 0:
            if isinstance(raw_cnf_rep[0], list):
                result = raw_cnf_rep
            else:
                result = [raw_cnf_rep]
        elif isinstance(raw_cnf_rep, tuple):
            result = [[raw_cnf_rep]]
        for sentence in result:
            sentence.sort(key=lambda x: x[0])
        return result
