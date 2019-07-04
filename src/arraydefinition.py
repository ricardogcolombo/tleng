import random

class Array(object):
    def __init__(self, attributes):
        self.attributes = attributes

    def value(self, structs_defined):
        res =  ''
        for num in range(0,random.randint(0,5)):
            if(num > 0):
                res = res + ", \n"
            res = res + self.attributes.value(structs_defined)
        return '[ \n' + self.add_tabs(res) + '\n]'

    def type_is_defined(self, structs):
        return self.attributes.type_is_defined(structs)

    def validate_not_circular_definition(self, dependencies, struct_defined):
        return self.attributes.validate_not_circular_definition(dependencies, struct_defined)

    def add_tabs(self, val):
        return "\t" + "\t".join(val.splitlines(True))
