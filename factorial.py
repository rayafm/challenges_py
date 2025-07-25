# Factorial
# Complete the factorial() function. It should calculate the factorial of a number. 
# A factorial of a number is the product of all positive integers less than or equal to that number.
# For example:
# 4! = 4 * 3 * 2 * 1 = 24

def factorial(num):

    fact = 1

    for i in range(num, 0, -1):
        fact *= i

    return fact