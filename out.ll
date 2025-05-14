; ModuleID = "main"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = add i32 5, 3
  store i32 %".2", i32* @"a"
  %"a" = load i32, i32* @"a"
  %".4" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %"a")
  %".6" = sitofp i32 3 to double
  %".7" = fdiv double 0x4014666666666666, %".6"
  %".8" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", double %".7")
  %".10" = bitcast [16 x i8]* @"str_0" to i8*
  %".11" = bitcast [5 x i8]* @"str_2" to i8*
  %".12" = bitcast [9 x i8]* @"str_4" to i8*
  %".13" = bitcast [6 x i8]* @"str_6" to i8*
  store i8* %".13", i8** @"b"
  %"b" = load i8*, i8** @"b"
  %".15" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15", i8* %"b")
  %".17" = bitcast [5 x i8]* @"str_7" to i8*
  store i8* %".17", i8** @"b"
  %"b.1" = load i8*, i8** @"b"
  %".19" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i8* %"b.1")
  %".21" = getelementptr [3 x i8*], [3 x i8*]* @"Dognames", i32 0, i32 2
  %".22" = load i8*, i8** %".21"
  %".23" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i8* %".22")
  %".25" = getelementptr [2 x i32], [2 x i32]* @"Age", i32 0, i32 1
  %".26" = load i32, i32* %".25"
  %".27" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %".26")
  store i32 1, i32* @"z"
  call void @"greet"(double 0x4000cccccccccccd, i32 4)
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.1" = load i32, i32* %"i"
  %".33" = icmp slt i32 %"i.1", 3
  br i1 %".33", label %"for.body", label %"for.end"
for.body:
  %"b.2" = load i8*, i8** @"b"
  %".35" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", i8* %"b.2")
  br label %"for.inc"
for.inc:
  %"i.2" = load i32, i32* %"i"
  %".38" = add i32 %"i.2", 1
  store i32 %".38", i32* %"i"
  br label %"for.cond"
for.end:
  %"a.1" = load i32, i32* @"a"
  %".41" = icmp slt i32 %"a.1", 3
  br i1 %".41", label %"if.then", label %"if.else"
if.then:
  %".43" = getelementptr [3 x i8*], [3 x i8*]* @"Dognames", i32 0, i32 2
  %".44" = load i8*, i8** %".43"
  %".45" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", i8* %".44")
  br label %"if.end"
if.else:
  %".48" = getelementptr [3 x i8*], [3 x i8*]* @"Dognames", i32 0, i32 0
  %".49" = load i8*, i8** %".48"
  %".50" = bitcast [4 x i8]* @"fmt_string" to i8*
  %".51" = call i32 (i8*, ...) @"printf"(i8* %".50", i8* %".49")
  br label %"if.end"
if.end:
  ret void
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt_int" = constant [4 x i8] c"%d\0a\00"
@"fmt_float" = constant [4 x i8] c"%f\0a\00"
@"fmt_string" = constant [4 x i8] c"%s\0a\00"
declare i32 @"scanf"(i8* %".1", ...)

@"fmt_scanf_int" = constant [3 x i8] c"%d\00"
@"fmt_scanf_float" = constant [4 x i8] c"%lf\00"
@"a" = common global i32 0, align 4
@"str_0" = constant [16 x i8] c"Thommas Schelby\00"
@"str_1" = constant [16 x i8] c"Thommas Schelby\00"
@"str_2" = constant [5 x i8] c"Pies\00"
@"str_3" = constant [5 x i8] c"Pies\00"
@"str_4" = constant [9 x i8] c"Dumpling\00"
@"str_5" = constant [9 x i8] c"Dumpling\00"
@"Dognames" = constant [3 x i8*] [i8* getelementptr ([16 x i8], [16 x i8]* @"str_1", i32 0, i32 0), i8* getelementptr ([5 x i8], [5 x i8]* @"str_3", i32 0, i32 0), i8* getelementptr ([9 x i8], [9 x i8]* @"str_5", i32 0, i32 0)]
@"str_6" = constant [6 x i8] c"Tomek\00"
@"b" = common global i8* null, align 4
@"str_7" = constant [5 x i8] c"Asia\00"
@"Age" = constant [2 x i32] [i32 1, i32 20]
@"z" = common global i32 0, align 4
define void @"greet"(double %"c", i32 %"d")
{
entry:
  %"c.1" = alloca double
  store double %"c", double* %"c.1"
  %"d.1" = alloca i32
  store i32 %"d", i32* %"d.1"
  %"z" = load i32, i32* @"z"
  %".6" = bitcast [4 x i8]* @"fmt_int" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %"z")
  %"c.2" = load double, double* %"c.1"
  %"d.2" = load i32, i32* %"d.1"
  %".8" = sitofp i32 %"d.2" to double
  %".9" = fadd double %"c.2", %".8"
  %".10" = bitcast [4 x i8]* @"fmt_float" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", double %".9")
  ret void
}
