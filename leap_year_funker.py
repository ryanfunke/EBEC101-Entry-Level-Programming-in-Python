"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 02.1 - Leap Year
Date: 02/13/2022

Description:
    This program takes input from the user for a year, which it then analyzes to determine if it is a leap year. It also outputs the 
    number of days in the month of February for the specified year.

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
    
    # This statement asks the user for input and then stores the year as an integer.
    year = int(input("Enter a year: "))
    # This decision tree decides if the year is a leap year or not by using modulus to determine if the year is evenly divisble by 4 or 400.
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print("The year " + str(year) + " is a leap year.")
                print("February of " + str(year) + " has 29 days.")
            else: 
                print("The year " + str(year) + " is not a leap year.")
                print("February of " + str(year) + " has 28 days.")
        else:
            print("The year " + str(year) + " is a leap year.")
            print("February of " + str(year) + " has 29 days.")
    else:
        print("The year " + str(year) + " is not a leap year.")
        print("February of " + str(year) + " has 28 days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
