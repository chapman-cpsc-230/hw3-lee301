"""
File: turtlestar.py

Copyright (c) 2016 Krystal

License: MIT

Draw a hendecagram using user inputs.
"""

import turtle

# Ask user for input here.

# Now create a graphics window.
t = turtle.Pen()

#side = 5
for j in range(1):
    for i in range(11):
        t.forward(200)
        t.left(163.5)

# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
