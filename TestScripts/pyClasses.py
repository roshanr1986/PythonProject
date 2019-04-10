class Employee:
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.pay=pay
        self.email=firstname+'.'+lastname+'@company.com'

    def getFullname(self):
        return '{} {}'.format(self.firstname,self.lastname)




e1=Employee('Roshan','Ranasinghe',7000)
print(e1.email)
print(e1.getFullname())

nums=['a','b','c','d','e']

print(nums.index('c'))

for num in range(1,3):

    if num==3:
        print("found",num)
        continue
    print(num)

letters=['a','b','c']
numbers=[1,2,3,5,4,6,8,7,9,10,11,12]

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in numbers])
print(A2)

