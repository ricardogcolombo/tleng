import ply.yacc as yacc
import ply.lex as lex
import random
from constructor import RandomBool, RandomInt, RandomFloat, RandomString
from lexer import tokens

### Struct definition

def p_struct_recursive(p):
    'struct_block : TYPE type_name STRUCT struct_definition struct_block '
    p[0] = '{\n' + p[4] + '\n}'

def p_struct_final(p):
    'struct_block : TYPE type_name STRUCT struct_definition '
    p[0] = '{\n' + p[4] + '\n}'

def p_attributes(p):
    'struct_definition : LBRACKET attributes_definition RBRACKET'
    p[0] = p[2]

def p_type_name(p):
    'type_name : WORD'
    p[0] = p[1]

### Attributes definition

def p_attributes_definition_recursive(p):
    'attributes_definition : attribute_value attributes_definition'
    p[0] = p[1] + '\n' + p[2]

def p_attributes_definition_final(p):
    'attributes_definition : attribute_value'
    p[0] = p[1]

### Value definition

def p_attribute(p):
    'attribute : WORD'
    p[0] = p[1]

### STRING
def p_string_value(p):
    'attribute_value : attribute STRING'
    p[0] = RandomString(p[1]).evaluate_single()

def p_array_string_value(p):
    'attribute_value : attribute ARRAY STRING'
    p[0] = RandomString(p[1]).evaluate_array()

### INT
def p_int_value(p):
    'attribute_value : attribute INT'
    p[0] = RandomInt(p[1]).evaluate_single()

def p_array_int_value(p):
    'attribute_value : attribute ARRAY INT'
    p[0] = RandomInt(p[1]).evaluate_array()

### FLOAT64
def p_float_value(p):
    'attribute_value : attribute FLOAT64'
    p[0] = RandomFloat(p[1]).evaluate_single()

def p_array_float_value(p):
    'attribute_value : attribute ARRAY FLOAT64'
    p[0] = RandomFloat(p[1]).evaluate_array()

### BOOL
def p_bool_value(p):
    'attribute_value : attribute BOOL'
    p[0] = RandomBool(p[1]).evaluate_single()

def p_array_bool_value(p):
    'attribute_value : attribute ARRAY BOOL'
    p[0] = RandomBool(p[1]).evaluate_array()

### NEW TYPE
def p_new_type_value(p):
    'attribute_value : attribute type_name'
    p[0] = '\"' + p[1] + '\": ' + p[2]

def p_array_new_type_value(p):
    'attribute_value : attribute ARRAY type_name'
    res =  '\"' + p[1] + '\": ' + '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + p[3] + ", \n"
    p[0] = res + '\n]'

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
