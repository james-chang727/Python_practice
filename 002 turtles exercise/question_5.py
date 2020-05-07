# Name: question_5.py
#
# Description:
#
# Draw shapes.
#
# Author: Rae Harbird
#
# Date: August 2018
#
# Here is a list of colours: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

from turtle import *


#
# Function to draw a polygon
#
def draw_Ngon(sides, side_length):
    
# Add your code here



# place the turtle on the left hand side of your canvas
penup()
setpos(-300,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle
draw_Ngon(3, 50)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()