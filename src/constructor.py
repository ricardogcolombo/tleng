import random
import string

class Structs(object):
    def __init__(self, name, attributes, structs):
        self.name = name
        self.attributes = attributes
        if(self.is_valid_struct(structs)):
            self.structs = [self] + structs

    def evaluate(self):
        return "{" + self.attributes.evaluate(self.structs) + " \n}"

    def is_valid_struct(self, structs):
        for struct in structs:
            if(struct.name == self.name):
                raise Exception(self.name + " was already defined")
        return True

class Attributes(object):
    def __init__(self, value, attributes):
        self.attributes = [value] + attributes

    def evaluate(self, structs_defined):
        res = ''
        first_run = True
        for attribute in self.attributes:
            if(first_run):
                first_run = False
            else:
                res = res + ","
            res = res + "\n \t" + attribute.evaluate(structs_defined)
        return res

##TYPES
class Type(object):
    def __init__(self, name, type_name, is_array=False):
        self.name = name
        self.type_name = type_name
        self.is_array = is_array

    def value(self, structs_defined):
        raise NotImplementedError

    def evaluate(self, structs_defined):
        if(self.is_array):
            return self.evaluate_array(structs_defined)
        return self.evaluate_single(structs_defined)

    def evaluate_single(self, structs_defined):
        return "\"" + self.name + "\":" + self.value(structs_defined)

    def evaluate_array(self, structs_defined):
        res =  '\"' + self.name + '\": ' + '[ \n'
        for num in range(0,random.randint(0,5)):
            if(num > 0):
                res = res + ", \n"
            res = res + "\t \t" + self.value(structs_defined)
        return res + '\n \t]'

class DefinedType(Type):
    def __init__(self, name, is_array=False):
        self.name = name
        self.is_array = is_array

class RandomBool(DefinedType):
    def value(self, structs_defined):
        return str(bool(random.getrandbits(1)))

class RandomInt(DefinedType):
    def value(self, structs_defined):
        return str(random.randint(0,100))

class RandomFloat(DefinedType):
    def value(self, structs_defined):
        return str(random.uniform(0,100))

class RandomString(DefinedType):
    def value(self, structs_defined):
        val = ''.join(random.sample(string.ascii_lowercase,random.randint(1,30)))
        return "\"" + val + "\""

class RandomStruct(Type):
    def value(self, structs_defined):
        for struct in structs_defined:
            if(self.type_name == struct.name):
                value = struct.attributes.evaluate(structs_defined) + "\n}"
                return "{" + "\t".join(value.splitlines(True))
        raise Exception(self.type_name + " was never defined")

class RandomStructInline(Type):
    def __init__(self, name, attributes, is_array=False):
        self.name = name
        self.attributes = attributes
        self.is_array = is_array

    def value(self, structs_defined):
        return "{" + "\t".join(self.attributes.evaluate(structs_defined).splitlines(True)) + "\n \t}"
