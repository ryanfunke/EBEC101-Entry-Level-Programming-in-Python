"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 01.2 - Interest
Date: 02/06/2022

Description:
    This program asks the user for input about the quantities of a financial amount being deposited to an account, which are then used 
    to calculate the hypothetical future value it would earn by remaining invested within the account. 

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
    # Defines the identifier for the future value total
    futureValue = 0.0
    # Initial user prompt for input
    print("Enter the following parameters.")

    # Inputs asking user to specify the quantities of the deposit
    principle = input("  The initial deposit? ")
    interestRate = input("  The annual interest rate in percent? ")
    timePeriod = input("  The number of years the account earn interest? ")
    timesCompoundedPerYear = input("  The number of times interest is compounded each year: ")
    futureValue = float(principle) * pow((1.0 + (float(interestRate) / 100.0) / float(timesCompoundedPerYear)), float(timesCompoundedPerYear) * float(timePeriod))
    
    # Printing of result
    print("The balance of this account will be " + str("${:,.2f}").format(futureValue) + " after " + str(float(timePeriod)) + " years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
