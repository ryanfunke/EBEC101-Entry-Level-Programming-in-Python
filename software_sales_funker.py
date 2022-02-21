"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 02.2 - Software Sales
Date: 02/14/2022

Description:
    This program asks the user for input in terms of the quantity desired for a software package. It then runs the quantity through a series of 
    decision structures to apply a discount depending on what discount tier it lies within.

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
    # Asks the user for input in terms of packages they would like to purchase
    numPackages = int(input("How many packages will be purchased: "))

    # This decision tree has cases for each interval within the discount pricing tiers.
    if numPackages < 0:
        print("  Invalid Input!")
    elif numPackages >= 0 and numPackages <= 3:
        print("  No discount applied.")
        print("  The total price to purchase " + str(numPackages) + " packages is " + "${:,.2f}".format((numPackages * 880.0)) + ".")
    elif numPackages >= 4 and numPackages <= 39:
        print("  10% discount applied.")
        print("  The total price to purchase " + str(numPackages) + " packages is " + "${:,.2f}".format((numPackages * 880.0 * .9)) + ".")
    elif numPackages >= 40 and numPackages <= 199:
        print("  15% discount applied.")
        print("  The total price to purchase " + str(numPackages) + " packages is " + "${:,.2f}".format((numPackages * 880.0 * .85)) + ".")
    elif numPackages >= 200 and numPackages <= 999:
        print("  30% discount applied.")
        print("  The total price to purchase " + str(numPackages) + " packages is " + "${:,.2f}".format((numPackages * 880.0 * .70)) + ".")
    elif numPackages >= 1000:
        print("  42% discount applied.")
        print("  The total price to purchase " + str(numPackages) + " packages is " + "${:,.2f}".format((numPackages * 880.0 * .58)) + ".")
    else:
        print()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
