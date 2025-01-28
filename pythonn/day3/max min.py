def get_input():
    nums = [int(input(f"Enter number {i+1}:")) for i in range((int(input("Enter the size of nums:"))))]
    return nums

def small_big(nums):
    small = nums[0]
    big = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < small:
            small = nums[i]
        elif nums[i] > big:
            big = nums[i]
    print(f"Smallest Number is:{small}")
    print(f"Biggest Number is: {big}")
    
    return small,big
def main():
    nums = get_input()
    small_big(nums)
main()