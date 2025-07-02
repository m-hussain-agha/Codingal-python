# Python program to check if a number is prime
# take input from the user
num = int(input("Enter a number"))
# check if number is greater than 1 (since primes are > 1)
if num > 1:
    # loop only upto the square root if num for efficiency
    for i in range(2, int(num**0.5) + 1):
        # if num is divisible by any number, its not prime
        if num % i == 0:
            print(f"{num} is not a prime number")
            break # if no divisors were found,the number is prime
    else:
        print(f"{num} is a prime number.")
else:
    # Numbers less than 2 are not prime
    print(f"{num}is not a prime number")