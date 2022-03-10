# Generated from BNF.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write(">\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7(\n\7")
        buf.write("\3\b\3\b\3\b\5\b-\n\b\3\t\6\t\60\n\t\r\t\16\t\61\3\n\3")
        buf.write("\n\3\13\6\13\67\n\13\r\13\16\138\3\13\3\13\3\f\3\f\2\2")
        buf.write("\r\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\3\2\7\5\2((``\u2229\u2229\4\2~~\u222a\u222a\4\2##\u00ae")
        buf.write("\u00ae\6\2\62;C\\aac|\4\2\13\13\"\"\2A\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2")
        buf.write("\t\37\3\2\2\2\13!\3\2\2\2\r\'\3\2\2\2\17,\3\2\2\2\21/")
        buf.write("\3\2\2\2\23\63\3\2\2\2\25\66\3\2\2\2\27<\3\2\2\2\31\32")
        buf.write("\7*\2\2\32\4\3\2\2\2\33\34\7+\2\2\34\6\3\2\2\2\35\36\t")
        buf.write("\2\2\2\36\b\3\2\2\2\37 \t\3\2\2 \n\3\2\2\2!\"\t\4\2\2")
        buf.write("\"\f\3\2\2\2#$\7>\2\2$%\7?\2\2%(\7@\2\2&(\7\u21d6\2\2")
        buf.write("\'#\3\2\2\2\'&\3\2\2\2(\16\3\2\2\2)*\7?\2\2*-\7@\2\2+")
        buf.write("-\7\u21d4\2\2,)\3\2\2\2,+\3\2\2\2-\20\3\2\2\2.\60\t\5")
        buf.write("\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\22\3\2\2\2\63\64\7\f\2\2\64\24\3\2\2\2\65\67\t\6\2")
        buf.write("\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29:\3")
        buf.write("\2\2\2:;\b\13\2\2;\26\3\2\2\2<=\13\2\2\2=\30\3\2\2\2\7")
        buf.write("\2\',\618\3\b\2\2")
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
    ErrorCharacter = 11

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'('", "')'", "'\n'"]

    symbolicNames = ["<INVALID>",
                     "LEFT_PAREN", "RIGHT_PAREN", "AND", "OR", "NOT", "IFF", "IMPLIES",
                     "ATOM", "NL", "WS", "ErrorCharacter"]

    ruleNames = ["LEFT_PAREN", "RIGHT_PAREN", "AND", "OR", "NOT", "IFF",
                 "IMPLIES", "ATOM", "NL", "WS", "ErrorCharacter"]

    grammarFileName = "BNF.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
