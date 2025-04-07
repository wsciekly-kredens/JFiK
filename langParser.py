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
        4,1,16,119,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,3,0,30,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,3,5,89,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,100,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,111,8,7,1,8,1,8,1,8,1,8,
        3,8,117,8,8,1,8,0,1,4,9,0,2,4,6,8,10,12,14,16,0,3,1,0,13,14,1,0,
        11,12,1,0,7,10,133,0,19,1,0,0,0,2,39,1,0,0,0,4,53,1,0,0,0,6,66,1,
        0,0,0,8,77,1,0,0,0,10,88,1,0,0,0,12,99,1,0,0,0,14,110,1,0,0,0,16,
        116,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,19,20,1,0,0,0,20,25,1,0,
        0,0,21,22,5,15,0,0,22,24,3,2,1,0,23,21,1,0,0,0,24,27,1,0,0,0,25,
        23,1,0,0,0,25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,28,30,5,15,
        0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,32,5,4,0,0,32,40,
        3,4,2,0,33,34,5,6,0,0,34,35,5,1,0,0,35,40,3,4,2,0,36,37,5,5,0,0,
        37,40,5,6,0,0,38,40,3,4,2,0,39,31,1,0,0,0,39,33,1,0,0,0,39,36,1,
        0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,41,42,6,2,-1,0,42,43,5,2,0,0,43,
        44,3,4,2,0,44,45,5,3,0,0,45,54,1,0,0,0,46,47,5,9,0,0,47,54,3,4,2,
        5,48,49,5,10,0,0,49,54,3,4,2,4,50,54,5,7,0,0,51,54,5,8,0,0,52,54,
        5,6,0,0,53,41,1,0,0,0,53,46,1,0,0,0,53,48,1,0,0,0,53,50,1,0,0,0,
        53,51,1,0,0,0,53,52,1,0,0,0,54,63,1,0,0,0,55,56,10,8,0,0,56,57,7,
        0,0,0,57,62,3,4,2,9,58,59,10,7,0,0,59,60,7,1,0,0,60,62,3,4,2,8,61,
        55,1,0,0,0,61,58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,
        0,64,5,1,0,0,0,65,63,1,0,0,0,66,67,7,2,0,0,67,7,1,0,0,0,68,78,3,
        6,3,0,69,70,3,6,3,0,70,71,5,11,0,0,71,72,3,6,3,0,72,78,1,0,0,0,73,
        74,3,6,3,0,74,75,5,11,0,0,75,76,3,16,8,0,76,78,1,0,0,0,77,68,1,0,
        0,0,77,69,1,0,0,0,77,73,1,0,0,0,78,9,1,0,0,0,79,89,3,6,3,0,80,81,
        3,6,3,0,81,82,5,12,0,0,82,83,3,6,3,0,83,89,1,0,0,0,84,85,3,6,3,0,
        85,86,5,12,0,0,86,87,3,16,8,0,87,89,1,0,0,0,88,79,1,0,0,0,88,80,
        1,0,0,0,88,84,1,0,0,0,89,11,1,0,0,0,90,100,3,6,3,0,91,92,3,6,3,0,
        92,93,5,13,0,0,93,94,3,6,3,0,94,100,1,0,0,0,95,96,3,6,3,0,96,97,
        5,13,0,0,97,98,3,16,8,0,98,100,1,0,0,0,99,90,1,0,0,0,99,91,1,0,0,
        0,99,95,1,0,0,0,100,13,1,0,0,0,101,111,3,6,3,0,102,103,3,6,3,0,103,
        104,5,14,0,0,104,105,3,6,3,0,105,111,1,0,0,0,106,107,3,6,3,0,107,
        108,5,14,0,0,108,109,3,16,8,0,109,111,1,0,0,0,110,101,1,0,0,0,110,
        102,1,0,0,0,110,106,1,0,0,0,111,15,1,0,0,0,112,117,3,8,4,0,113,117,
        3,10,5,0,114,117,3,12,6,0,115,117,3,14,7,0,116,112,1,0,0,0,116,113,
        1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,17,1,0,0,0,12,19,25,
        29,39,53,61,63,77,88,99,110,116
    ]

class langParser ( Parser ):

    grammarFileName = "lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'bark'", "'listen'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'(int)'", "'(float)'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WRITE", "READ", "ID", "INT", "FLOAT", "TOINT", "TOFLOAT", 
                      "ADD", "SUBSTRACT", "MULT", "DIVIDE", "NEWLINE", "WS" ]

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
    WRITE=4
    READ=5
    ID=6
    INT=7
    FLOAT=8
    TOINT=9
    TOFLOAT=10
    ADD=11
    SUBSTRACT=12
    MULT=13
    DIVIDE=14
    NEWLINE=15
    WS=16

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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2036) != 0):
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
            if _la==15:
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
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = langParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(langParser.T__1)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(langParser.T__2)
                pass
            elif token in [9]:
                localctx = langParser.CastToIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(langParser.TOINT)
                self.state = 47
                self.expr(5)
                pass
            elif token in [10]:
                localctx = langParser.CastToFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(langParser.TOFLOAT)
                self.state = 49
                self.expr(4)
                pass
            elif token in [7]:
                localctx = langParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(langParser.INT)
                pass
            elif token in [8]:
                localctx = langParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(langParser.FLOAT)
                pass
            elif token in [6]:
                localctx = langParser.VarExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(langParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = langParser.MulDivContext(self, langParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = langParser.AddSubContext(self, langParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(8)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 66
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.num()
                self.state = 70
                self.match(langParser.ADD)
                self.state = 71
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.num()
                self.state = 74
                self.match(langParser.ADD)
                self.state = 75
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.num()
                self.state = 81
                self.match(langParser.SUBSTRACT)
                self.state = 82
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.num()
                self.state = 85
                self.match(langParser.SUBSTRACT)
                self.state = 86
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
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.num()
                self.state = 92
                self.match(langParser.MULT)
                self.state = 93
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.num()
                self.state = 96
                self.match(langParser.MULT)
                self.state = 97
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
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.num()
                self.state = 103
                self.match(langParser.DIVIDE)
                self.state = 104
                self.num()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.num()
                self.state = 107
                self.match(langParser.DIVIDE)
                self.state = 108
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
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.sum_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.diff()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.prod()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
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
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




