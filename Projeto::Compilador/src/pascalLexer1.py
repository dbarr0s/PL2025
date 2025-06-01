import ply.lex as lex

tokens = (
	# Assignment
	'IDENTIFIER', 'ASSIGNMENT', 'SEMICOLON', 'COLON', 'COMMA',
	# Main
    'COMMENT', 'PROGRAM', 'DOT',
	# Blocks
	'VAR', 'BEGIN', 'END',
	# Control Flow
	'IF', 'THEN', 'ELSE', 'FOR', 'WHILE', 'REPEAT', 'UNTIL', 'DO', 'TO', 'DOWNTO',
	# Logic
	'AND', 'OR', 'NOT',
	# Operations
	'PLUS', 'MINUS', 'TIMES', 'DIVISION', 'DIV', 'MOD', 'RANGE',
	# Comparations
	'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE',
	# Functions
	'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'PROCEDURE', 'FUNCTION', 'ARRAY', 'OF', 'WRITELN', 'READLN', 'LENGTH',
	# Types Names
	'NREAL', 'NINTEGER', 'NSTRING', 'NCHAR', 'NBOOLEAN',
	# Types
	'REAL', 'INTEGER', 'STRING', 'CHAR', 'BOOLEAN'
)

reserved_keywords = {
	'program': 'PROGRAM', 'var': 'VAR', 'begin': 'BEGIN', 'end': 'END',
	
	'if': 'IF', 'then': 'THEN', 'else': 'ELSE',
 
	'for': 'FOR', 'while': 'WHILE', 'repeat': 'REPEAT', 'do': 'DO', 'to': 'TO', 'downto': 'DOWNTO', 'until': 'UNTIL',
	
	'and': 'AND', 'or': 'OR', 'not': 'NOT',
	
	'div': 'DIV', 'mod': 'MOD',
	
	'procedure': 'PROCEDURE', 'function': 'FUNCTION', 
 
	'array': 'ARRAY', 'of': 'OF', 'writeln': 'WRITELN', 'readln': 'READLN', 'length': 'LENGTH',
	
	'real': 'NREAL', 'integer': 'NINTEGER', 'string': 'NSTRING', 'char': 'NCHAR', 'boolean': 'NBOOLEAN'
}

t_DOT = r"\."
t_ASSIGNMENT = r":="
t_SEMICOLON = r";"
t_COLON = r":"
t_COMMA	= r","

t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES	= r"\*"
t_DIVISION = r"\/"
t_RANGE = r"\.\."

t_EQ = r"\="
t_NEQ = r"\<\>"
t_LT = r"\<"
t_GT = r"\>"
t_LTE = r"\<\="
t_GTE = r"\>\="

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"

def t_BOOLEAN(t):
    r"true|false"
    return t
    
def t_REAL(t):
    r"(\-)?\d+\.\d+"
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r"(\-)?\d+"
    t.value = int(t.value)
    return t

def t_STRING(t):
    r"'([^']*)'"
    t.value = t.value[1:-1]
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z]([a-zA-Z0-9])*"
    if t.value.lower() in reserved_keywords:
        t.type = reserved_keywords[t.value.lower()]
    return t

def t_CHAR(t):
    r"'\w'"
    t.value = t.value[1]  
    return t

def t_COMMENT(t):
    r'\{.*?\}|\(\*.*?\*\)|\/\/.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter desconhecido '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()