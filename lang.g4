grammar lang;

prog: ( stat? NEWLINE )*;

stat:   WRITE expr        #write
    |   ID '=' expr       #assign
    |   READ ID           #read
    |   expr              #exprStat
    ;

expr:   value (MULT | DIVIDE) expr    #MulDiv
    |   value (ADD | SUBSTRACT) expr  #AddSub
    |   value                        #valExpr
    ;

value:  INT                          #intExpr
    |   FLOAT                        #floatExpr
    |   ID                           #varExpr
    |   TOINT value                   #CastToInt
    |   TOFLOAT value                 #CastToFloat
    |   LP expr RP                   #ParenExpr
    ;


WRITE:  'bark';
READ:   'listen';

ID:   ('a'..'z'|'A'..'Z')+;
INT:  '0'..'9'+;
FLOAT: '0'..'9'+ '.' '0'..'9'+;

TOINT: '(int)';
TOFLOAT: '(float)';

LP: '(';
RP: ')';
ADD: '+';
SUBSTRACT: '-';
MULT: '*';
DIVIDE: '/';

NEWLINE: '\r'? '\n';
WS:   (' '|'\t')+ -> skip;