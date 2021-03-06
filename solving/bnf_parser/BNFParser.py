# Generated from BNF.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
from typing import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\6\2\13\n\2\r\2\16\2")
        buf.write("\f\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\2\7\2\26\n\2\f\2")
        buf.write("\16\2\31\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\'\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4\65\n\4\f\4\16\48\13\4\3\4\2\3\6\5\2\4")
        buf.write("\6\2\2\2?\2\b\3\2\2\2\4\34\3\2\2\2\6&\3\2\2\2\b\21\5\4")
        buf.write("\3\2\t\13\7\13\2\2\n\t\3\2\2\2\13\f\3\2\2\2\f\n\3\2\2")
        buf.write("\2\f\r\3\2\2\2\r\16\3\2\2\2\16\20\5\4\3\2\17\n\3\2\2\2")
        buf.write("\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\27\3\2\2")
        buf.write("\2\23\21\3\2\2\2\24\26\7\13\2\2\25\24\3\2\2\2\26\31\3")
        buf.write("\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27")
        buf.write("\3\2\2\2\32\33\7\2\2\3\33\3\3\2\2\2\34\35\5\6\4\2\35\5")
        buf.write("\3\2\2\2\36\37\b\4\1\2\37\'\7\n\2\2 !\7\7\2\2!\'\5\6\4")
        buf.write("\b\"#\7\3\2\2#$\5\6\4\2$%\7\4\2\2%\'\3\2\2\2&\36\3\2\2")
        buf.write("\2& \3\2\2\2&\"\3\2\2\2\'\66\3\2\2\2()\f\7\2\2)*\7\5\2")
        buf.write("\2*\65\5\6\4\b+,\f\6\2\2,-\7\6\2\2-\65\5\6\4\7./\f\5\2")
        buf.write("\2/\60\7\t\2\2\60\65\5\6\4\6\61\62\f\4\2\2\62\63\7\b\2")
        buf.write("\2\63\65\5\6\4\5\64(\3\2\2\2\64+\3\2\2\2\64.\3\2\2\2\64")
        buf.write("\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("\7\3\2\2\28\66\3\2\2\2\b\f\21\27&\64\66")
        return buf.getvalue()


class BNFParser (Parser):

    grammarFileName = "BNF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'('", "')'", "<INVALID>", "<INVALID>",
                    "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "'\n'"]

    symbolicNames = ["<INVALID>", "LEFT_PAREN", "RIGHT_PAREN", "AND", "OR",
                     "NOT", "IFF", "IMPLIES", "ATOM", "NL", "WS", "ErrorCharacter"]

    RULE_bnf = 0
    RULE_bnf_rule = 1
    RULE_clause = 2

    ruleNames = ["bnf", "bnf_rule", "clause"]

    EOF = Token.EOF
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    AND = 3
    OR = 4
    NOT = 5
    IFF = 6
    IMPLIES = 7
    ATOM = 8
    NL = 9
    WS = 10
    ErrorCharacter = 11

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class BnfContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bnf_rule(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BNFParser.Bnf_ruleContext)
            else:
                return self.getTypedRuleContext(BNFParser.Bnf_ruleContext, i)

        def EOF(self):
            return self.getToken(BNFParser.EOF, 0)

        def NL(self, i: int = None):
            if i is None:
                return self.getTokens(BNFParser.NL)
            else:
                return self.getToken(BNFParser.NL, i)

        def getRuleIndex(self):
            return BNFParser.RULE_bnf

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBnf"):
                listener.enterBnf(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBnf"):
                listener.exitBnf(self)

    def bnf(self):

        localctx = BNFParser.BnfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_bnf)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.bnf_rule()
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 1, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 8
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 7
                        self.match(BNFParser.NL)
                        self.state = 10
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la == BNFParser.NL):
                            break

                    self.state = 12
                    self.bnf_rule()
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 1, self._ctx)

            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == BNFParser.NL:
                self.state = 18
                self.match(BNFParser.NL)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(BNFParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bnf_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self):
            return self.getTypedRuleContext(BNFParser.ClauseContext, 0)

        def getRuleIndex(self):
            return BNFParser.RULE_bnf_rule

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBnf_rule"):
                listener.enterBnf_rule(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBnf_rule"):
                listener.exitBnf_rule(self)

    def bnf_rule(self):

        localctx = BNFParser.Bnf_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bnf_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.clause(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClauseContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATOM(self):
            return self.getToken(BNFParser.ATOM, 0)

        def NOT(self):
            return self.getToken(BNFParser.NOT, 0)

        def clause(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(BNFParser.ClauseContext)
            else:
                return self.getTypedRuleContext(BNFParser.ClauseContext, i)

        def LEFT_PAREN(self):
            return self.getToken(BNFParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BNFParser.RIGHT_PAREN, 0)

        def AND(self):
            return self.getToken(BNFParser.AND, 0)

        def OR(self):
            return self.getToken(BNFParser.OR, 0)

        def IMPLIES(self):
            return self.getToken(BNFParser.IMPLIES, 0)

        def IFF(self):
            return self.getToken(BNFParser.IFF, 0)

        def getRuleIndex(self):
            return BNFParser.RULE_clause

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterClause"):
                listener.enterClause(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitClause"):
                listener.exitClause(self)

    def clause(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BNFParser.ClauseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_clause, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BNFParser.ATOM]:
                self.state = 29
                self.match(BNFParser.ATOM)
                pass
            elif token in [BNFParser.NOT]:
                self.state = 30
                self.match(BNFParser.NOT)
                self.state = 31
                self.clause(6)
                pass
            elif token in [BNFParser.LEFT_PAREN]:
                self.state = 32
                self.match(BNFParser.LEFT_PAREN)
                self.state = 33
                self.clause(0)
                self.state = 34
                self.match(BNFParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(
                        self._input, 4, self._ctx)
                    if la_ == 1:
                        localctx = BNFParser.ClauseContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_clause)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        self.match(BNFParser.AND)
                        self.state = 40
                        self.clause(6)
                        pass

                    elif la_ == 2:
                        localctx = BNFParser.ClauseContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_clause)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        self.match(BNFParser.OR)
                        self.state = 43
                        self.clause(5)
                        pass

                    elif la_ == 3:
                        localctx = BNFParser.ClauseContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_clause)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(BNFParser.IMPLIES)
                        self.state = 46
                        self.clause(4)
                        pass

                    elif la_ == 4:
                        localctx = BNFParser.ClauseContext(
                            self, _parentctx, _parentState)
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_clause)
                        self.state = 47
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 2)")
                        self.state = 48
                        self.match(BNFParser.IFF)
                        self.state = 49
                        self.clause(3)
                        pass

                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.clause_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def clause_sempred(self, localctx: ClauseContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 5)

        if predIndex == 1:
            return self.precpred(self._ctx, 4)

        if predIndex == 2:
            return self.precpred(self._ctx, 3)

        if predIndex == 3:
            return self.precpred(self._ctx, 2)
