# Generated from lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser

# This class defines a complete listener for a parse tree produced by langParser.
class langListener(ParseTreeListener):

    # Enter a parse tree produced by langParser#prog.
    def enterProg(self, ctx:langParser.ProgContext):
        pass

    # Exit a parse tree produced by langParser#prog.
    def exitProg(self, ctx:langParser.ProgContext):
        pass


    # Enter a parse tree produced by langParser#write.
    def enterWrite(self, ctx:langParser.WriteContext):
        pass

    # Exit a parse tree produced by langParser#write.
    def exitWrite(self, ctx:langParser.WriteContext):
        pass


    # Enter a parse tree produced by langParser#assign.
    def enterAssign(self, ctx:langParser.AssignContext):
        pass

    # Exit a parse tree produced by langParser#assign.
    def exitAssign(self, ctx:langParser.AssignContext):
        pass


    # Enter a parse tree produced by langParser#read.
    def enterRead(self, ctx:langParser.ReadContext):
        pass

    # Exit a parse tree produced by langParser#read.
    def exitRead(self, ctx:langParser.ReadContext):
        pass


    # Enter a parse tree produced by langParser#exprStat.
    def enterExprStat(self, ctx:langParser.ExprStatContext):
        pass

    # Exit a parse tree produced by langParser#exprStat.
    def exitExprStat(self, ctx:langParser.ExprStatContext):
        pass


    # Enter a parse tree produced by langParser#array.
    def enterArray(self, ctx:langParser.ArrayContext):
        pass

    # Exit a parse tree produced by langParser#array.
    def exitArray(self, ctx:langParser.ArrayContext):
        pass


    # Enter a parse tree produced by langParser#stringExpr.
    def enterStringExpr(self, ctx:langParser.StringExprContext):
        pass

    # Exit a parse tree produced by langParser#stringExpr.
    def exitStringExpr(self, ctx:langParser.StringExprContext):
        pass


    # Enter a parse tree produced by langParser#floatExpr.
    def enterFloatExpr(self, ctx:langParser.FloatExprContext):
        pass

    # Exit a parse tree produced by langParser#floatExpr.
    def exitFloatExpr(self, ctx:langParser.FloatExprContext):
        pass


    # Enter a parse tree produced by langParser#varExpr.
    def enterVarExpr(self, ctx:langParser.VarExprContext):
        pass

    # Exit a parse tree produced by langParser#varExpr.
    def exitVarExpr(self, ctx:langParser.VarExprContext):
        pass


    # Enter a parse tree produced by langParser#arrayElem.
    def enterArrayElem(self, ctx:langParser.ArrayElemContext):
        pass

    # Exit a parse tree produced by langParser#arrayElem.
    def exitArrayElem(self, ctx:langParser.ArrayElemContext):
        pass


    # Enter a parse tree produced by langParser#intExpr.
    def enterIntExpr(self, ctx:langParser.IntExprContext):
        pass

    # Exit a parse tree produced by langParser#intExpr.
    def exitIntExpr(self, ctx:langParser.IntExprContext):
        pass


    # Enter a parse tree produced by langParser#CastToFloat.
    def enterCastToFloat(self, ctx:langParser.CastToFloatContext):
        pass

    # Exit a parse tree produced by langParser#CastToFloat.
    def exitCastToFloat(self, ctx:langParser.CastToFloatContext):
        pass


    # Enter a parse tree produced by langParser#MulDiv.
    def enterMulDiv(self, ctx:langParser.MulDivContext):
        pass

    # Exit a parse tree produced by langParser#MulDiv.
    def exitMulDiv(self, ctx:langParser.MulDivContext):
        pass


    # Enter a parse tree produced by langParser#AddSub.
    def enterAddSub(self, ctx:langParser.AddSubContext):
        pass

    # Exit a parse tree produced by langParser#AddSub.
    def exitAddSub(self, ctx:langParser.AddSubContext):
        pass


    # Enter a parse tree produced by langParser#CastToInt.
    def enterCastToInt(self, ctx:langParser.CastToIntContext):
        pass

    # Exit a parse tree produced by langParser#CastToInt.
    def exitCastToInt(self, ctx:langParser.CastToIntContext):
        pass


    # Enter a parse tree produced by langParser#ParenExpr.
    def enterParenExpr(self, ctx:langParser.ParenExprContext):
        pass

    # Exit a parse tree produced by langParser#ParenExpr.
    def exitParenExpr(self, ctx:langParser.ParenExprContext):
        pass


    # Enter a parse tree produced by langParser#num.
    def enterNum(self, ctx:langParser.NumContext):
        pass

    # Exit a parse tree produced by langParser#num.
    def exitNum(self, ctx:langParser.NumContext):
        pass


    # Enter a parse tree produced by langParser#sum.
    def enterSum(self, ctx:langParser.SumContext):
        pass

    # Exit a parse tree produced by langParser#sum.
    def exitSum(self, ctx:langParser.SumContext):
        pass


    # Enter a parse tree produced by langParser#diff.
    def enterDiff(self, ctx:langParser.DiffContext):
        pass

    # Exit a parse tree produced by langParser#diff.
    def exitDiff(self, ctx:langParser.DiffContext):
        pass


    # Enter a parse tree produced by langParser#prod.
    def enterProd(self, ctx:langParser.ProdContext):
        pass

    # Exit a parse tree produced by langParser#prod.
    def exitProd(self, ctx:langParser.ProdContext):
        pass


    # Enter a parse tree produced by langParser#quotient.
    def enterQuotient(self, ctx:langParser.QuotientContext):
        pass

    # Exit a parse tree produced by langParser#quotient.
    def exitQuotient(self, ctx:langParser.QuotientContext):
        pass


    # Enter a parse tree produced by langParser#artoperation.
    def enterArtoperation(self, ctx:langParser.ArtoperationContext):
        pass

    # Exit a parse tree produced by langParser#artoperation.
    def exitArtoperation(self, ctx:langParser.ArtoperationContext):
        pass



del langParser