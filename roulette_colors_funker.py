"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 02/14/2022

Description:
    This program asks the user for an input for a pocket number on a roulette table, and then uses the modulus
    operator to decide if the pocket number is even or not. This is then used to determine the pocket color.

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
    """Write your mainline logic below this line (then delete this line)."""
    # This line asks the user to choose a pocket number for input.
    pocketNum = int(input("Please choose a pocket number: "))

    # This decision tree has cases to decide the color.
    if ((pocketNum < 0) or (pocketNum > 36)):
        print("  Invalid Input!")
    elif pocketNum == 0:
        print("  Pocket number " + str(pocketNum) + " is green.")
    elif pocketNum >= 1 and pocketNum <= 10:
        if pocketNum % 2 == 0:
            print("  Pocket number " + str(pocketNum) + " is black.")
        else:
            print("  Pocket number " + str(pocketNum) + " is red.")
    elif pocketNum >= 11 and pocketNum <= 18:
        if pocketNum % 2 == 0:
            print("  Pocket number " + str(pocketNum) + " is red.")
        else:
            print("  Pocket number " + str(pocketNum) + " is black.")
    elif pocketNum >= 19 and pocketNum <= 28:
        if pocketNum % 2 == 0:
            print("  Pocket number " + str(pocketNum) + " is black.")
        else:
            print("  Pocket number " + str(pocketNum) + " is red.")
    elif pocketNum >= 29 and pocketNum <= 36:
        if pocketNum % 2 == 0:
            print("  Pocket number " + str(pocketNum) + " is red.")
        else:
            print("  Pocket number " + str(pocketNum) + " is black.")
    else:
        print()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
