# 1 way to check if the number given is prime or not 

def check_prime(n):
    if n <= 1:
        print("Not Prime")
        return

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")

# 2nd way to check if the number given is prime or not.

def check_prime(n):
   if n <= 1:
        print("Not Prime")
        return
   for i in range(2, n//2 + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return
    print(f"{n} is a prime number.")

check_prime(19)


# 3rd way to check if the number is a prime number or not.

import math

def check_prime(n):
    if n <= 1:
        print("Not Prime")
        return

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("Not Prime")
            return

    print(f"{n} Prime Number ")
    
check_prime(11)

# Time Complexity:
# O(√n)



