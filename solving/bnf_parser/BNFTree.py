
from typing import List, Union, Tuple

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from .BNFLexer import BNFLexer
from .BNFParser import BNFParser
from .BNFListener import BNFListener


class BNFNode:
    ATOM = 1
    BINARY_CLAUSE = 2
    GROUPED = 3

    AND = '&'
    OR = '|'
    IMPLIES = '=>'
    IFF = '<=>'

    type: int
    left_child: Union["BNFNode", Tuple[str, bool]]
    operator: Union[str, None]
    right_child: Union["BNFNode", Tuple[str, bool], None]

    def __init__(self, type: int, left_child: Union["BNFNode", Tuple[str, bool]], operator: Union[str, None] = None, right_child: Union["BNFNode", Tuple[str, bool], None] = None):
        self.type = type
        self.left_child = left_child
        self.operator = operator
        self.right_child = right_child


def bnf_text_to_tree(text: str) -> BNFNode:
    """
    Converts a BNF text to a BNF Tree
    :param text: The BNF text to convert.
    :return: The BNFTree representation of the BNF.
    """

    lexer = BNFLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = BNFParser(stream)
    tree = parser.bnf()
    listener = BNFListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.bnf_tree
