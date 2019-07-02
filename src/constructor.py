import random
import string

class Structs(object):

    def __init__(self, name, attributes, structs):
        self.name = name
        self.attributes = attributes
        if(self.is_valid_struct(structs)):
            self.structs = [self] + structs

    def evaluate(self):
        res = ''
        for struct in self.structs:
            res = "{ \n \t" + res + struct.attributes.evaluate() + " \n}"
        return res

    def is_valid_struct(self, structs):
        for struct in structs:
            if(struct.name == self.name):
                raise Exception(self.name + " was already defined")
        return True

class Attributes(object):
    def __init__(self, value, attributes):
        self.attributes = [value] + attributes

    def evaluate(self):
        res = ''
        for attribute in self.attributes:
            res = res + "\n \t" + attribute.evaluate()
        return res

##TYPES
class Type(object):
    def __init__(self, name, is_array=False):
        self.name = name
        self.is_array = is_array

    def value(self):
        raise NotImplementedError

    def evaluate(self):
        if(self.is_array):
            return self.evaluate_array()
        return self.evaluate_single()

    def evaluate_single(self):
        return "\"" + self.name + "\":" + self.value()

    def evaluate_array(self):
        res =  '\"' + self.name + '\": ' + '[ \n'
        for num in range(0,random.randint(0,4)):
            res = res + self.value() + ", \n"
        return res + '\n]'

class RandomBool(Type):
    def value(self):
        return str(bool(random.getrandbits(1)))

class RandomInt(Type):
    def value(self):
        return str(random.randint(0,100))

class RandomFloat(Type):
    def value(self):
        return str(random.uniform(0,100))

class RandomString(Type):
    def value(self):
        val = ''.join(random.sample(string.ascii_lowercase,random.randint(1,30)))
        return "\"" + val + "\""
