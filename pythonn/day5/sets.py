empty_set=set()
fruits= {'apple','orange','banana'}
print("Empty set:",empty_set)
print("Fruits",fruits)

fruits.add('grapes')
print("Fruits set after adding grapes",fruits)

fruits.remove('apple')
print("Fruits set after removing apple",fruits)

fruits.clear()
print("Fruits after clearing",fruits)

fruits.update('kiwi')
print("Fruits after updating kiwi",fruits)
fruits.update(['kiwi'])
print("Fruits after updating list kiwi",fruits)
