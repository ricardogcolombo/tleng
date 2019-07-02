import random
import string

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

    def type_is_defined(self, structs):
        return True

    def validate_not_circular_definition(self, dependencies, structs_defined):
        return True

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
        val = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1,30)))
        return "\"" + val + "\""

class RandomStruct(Type):
    def value(self, structs_defined):
        for struct in structs_defined:
            if(self.type_name == struct.name):
                value = struct.attributes.evaluate(structs_defined) + "\n}"
                return "{" + "\t".join(value.splitlines(True))

    def type_is_defined(self, structs_defined):
        for struct in structs_defined:
            if(self.type_name == struct.name):
                return True
        raise Exception(self.type_name + " was never defined")

    def validate_not_circular_definition(self, dependencies, structs_defined):
        if(self.type_name in dependencies):
            raise Exception(self.type_name + " has a circular dependency")
        else:
            for struct in structs_defined:
                if(self.type_name == struct.name):
                    return struct.attributes.validate_not_circular_definition([self.type_name] + dependencies, structs_defined)

class RandomStructInline(Type):
    def __init__(self, name, attributes, is_array=False):
        self.name = name
        self.attributes = attributes
        self.is_array = is_array

    def type_is_defined(self, structs):
        for attribute in self.attributes:
            if(not attribute.type_is_defined()):
                return False
        return True

    def value(self, structs_defined):
        return "{" + "\t".join(self.attributes.evaluate(structs_defined).splitlines(True)) + "\n \t}"
