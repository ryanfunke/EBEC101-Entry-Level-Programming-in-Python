"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 03.1 - Arrows
Date: 02/19/2022

Description:
    This program asks the user for the number of arrows they would like the program to draw, and then creates the arrows with each one getting longer than the previous.

Contributors:
    Ryan Funke

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
    """Write your mainline logic below this line (then delete this line)."""
    
    # Asks the user for input and initializes variables
    numArrows = int(input("Enter the number of arrows to draw: "))
    i = 0
    # Adds a new body to the arrow for each loop
    while(i < numArrows):
        counter = 0
        arrowOut = ""
        while(counter < i):
            arrowOut = arrowOut + "="
            counter = counter + 1
        print("<" + arrowOut + ">")
        i = i + 1



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
