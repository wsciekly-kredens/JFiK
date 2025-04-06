grammar lang;

prog: stat? (NEWLINE stat)* NEWLINE?;

stat:   WRITE expr        #write
    |   ID '=' expr       #assign
    |   READ ID           #read
    |   expr              #exprStat
    |   ARRAY ID '[' (INT)? ']' ('=' '{' expr (',' expr)* '}' )?  #array
    ;

expr:   expr (MULT | DIVIDE) expr    #MulDiv
    |   expr (ADD | SUBSTRACT) expr  #AddSub
    |   '(' expr ')'                 #ParenExpr
    |   TOINT expr                   #CastToInt
    |   TOFLOAT expr                 #CastToFloat
    |   INT                          #intExpr
    |   FLOAT                        #floatExpr
    |   ID                           #varExpr
    |   STRING                       #stringExpr
    |   ID ('[' INT ']')?            #arrayElem
    ;

num: INT
   | FLOAT
   | TOINT
   | TOFLOAT
   ;

sum: num
    | num ADD num
    | num ADD artoperation
    ;

diff: num
    | num SUBSTRACT num
    | num SUBSTRACT artoperation
    ;

prod: num
    | num MULT num
    | num MULT artoperation
    ;

quotient: num
    | num DIVIDE num
    | num DIVIDE artoperation
    ;


artoperation: sum | diff | prod | quotient;

WRITE:  'bark';
READ:   'listen';
ARRAY:  'pack';

ID:   ('a'..'z'|'A'..'Z')+;
INT:  '0'..'9'+;
FLOAT: '0'..'9'+ '.' '0'..'9'+;
STRING :  '"' ( ~('\\'|'"') )* '"';

TOINT: '(int)';
TOFLOAT: '(float)';

ADD: '+';
SUBSTRACT: '-';
MULT: '*';
DIVIDE: '/';

NEWLINE: '\r'? '\n';
WS:   (' '|'\t')+ -> skip;