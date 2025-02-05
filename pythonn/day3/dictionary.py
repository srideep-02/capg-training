dictionary={}
print("Empty dict",dictionary)

dic1={'chicken':1,'egg':2}
print("Two item dict",dic1)

dic2={'Food':{'chickens':1,'eggs':2}}
print("Nested dict",dic2)

dic3=dict(name='qwerty', age=123 )
print("dictinary 3",dic3)

keys=[1,2,3,4,5]
values=['a','b','c','d','e','f']
d=dict(zip(keys,values))
d1=dict.fromkeys(['a','b'])
print("zip dict:",d)    
dic1.update(dic3)
print("merging using update:",dic1)
print(dic1.items())
print(dic1.copy())
print(dic1.values())
print(dic1.keys())