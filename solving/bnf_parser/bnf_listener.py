from typing import List, Union, Tuple

from antlr4 import ParseTreeListener
from antlr4.error.ErrorListener import ErrorListener

from .bnf_node import BNFNode
from .BNFParser import BNFParser


class BNFParserError(Exception):
    """
    Exception for BNF Parser errors.
    """
    pass


class BNFErrorListener(ErrorListener):
    def __init__(self):
        super(BNFErrorListener, self).__init__()

    def syntaxError(self, _recognizer, _offending_symbol, line, column, msg, _e):
        raise BNFParserError(f"line {line}:{column} {msg}")


class BNFListener(ParseTreeListener):
    rules: List[BNFNode] = []
    stack: List[Union[BNFNode, Tuple[str, bool]]] = []
    # Enter a parse tree produced by BNFParser#bnf.

    def enterBnf(self, ctx: BNFParser.BnfContext):
        pass

    # Exit a parse tree produced by BNFParser#bnf.
    def exitBnf(self, ctx: BNFParser.BnfContext):
        pass

    # Enter a parse tree produced by BNFParser#bnf_rule.
    def enterBnf_rule(self, ctx: BNFParser.Bnf_ruleContext):
        self.stack = []

    # Exit a parse tree produced by BNFParser#bnf_rule.
    def exitBnf_rule(self, ctx: BNFParser.Bnf_ruleContext):
        if len(self.stack) != 1:
            raise BNFParserError(
                f"Internal state error, stack should have one element, but has {len(self.stack)}")
        self.rules.append(self.stack[0])

    # Enter a parse tree produced by BNFParser#clause.
    def enterClause(self, ctx: BNFParser.ClauseContext):
        child_count = ctx.getChildCount()
        if child_count == 1:
            # Clause is an atom
            self.stack.append(
                BNFNode(BNFNode.ATOM, None, (ctx.getChild(0).getText(), True)))
        elif child_count == 2:
            # Clause is a not clause
            self.stack.append(
                BNFNode(BNFNode.NOT)
            )
        elif child_count == 3:
            left_token_str = ctx.getChild(0).getText()
            if left_token_str == '(':
                # Clause is a grouped clause
                self.stack.append(BNFNode(BNFNode.GROUPED))
            else:
                # Clause is a binary clause
                operator_token = ctx.getChild(1).getPayload()
                operator = None
                if operator_token.type == BNFParser.AND:
                    operator = BNFNode.AND
                elif operator_token.type == BNFParser.OR:
                    operator = BNFNode.OR
                elif operator_token.type == BNFParser.IMPLIES:
                    operator = BNFNode.IMPLIES
                elif operator_token.type == BNFParser.IFF:
                    operator = BNFNode.IFF
                self.stack.append(
                    BNFNode(BNFNode.BINARY_CLAUSE, operator)
                )

    # Exit a parse tree produced by BNFParser#clause.
    def exitClause(self, ctx: BNFParser.ClauseContext):
        child_count = ctx.getChildCount()
        if child_count == 2:
            # Clause is a not clause
            child_node = self.stack.pop()
            self.stack[-1].left_child = child_node
        elif child_count == 3:
            left_token_str = ctx.getChild(0).getText()
            if left_token_str == '(':
                # Clause is a grouped clause
                child_node = self.stack.pop()
                self.stack.pop()
                self.stack.append(child_node)
            else:
                # Clause is a binary clause
                child_node = self.stack.pop()
                left_node = self.stack.pop()
                self.stack[-1].left_child = left_node
                self.stack[-1].right_child = child_node
