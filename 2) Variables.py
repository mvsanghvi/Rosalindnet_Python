# Problem:

# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.


[a,b]= [] #insert intergers here
n=(a**2 + b**2)
print(n)

# Alternative #1 (recommended)
import os

a = os.getenv('ENVIRONMENT_VARIABLE_A')
B = os.getenv('ENVIRONMENT_VARIABLE_B')

def squared(a, b):
    return a**2 + b**2


# Alternative #2
def squared(a, b):
    return a**2 + b**2

print('Enter value for variable a:')
a = int(input())
print('Enter value for variable b:')
b = int(input())
print(squared(a,b))
