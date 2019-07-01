import random
import string

STRUCT_MAP = {}

def define_type(val):
    if(val == "int"):
        return str(random.randint(0,100))
    elif(val == "string"):
        return create_random_string()
    elif(val == "float64"):
        return str(random.uniform(0,100))
    elif(val == "bool"):
        return str(bool(random.getrandbits(1)))
    else:
        print(STRUCT_MAP)
        return STRUCT_MAP[val]

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
