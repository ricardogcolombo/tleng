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
            res = res + "\n" + attribute.evaluate(structs_defined)
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
