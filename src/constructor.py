import random
import string

class Structs(object):
    def __init__(self, name, attributes, structs):
        self.name = name
        self.attributes = attributes
        if(self.is_not_duplicated(structs)):
            self.structs = [self] + structs

    def evaluate(self):
        self.validate_all_structs_are_defined()
        self.validate_not_circular_definition()
        return "{" + self.attributes.evaluate(self.structs) + " \n}"

    def is_not_duplicated(self, structs):
        for struct in structs:
            if(struct.name == self.name):
                raise Exception(self.name + " was already defined")
        return True

    def validate_all_structs_are_defined(self):
        for struct in self.structs:
            struct.attributes.validate_all_attributes_are_defined(self.structs)

    def validate_not_circular_definition(self):
        for struct in self.structs:
            struct.attributes.validate_not_circular_definition([struct.name], self.structs)

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

    def validate_all_attributes_are_defined(self, structs_defined):
        for attribute in self.attributes:
            attribute.type_is_defined(structs_defined)

    def validate_not_circular_definition(self, dependencies, structs_defined):
        for attribute in self.attributes:
            attribute.validate_not_circular_definition(dependencies, structs_defined)

class EmptyAttributes(object):
    def evaluate(self, structs_defined):
        return ''

    def validate_all_attributes_are_defined(self, structs_defined):
        return True

    def validate_not_circular_definition(self, dependencies, structs_defined):
        return True

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
