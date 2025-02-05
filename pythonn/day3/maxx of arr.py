numbers=[int(input(f"Enter number {i+1}:"))for i in range(5)]
def addition():
    total=sum(numbers)
def maximum():
    numbers.sorted(reverse=True)
    print("Maximum value is",numbers[1])
def minimum():
    numbers.sorted()
    print("Minimum value is",numbers[0])
maximum()
minimum()


def get_input():
    n=int(input("Enter the size of the program"))
    lista=list(map((int,input(f""))))
    