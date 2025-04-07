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
        4,1,16,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,3,0,10,8,0,1,0,5,0,
        13,8,0,10,0,12,0,16,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,
        13,14,1,0,11,12,59,0,14,1,0,0,0,2,25,1,0,0,0,4,36,1,0,0,0,6,49,1,
        0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,13,
        5,15,0,0,12,9,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,
        15,1,1,0,0,0,16,14,1,0,0,0,17,18,5,2,0,0,18,26,3,4,2,0,19,20,5,4,
        0,0,20,21,5,1,0,0,21,26,3,4,2,0,22,23,5,3,0,0,23,26,5,4,0,0,24,26,
        3,4,2,0,25,17,1,0,0,0,25,19,1,0,0,0,25,22,1,0,0,0,25,24,1,0,0,0,
        26,3,1,0,0,0,27,28,3,6,3,0,28,29,7,0,0,0,29,30,3,4,2,0,30,37,1,0,
        0,0,31,32,3,6,3,0,32,33,7,1,0,0,33,34,3,4,2,0,34,37,1,0,0,0,35,37,
        3,6,3,0,36,27,1,0,0,0,36,31,1,0,0,0,36,35,1,0,0,0,37,5,1,0,0,0,38,
        50,5,5,0,0,39,50,5,6,0,0,40,50,5,4,0,0,41,42,5,7,0,0,42,50,3,6,3,
        0,43,44,5,8,0,0,44,50,3,6,3,0,45,46,5,9,0,0,46,47,3,4,2,0,47,48,
        5,10,0,0,48,50,1,0,0,0,49,38,1,0,0,0,49,39,1,0,0,0,49,40,1,0,0,0,
        49,41,1,0,0,0,49,43,1,0,0,0,49,45,1,0,0,0,50,7,1,0,0,0,5,9,14,25,
        36,49
    ]

class langParser ( Parser ):

    grammarFileName = "lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'bark'", "'listen'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'(int)'", "'(float)'", "'('", 
                     "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WRITE", "READ", "ID", "INT", 
                      "FLOAT", "TOINT", "TOFLOAT", "LP", "RP", "ADD", "SUBSTRACT", 
                      "MULT", "DIVIDE", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_value = 3

    ruleNames =  [ "prog", "stat", "expr", "value" ]

    EOF = Token.EOF
    T__0=1
    WRITE=2
    READ=3
    ID=4
    INT=5
    FLOAT=6
    TOINT=7
    TOFLOAT=8
    LP=9
    RP=10
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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(langParser.NEWLINE)
            else:
                return self.getToken(langParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(langParser.StatContext)
            else:
                return self.getTypedRuleContext(langParser.StatContext,i)


        def getRuleIndex(self):
            return langParser.RULE_prog

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

        localctx = langParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33788) != 0):
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1020) != 0):
                    self.state = 8
                    self.stat()


                self.state = 11
                self.match(langParser.NEWLINE)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStat" ):
                return visitor.visitExprStat(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = langParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = langParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(langParser.WRITE)
                self.state = 18
                self.expr()
                pass

            elif la_ == 2:
                localctx = langParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(langParser.ID)
                self.state = 20
                self.match(langParser.T__0)
                self.state = 21
                self.expr()
                pass

            elif la_ == 3:
                localctx = langParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(langParser.READ)
                self.state = 23
                self.match(langParser.ID)
                pass

            elif la_ == 4:
                localctx = langParser.ExprStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.expr()
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



    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(langParser.ValueContext,0)

        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(langParser.ValueContext,0)

        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ValExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(langParser.ValueContext,0)


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

        localctx = langParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = langParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.value()
                self.state = 28
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 29
                self.expr()
                pass

            elif la_ == 2:
                localctx = langParser.AddSubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.value()
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.expr()
                pass

            elif la_ == 3:
                localctx = langParser.ValExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.value()
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
            return langParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ValueContext
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class VarExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ValueContext
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExpr" ):
                return visitor.visitVarExpr(self)
            else:
                return visitor.visitChildren(self)


    class IntExprContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ValueContext
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntExpr" ):
                return visitor.visitIntExpr(self)
            else:
                return visitor.visitChildren(self)


    class CastToFloatContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOFLOAT(self):
            return self.getToken(langParser.TOFLOAT, 0)
        def value(self):
            return self.getTypedRuleContext(langParser.ValueContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(langParser.TOINT, 0)
        def value(self):
            return self.getTypedRuleContext(langParser.ValueContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a langParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(langParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(langParser.ExprContext,0)

        def RP(self):
            return self.getToken(langParser.RP, 0)

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

        localctx = langParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = langParser.IntExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(langParser.INT)
                pass
            elif token in [6]:
                localctx = langParser.FloatExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(langParser.FLOAT)
                pass
            elif token in [4]:
                localctx = langParser.VarExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(langParser.ID)
                pass
            elif token in [7]:
                localctx = langParser.CastToIntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(langParser.TOINT)
                self.state = 42
                self.value()
                pass
            elif token in [8]:
                localctx = langParser.CastToFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(langParser.TOFLOAT)
                self.state = 44
                self.value()
                pass
            elif token in [9]:
                localctx = langParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.match(langParser.LP)
                self.state = 46
                self.expr()
                self.state = 47
                self.match(langParser.RP)
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





