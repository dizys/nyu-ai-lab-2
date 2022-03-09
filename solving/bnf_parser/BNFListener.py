# Generated from BNF.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BNFParser import BNFParser
else:
    from BNFParser import BNFParser

# This class defines a complete listener for a parse tree produced by BNFParser.


class BNFListener(ParseTreeListener):

    # Enter a parse tree produced by BNFParser#bnf.
    def enterBnf(self, ctx: BNFParser.BnfContext):
        pass

    # Exit a parse tree produced by BNFParser#bnf.
    def exitBnf(self, ctx: BNFParser.BnfContext):
        pass

    # Enter a parse tree produced by BNFParser#bnf_rule.
    def enterBnf_rule(self, ctx: BNFParser.Bnf_ruleContext):
        pass

    # Exit a parse tree produced by BNFParser#bnf_rule.
    def exitBnf_rule(self, ctx: BNFParser.Bnf_ruleContext):
        pass

    # Enter a parse tree produced by BNFParser#clause.
    def enterClause(self, ctx: BNFParser.ClauseContext):
        pass

    # Exit a parse tree produced by BNFParser#clause.
    def exitClause(self, ctx: BNFParser.ClauseContext):
        pass


del BNFParser
