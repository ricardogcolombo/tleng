import ply.yacc as yacc
import ply.lex as lex
import random
from lexer import tokens

def p_struct_recursive(p):
    'struct : TYPE type_name STRUCT struct_definition struct '
    p[0] = '{\n' + p[4] + '\n}' + p[5]

def p_struct_final(p):
    'struct : TYPE type_name STRUCT struct_definition '
    p[0] = '{\n' + p[4] + '\n}'

def p_attributes(p):
    'struct_definition : LBRACKET attributes_definition RBRACKET'
    p[0] = p[2]

def p_type_name(p):
    'type_name : ATT_TYPE_NAME'
    p[0] = p[1] + '\n'

def p_attributes_definition_recursive(p):
    'attributes_definition : attribute type attributes_definition'
    p[0] = '\"' + p[1] + '\": ' + p[2] + '\n' + p[3]

def p_attributes_definition_final(p):
    'attributes_definition : attribute type'
    p[0] = '\"' + p[1] + '\": ' + p[2]

def p_attribute(p):
    'attribute : ATT_TYPE_NAME'
    p[0] = p[1]

def p_type_string(p):
    'type : STRING'
    p[0] = p[1]

def p_type_int(p):
    'type : INT'
    p[0] = str(random.randint(0,100))

def p_type_float(p):
    'type : FLOAT64'
    p[0] = str(random.uniform(0, 100))

def p_type_bool(p):
    'type : BOOL'
    p[0] = str(bool(random.getrandbits(1)))

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
