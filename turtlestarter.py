import turtle

def draw_side(t,side_len,num_bumps):
    if num_bumps == 0:
        t.forward(side_len)
    else:
        draw_side(t,side_len,3.0,num_bumps-1)
        t.left(-60)
        draw_side(t,side_len,3.0,num_bumps-1)
        t.left(120)
        draw_side(t,side_len,3.0,num_bumps-1)
        t.left(-60)
        draw_side(t,side_len,3.0,num_bumps-1)
        
# Ask user for input here.

# Now create a graphics window.
bob = turtle.Pen()

#side = 10
for j in range (20):
    draw_side(bob,100,10)
    bob.left(360.0/3)
    #draw_square(bob,side)
    #side += 5

# Put the rest of your code can go here

# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
