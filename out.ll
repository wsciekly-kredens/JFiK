; ModuleID = "main"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = add i32 5, 3
  %"a" = alloca i32
  store i32 %".2", i32* %"a"
  %"a.1" = load i32, i32* %"a"
  %".4" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %"a.1")
  %".6" = sitofp i32 3 to double
  %".7" = fmul double 0x4014666666666666, %".6"
  %".8" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", double %".7")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt_int" = constant [4 x i8] c"%d\0a\00"
@"fmt_float" = constant [4 x i8] c"%f\0a\00"
