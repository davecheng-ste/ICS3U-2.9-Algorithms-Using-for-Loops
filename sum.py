"""
File: sum.py
Author: Dave Cheng
Date: 2024-03-19
Description: A program that asks for user input, n, and calculates the
             sum of numbers from 1 to n using an accumulator variable.
"""

# Get user input, n
n = int(input("Enter a number: "))

# Initialize accumulator variable, sum
sum = 0

for index in range(1, n + 1, 1):  # range is inclusive of n
    sum += index
    index += 1

# Output result
print("\nSum of numbers from 1 to " + str(n) + ": " + str(sum))