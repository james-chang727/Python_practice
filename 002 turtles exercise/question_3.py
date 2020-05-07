# Name: question_3.py
#
# Description:
#
# Draw squares.
#
# Author: 
#
# Date: 
#
# Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

from turtle import *

#
# Function to draw a square
#
def draw_square(side_length):
    
    for counter in range(4):
        fd(side_length)
        lt(90)


# place the turtle on the left hand side of your canvas
penup()
setpos(-225,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw square
draw_square(50)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()