"""
File: miles.py
Author: Dave Cheng
Date: 2024-03-19
Description: A program that outputs values for kilometres and equivalent miles 
             every 10 km up to 100 km.
"""

for km in range(10, 101, 10):  # this generates 10, 20, 30 ... 100
    miles = km * 0.625
    # Output km = miles
    print(str(km) + " km = " + str(miles) + " miles")
