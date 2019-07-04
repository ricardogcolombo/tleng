import random
import string

##TYPES
class Type(object):
    def __init__(self, type_name, name=""):
        self.name = name
        self.type_name = type_name

    def value(self, structs_defined):
        raise NotImplementedError

    def evaluate(self, structs_defined):
        return "\"" + self.name + "\":" + self.value(structs_defined)

    def add_tabs(self, val):
        return "\t" + "\t".join(val.splitlines(True))

class DefinedType(Type):
    def __init__(self, name=""):
        self.name = name

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
                value = struct.attributes.evaluate(structs_defined)
                return "{" + "\t".join(value.splitlines(True)) + "\n}"

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
    def __init__(self, attributes, name=""):
        self.name = name
        self.attributes = attributes

    def type_is_defined(self, structs):
        return self.attributes.validate_all_attributes_are_defined(structs)

    def validate_not_circular_definition(self, dependencies, struct_defined):
        return self.attributes.validate_not_circular_definition(dependencies, struct_defined)

    def value(self, structs_defined):
        return "{" + "\t".join(self.attributes.evaluate(structs_defined).splitlines(True)) + "\n}"


class RandomArray(Type):
    def __init__(self, attributes, name):
        self.name = name
        self.attributes = attributes

    def value(self, structs_defined):
        return self.attributes.value(structs_defined)

    def type_is_defined(self, structs):
        return self.attributes.type_is_defined(structs)

    def validate_not_circular_definition(self, dependencies, struct_defined):
        return self.attributes.validate_not_circular_definition(dependencies, struct_defined)
