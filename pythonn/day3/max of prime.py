def get_input():
    num1=int(input("Enter the range for prime numbers"))
    list1=[]
    for i in range(num1):
        if num1<=1:
            return False
        for i in range(2, int(num1**0.5) + 1):
            if num1 % i != 0:
                list1.append(i)
            else:
                return False
    
ll