def getMyName(name = 'There !'):
    print("Hello",name)

def getSum(x, y):
    return x+y


try:
    getMyName("Roshan")
except:
    pass

try:
    print("Total:",getSum(22,10))
except:
    print("Exception")

x = lambda greeting: "Hello "+greeting
print(x("Roshan Ranasinghe"))

cars = list(("A", "B", "C"))
index = cars.index('B')
print(index)

for x in cars :
    if x=="C":
        break
    print(x)

mystr ="hello.world"
print ("Location -",(mystr.index("o")))
print(mystr.split(".").__getitem__(1))



