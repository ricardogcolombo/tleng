import random

def define_type(val):
    if(val == "int"):
        return str(random.randint(0,100))
    else:
        return "limpiame sucio"

def create_array(val):
    asa = ''
    for num in range(0,random.randint(1,5)):
        asa = asa + define_type(val) + ", "
    return asa
