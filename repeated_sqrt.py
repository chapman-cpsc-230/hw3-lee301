"""
File: repeated_sqrt.py

Copyright (c) 2016 Krystal Lee

License: MIT

Explain  what the code does and investigate to print the value r.
"""

from math import sqrt
for n in range(1,26): #we set the n value in the range of 1 to 26.
    r = 2.0 #the variable r equals to 2
    for i in range (n):
        r = sqrt(r) #the variable r now equals to the sqaure root of r
    for i in range (n):
        r = r**2 #the variable r now equals to squared r

    print r
