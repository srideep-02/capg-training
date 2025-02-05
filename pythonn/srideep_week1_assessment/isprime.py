def is_prime(n):
    if n<=1:  
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

def prime_number(n):
    return is_prime(n)  

def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            print("Prime numbers are:",i)
            count += 1
    return count

def main():
    n = int(input("Enter a number: "))
    print(prime_number(n))  
    print(count_primes(n))