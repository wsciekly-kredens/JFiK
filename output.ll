; ModuleID = "main"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = sitofp i32 3 to double
  %".3" = fadd double 0x4014666666666666, %".2"
  %"a" = alloca double
  store double %".3", double* %"a"
  %"a.1" = load double, double* %"a"
  %".5" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", double %"a.1")
  %".7" = sitofp i32 3 to double
  %".8" = fmul double 0x4014666666666666, %".7"
  %".9" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", double %".8")
  %".11" = bitcast [16 x i8]* @"str_0" to i8*
  %".12" = bitcast [5 x i8]* @"str_2" to i8*
  %".13" = bitcast [9 x i8]* @"str_4" to i8*
  %".14" = bitcast [6 x i8]* @"str_6" to i8*
  %"b" = alloca i8*
  store i8* %".14", i8** %"b"
  %"b.1" = load i8*, i8** %"b"
  %".16" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".17" = call i32 (i8*, ...) @"printf"(i8* %".16", i8* %"b.1")
  %".18" = getelementptr [3 x i8*], [3 x i8*]* @"Dognames", i32 0, i32 2
  %".19" = load i8*, i8** %".18"
  %".20" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".21" = call i32 (i8*, ...) @"printf"(i8* %".20", i8* %".19")
  %".22" = getelementptr [2 x i32], [2 x i32]* @"Age", i32 0, i32 1
  %".23" = load i32, i32* %".22"
  %".24" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".25" = call i32 (i8*, ...) @"printf"(i8* %".24", i32 %".23")
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt_int" = constant [4 x i8] c"%d\0a\00"
@"fmt_float" = constant [4 x i8] c"%f\0a\00"
@"fmt_string" = constant [4 x i8] c"%s\0a\00"
declare i32 @"scanf"(i8* %".1", ...)

@"fmt_scanf_int" = constant [3 x i8] c"%d\00"
@"fmt_scanf_float" = constant [4 x i8] c"%lf\00"
@"str_0" = constant [16 x i8] c"Thommas Schelby\00"
@"str_1" = constant [16 x i8] c"Thommas Schelby\00"
@"str_2" = constant [5 x i8] c"Pies\00"
@"str_3" = constant [5 x i8] c"Pies\00"
@"str_4" = constant [9 x i8] c"Dumpling\00"
@"str_5" = constant [9 x i8] c"Dumpling\00"
@"Dognames" = constant [3 x i8*] [i8* getelementptr ([16 x i8], [16 x i8]* @"str_1", i32 0, i32 0), i8* getelementptr ([5 x i8], [5 x i8]* @"str_3", i32 0, i32 0), i8* getelementptr ([9 x i8], [9 x i8]* @"str_5", i32 0, i32 0)]
@"str_6" = constant [6 x i8] c"Tomek\00"
@"Age" = constant [2 x i32] [i32 1, i32 20]