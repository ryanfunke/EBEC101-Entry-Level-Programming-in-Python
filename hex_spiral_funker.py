"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 05.2 - Hex Spiral
Date: MM/DD/YYYY

Description:
    This program draws a spiral where the length of the spirals sides incresaed by 6 pixels after every 60 degree turn.

Contributors:
    Ryan Funke, funker@purdue.edu

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width('5')


def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Sets the starting position for the illustration
    goto(0,0)
    i = 0
    j = 6
    # Carries out the movement to trace the spiral
    while i < 39:
        pendown()
        forward(j)
        right(60)
        j += 6
        i += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
