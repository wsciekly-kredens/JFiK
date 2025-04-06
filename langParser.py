# Generated from lang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,147,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,3,0,30,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,44,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,55,9,1,
        1,1,1,1,3,1,59,8,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,80,8,2,3,2,82,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,90,8,2,10,2,12,2,93,9,2,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,106,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,117,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,128,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,139,8,7,1,8,1,8,1,8,
        1,8,3,8,145,8,8,1,8,0,1,4,9,0,2,4,6,8,10,12,14,16,0,3,1,0,20,21,
        1,0,18,19,2,0,13,14,16,17,168,0,19,1,0,0,0,2,60,1,0,0,0,4,81,1,0,
        0,0,6,94,1,0,0,0,8,105,1,0,0,0,10,116,1,0,0,0,12,127,1,0,0,0,14,
        138,1,0,0,0,16,144,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,19,20,1,0,
        0,0,20,25,1,0,0,0,21,22,5,22,0,0,22,24,3,2,1,0,23,21,1,0,0,0,24,
        27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,
        0,28,30,5,22,0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,32,
        5,9,0,0,32,61,3,4,2,0,33,34,5,12,0,0,34,35,5,1,0,0,35,61,3,4,2,0,
        36,37,5,10,0,0,37,61,5,12,0,0,38,61,3,4,2,0,39,40,5,11,0,0,40,41,
        5,12,0,0,41,43,5,2,0,0,42,44,5,13,0,0,43,42,1,0,0,0,43,44,1,0,0,
        0,44,45,1,0,0,0,45,58,5,3,0,0,46,47,5,1,0,0,47,48,5,4,0,0,48,53,
        3,4,2,0,49,50,5,5,0,0,50,52,3,4,2,0,51,49,1,0,0,0,52,55,1,0,0,0,
        53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,
        6,0,0,57,59,1,0,0,0,58,46,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,
        31,1,0,0,0,60,33,1,0,0,0,60,36,1,0,0,0,60,38,1,0,0,0,60,39,1,0,0,
        0,61,3,1,0,0,0,62,63,6,2,-1,0,63,64,5,7,0,0,64,65,3,4,2,0,65,66,
        5,8,0,0,66,82,1,0,0,0,67,68,5,16,0,0,68,82,3,4,2,7,69,70,5,17,0,
        0,70,82,3,4,2,6,71,82,5,13,0,0,72,82,5,14,0,0,73,82,5,12,0,0,74,
        82,5,15,0,0,75,79,5,12,0,0,76,77,5,2,0,0,77,78,5,13,0,0,78,80,5,
        3,0,0,79,76,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,62,1,0,0,0,81,
        67,1,0,0,0,81,69,1,0,0,0,81,71,1,0,0,0,81,72,1,0,0,0,81,73,1,0,0,
        0,81,74,1,0,0,0,81,75,1,0,0,0,82,91,1,0,0,0,83,84,10,10,0,0,84,85,
        7,0,0,0,85,90,3,4,2,11,86,87,10,9,0,0,87,88,7,1,0,0,88,90,3,4,2,
        10,89,83,1,0,0,0,89,86,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,
        1,0,0,0,92,5,1,0,0,0,93,91,1,0,0,0,94,95,7,2,0,0,95,7,1,0,0,0,96,
        106,3,6,3,0,97,98,3,6,3,0,98,99,5,18,0,0,99,100,3,6,3,0,100,106,
        1,0,0,0,101,102,3,6,3,0,102,103,5,18,0,0,103,104,3,16,8,0,104,106,
        1,0,0,0,105,96,1,0,0,0,105,97,1,0,0,0,105,101,1,0,0,0,106,9,1,0,
        0,0,107,117,3,6,3,0,108,109,3,6,3,0,109,110,5,19,0,0,110,111,3,6,
        3,0,111,117,1,0,0,0,112,113,3,6,3,0,113,114,5,19,0,0,114,115,3,16,
        8,0,115,117,1,0,0,0,116,107,1,0,0,0,116,108,1,0,0,0,116,112,1,0,
        0,0,117,11,1,0,0,0,118,128,3,6,3,0,119,120,3,6,3,0,120,121,5,20,
        0,0,121,122,3,6,3,0,122,128,1,0,0,0,123,124,3,6,3,0,124,125,5,20,
        0,0,125,126,3,16,8,0,126,128,1,0,0,0,127,118,1,0,0,0,127,119,1,0,
        0,0,127,123,1,0,0,0,128,13,1,0,0,0,129,139,3,6,3,0,130,131,3,6,3,
        0,131,132,5,21,0,0,132,133,3,6,3,0,133,139,1,0,0,0,134,135,3,6,3,
        0,135,136,5,21,0,0,136,137,3,16,8,0,137,139,1,0,0,0,138,129,1,0,
        0,0,138,130,1,0,0,0,138,134,1,0,0,0,139,15,1,0,0,0,140,145,3,8,4,
        0,141,145,3,10,5,0,142,145,3,12,6,0,143,145,3,14,7,0,144,140,1,0,
        0,0,144,141,1,0,0,0,144,142,1,0,0,0,144,143,1,0,0,0,145,17,1,0,0,
        0,16,19,25,29,43,53,58,60,79,81,89,91,105,116,127,138,144
    ]

class langParser ( Parser ):

    grammarFileName = "lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "'{'", "','", "'}'", 
                     "'('", "')'", "'bark'", "'listen'", "'pack'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'(int)'", "'(float)'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WRITE", "READ", "ARRAY", "ID", "INT", 
                      "FLOAT", "STRING", "TOINT", "TOFLOAT", "ADD", "SUBSTRACT", 
                      "MULT", "DIVIDE", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_num = 3
    RULE_sum = 4
    RULE_diff = 5
    RULE_prod = 6
    RULE_quotient = 7
    RULE_artoperation = 8

    ruleNames =  [ "prog", "stat", "expr", "num", "sum", "diff", "prod", 
                   "quotient", "artoperation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    WRITE=9
    READ=10
    ARRAY=11
    ID=12
    INT=13
    FLOAT=14
    STRING=15
    TOINT=16
    TOFLOAT=17
    ADD=18
    SUBSTRACT=19
    MULT=20
    DIVIDE=21
    NEWLINE=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.StatContext)
            else:
                return self.getTypedRuleContext(langParser.StatContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(langParser.NEWLINE)
            else:
                return self.getToken(langParser.NEWLINE, i)

        def getRuleIndex(self):
            return langParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = langParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 261760) != 0):
                self.state = 18
                self.stat()


            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self.match(langParser.NEWLINE)
                    self.state = 22
                    self.stat() 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 28
                self.match(langParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return langParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(langParser.READ, 0)
        def ID(self):
            return self.getToken(langParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)


    class ArrayContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ARRAY(self):
            return self.getToken(langParser.ARRAY, 0)
        def ID(self):
            return self.getToken(langParser.ID, 0)
        def INT(self):
            return self.getToken(langParser.INT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.ExprContext)
            else:
                return self.getTypedRuleContext(langParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)


    class ExprStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStat" ):
                listener.enterExprStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStat" ):
                listener.exitExprStat(self)


    class WriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(langParser.WRITE, 0)
        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(langParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = langParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = langParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(langParser.WRITE)
                self.state = 32
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = langParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(langParser.ID)
                self.state = 34
                self.match(langParser.T__0)
                self.state = 35
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = langParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(langParser.READ)
                self.state = 37
                self.match(langParser.ID)
                pass

            elif la_ == 4:
                localctx = langParser.ExprStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = langParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.match(langParser.ARRAY)
                self.state = 40
                self.match(langParser.ID)
                self.state = 41
                self.match(langParser.T__1)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 42
                    self.match(langParser.INT)


                self.state = 45
                self.match(langParser.T__2)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 46
                    self.match(langParser.T__0)
                    self.state = 47
                    self.match(langParser.T__3)
                    self.state = 48
                    self.expr(0)
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 49
                        self.match(langParser.T__4)
                        self.state = 50
                        self.expr(0)
                        self.state = 55
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 56
                    self.match(langParser.T__5)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return langParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(langParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(langParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)


    class VarExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(langParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)


    class ArrayElemContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(langParser.ID, 0)
        def INT(self):
            return self.getToken(langParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayElem" ):
                listener.enterArrayElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayElem" ):
                listener.exitArrayElem(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(langParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)


    class CastToFloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOFLOAT(self):
            return self.getToken(langParser.TOFLOAT, 0)
        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastToFloat" ):
                listener.enterCastToFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastToFloat" ):
                listener.exitCastToFloat(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.ExprContext)
            else:
                return self.getTypedRuleContext(langParser.ExprContext,i)

        def MULT(self):
            return self.getToken(langParser.MULT, 0)
        def DIVIDE(self):
            return self.getToken(langParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.ExprContext)
            else:
                return self.getTypedRuleContext(langParser.ExprContext,i)

        def ADD(self):
            return self.getToken(langParser.ADD, 0)
        def SUBSTRACT(self):
            return self.getToken(langParser.SUBSTRACT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class CastToIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(langParser.TOINT, 0)
        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastToInt" ):
                listener.enterCastToInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastToInt" ):
                listener.exitCastToInt(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = langParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = langParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.match(langParser.T__6)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(langParser.T__7)
                pass

            elif la_ == 2:
                localctx = langParser.CastToIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(langParser.TOINT)
                self.state = 68
                self.expr(7)
                pass

            elif la_ == 3:
                localctx = langParser.CastToFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(langParser.TOFLOAT)
                self.state = 70
                self.expr(6)
                pass

            elif la_ == 4:
                localctx = langParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(langParser.INT)
                pass

            elif la_ == 5:
                localctx = langParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(langParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = langParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(langParser.ID)
                pass

            elif la_ == 7:
                localctx = langParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(langParser.STRING)
                pass

            elif la_ == 8:
                localctx = langParser.ArrayElemContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(langParser.ID)
                self.state = 79
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 76
                    self.match(langParser.T__1)
                    self.state = 77
                    self.match(langParser.INT)
                    self.state = 78
                    self.match(langParser.T__2)


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = langParser.MulDivContext(self, langParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 84
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = langParser.AddSubContext(self, langParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 87
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expr(10)
                        pass

             
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(langParser.INT, 0)

        def FLOAT(self):
            return self.getToken(langParser.FLOAT, 0)

        def TOINT(self):
            return self.getToken(langParser.TOINT, 0)

        def TOFLOAT(self):
            return self.getToken(langParser.TOFLOAT, 0)

        def getRuleIndex(self):
            return langParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)




    def num(self):

        localctx = langParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 221184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.NumContext)
            else:
                return self.getTypedRuleContext(langParser.NumContext,i)


        def ADD(self):
            return self.getToken(langParser.ADD, 0)

        def artoperation(self):
            return self.getTypedRuleContext(langParser.ArtoperationContext,0)


        def getRuleIndex(self):
            return langParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)




    def sum_(self):

        localctx = langParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sum)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.num()
                self.state = 98
                self.match(langParser.ADD)
                self.state = 99
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.num()
                self.state = 102
                self.match(langParser.ADD)
                self.state = 103
                self.artoperation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.NumContext)
            else:
                return self.getTypedRuleContext(langParser.NumContext,i)


        def SUBSTRACT(self):
            return self.getToken(langParser.SUBSTRACT, 0)

        def artoperation(self):
            return self.getTypedRuleContext(langParser.ArtoperationContext,0)


        def getRuleIndex(self):
            return langParser.RULE_diff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiff" ):
                listener.enterDiff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiff" ):
                listener.exitDiff(self)




    def diff(self):

        localctx = langParser.DiffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_diff)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.num()
                self.state = 109
                self.match(langParser.SUBSTRACT)
                self.state = 110
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.num()
                self.state = 113
                self.match(langParser.SUBSTRACT)
                self.state = 114
                self.artoperation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.NumContext)
            else:
                return self.getTypedRuleContext(langParser.NumContext,i)


        def MULT(self):
            return self.getToken(langParser.MULT, 0)

        def artoperation(self):
            return self.getTypedRuleContext(langParser.ArtoperationContext,0)


        def getRuleIndex(self):
            return langParser.RULE_prod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProd" ):
                listener.enterProd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProd" ):
                listener.exitProd(self)




    def prod(self):

        localctx = langParser.ProdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_prod)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.num()
                self.state = 120
                self.match(langParser.MULT)
                self.state = 121
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.num()
                self.state = 124
                self.match(langParser.MULT)
                self.state = 125
                self.artoperation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotientContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.NumContext)
            else:
                return self.getTypedRuleContext(langParser.NumContext,i)


        def DIVIDE(self):
            return self.getToken(langParser.DIVIDE, 0)

        def artoperation(self):
            return self.getTypedRuleContext(langParser.ArtoperationContext,0)


        def getRuleIndex(self):
            return langParser.RULE_quotient

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuotient" ):
                listener.enterQuotient(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuotient" ):
                listener.exitQuotient(self)




    def quotient(self):

        localctx = langParser.QuotientContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quotient)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.num()
                self.state = 131
                self.match(langParser.DIVIDE)
                self.state = 132
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.num()
                self.state = 135
                self.match(langParser.DIVIDE)
                self.state = 136
                self.artoperation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArtoperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sum_(self):
            return self.getTypedRuleContext(langParser.SumContext,0)


        def diff(self):
            return self.getTypedRuleContext(langParser.DiffContext,0)


        def prod(self):
            return self.getTypedRuleContext(langParser.ProdContext,0)


        def quotient(self):
            return self.getTypedRuleContext(langParser.QuotientContext,0)


        def getRuleIndex(self):
            return langParser.RULE_artoperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArtoperation" ):
                listener.enterArtoperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArtoperation" ):
                listener.exitArtoperation(self)




    def artoperation(self):

        localctx = langParser.ArtoperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_artoperation)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.sum_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.diff()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.prod()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.quotient()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         




