# Check if the given number is ODD NUMBER 
def check_even(n):
    if n % 2 == 0:
        print(f"{n} is not an odd number ")
    else:
        print(f"{n} is an odd number")

n=int(input("Enter the number u want to see odd or even "))
check_even(n)
