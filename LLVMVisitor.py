from langVisitor import langVisitor
from llvmlite import ir

class LLVMVisitor(langVisitor):
    def __init__(self):
        self.module = ir.Module(name="main")
        func_type = ir.FunctionType(ir.VoidType(), [])
        self.function = ir.Function(self.module, func_type, name="main")
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.variables = {}

        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        self._fmt_int = self._create_global_fmt_str("%d\n\0", "fmt_int")
        self._fmt_float = self._create_global_fmt_str("%f\n\0", "fmt_float")

        scanf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_ty, name="scanf")

        self._fmt_scanf_int = self._create_global_fmt_str("%d\0", "fmt_scanf_int")
        self._fmt_scanf_float = self._create_global_fmt_str("%lf\0", "fmt_scanf_float")


    def _create_global_fmt_str(self, text, name):
        arr_type = ir.ArrayType(ir.IntType(8), len(text))
        global_var = ir.GlobalVariable(self.module, arr_type, name=name)
        global_var.global_constant = True
        global_var.initializer = ir.Constant(arr_type, bytearray(text.encode("utf8")))
        return global_var

    def visitProg(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)
        self.builder.ret_void()
        return self.module

    def visitAssign(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        ptr = self.builder.alloca(value.type, name=var_name)
        self.builder.store(value, ptr)
        self.variables[var_name] = ptr

    def visitWrite(self, ctx):
        val = self.visit(ctx.expr())
        if val.type == ir.IntType(32):
            fmt_ptr = self.builder.bitcast(self._fmt_int, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, val])
        elif val.type == ir.DoubleType():
            fmt_ptr = self.builder.bitcast(self._fmt_float, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, val])
        else:
            raise Exception(f"Nieobsługiwany typ dla 'bark': {val.type}")

    def visitRead(self, ctx):
        var_name = ctx.ID().getText()

        # Domyślnie alokuj int, jeśli zmienna nie istnieje
        ptr = self.variables.get(var_name)
        if ptr is None:
            ptr = self.builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = ptr

        var_type = ptr.type.pointee

        if var_type == ir.IntType(32):
            fmt_ptr = self.builder.bitcast(self._fmt_scanf_int, ir.IntType(8).as_pointer())
        elif var_type == ir.DoubleType():
            fmt_ptr = self.builder.bitcast(self._fmt_scanf_float, ir.IntType(8).as_pointer())
        else:
            raise Exception(f"Nieobsługiwany typ zmiennej przy 'listen': {var_type}")

        self.builder.call(self.scanf, [fmt_ptr, ptr])

    def visitVarExpr(self, ctx):
        var_name = ctx.ID().getText()
        ptr = self.variables.get(var_name)
        return self.builder.load(ptr, var_name)

    def visitIntExpr(self, ctx):
        return ir.Constant(ir.IntType(32), int(ctx.INT().getText()))

    def visitFloatExpr(self, ctx):
        return ir.Constant(ir.DoubleType(), float(ctx.FLOAT().getText()))

    def visitAddSub(self, ctx):
        left = self.visit(ctx.value())
        right = self.visit(ctx.expr())

        if left.type != right.type:
            if left.type == ir.IntType(32) and right.type == ir.DoubleType():
                left = self.builder.sitofp(left, ir.DoubleType())
            elif left.type == ir.DoubleType() and right.type == ir.IntType(32):
                right = self.builder.sitofp(right, ir.DoubleType())

        if ctx.ADD():
            return self.builder.fadd(left, right) if left.type == ir.DoubleType() else self.builder.add(left, right)
        else:
            return self.builder.fsub(left, right) if left.type == ir.DoubleType() else self.builder.sub(left, right)

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.value())
        right = self.visit(ctx.expr())

        if left.type != right.type:
            if left.type == ir.IntType(32) and right.type == ir.DoubleType():
                left = self.builder.sitofp(left, ir.DoubleType())
            elif left.type == ir.DoubleType() and right.type == ir.IntType(32):
                right = self.builder.sitofp(right, ir.DoubleType())

        if ctx.MULT():
            return self.builder.fmul(left, right) if left.type == ir.DoubleType() else self.builder.mul(left, right)
        else:
            return self.builder.fdiv(left, right) if left.type == ir.DoubleType() else self.builder.sdiv(left, right)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitCastToInt(self, ctx):
        val = self.visit(ctx.value())
        return self.builder.fptosi(val, ir.IntType(32))

    def visitCastToFloat(self, ctx):
        val = self.visit(ctx.value())
        return self.builder.sitofp(val, ir.DoubleType())
