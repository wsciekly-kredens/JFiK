from pawtonVisitor import pawtonVisitor
from pawtonParser import pawtonParser
from llvmlite import ir


class LLVMVisitor(pawtonVisitor):
    def __init__(self):
        self.module = ir.Module(name="main")
        func_type = ir.FunctionType(ir.VoidType(), [])
        self.function = ir.Function(self.module, func_type, name="main")
        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        self.variables = {}
        self.string_counter = 0

        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        self._fmt_int = self._create_global_fmt_str("%d\n\0", "fmt_int")
        self._fmt_float = self._create_global_fmt_str("%f\n\0", "fmt_float")
        self._fmt_string = self._create_global_fmt_str("%s\n\0", "fmt_string")

        scanf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.scanf = ir.Function(self.module, scanf_ty, name="scanf")

        self._fmt_scanf_int = self._create_global_fmt_str("%d\0", "fmt_scanf_int")
        self._fmt_scanf_float = self._create_global_fmt_str("%lf\0", "fmt_scanf_float")

        self.functions = {}
        self.function_types = {}
        self.function_definitions = {}

        self.global_variables = {}
        self.local_variables_stack = []

    def _create_global_fmt_str(self, text, name):
        arr_type = ir.ArrayType(ir.IntType(8), len(text))
        global_var = ir.GlobalVariable(self.module, arr_type, name=name)
        global_var.global_constant = True
        global_var.initializer = ir.Constant(arr_type, bytearray(text.encode("utf8")))
        return global_var

    def _generate_function_body(self, function, func_ctx, param_names, param_types):
        saved_builder = self.builder
        saved_variables = self.variables.copy()

        entry_block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)

        function_scope = {}
        self.local_variables_stack.append(function_scope)
        self.variables = function_scope

        for i, arg in enumerate(function.args):
            arg_llvm_type = param_types[i]
            arg_name = param_names[i]
            arg.name = arg_name

            ptr = self.builder.alloca(arg_llvm_type, name=arg_name)
            self.builder.store(arg, ptr)
            self.variables[arg_name] = ptr

        self.visit(func_ctx.block())

        if not self.builder.block.is_terminated:
            self.builder.ret_void()

        self.builder = saved_builder
        self.variables = saved_variables
        self.local_variables_stack.pop()
        self.variables = (
            self.local_variables_stack[-1] if self.local_variables_stack else {}
        )

    def visitProg(self, ctx):
        self._visitStatements(ctx)
        self.builder.ret_void()
        return self.module

    def _visitStatements(self, prog_ctx):
        for stat in prog_ctx.stat():
            self.visit(stat)

    def visitSimpleAssign(self, ctx: pawtonParser.SimpleAssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        if var_name in self.variables:
            ptr = self.variables[var_name]
            if ptr.type.pointee != value.type:
                if value.type != ptr.type.pointee:
                    if isinstance(value.type, ir.DoubleType) and isinstance(
                        ptr.type.pointee, ir.IntType
                    ):
                        value = self.builder.fptosi(value, ptr.type.pointee)
                    elif isinstance(value.type, ir.IntType) and isinstance(
                        ptr.type.pointee, ir.DoubleType
                    ):
                        value = self.builder.sitofp(value, ptr.type.pointee)
                    elif value.type != ptr.type.pointee:
                        raise Exception(
                            f"Błąd typu przy przypisaniu do istniejącej zmiennej '{var_name}': oczekiwano {ptr.type.pointee}, otrzymano {value.type}"
                        )

            self.builder.store(value, ptr)
        else:
            ptr = self.builder.alloca(value.type, name=var_name)
            self.builder.store(value, ptr)
            self.variables[var_name] = ptr

    def visitAssign(self, ctx: pawtonParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        def convert_if_needed(target_type, val):
            if val.type == target_type:
                return val
            if isinstance(val.type, ir.IntType) and isinstance(
                target_type, ir.DoubleType
            ):
                return self.builder.sitofp(val, ir.DoubleType())
            if isinstance(val.type, ir.DoubleType) and isinstance(
                target_type, ir.IntType
            ):
                return self.builder.fptosi(val, ir.IntType(32))
            raise Exception(
                f"Błąd typu przy przypisaniu do '{var_name}': oczekiwano {target_type}, "
                f"otrzymano {val.type}"
            )

        if self.local_variables_stack:
            if var_name in self.variables:
                ptr = self.variables[var_name]
                value = convert_if_needed(ptr.type.pointee, value)
                self.builder.store(value, ptr)
            else:
                ptr = self.builder.alloca(value.type, name=var_name)
                self.builder.store(value, ptr)
                self.variables[var_name] = ptr
        else:
            if var_name in self.global_variables:
                gvar = self.global_variables[var_name]
                value = convert_if_needed(gvar.type.pointee, value)
                self.builder.store(value, gvar)
            else:
                gvar = ir.GlobalVariable(self.module, value.type, name=var_name)
                gvar.linkage = "common"
                gvar.align = 4
                zero = ir.Constant(value.type, None)
                gvar.initializer = zero
                self.builder.store(value, gvar)
                self.global_variables[var_name] = gvar

    def visitWrite(self, ctx):
        try:
            val = self.visit(ctx.expr())
        except Exception as e:
            print(f"Błąd: {e}")
            exit()
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

    def visitRead(self, ctx):
        var_name = ctx.ID().getText()

        ptr = self.variables.get(var_name)
        if ptr is None:
            ptr = self.builder.alloca(ir.IntType(32), name=var_name)
            self.variables[var_name] = ptr

        var_type = ptr.type.pointee

        if var_type == ir.IntType(32):
            fmt_ptr = self.builder.bitcast(
                self._fmt_scanf_int, ir.IntType(8).as_pointer()
            )
        elif var_type == ir.DoubleType():
            fmt_ptr = self.builder.bitcast(
                self._fmt_scanf_float, ir.IntType(8).as_pointer()
            )
        else:
            raise Exception(f"Nieobsługiwany typ zmiennej przy 'listen': {var_type}")

        self.builder.call(self.scanf, [fmt_ptr, ptr])

    def visitVarExpr(self, ctx):
        var_name = ctx.ID().getText()

        ptr = self.variables.get(var_name)
        if ptr is not None:
            return self.builder.load(ptr, var_name)

        global_ptr = self.global_variables.get(var_name)
        if global_ptr is not None:
            return self.builder.load(global_ptr, var_name)

        raise Exception(
            f"Zmienna '{var_name}' nie została zadeklarowana ani przypisana."
        )

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

    def visitCompare(self, ctx):
        left = self.visit(ctx.value())
        right = self.visit(ctx.expr())
        op = ctx.getChild(1).getText()

        if left.type != right.type:
            if left.type == ir.IntType(32) and right.type == ir.DoubleType():
                left = self.builder.sitofp(left, ir.DoubleType())
            elif left.type == ir.DoubleType() and right.type == ir.IntType(32):
                right = self.builder.sitofp(right, ir.DoubleType())
            else:
                raise Exception(f"Nie można porównać typów {left.type} i {right.type}")

        if left.type == ir.IntType(32):
            mapping = {
                "<": lambda: self.builder.icmp_signed("<", left, right),
                "<=": lambda: self.builder.icmp_signed("<=", left, right),
                ">": lambda: self.builder.icmp_signed(">", left, right),
                ">=": lambda: self.builder.icmp_signed(">=", left, right),
                "==": lambda: self.builder.icmp_signed("==", left, right),
                "!=": lambda: self.builder.icmp_signed("!=", left, right),
            }
            if op not in mapping:
                raise Exception(f"Nieobsługiwany operator porównania: {op}")
            return mapping[op]()

        if left.type == ir.DoubleType():
            mapping = {
                "<": lambda: self.builder.fcmp_ordered("<", left, right),
                "<=": lambda: self.builder.fcmp_ordered("<=", left, right),
                ">": lambda: self.builder.fcmp_ordered(">", left, right),
                ">=": lambda: self.builder.fcmp_ordered(">=", left, right),
                "==": lambda: self.builder.fcmp_ordered("==", left, right),
                "!=": lambda: self.builder.fcmp_ordered("!=", left, right),
            }
            if op not in mapping:
                raise Exception(f"Nieobsługiwany operator porównania: {op}")
            return mapping[op]()

        raise Exception(f"Nieobsługiwany typ do porównań: {left.type}")

    def visitAddSub(self, ctx):
        left = self.visit(ctx.value())
        right = self.visit(ctx.expr())

        if left.type != right.type:
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
        left = self.visit(ctx.value())
        right = self.visit(ctx.expr())

        if left.type != right.type:
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
        val = self.visit(ctx.value())
        return self.builder.fptosi(val, ir.IntType(32))

    def visitCastToFloat(self, ctx):
        val = self.visit(ctx.value())
        return self.builder.sitofp(val, ir.DoubleType())

    def visitArray(self, ctx):
        array_name = ctx.ID().getText()
        exprs = ctx.expr()

        if not exprs:
            raise Exception(f"Tablica '{array_name}' nie zawiera żadnych elementów.")

        elements = []
        element_type = None

        for i, expr in enumerate(exprs):
            val = self.visit(expr)

            if isinstance(val.type, ir.PointerType) and val.type.pointee == ir.IntType(
                8
            ):
                text = expr.getText().strip('"') + "\0"
                name = f"str_{self.string_counter}"
                self.string_counter += 1
                arr_type = ir.ArrayType(ir.IntType(8), len(text))
                global_str = ir.GlobalVariable(self.module, arr_type, name=name)
                global_str.global_constant = True
                global_str.initializer = ir.Constant(
                    arr_type, bytearray(text.encode("utf8"))
                )

                gep = global_str.gep(
                    [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0)]
                )
                val = gep

            if element_type is None:
                element_type = val.type
            else:
                if val.type != element_type:
                    raise Exception(
                        f"Typ elementu nr {i+1} w tablicy '{array_name}' ({val.type}) "
                        f"nie pasuje do pierwszego typu ({element_type})."
                    )

            elements.append(val)

        allowed_types = (
            ir.IntType(32),
            ir.DoubleType(),
            ir.IntType(8).as_pointer(),
        )
        if not isinstance(element_type, type) and element_type not in allowed_types:
            raise Exception(
                f"Typ elementów tablicy '{array_name}' ({element_type}) nie jest obsługiwany."
            )

        array_type = ir.ArrayType(element_type, len(elements))
        initializer = ir.Constant(array_type, elements)
        global_array = ir.GlobalVariable(self.module, array_type, name=array_name)
        global_array.global_constant = True
        global_array.initializer = initializer

        if self.local_variables_stack:
            self.variables[array_name] = global_array
        else:
            self.global_variables[array_name] = global_array

        return global_array

    def visitArrayElem(self, ctx):
        array_name = ctx.ID().getText()
        index_raw = ctx.INT().getText()

        try:
            index = int(index_raw)
        except ValueError:
            raise Exception(
                f"Indeks tablicy '{array_name}' nie jest liczbą całkowitą: '{index_raw}'"
            )

        array_ptr = self.variables.get(array_name)
        if array_ptr is None:
            array_ptr = self.global_variables.get(array_name)
        if array_ptr is None:
            raise Exception(f"Nie odnaleziono tablicy '{array_name}'")

        if not isinstance(array_ptr.type.pointee, ir.types.ArrayType):
            raise Exception(
                f"'{array_name}' nie jest tablicą (ma typ {array_ptr.type})"
            )

        array_type = array_ptr.type.pointee
        array_length = array_type.count

        if index < 0 or index >= array_length:
            raise Exception(
                f"Indeks {index} poza zakresem tablicy '{array_name}' (rozmiar: {array_length})"
            )

        array_bitcast = self.builder.bitcast(
            array_ptr, array_ptr.type.pointee.as_pointer()
        )
        element_ptr = self.builder.gep(
            array_bitcast,
            [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), index)],
        )
        return self.builder.load(element_ptr)

    def visitFuncDef(self, ctx):
        func_name = ctx.ID(0).getText()
        if func_name in self.function_definitions:
            print(f"Ostrzeżenie: Redefinicja funkcji '{func_name}'.")
        self.function_definitions[func_name] = ctx

    def visitFuncCall(self, ctx):
        func_name = ctx.ID().getText()

        args = []
        arg_types = []
        if ctx.expr():
            for expr in ctx.expr():
                val = self.visit(expr)
                if not isinstance(
                    val.type, (ir.IntType, ir.DoubleType, ir.PointerType)
                ):
                    if isinstance(val.type, ir.PointerType):
                        if (
                            not isinstance(val.type.pointee, ir.IntType)
                            or val.type.pointee.width != 8
                        ):
                            raise Exception(
                                f"Niedozwolony typ wskaźnika '{val.type}' jako argument funkcji '{func_name}'. Dozwolony tylko i8* (string)."
                            )
                    else:
                        raise Exception(
                            f"Niedozwolony typ argumentu '{val.type}' dla funkcji '{func_name}'. Dozwolone int, float, string."
                        )

                args.append(val)
                arg_types.append(val.type)

        llvm_func = self.functions.get(func_name)

        if llvm_func:
            expected_types = self.function_types[func_name].args
            if len(args) != len(expected_types):
                raise Exception(
                    f"Zła liczba argumentów dla funkcji '{func_name}'. Oczekiwano {len(expected_types)}, podano {len(args)}."
                )

            for i, (arg, exp_type) in enumerate(zip(args, expected_types)):
                if arg.type != exp_type:
                    raise Exception(
                        f"Niezgodność typu argumentu {i + 1} w wywołaniu funkcji '{func_name}'. Oczekiwano {exp_type}, podano {arg.type}."
                    )
        else:
            func_def_ctx = self.function_definitions.get(func_name)
            if func_def_ctx is None:
                raise Exception(
                    f"Funkcja '{func_name}' nie została zdefiniowana przed wywołaniem."
                )

            param_names = [id.getText() for id in func_def_ctx.ID()[1:]]
            if len(param_names) != len(arg_types):
                raise Exception(
                    f"Definicja funkcji '{func_name}' oczekuje {len(param_names)} parametrów, a wywołanie dostarczyło {len(arg_types)}."
                )

            func_type = ir.FunctionType(ir.VoidType(), arg_types)
            llvm_func = ir.Function(self.module, func_type, name=func_name)

            self.functions[func_name] = llvm_func
            self.function_types[func_name] = func_type

            self._generate_function_body(
                llvm_func, func_def_ctx, param_names, arg_types
            )

        return self.builder.call(llvm_func, args)

    def visitIfStat(self, ctx):
        cond_value = self.visit(ctx.expr())
        if cond_value.type != ir.IntType(1):
            cond_value = self.builder.icmp_signed(
                "!=", cond_value, ir.Constant(cond_value.type, 0)
            )

        then_block = self.function.append_basic_block(name="if.then")
        else_block = (
            self.function.append_basic_block(name="if.else") if ctx.ELSE() else None
        )
        end_block = self.function.append_basic_block(name="if.end")

        self.builder.cbranch(cond_value, then_block, else_block or end_block)

        self.builder.position_at_end(then_block)
        self._visitStatements(ctx.prog(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(end_block)

        if else_block:
            self.builder.position_at_end(else_block)
            self._visitStatements(ctx.prog(1))
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)

        self.builder.position_at_end(end_block)

    def visitForstat(self, ctx: pawtonParser.ForstatContext):
        init = ctx.simpleAssign(0) or ctx.assign(0)
        if init:
            self.visit(init)

        cond_block = self.function.append_basic_block("for.cond")
        body_block = self.function.append_basic_block("for.body")
        inc_block = self.function.append_basic_block("for.inc")
        end_block = self.function.append_basic_block("for.end")

        self.builder.branch(cond_block)

        self.builder.position_at_end(cond_block)
        cond_value = self.visit(ctx.expr())
        if cond_value.type != ir.IntType(1):
            cond_value = self.builder.icmp_signed(
                "!=", cond_value, ir.Constant(cond_value.type, 0)
            )
        self.builder.cbranch(cond_value, body_block, end_block)

        self.builder.position_at_end(body_block)
        self._visitStatements(ctx.prog())
        if not self.builder.block.is_terminated:
            self.builder.branch(inc_block)

        self.builder.position_at_end(inc_block)
        inc = ctx.simpleAssign(1) or ctx.assign(1)
        if inc:
            self.visit(inc)
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder.position_at_end(end_block)
