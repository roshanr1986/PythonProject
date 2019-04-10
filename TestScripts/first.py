# this is a comment in python
print('Hello world')
thisdict = dict( name='Roshan', age=32, city='Singapore')
print(thisdict.get('age'))
thisdict.update(lastname='Ranasinghe')
print(thisdict.get('lastname'))
print("Boarn on ",2019-thisdict.get('age'))
a=10
b=20
a=a+b
b=a-b
a=a-b
print('A = ',a)
print('B = ',b)
if a>b: print('A is greater than B')
else: print('A is less than B')

i = 0
while i < 6:
  i += 1
  if i == 3:
    break
  print(i)
print('loop ended')


for x in range(2, 6):
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
  else : print("End of fruit loops")
else: print("End of adjective loop")