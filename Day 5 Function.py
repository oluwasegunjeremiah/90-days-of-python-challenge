# Usind def to print Facrorial number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input from user
number = int(input("Enter a number: "))

# Calculate factorial
result = factorial(number)

# Print the result
print(f"The factorial of {number} is {result}")
