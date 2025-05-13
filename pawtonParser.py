# Generated from pawton.g4 by ANTLR 4.13.2
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
        4,1,24,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,
        0,1,0,5,0,15,8,0,10,0,12,0,18,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,32,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,
        10,1,12,1,43,9,1,1,1,1,1,3,1,47,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,
        55,8,1,10,1,12,1,58,9,1,3,1,60,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,69,8,1,10,1,12,1,72,9,1,3,1,74,8,1,1,1,3,1,77,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,3,2,95,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,108,8,3,1,4,1,
        4,3,4,112,8,4,1,4,5,4,115,8,4,10,4,12,4,118,9,4,1,4,1,4,1,4,0,0,
        5,0,2,4,6,8,0,2,1,0,21,22,1,0,19,20,143,0,16,1,0,0,0,2,76,1,0,0,
        0,4,94,1,0,0,0,6,107,1,0,0,0,8,109,1,0,0,0,10,12,3,2,1,0,11,10,1,
        0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,15,5,23,0,0,14,11,1,0,0,0,15,
        18,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,1,1,0,0,0,18,16,1,0,0,
        0,19,20,5,7,0,0,20,77,3,4,2,0,21,22,5,11,0,0,22,23,5,1,0,0,23,77,
        3,4,2,0,24,25,5,8,0,0,25,77,5,11,0,0,26,77,3,4,2,0,27,28,5,9,0,0,
        28,29,5,11,0,0,29,31,5,2,0,0,30,32,5,12,0,0,31,30,1,0,0,0,31,32,
        1,0,0,0,32,33,1,0,0,0,33,46,5,3,0,0,34,35,5,1,0,0,35,36,5,4,0,0,
        36,41,3,4,2,0,37,38,5,5,0,0,38,40,3,4,2,0,39,37,1,0,0,0,40,43,1,
        0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,
        45,5,6,0,0,45,47,1,0,0,0,46,34,1,0,0,0,46,47,1,0,0,0,47,77,1,0,0,
        0,48,49,5,10,0,0,49,50,5,11,0,0,50,59,5,17,0,0,51,56,5,11,0,0,52,
        53,5,5,0,0,53,55,5,11,0,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,
        0,0,56,57,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,59,51,1,0,0,0,59,60,
        1,0,0,0,60,61,1,0,0,0,61,62,5,18,0,0,62,77,3,8,4,0,63,64,5,11,0,
        0,64,73,5,17,0,0,65,70,3,4,2,0,66,67,5,5,0,0,67,69,3,4,2,0,68,66,
        1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,74,1,0,0,0,
        72,70,1,0,0,0,73,65,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,77,5,
        18,0,0,76,19,1,0,0,0,76,21,1,0,0,0,76,24,1,0,0,0,76,26,1,0,0,0,76,
        27,1,0,0,0,76,48,1,0,0,0,76,63,1,0,0,0,77,3,1,0,0,0,78,79,3,6,3,
        0,79,80,7,0,0,0,80,81,3,4,2,0,81,95,1,0,0,0,82,83,3,6,3,0,83,84,
        7,1,0,0,84,85,3,4,2,0,85,95,1,0,0,0,86,95,3,6,3,0,87,95,5,14,0,0,
        88,92,5,11,0,0,89,90,5,2,0,0,90,91,5,12,0,0,91,93,5,3,0,0,92,89,
        1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,78,1,0,0,0,94,82,1,0,0,0,
        94,86,1,0,0,0,94,87,1,0,0,0,94,88,1,0,0,0,95,5,1,0,0,0,96,108,5,
        12,0,0,97,108,5,13,0,0,98,108,5,11,0,0,99,100,5,15,0,0,100,108,3,
        6,3,0,101,102,5,16,0,0,102,108,3,6,3,0,103,104,5,17,0,0,104,105,
        3,4,2,0,105,106,5,18,0,0,106,108,1,0,0,0,107,96,1,0,0,0,107,97,1,
        0,0,0,107,98,1,0,0,0,107,99,1,0,0,0,107,101,1,0,0,0,107,103,1,0,
        0,0,108,7,1,0,0,0,109,116,5,4,0,0,110,112,3,2,1,0,111,110,1,0,0,
        0,111,112,1,0,0,0,112,113,1,0,0,0,113,115,5,23,0,0,114,111,1,0,0,
        0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,
        0,118,116,1,0,0,0,119,120,5,6,0,0,120,9,1,0,0,0,15,11,16,31,41,46,
        56,59,70,73,76,92,94,107,111,116
    ]

class pawtonParser ( Parser ):

    grammarFileName = "pawton.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "'{'", "','", "'}'", 
                     "'bark'", "'listen'", "'pack'", "'command'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'(int)'", "'(float)'", 
                     "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WRITE", "READ", 
                      "ARRAY", "FUNC", "ID", "INT", "FLOAT", "STRING", "TOINT", 
                      "TOFLOAT", "LP", "RP", "ADD", "SUBSTRACT", "MULT", 
                      "DIVIDE", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_value = 3
    RULE_block = 4

    ruleNames =  [ "prog", "stat", "expr", "value", "block" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WRITE=7
    READ=8
    ARRAY=9
    FUNC=10
    ID=11
    INT=12
    FLOAT=13
    STRING=14
    TOINT=15
    TOFLOAT=16
    LP=17
    RP=18
    ADD=19
    SUBSTRACT=20
    MULT=21
    DIVIDE=22
    NEWLINE=23
    WS=24

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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(pawtonParser.NEWLINE)
            else:
                return self.getToken(pawtonParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pawtonParser.StatContext)
            else:
                return self.getTypedRuleContext(pawtonParser.StatContext,i)


        def getRuleIndex(self):
            return pawtonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = pawtonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8650624) != 0):
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 262016) != 0):
                    self.state = 10
                    self.stat()


                self.state = 13
                self.match(pawtonParser.NEWLINE)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return pawtonParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(pawtonParser.READ, 0)
        def ID(self):
            return self.getToken(pawtonParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class ArrayContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ARRAY(self):
            return self.getToken(pawtonParser.ARRAY, 0)
        def ID(self):
            return self.getToken(pawtonParser.ID, 0)
        def INT(self):
            return self.getToken(pawtonParser.INT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pawtonParser.ExprContext)
            else:
                return self.getTypedRuleContext(pawtonParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)


    class ExprStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(pawtonParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStat" ):
                listener.enterExprStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStat" ):
                listener.exitExprStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStat" ):
                return visitor.visitExprStat(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pawtonParser.ID, 0)
        def LP(self):
            return self.getToken(pawtonParser.LP, 0)
        def RP(self):
            return self.getToken(pawtonParser.RP, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pawtonParser.ExprContext)
            else:
                return self.getTypedRuleContext(pawtonParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(pawtonParser.WRITE, 0)
        def expr(self):
            return self.getTypedRuleContext(pawtonParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pawtonParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(pawtonParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class FuncDefContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FUNC(self):
            return self.getToken(pawtonParser.FUNC, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pawtonParser.ID)
            else:
                return self.getToken(pawtonParser.ID, i)
        def LP(self):
            return self.getToken(pawtonParser.LP, 0)
        def RP(self):
            return self.getToken(pawtonParser.RP, 0)
        def block(self):
            return self.getTypedRuleContext(pawtonParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = pawtonParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = pawtonParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(pawtonParser.WRITE)
                self.state = 20
                self.expr()
                pass

            elif la_ == 2:
                localctx = pawtonParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(pawtonParser.ID)
                self.state = 22
                self.match(pawtonParser.T__0)
                self.state = 23
                self.expr()
                pass

            elif la_ == 3:
                localctx = pawtonParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(pawtonParser.READ)
                self.state = 25
                self.match(pawtonParser.ID)
                pass

            elif la_ == 4:
                localctx = pawtonParser.ExprStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.expr()
                pass

            elif la_ == 5:
                localctx = pawtonParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.match(pawtonParser.ARRAY)
                self.state = 28
                self.match(pawtonParser.ID)
                self.state = 29
                self.match(pawtonParser.T__1)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 30
                    self.match(pawtonParser.INT)


                self.state = 33
                self.match(pawtonParser.T__2)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 34
                    self.match(pawtonParser.T__0)
                    self.state = 35
                    self.match(pawtonParser.T__3)
                    self.state = 36
                    self.expr()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 37
                        self.match(pawtonParser.T__4)
                        self.state = 38
                        self.expr()
                        self.state = 43
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 44
                    self.match(pawtonParser.T__5)


                pass

            elif la_ == 6:
                localctx = pawtonParser.FuncDefContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(pawtonParser.FUNC)
                self.state = 49
                self.match(pawtonParser.ID)
                self.state = 50
                self.match(pawtonParser.LP)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 51
                    self.match(pawtonParser.ID)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 52
                        self.match(pawtonParser.T__4)
                        self.state = 53
                        self.match(pawtonParser.ID)
                        self.state = 58
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 61
                self.match(pawtonParser.RP)
                self.state = 62
                self.block()
                pass

            elif la_ == 7:
                localctx = pawtonParser.FuncCallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.match(pawtonParser.ID)
                self.state = 64
                self.match(pawtonParser.LP)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 260096) != 0):
                    self.state = 65
                    self.expr()
                    self.state = 70
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 66
                        self.match(pawtonParser.T__4)
                        self.state = 67
                        self.expr()
                        self.state = 72
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 75
                self.match(pawtonParser.RP)
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
            return pawtonParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(pawtonParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayElemContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pawtonParser.ID, 0)
        def INT(self):
            return self.getToken(pawtonParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayElem" ):
                listener.enterArrayElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayElem" ):
                listener.exitArrayElem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElem" ):
                return visitor.visitArrayElem(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(pawtonParser.ValueContext,0)

        def expr(self):
            return self.getTypedRuleContext(pawtonParser.ExprContext,0)

        def MULT(self):
            return self.getToken(pawtonParser.MULT, 0)
        def DIVIDE(self):
            return self.getToken(pawtonParser.DIVIDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(pawtonParser.ValueContext,0)

        def expr(self):
            return self.getTypedRuleContext(pawtonParser.ExprContext,0)

        def ADD(self):
            return self.getToken(pawtonParser.ADD, 0)
        def SUBSTRACT(self):
            return self.getToken(pawtonParser.SUBSTRACT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ValExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(pawtonParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValExpr" ):
                listener.enterValExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValExpr" ):
                listener.exitValExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValExpr" ):
                return visitor.visitValExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = pawtonParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = pawtonParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.value()
                self.state = 79
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 80
                self.expr()
                pass

            elif la_ == 2:
                localctx = pawtonParser.AddSubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.value()
                self.state = 83
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 84
                self.expr()
                pass

            elif la_ == 3:
                localctx = pawtonParser.ValExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 86
                self.value()
                pass

            elif la_ == 4:
                localctx = pawtonParser.StringExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.match(pawtonParser.STRING)
                pass

            elif la_ == 5:
                localctx = pawtonParser.ArrayElemContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 88
                self.match(pawtonParser.ID)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 89
                    self.match(pawtonParser.T__1)
                    self.state = 90
                    self.match(pawtonParser.INT)
                    self.state = 91
                    self.match(pawtonParser.T__2)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pawtonParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(pawtonParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pawtonParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExpr" ):
                listener.enterVarExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExpr" ):
                listener.exitVarExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(pawtonParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class CastToFloatContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOFLOAT(self):
            return self.getToken(pawtonParser.TOFLOAT, 0)
        def value(self):
            return self.getTypedRuleContext(pawtonParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastToFloat" ):
                listener.enterCastToFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastToFloat" ):
                listener.exitCastToFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastToFloat" ):
                return visitor.visitCastToFloat(self)
            else:
                return visitor.visitChildren(self)


    class CastToIntContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(pawtonParser.TOINT, 0)
        def value(self):
            return self.getTypedRuleContext(pawtonParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastToInt" ):
                listener.enterCastToInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastToInt" ):
                listener.exitCastToInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastToInt" ):
                return visitor.visitCastToInt(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pawtonParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(pawtonParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(pawtonParser.ExprContext,0)

        def RP(self):
            return self.getToken(pawtonParser.RP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = pawtonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = pawtonParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(pawtonParser.INT)
                pass
            elif token in [13]:
                localctx = pawtonParser.FloatExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(pawtonParser.FLOAT)
                pass
            elif token in [11]:
                localctx = pawtonParser.VarExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.match(pawtonParser.ID)
                pass
            elif token in [15]:
                localctx = pawtonParser.CastToIntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.match(pawtonParser.TOINT)
                self.state = 100
                self.value()
                pass
            elif token in [16]:
                localctx = pawtonParser.CastToFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.match(pawtonParser.TOFLOAT)
                self.state = 102
                self.value()
                pass
            elif token in [17]:
                localctx = pawtonParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 103
                self.match(pawtonParser.LP)
                self.state = 104
                self.expr()
                self.state = 105
                self.match(pawtonParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(pawtonParser.NEWLINE)
            else:
                return self.getToken(pawtonParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pawtonParser.StatContext)
            else:
                return self.getTypedRuleContext(pawtonParser.StatContext,i)


        def getRuleIndex(self):
            return pawtonParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = pawtonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(pawtonParser.T__3)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8650624) != 0):
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 262016) != 0):
                    self.state = 110
                    self.stat()


                self.state = 113
                self.match(pawtonParser.NEWLINE)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(pawtonParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





