
from typing import List, Union, Tuple

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from .BNFLexer import BNFLexer
from .BNFParser import BNFParser
from .bnf_node import BNFNode
from .bnf_listener import BNFListener, BNFErrorListener


def bnf_text_to_trees(text: str) -> List[BNFNode]:
    """
    Converts a BNF text to a BNF Tree
    :param text: The BNF text to convert.
    :return: The BNFTree representation of the BNF.
    """

    lexer = BNFLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = BNFParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(BNFErrorListener())

    tree = parser.bnf()
    listener = BNFListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.rules
