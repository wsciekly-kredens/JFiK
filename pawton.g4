grammar pawton;
simpleAssign: ID '=' expr ;

prog: ( stat? NEWLINE )*;

stat:   WRITE expr        #write
    |   ID '=' expr       #assign
    |   READ ID           #read
    |   expr              #exprStat
    |   ARRAY ID '[' (INT)? ']' ('=' '{' expr (',' expr)* '}' )?  #array
    |   FUNC ID LP (ID (',' ID)*)? RP block   #funcDef
    |   ID LP (expr (',' expr)*)? RP          #funcCall
    |   IF LP expr RP LBRACE prog RBRACE (ELSE LBRACE prog RBRACE)?  #ifStat
    |   FOR LP simpleAssign? SEMICOL expr? SEMICOL simpleAssign? RP LBRACE prog RBRACE  #forstat
    ;

expr:   value (MULT | DIVIDE) expr    #MulDiv
    |   value (ADD | SUBSTRACT) expr  #AddSub
    |   value (LT | GT | LE | GE | EQ | NEQ) expr  #Compare
    |   value                        #valExpr
    |   STRING                       #stringExpr
    |   ID ('[' INT ']')?            #arrayElem
    ;

value:  INT                          #intExpr
    |   FLOAT                        #floatExpr
    |   ID                           #varExpr
    |   TOINT value                   #CastToInt
    |   TOFLOAT value                 #CastToFloat
    |   LP expr RP                   #ParenExpr
    ;

block: '{' (stat? NEWLINE)* '}';


WRITE:  'bark';
READ:   'listen';
ARRAY:  'pack';
FUNC: 'command';
IF: 'if';
ELSE: 'else';
FOR: 'pivot';

LP: '(';
RP: ')';
LBRACE: '{';
RBRACE: '}';
SEMICOL: ';';
ADD: '+';
SUBSTRACT: '-';
MULT: '*';
DIVIDE: '/';
LT: '<';
GT: '>';
EQ: '==';
NEQ: '!=';
LE: '<=';
GE: '>=';

ID:   ('a'..'z'|'A'..'Z')+;
INT:  '0'..'9'+;
FLOAT: '0'..'9'+ '.' '0'..'9'+;
STRING :  '"' ( ~('\\'|'"') )* '"';

TOINT: '(int)';
TOFLOAT: '(float)';

NEWLINE: '\r'? '\n';
WS:   (' '|'\t')+ -> skip;