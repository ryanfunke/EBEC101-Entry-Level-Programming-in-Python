"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 02/06/2022

Description:
    This program asks the user for input about how many cookies they would like to make, and then returns the measurements of ingrediants that 
    they would need in order to succesfully make the recipe.

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

    # Asks the user for the input of cookies to make
    totalCookies = int(input("How many cookies do you want to make? "))

    # Calculates the ratio of ingrediants for each type
    totalBase = totalCookies / 48
    butterAmt = 1.25 * totalBase
    sugarAmt = 1.5 * totalBase
    flourAmt = 2.5 * totalBase

    # Printing of result
    print(("To make {:,} cookies, you will need:").format(totalCookies))
    if(flourAmt >= 10000):
        {
        print("  " + "{:,.2f}".format(butterAmt) + " cups of butter"),
        print("  " + "{:,.2f}".format(sugarAmt) + " cups of sugar"),
        print(" " + "{:,.2f}".format(flourAmt) + " cups of flour")
        }
    else:
        {
        print("      " + "{:,.2f}".format(butterAmt) + " cups of butter"),
        print("      " + "{:,.2f}".format(sugarAmt) + " cups of sugar"),
        print("      " + "{:,.2f}".format(flourAmt) + " cups of flour")
        }

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
