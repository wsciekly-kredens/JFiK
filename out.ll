; ModuleID = "main"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = sitofp i32 1 to double
  %".3" = fadd double 0x4014666666666666, %".2"
  %"a" = alloca double
  store double %".3", double* %"a"
  %"a.1" = load double, double* %"a"
  %".5" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", double %"a.1")
  %"g" = alloca i32
  %".7" = bitcast [3 x i8]* @"fmt_scanf_int" to i8*
  %".8" = call i32 (i8*, ...) @"scanf"(i8* %".7", i32* %"g")
  %"g.1" = load i32, i32* %"g"
  %".9" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %"g.1")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt_int" = constant [4 x i8] c"%d\0a\00"
@"fmt_float" = constant [4 x i8] c"%f\0a\00"
declare i32 @"scanf"(i8* %".1", ...)

@"fmt_scanf_int" = constant [3 x i8] c"%d\00"
@"fmt_scanf_float" = constant [4 x i8] c"%lf\00"
