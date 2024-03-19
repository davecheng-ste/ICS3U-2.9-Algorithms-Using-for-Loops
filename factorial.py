"""
File: factorial.py
Author: Dave Cheng
Date: 2024-03-19
Description: A program that asks for user input, n, and calculates the
             factorial n! outputting the final value.
"""

# Get user input - NO ERROR CHECKING FOR INVALID INPUT
n = int(input("Enter a number: "))

# Initialize variable to store total factorial
fact = 1

# Iterate from 1 to n
for i in range(1, n + 1, 1):
    fact *= i

# Output factorial result
print("\n" + str(n) + "! = " + str(fact))