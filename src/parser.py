import ply.yacc as yacc
import ply.lex as lex
import random
from constructor import define_type, create_array, register_struct
from lexer import tokens

def p_struct_recursive(p):
    'struct_block : type type_name struct struct_definition struct_block '
    register_struct(p[4], p[2])
    p[0] = '{\n' + p[4] + '\n}'

def p_struct_final(p):
    'struct_block : type type_name struct struct_definition '
    register_struct(p[4], p[2])
    p[0] = '{\n' + p[4] + '\n}'

def p_attributes(p):
    'struct_definition : LBRACKET attributes_definition RBRACKET'
    p[0] = p[2]

def p_type_name(p):
    'type_name : STRING'
    p[0] = p[1]

def p_array_type_name(p):
    'array_type_name : STRING'
    p[0] = create_array(p[1])

def p_array_struct(p):
    'array_struct : array array_type_name'
    p[0] = p[2]

def p_attributes_definition_recursive(p):
    'attributes_definition : attribute type_name attributes_definition'
    p[0] = '\"' + define_type(p[1]) + '\": ' + p[2] + '\n' + p[3]

def p_attributes_definition_final(p):
    'attributes_definition : attribute type_name'
    p[0] = '\"' + define_type(p[1]) + '\": ' + p[2]

def p_attributes_definition_list_recursive(p):
    'attributes_definition : attribute array_struct attributes_definition'
    p[0] = '\"' + p[1] + '\": ' + p[2] + '\n' + p[3]

def p_attributes_definition_list_final(p):
    'attributes_definition : attribute array_struct'
    p[0] = '\"' + p[1] + '\": ' + p[2]

def p_attribute(p):
    'attribute : STRING'
    p[0] = p[1]

def p_array(p):
    'array : ARRAY'
    p[0] = p[1]

def p_type_string(p):
    'type : STRING'
    if(p[1] == "type"):
        p[0] = p[1]
    else:
        raise Exception("Te equivocaste perri, me mandaste " + p[1])

def p_struct_string(p):
    'struct : STRING'
    if(p[1] == "struct"):
        p[0] = p[1]
    else:
        raise Exception("Te equivocaste perri, me mandaste " + p[1])

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
