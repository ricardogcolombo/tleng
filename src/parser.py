import ply.yacc as yacc
import ply.lex as lex
import random
from constructor import create_random_string
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
    p[0] = '\"' + p[1] + '\": ' + create_random_string()

def p_array_string_value(p):
    'attribute_value : attribute ARRAY STRING'
    res =  '\"' + p[1] + '\": ' + '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + create_random_string() + ", \n"
    p[0] = res + '\n]'

### INT
def p_int_value(p):
    'attribute_value : attribute INT'
    p[0] = '\"' + p[1] + '\": ' + str(random.randint(0,100))

def p_array_int_value(p):
    'attribute_value : attribute ARRAY INT'
    res =  '\"' + p[1] + '\": ' + '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + str(random.randint(0,100)) + ", \n"
    p[0] = res + '\n]'

### FLOAT64
def p_float_value(p):
    'attribute_value : attribute FLOAT64'
    p[0] = '\"' + p[1] + '\": ' + str(random.uniform(0,100))

def p_array_float_value(p):
    'attribute_value : attribute ARRAY FLOAT64'
    res =  '\"' + p[1] + '\": ' + '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + str(random.uniform(0,100)) + ", \n"
    p[0] = res + '\n]'

### BOOL
def p_bool_value(p):
    'attribute_value : attribute BOOL'
    p[0] = '\"' + p[1] + '\": ' + str(bool(random.getrandbits(1)))

def p_array_bool_value(p):
    'attribute_value : attribute ARRAY BOOL'
    res =  '\"' + p[1] + '\": ' + '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + str(bool(random.getrandbits(1))) + ", \n"
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
