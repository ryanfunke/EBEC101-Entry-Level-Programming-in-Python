"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 04.2 - Maximum
Date: 02/28/2022

Description:
    This program takes input from a user and then runs them through a user defined function to determine which is 
    greater of the two.

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
# Function that returns the value of the greater input
def max_of_two(x, y):
    if x > y:
        return(x)
    else: 
        return(y)

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Inputs from user
    x = int(input("Enter the first integer: "))
    y = int(input("Enter the second integer: "))
    # Output of result
    print("The number " + str(max_of_two(x, y)) + " is greater.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()