# Generated from pawton.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pawtonParser import pawtonParser
else:
    from pawtonParser import pawtonParser

# This class defines a complete listener for a parse tree produced by pawtonParser.
class pawtonListener(ParseTreeListener):

    # Enter a parse tree produced by pawtonParser#prog.
    def enterProg(self, ctx:pawtonParser.ProgContext):
        pass

    # Exit a parse tree produced by pawtonParser#prog.
    def exitProg(self, ctx:pawtonParser.ProgContext):
        pass


    # Enter a parse tree produced by pawtonParser#write.
    def enterWrite(self, ctx:pawtonParser.WriteContext):
        pass

    # Exit a parse tree produced by pawtonParser#write.
    def exitWrite(self, ctx:pawtonParser.WriteContext):
        pass


    # Enter a parse tree produced by pawtonParser#assign.
    def enterAssign(self, ctx:pawtonParser.AssignContext):
        pass

    # Exit a parse tree produced by pawtonParser#assign.
    def exitAssign(self, ctx:pawtonParser.AssignContext):
        pass


    # Enter a parse tree produced by pawtonParser#read.
    def enterRead(self, ctx:pawtonParser.ReadContext):
        pass

    # Exit a parse tree produced by pawtonParser#read.
    def exitRead(self, ctx:pawtonParser.ReadContext):
        pass


    # Enter a parse tree produced by pawtonParser#exprStat.
    def enterExprStat(self, ctx:pawtonParser.ExprStatContext):
        pass

    # Exit a parse tree produced by pawtonParser#exprStat.
    def exitExprStat(self, ctx:pawtonParser.ExprStatContext):
        pass


    # Enter a parse tree produced by pawtonParser#array.
    def enterArray(self, ctx:pawtonParser.ArrayContext):
        pass

    # Exit a parse tree produced by pawtonParser#array.
    def exitArray(self, ctx:pawtonParser.ArrayContext):
        pass


    # Enter a parse tree produced by pawtonParser#funcDef.
    def enterFuncDef(self, ctx:pawtonParser.FuncDefContext):
        pass

    # Exit a parse tree produced by pawtonParser#funcDef.
    def exitFuncDef(self, ctx:pawtonParser.FuncDefContext):
        pass


    # Enter a parse tree produced by pawtonParser#funcCall.
    def enterFuncCall(self, ctx:pawtonParser.FuncCallContext):
        pass

    # Exit a parse tree produced by pawtonParser#funcCall.
    def exitFuncCall(self, ctx:pawtonParser.FuncCallContext):
        pass


    # Enter a parse tree produced by pawtonParser#MulDiv.
    def enterMulDiv(self, ctx:pawtonParser.MulDivContext):
        pass

    # Exit a parse tree produced by pawtonParser#MulDiv.
    def exitMulDiv(self, ctx:pawtonParser.MulDivContext):
        pass


    # Enter a parse tree produced by pawtonParser#AddSub.
    def enterAddSub(self, ctx:pawtonParser.AddSubContext):
        pass

    # Exit a parse tree produced by pawtonParser#AddSub.
    def exitAddSub(self, ctx:pawtonParser.AddSubContext):
        pass


    # Enter a parse tree produced by pawtonParser#valExpr.
    def enterValExpr(self, ctx:pawtonParser.ValExprContext):
        pass

    # Exit a parse tree produced by pawtonParser#valExpr.
    def exitValExpr(self, ctx:pawtonParser.ValExprContext):
        pass


    # Enter a parse tree produced by pawtonParser#stringExpr.
    def enterStringExpr(self, ctx:pawtonParser.StringExprContext):
        pass

    # Exit a parse tree produced by pawtonParser#stringExpr.
    def exitStringExpr(self, ctx:pawtonParser.StringExprContext):
        pass


    # Enter a parse tree produced by pawtonParser#arrayElem.
    def enterArrayElem(self, ctx:pawtonParser.ArrayElemContext):
        pass

    # Exit a parse tree produced by pawtonParser#arrayElem.
    def exitArrayElem(self, ctx:pawtonParser.ArrayElemContext):
        pass


    # Enter a parse tree produced by pawtonParser#intExpr.
    def enterIntExpr(self, ctx:pawtonParser.IntExprContext):
        pass

    # Exit a parse tree produced by pawtonParser#intExpr.
    def exitIntExpr(self, ctx:pawtonParser.IntExprContext):
        pass


    # Enter a parse tree produced by pawtonParser#floatExpr.
    def enterFloatExpr(self, ctx:pawtonParser.FloatExprContext):
        pass

    # Exit a parse tree produced by pawtonParser#floatExpr.
    def exitFloatExpr(self, ctx:pawtonParser.FloatExprContext):
        pass


    # Enter a parse tree produced by pawtonParser#varExpr.
    def enterVarExpr(self, ctx:pawtonParser.VarExprContext):
        pass

    # Exit a parse tree produced by pawtonParser#varExpr.
    def exitVarExpr(self, ctx:pawtonParser.VarExprContext):
        pass


    # Enter a parse tree produced by pawtonParser#CastToInt.
    def enterCastToInt(self, ctx:pawtonParser.CastToIntContext):
        pass

    # Exit a parse tree produced by pawtonParser#CastToInt.
    def exitCastToInt(self, ctx:pawtonParser.CastToIntContext):
        pass


    # Enter a parse tree produced by pawtonParser#CastToFloat.
    def enterCastToFloat(self, ctx:pawtonParser.CastToFloatContext):
        pass

    # Exit a parse tree produced by pawtonParser#CastToFloat.
    def exitCastToFloat(self, ctx:pawtonParser.CastToFloatContext):
        pass


    # Enter a parse tree produced by pawtonParser#ParenExpr.
    def enterParenExpr(self, ctx:pawtonParser.ParenExprContext):
        pass

    # Exit a parse tree produced by pawtonParser#ParenExpr.
    def exitParenExpr(self, ctx:pawtonParser.ParenExprContext):
        pass


    # Enter a parse tree produced by pawtonParser#block.
    def enterBlock(self, ctx:pawtonParser.BlockContext):
        pass

    # Exit a parse tree produced by pawtonParser#block.
    def exitBlock(self, ctx:pawtonParser.BlockContext):
        pass



del pawtonParser