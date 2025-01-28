import array #not required
l1=[]
print("1. A empty list",l1)

l2=[1,2,3,4]
print("2. list with four items",l2)

l3=['abc',['def','ghi']]
print("3. A nested list",l3)

l4=list('spam')
print("4. list created from",l4)

l5=list[(range(-4,4))]
print("5. list created from range -4 to 4",l5)

l6=[10,20,30,40]
print("6. element created at index 2 if l6",l6[2])

l7=[[10,20,30],[40,50,60]]
print("7. ellement at l7[1][2](nested list)",l7[1][2])

l8=['x',[10,20,30],'y']
print("8. list created from range -4 to 4",l8[2:4])
print("9.Length of l8:",len[l8])

l9= [10,[100,200,300,400],50]
print("10a.element at L9[1]:",l9[1])
print("10b.element at L9[1][3]:",l9[1][3])
print("10c. slicing sublist L9[1]1:[3]:",l9[1][1:3])
print("\n Summaryof outputs")
print("L1:",l1)
print("L2:",l2)
print("L1:",l3)
print("L1:",l4)
print("L1:",l5)
print("L1:",l6)
print("L1:",l7)
print("L1:",l8)
print("L1:",l9)



#listtt functionsss
print(len([1,2,3]))
combinedList =[1,1,1,1][2,2,2,2]
print(combinedList)

sameValuelist=['abc']*4
print(sameValuelist)

print(str([1,2]) + "34")   #  1,2,34

print([1,2]+list("34"))      #1,2,3,4

print(3 in [1,2,3])

for x in [1,2,3]:
    print(x, end=' ')
    
res = [c * 4 for c in 'SPAM']
res    #['SSSS,PPPP,AAAA,MMMM']



