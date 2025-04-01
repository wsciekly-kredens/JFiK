grammar lang;

prog: ( stat? NEWLINE )* ;

stat:  WRITE expr         #write
    |   ID '=' expr       #assign
    |   READ ID           #read
    ;

expr:  INT               #intExpr
    |   FLOAT             #floatExpr
    |   ID                #varExpr
    ;

WRITE:  'bark';
READ:   'read';

ID:   ('a'..'z'|'A'..'Z')+;
INT:  '0'..'9'+;
FLOAT: '0'..'9'+ '.' '0'..'9'+;

NEWLINE: '\r'? '\n';
WS:   (' '|'\t')+ -> skip;