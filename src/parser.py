import ply.yacc as yacc
import ply.lex as lex
import random
from constructor import create_random_string
from lexer import tokens

def p_struct_recursive(p):
    'struct_block : type type_name struct struct_definition struct_block '
    p[0] = '{\n' + p[4] + '\n}'

def p_struct_final(p):
    'struct_block : type type_name struct struct_definition '
    p[0] = '{\n' + p[4] + '\n}'

def p_attributes(p):
    'struct_definition : LBRACKET attributes_definition RBRACKET'
    p[0] = p[2]

def p_type_name(p):
    'type_name : WORD'
    p[0] = p[1]

def p_array_struct(p):
    'array_struct : array WORD'
    p[0] = p[2]

def p_array_string_struct(p):
    'array_struct : array STRING'
    res = '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + create_random_string() + ", \n"
    p[0] = res + '\n]'

def p_array_int_struct(p):
    'array_struct : array INT'
    res = '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + str(random.randint(0,100)) + ", \n"
    p[0] = res + '\n]'

def p_array_float_struct(p):
    'array_struct : array FLOAT64'
    res = '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + str(random.uniform(0,100)) + ", \n"
    p[0] = res + '\n]'

def p_array_bool_struct(p):
    'array_struct : array BOOL'
    res = '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + str(bool(random.getrandbits(1))) + ", \n"
    p[0] = res + '\n]'

def p_attributes_definition_recursive(p):
    'attributes_definition : attribute type_name attributes_definition'
    p[0] = '\"' + p[1] + '\": ' + p[2] + '\n' + p[3]

def p_attributes_definition_final(p):
    'attributes_definition : attribute type_name'
    p[0] = '\"' + p[1] + '\": ' + p[2]

def p_attributes_definition_list_recursive(p):
    'attributes_definition : attribute array_struct attributes_definition'
    p[0] = '\"' + p[1] + '\": ' + p[2] + '\n' + p[3]

def p_attributes_definition_list_final(p):
    'attributes_definition : attribute array_struct'
    p[0] = '\"' + p[1] + '\": ' + p[2]

def p_attribute(p):
    'attribute : WORD'
    p[0] = p[1]

def p_array(p):
    'array : ARRAY'
    p[0] = p[1]

def p_type_word(p):
    'type : TYPE'
    p[0] = p[1]

def p_struct_word(p):
    'struct : STRUCT'
    p[0] = p[1]

def p_string_word(p):
    'type_name : STRING'
    p[0] = create_random_string()

def p_int_word(p):
    'type_name : INT'
    p[0] = str(random.randint(0,100))

def p_bool_word(p):
    'type_name : BOOL'
    p[0] = str(bool(random.getrandbits(1)))

def p_float_word(p):
    'type_name : FLOAT64'
    p[0] = str(random.uniform(0,100))

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
