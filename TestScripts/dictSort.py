d={1:"John",2:"John",3:"Alex"}
v={}

for key, value in sorted(d.items()):
    print("value is ",value)
    print("Key is ",key)
    v.setdefault(value, []).append(key)
print(v)