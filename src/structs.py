class Structs(object):
    def __init__(self, name, attributes, structs):
        self.name = name
        self.attributes = attributes
        if(self.is_not_duplicated(structs)):
            self.structs = [self] + structs

    def evaluate(self):
        self.validate_all_structs_are_defined()
        self.validate_not_circular_definition()
        return "{" + self.add_tabs(self.attributes.evaluate(self.structs)) + " \n}"

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

    def add_tabs(self, val):
        return "\t".join(val.splitlines(True))
