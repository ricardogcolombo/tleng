import random
import string

DEPENDENCIES_LIST = []

class Type(object):

    def __init__(self, attribute):
        self.attribute = attribute

    def value(self):
        raise NotImplementedError

    def evaluate_single(self):
        return "\"" + self.attribute + "\":" + self.value()

    def evaluate_array(self):
        res =  '\"' + self.attribute + '\": ' + '[ \n'
        for num in range(0,random.randint(0,4)):
            res = res + self.value() + ", \n"
        p[0] = res + '\n]'

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
