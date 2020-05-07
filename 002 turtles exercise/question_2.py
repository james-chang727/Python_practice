# Name: question_2.py
#
# Description:
#
# Draw a square.
#
# Author: 
#
# Date: 
#

from turtle import *

# Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm


# place the turtle on the left hand side of your canvas
penup()
setpos(-300,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw the smallest square

for counter in range(4): # repeat 4 times
    forward(50)
    left(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()