import ply.yacc as yacc
import ply.lex as lex
import random
import sys
from attributes import Attributes, EmptyAttributes
from structs import Structs
from typesdefinition import RandomBool, RandomInt, RandomFloat, RandomString, RandomStruct, RandomStructInline, RandomArray
from arraydefinition import Array
from lexer import tokens

### Struct definition

def p_final_struct(p):
    'final_struct : struct_block'
    p[0] = p[1].evaluate()

def p_struct_recursive(p):
    'struct_block : TYPE type_name STRUCT struct_definition struct_block '
    p[0] = Structs(p[2], p[4], p[5].structs)

def p_struct_final(p):
    'struct_block : TYPE type_name STRUCT struct_definition '
    p[0] = Structs(p[2], p[4], [])

def p_attributes(p):
    'struct_definition : LBRACKET attributes_definition RBRACKET'
    p[0] = p[2]

def p_attributes_empty(p):
    'struct_definition : LBRACKET RBRACKET'
    p[0] = EmptyAttributes()

def p_type_name(p):
    'type_name : WORD'
    p[0] = p[1]

### Attributes definition

def p_attributes_definition_recursive(p):
    'attributes_definition : attribute_value attributes_definition'
    p[0] = Attributes(p[1], p[2].attributes)

def p_attributes_definition_final(p):
    'attributes_definition : attribute_value'
    p[0] = Attributes(p[1], [])

### Value definition

def p_attribute(p):
    'attribute : WORD'
    p[0] = p[1]

def p_attribute_struct_value(p):
    'attribute_value : attribute STRUCT struct_definition '
    p[0] = RandomStructInline(p[3], p[1])

### STRING
def p_string_value(p):
    'attribute_value : attribute STRING'
    p[0] = RandomString(p[1])

### INT
def p_int_value(p):
    'attribute_value : attribute INT'
    p[0] = RandomInt(p[1])

### FLOAT64
def p_float_value(p):
    'attribute_value : attribute FLOAT64'
    p[0] = RandomFloat(p[1])

### BOOL
def p_bool_value(p):
    'attribute_value : attribute BOOL'
    p[0] = RandomBool(p[1])

### NEW STRUCT
def p_new_struct_value(p):
    'attribute_value : attribute type_name'
    p[0] = RandomStruct(p[2], p[1])

### ARRAY
def p_array_attribute_value(p):
    'attribute_value : attribute array_value'
    p[0] = RandomArray(p[2], p[1])

def p_array_value_recursive(p):
    'array_value : ARRAY array_value'
    p[0] = Array(p[2])

def p_array_string_value(p):
    'array_value : ARRAY STRING'
    p[0] = Array(RandomString())

def p_array_int_value(p):
    'array_value : ARRAY INT'
    p[0] = Array(RandomInt())

def p_array_float_value(p):
    'array_value : ARRAY FLOAT64'
    p[0] = Array(RandomFloat())

def p_array_bool_value(p):
    'array_value : ARRAY BOOL'
    p[0] = Array(RandomBool())

def p_array_new_struct_value(p):
    'array_value : ARRAY type_name'
    p[0] = Array(RandomStruct(p[2]))

def p_array_struct_inline_value(p):
    'array_value : ARRAY STRUCT struct_definition '
    p[0] = Array(RandomStructInline(p[3]))


# Error rule for syntax errors
def p_error(p):
    raise Exception("Syntax error in input")

#############################################

def parseFile():
    if(sys.argv[1] == "--f"):
        with open (sys.argv[2], "r") as myfile:
            parser = yacc.yacc()
            data = myfile.read().replace('\n', '')
            print(parser.parse(data))
    else:
        raise Exception("Too many arguments")

if __name__ == "__main__":
    if(len(sys.argv) > 2):
        parseFile()
    else:
        if(len(sys.argv) == 2):
            parser = yacc.yacc()
            print(parser.parse(sys.argv[1]))
        else:
             raise Exception("Argument expected")
