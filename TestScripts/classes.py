class MyClass:
    x=5

newClass = MyClass()
print(newClass.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age

    def getNameWithGreeting(self):
        print("Hello !, My name is",self.name)

    def getAge(self,newage):
        print(self.name,"says Age is",newage)

p1=Person("Roshan",32)
print(p1.name)
print(p1.age)
p1.getNameWithGreeting()
p1.getAge(25)

p2 =Person("Madhu", 31)
print(p2.name)
print(p2.age)
p2.getNameWithGreeting()

