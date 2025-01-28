def get_sum():
    numbers=[1,3,5,7,9]
    for i in range(len(numbers)):
        sum=numbers[i]+sum
        return sum
avg=sum/len(l1)
print("The sum is :",sum)
print("The average of list is:",avg)

# numbers = [int(input(f"Enter number {i+1}:"))for i in range(5)]
# total =sum(numbers)
# print("The sum of the numbers is:"total)