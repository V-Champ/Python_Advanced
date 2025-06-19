#The range() is a built-in function in Python. Syntax of
#range() function is:
#range([start], stop[, step])
#Write a Python program to check if a given number is prime or not.
n=int(input("enter the number\n"))
def print_primes_up_to_100_optimized():
    """Prints prime numbers from 1 to n using an optimized trial division method."""
    print("Prime numbers from 1 to 100 (Optimized):")
    for num in range(2, n):  # Start from 2, as 1 is not prime
        is_prime = True
        if num < 2:  # Numbers less than 2 are not prime
            is_prime = False
        else:
            # Check for divisibility from 2 up to the square root of num
            # If a number has a divisor greater than its square root,
            # it must also have a divisor smaller than its square root.
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break  # Not prime, no need to check further
        if is_prime:
            print(num, end=" ")
    print()  # For a new line at the end
print_primes_up_to_100_optimized()