# res=-7
#  print(abs(res))

# # 2.pow 
# import math
# a,b=2,3
# print(math.pow(a,b))

# 3..
import math
def display(avg):
    print(f"the average value is{avg}")
    
def get_input():
    a=int(input("Enter A value"))
    b=int(input("Enter B value"))
    c=int(input("Enter C value"))
    d=int(input("Enter D value"))
    return a,b,c,d
def get_avg(a,b,c,d):
    sum=a+b+c+d
    avg=sum/4
    return avg
def main():
    a,b,c,d=get_input()
    avg=get_avg(a,b,c,d)
    display(avg)
    
main()
