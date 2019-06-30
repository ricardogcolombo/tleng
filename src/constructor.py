import random

def define_type(val):
    if(val == "int"):
        return str(random.randint(0,100))
    else:
        return "limpiame sucio"

def create_array(val):
    res = '[ \n'
    for num in range(0,random.randint(0,4)):
        res = res + define_type(val) + ", \n"
    return res + define_type(val) + '\n]'
