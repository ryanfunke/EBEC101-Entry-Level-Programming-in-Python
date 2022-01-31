"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 01.1 - Vineyard
Date: 1/31/2022

Description:
    This program asks the user to input the dimensions of a hypothetical vineyard, to make planning 
    of the vineyard easier. The user asks for three inputs for three dimensions, and then outputs the number of 
    grapevines that will fit in each row. 

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

"""Write new functions below this line (starting with unit 4)."""


def main():
    # Defines the number of vineyards possible
    V = 0
    # Notes to the user what unit to use for inputs
    print("Enter each of the following quantities in meters.")

    # Inputs asking user to specify the dimensions of the vineyard
    E = input(" How wide is the end-post assembly? ")
    S = input(" How much space should be between the vines? ")
    R = input(" How long is this row? ")
    V = int((float(R) - (2 * float(E))) / float(S))
    
    # Printing of result
    print("There is enough space for " + str(V) + " vine(s) in this row.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
