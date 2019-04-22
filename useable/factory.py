'''
  工厂模式
'''
class Person(object):
    def __init__(self):
        self.name = None
        self.gener = None

    def getName(self):
        return self.name

    def getGener(self):
        return self.gener


class Male(Person):
    def __init__(self, name):
        print('Hello Mr.'+name)


class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)



class Factory(object):
    def getPerson(self, name, gener):
        if gener == 'M':
            return Male(name)
        if gener == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson('Chetan', 'M')
