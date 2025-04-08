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
        self.string_counter = 0  # Do unikalnych nazw stringów

        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")
        self._fmt_int = self._create_global_fmt_str("%d\n\0", "fmt_int")
        self._fmt_float = self._create_global_fmt_str("%f\n\0", "fmt_float")
        self._fmt_string = self._create_global_fmt_str("%s\n\0", "fmt_string")

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
        elif val.type == ir.IntType(8).as_pointer():
            fmt_ptr = self.builder.bitcast(self._fmt_string, ir.IntType(8).as_pointer())
            self.builder.call(self.printf, [fmt_ptr, val])
        else:
            raise Exception(f"Nieobsługiwany typ dla 'bark': {val.type}")

    def visitVarExpr(self, ctx):
        var_name = ctx.ID().getText()
        ptr = self.variables.get(var_name)
        return self.builder.load(ptr, var_name)

    def visitIntExpr(self, ctx):
        return ir.Constant(ir.IntType(32), int(ctx.INT().getText()))

    def visitFloatExpr(self, ctx):
        return ir.Constant(ir.DoubleType(), float(ctx.FLOAT().getText()))

    def visitStringExpr(self, ctx):
        text = ctx.STRING().getText().strip('"')
        text += "\0"
        name = f"str_{self.string_counter}"
        self.string_counter += 1
        arr_type = ir.ArrayType(ir.IntType(8), len(text))
        global_var = ir.GlobalVariable(self.module, arr_type, name=name)
        global_var.global_constant = True
        global_var.initializer = ir.Constant(arr_type, bytearray(text.encode("utf8")))
        return self.builder.bitcast(global_var, ir.IntType(8).as_pointer())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # Jeśli left i right mają różne typy, musimy je skonwertować
        if left.type != right.type:
            # Jeśli jeden jest float, a drugi int, konwertujemy oba na float
            if left.type == ir.IntType(32) and right.type == ir.DoubleType():
                left = self.builder.sitofp(left, ir.DoubleType())
            elif left.type == ir.DoubleType() and right.type == ir.IntType(32):
                right = self.builder.sitofp(right, ir.DoubleType())

        if ctx.ADD():
            return (
                self.builder.fadd(left, right)
                if left.type == ir.DoubleType()
                else self.builder.add(left, right)
            )
        else:
            return (
                self.builder.fsub(left, right)
                if left.type == ir.DoubleType()
                else self.builder.sub(left, right)
            )

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # Konwertujemy typy w przypadku różnych typów operandów
        if left.type != right.type:
            # Jeśli jeden jest float, a drugi int, konwertujemy oba na float
            if left.type == ir.IntType(32) and right.type == ir.DoubleType():
                left = self.builder.sitofp(left, ir.DoubleType())
            elif left.type == ir.DoubleType() and right.type == ir.IntType(32):
                right = self.builder.sitofp(right, ir.DoubleType())

        if ctx.MULT():
            return (
                self.builder.fmul(left, right)
                if left.type == ir.DoubleType()
                else self.builder.mul(left, right)
            )
        else:
            return (
                self.builder.fdiv(left, right)
                if left.type == ir.DoubleType()
                else self.builder.sdiv(left, right)
            )

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitCastToInt(self, ctx):
        val = self.visit(ctx.expr())
        return self.builder.fptosi(val, ir.IntType(32))

    def visitCastToFloat(self, ctx):
        val = self.visit(ctx.expr())
        return self.builder.sitofp(val, ir.DoubleType())

    def visitArray(self, ctx):
        array_name = ctx.ID().getText()
        elements = [self.visit(expr) for expr in ctx.expr()]
        array_size = len(elements)
        element_type = elements[0].type

        allowed_types = (ir.IntType(32), ir.DoubleType(), ir.IntType(8).as_pointer())
        if not isinstance(element_type, type) and element_type not in allowed_types:
            raise Exception(f"Nieobsługiwany typ tablicy: {element_type}")


        array_type = ir.ArrayType(element_type, array_size)
        initializer = ir.Constant(array_type, elements)
        global_array = ir.GlobalVariable(self.module, array_type, name=array_name)
        global_array.initializer = initializer
        global_array.global_constant = True
        self.variables[array_name] = global_array
        return global_array

    def visitArrayElem(self, ctx):
        array_name = ctx.ID().getText()
        index = int(ctx.INT().getText())
        array_ptr = self.variables.get(array_name)

        if not array_ptr:
            raise Exception(f"Nie odnaleziono tablicy {array_name}")

        array_bitcast = self.builder.bitcast(array_ptr, array_ptr.type.pointee.as_pointer())
        element_ptr = self.builder.gep(
            array_bitcast,
            [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), index)],
        )
        return self.builder.load(element_ptr)