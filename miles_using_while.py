"""
File: miles_using_while.py
Author: Dave Cheng
Date: 2024-03-19
Description: A program that outputs values for kilometres and equivalent miles 
             every 10 km up to 100 km. Algorithm uses while instead of for.
"""

# Initialize counter
km = 10

while km <= 100:
    miles = km * 0.625
    # Output km = miles
    print(str(km) + " km = " + str(miles) + " miles")
    # Increment counter by 10
    km += 10
