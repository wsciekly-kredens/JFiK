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
        4,1,23,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,3,0,10,8,0,1,0,5,0,
        13,8,0,10,0,12,0,16,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,30,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,
        41,9,1,1,1,1,1,3,1,45,8,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,63,8,2,3,2,65,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,78,8,3,1,3,0,0,4,0,2,4,6,0,2,1,
        0,20,21,1,0,18,19,94,0,14,1,0,0,0,2,46,1,0,0,0,4,64,1,0,0,0,6,77,
        1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,13,
        5,22,0,0,12,9,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,
        15,1,1,0,0,0,16,14,1,0,0,0,17,18,5,7,0,0,18,47,3,4,2,0,19,20,5,10,
        0,0,20,21,5,1,0,0,21,47,3,4,2,0,22,23,5,8,0,0,23,47,5,10,0,0,24,
        47,3,4,2,0,25,26,5,9,0,0,26,27,5,10,0,0,27,29,5,2,0,0,28,30,5,11,
        0,0,29,28,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,44,5,3,0,0,32,33,
        5,1,0,0,33,34,5,4,0,0,34,39,3,4,2,0,35,36,5,5,0,0,36,38,3,4,2,0,
        37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,
        0,0,0,41,39,1,0,0,0,42,43,5,6,0,0,43,45,1,0,0,0,44,32,1,0,0,0,44,
        45,1,0,0,0,45,47,1,0,0,0,46,17,1,0,0,0,46,19,1,0,0,0,46,22,1,0,0,
        0,46,24,1,0,0,0,46,25,1,0,0,0,47,3,1,0,0,0,48,49,3,6,3,0,49,50,7,
        0,0,0,50,51,3,4,2,0,51,65,1,0,0,0,52,53,3,6,3,0,53,54,7,1,0,0,54,
        55,3,4,2,0,55,65,1,0,0,0,56,65,3,6,3,0,57,65,5,13,0,0,58,62,5,10,
        0,0,59,60,5,2,0,0,60,61,5,11,0,0,61,63,5,3,0,0,62,59,1,0,0,0,62,
        63,1,0,0,0,63,65,1,0,0,0,64,48,1,0,0,0,64,52,1,0,0,0,64,56,1,0,0,
        0,64,57,1,0,0,0,64,58,1,0,0,0,65,5,1,0,0,0,66,78,5,11,0,0,67,78,
        5,12,0,0,68,78,5,10,0,0,69,70,5,14,0,0,70,78,3,6,3,0,71,72,5,15,
        0,0,72,78,3,6,3,0,73,74,5,16,0,0,74,75,3,4,2,0,75,76,5,17,0,0,76,
        78,1,0,0,0,77,66,1,0,0,0,77,67,1,0,0,0,77,68,1,0,0,0,77,69,1,0,0,
        0,77,71,1,0,0,0,77,73,1,0,0,0,78,7,1,0,0,0,9,9,14,29,39,44,46,62,
        64,77
    ]

class pawtonParser ( Parser ):

    grammarFileName = "pawton.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "'{'", "','", "'}'", 
                     "'bark'", "'listen'", "'pack'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'(int)'", "'(float)'", "'('", 
                     "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WRITE", "READ", 
                      "ARRAY", "ID", "INT", "FLOAT", "STRING", "TOINT", 
                      "TOFLOAT", "LP", "RP", "ADD", "SUBSTRACT", "MULT", 
                      "DIVIDE", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_value = 3

    ruleNames =  [ "prog", "stat", "expr", "value" ]

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
    ID=10
    INT=11
    FLOAT=12
    STRING=13
    TOINT=14
    TOFLOAT=15
    LP=16
    RP=17
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
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4325248) != 0):
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 130944) != 0):
                    self.state = 8
                    self.stat()


                self.state = 11
                self.match(pawtonParser.NEWLINE)
                self.state = 16
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



    def stat(self):

        localctx = pawtonParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = pawtonParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(pawtonParser.WRITE)
                self.state = 18
                self.expr()
                pass

            elif la_ == 2:
                localctx = pawtonParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(pawtonParser.ID)
                self.state = 20
                self.match(pawtonParser.T__0)
                self.state = 21
                self.expr()
                pass

            elif la_ == 3:
                localctx = pawtonParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(pawtonParser.READ)
                self.state = 23
                self.match(pawtonParser.ID)
                pass

            elif la_ == 4:
                localctx = pawtonParser.ExprStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.expr()
                pass

            elif la_ == 5:
                localctx = pawtonParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 25
                self.match(pawtonParser.ARRAY)
                self.state = 26
                self.match(pawtonParser.ID)
                self.state = 27
                self.match(pawtonParser.T__1)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 28
                    self.match(pawtonParser.INT)


                self.state = 31
                self.match(pawtonParser.T__2)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 32
                    self.match(pawtonParser.T__0)
                    self.state = 33
                    self.match(pawtonParser.T__3)
                    self.state = 34
                    self.expr()
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==5:
                        self.state = 35
                        self.match(pawtonParser.T__4)
                        self.state = 36
                        self.expr()
                        self.state = 41
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 42
                    self.match(pawtonParser.T__5)


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
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = pawtonParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.value()
                self.state = 49
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 50
                self.expr()
                pass

            elif la_ == 2:
                localctx = pawtonParser.AddSubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.value()
                self.state = 53
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.expr()
                pass

            elif la_ == 3:
                localctx = pawtonParser.ValExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.value()
                pass

            elif la_ == 4:
                localctx = pawtonParser.StringExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(pawtonParser.STRING)
                pass

            elif la_ == 5:
                localctx = pawtonParser.ArrayElemContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.match(pawtonParser.ID)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2:
                    self.state = 59
                    self.match(pawtonParser.T__1)
                    self.state = 60
                    self.match(pawtonParser.INT)
                    self.state = 61
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = pawtonParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(pawtonParser.INT)
                pass
            elif token in [12]:
                localctx = pawtonParser.FloatExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(pawtonParser.FLOAT)
                pass
            elif token in [10]:
                localctx = pawtonParser.VarExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(pawtonParser.ID)
                pass
            elif token in [14]:
                localctx = pawtonParser.CastToIntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.match(pawtonParser.TOINT)
                self.state = 70
                self.value()
                pass
            elif token in [15]:
                localctx = pawtonParser.CastToFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 71
                self.match(pawtonParser.TOFLOAT)
                self.state = 72
                self.value()
                pass
            elif token in [16]:
                localctx = pawtonParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.match(pawtonParser.LP)
                self.state = 74
                self.expr()
                self.state = 75
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





