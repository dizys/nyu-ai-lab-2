# Generated from BNF.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7&\n\7\3\b\3\b")
        buf.write("\3\b\5\b+\n\b\3\t\6\t.\n\t\r\t\16\t/\3\n\3\n\3\13\6\13")
        buf.write("\65\n\13\r\13\16\13\66\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\3\2\7\5\2((``\u2229\u2229")
        buf.write("\4\2~~\u222a\u222a\4\2##\u00ae\u00ae\6\2\62;C\\aac|\4")
        buf.write("\2\13\13\"\"\2=\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3")
        buf.write("\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13\37\3\2\2\2\r%\3\2")
        buf.write("\2\2\17*\3\2\2\2\21-\3\2\2\2\23\61\3\2\2\2\25\64\3\2\2")
        buf.write("\2\27\30\7*\2\2\30\4\3\2\2\2\31\32\7+\2\2\32\6\3\2\2\2")
        buf.write("\33\34\t\2\2\2\34\b\3\2\2\2\35\36\t\3\2\2\36\n\3\2\2\2")
        buf.write("\37 \t\4\2\2 \f\3\2\2\2!\"\7>\2\2\"#\7?\2\2#&\7@\2\2$")
        buf.write("&\7\u21d6\2\2%!\3\2\2\2%$\3\2\2\2&\16\3\2\2\2\'(\7?\2")
        buf.write("\2(+\7@\2\2)+\7\u21d4\2\2*\'\3\2\2\2*)\3\2\2\2+\20\3\2")
        buf.write("\2\2,.\t\5\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2")
        buf.write("\2\60\22\3\2\2\2\61\62\7\f\2\2\62\24\3\2\2\2\63\65\t\6")
        buf.write("\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3")
        buf.write("\2\2\2\678\3\2\2\289\b\13\2\29\26\3\2\2\2\7\2%*/\66\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class BNFLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'('", "')'", "'\n'"]

    symbolicNames = ["<INVALID>",
                     "LEFT_PAREN", "RIGHT_PAREN", "AND", "OR", "NOT", "IFF", "IMPLIES",
                     "ATOM", "NL", "WS"]

    ruleNames = ["LEFT_PAREN", "RIGHT_PAREN", "AND", "OR", "NOT", "IFF",
                 "IMPLIES", "ATOM", "NL", "WS"]

    grammarFileName = "BNF.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
