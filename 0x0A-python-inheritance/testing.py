class Parent:
    def __init__(self):
        self.__private_attribute = 42
        self.weight = 100

    def __private_method(self):
        return "I am a private method"


class Child(Parent):
    pass


obj = Child()
print(obj.weight)
print(obj._Parent__private_attribute)

print(obj._Parent__private_method())
