import random
import string

def define_type(val):
    if(val == "int"):
        return str(random.randint(0,100))
    elif(val == "string"):
        return ''.join(random.sample(string.ascii_lowercase,random.randint(1,30)))
    elif(val == "float64"):
        return str(random.uniform(0,100))
    elif(val == "bool"):
        return str(bool(random.getrandbits(1)))
    else:
        return "limpiame sucio"

def create_array(val):
    res = '[ \n'
    print(val)
    for num in range(0,random.randint(0,4)):
        res = res + define_type(val) + ", \n"
    return res + define_type(val) + '\n]'
