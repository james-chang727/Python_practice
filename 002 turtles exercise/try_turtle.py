# Name: try_turtle.py
#
# Description:
#
# Draw a square.
#
# Author: Rae Harbird
#
# Date: August 2018
#
# Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

from turtle import *


# place the turtle on the left hand side of your canvas
penup()
setpos(-300,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw a square

forward(50)     # move forward 50 pixels
left(90)        # turn left 90 degrees
forward(50)
lt(90)          # an abbreviation for turn left 
fd(50)          # an abbreviation for move forward
lt(90)
fd(50)
lt(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()