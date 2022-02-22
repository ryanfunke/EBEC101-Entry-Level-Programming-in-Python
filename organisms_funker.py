"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 03.4 - Organisms
Date: 02/21/2022

Description:
    This program asks the user to input a starting population (in thousands), an average daily increase, and number of days to multiply
    before calculating the approximate population of organisms after multiplying.

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
    #Declaration of initial variables
    population = 0.0
    dailyInc = 0.0
    numDays = 0
    i = 0

    #Asking the user for input to define quantities
    population = float(input("Starting population, in thousands: "))
    dailyInc = float(input("Average daily increase, in percent: ")) / 100.0
    numDays = int(input("Number of days to multiply: "))

    #Calculation and output
    print("Day   Approx. Pop")
    while i <= numDays: 
        if i > 0:
            population = population * (1 + dailyInc)
            print("{:3d}   {:>,11.3f}".format(i, population))
            i += 1
        else:
            print("{:3d}   {:>,11.3f}".format(i, population))
            i += 1
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
