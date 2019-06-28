import ply.yacc as yacc
import ply.lex as lex
from lexer import tokens

def p_type(p):
    'type_def : TYPE'
    p[0] = p[1]

def p_lbracket(p):
    'expression : LBRACKET'
    p[0] = p[1]

def p_rbracket(p):
    'expression : RBRACKET'
    p[0] = p[1]

def p_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_int(p):
    'expression : INT'
    p[0] = p[1]

def p_float(p):
    'expression : FLOAT64'
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
