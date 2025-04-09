# Generated from pawton.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .pawtonParser import pawtonParser
else:
    from pawtonParser import pawtonParser

# This class defines a complete generic visitor for a parse tree produced by pawtonParser.

class pawtonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pawtonParser#prog.
    def visitProg(self, ctx:pawtonParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#write.
    def visitWrite(self, ctx:pawtonParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#assign.
    def visitAssign(self, ctx:pawtonParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#read.
    def visitRead(self, ctx:pawtonParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#exprStat.
    def visitExprStat(self, ctx:pawtonParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#array.
    def visitArray(self, ctx:pawtonParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#MulDiv.
    def visitMulDiv(self, ctx:pawtonParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#AddSub.
    def visitAddSub(self, ctx:pawtonParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#valExpr.
    def visitValExpr(self, ctx:pawtonParser.ValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#stringExpr.
    def visitStringExpr(self, ctx:pawtonParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#arrayElem.
    def visitArrayElem(self, ctx:pawtonParser.ArrayElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#intExpr.
    def visitIntExpr(self, ctx:pawtonParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#floatExpr.
    def visitFloatExpr(self, ctx:pawtonParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#varExpr.
    def visitVarExpr(self, ctx:pawtonParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#CastToInt.
    def visitCastToInt(self, ctx:pawtonParser.CastToIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#CastToFloat.
    def visitCastToFloat(self, ctx:pawtonParser.CastToFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pawtonParser#ParenExpr.
    def visitParenExpr(self, ctx:pawtonParser.ParenExprContext):
        return self.visitChildren(ctx)



del pawtonParser