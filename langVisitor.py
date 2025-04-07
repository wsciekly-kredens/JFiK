# Generated from lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .langParser import langParser
else:
    from langParser import langParser

# This class defines a complete generic visitor for a parse tree produced by langParser.

class langVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by langParser#prog.
    def visitProg(self, ctx:langParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#write.
    def visitWrite(self, ctx:langParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#assign.
    def visitAssign(self, ctx:langParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#read.
    def visitRead(self, ctx:langParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#exprStat.
    def visitExprStat(self, ctx:langParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#MulDiv.
    def visitMulDiv(self, ctx:langParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#AddSub.
    def visitAddSub(self, ctx:langParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#valExpr.
    def visitValExpr(self, ctx:langParser.ValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#intExpr.
    def visitIntExpr(self, ctx:langParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#floatExpr.
    def visitFloatExpr(self, ctx:langParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#varExpr.
    def visitVarExpr(self, ctx:langParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#CastToInt.
    def visitCastToInt(self, ctx:langParser.CastToIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#CastToFloat.
    def visitCastToFloat(self, ctx:langParser.CastToFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by langParser#ParenExpr.
    def visitParenExpr(self, ctx:langParser.ParenExprContext):
        return self.visitChildren(ctx)



del langParser