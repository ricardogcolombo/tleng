import random
import string

DEPENDENCIES_LIST = []

def define_type(val):
    return val

def create_array(val):
    res = '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + define_type(val) + ", \n"
    return res + define_type(val) + '\n]'

def create_random_string():
    val = ''.join(random.sample(string.ascii_lowercase,random.randint(1,30)))
    return "\"" + val + "\""

def register_struct(struct, type_name):
    STRUCT_MAP[type_name] = struct
