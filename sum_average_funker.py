"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 03.2 - Sum Average
Date: 02/19/2022

Description:
    This program asks the user for input of numbers, which continues until the user inputs a negative number. At this point, 
    if numbers were entered the program will calculate the sum and averages and output these values to the user. 

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
    #Initializes variables needed for storing data and calculations
    x = 0
    results = []
    sumResults = 0
    avgResults = 0

    #Executes the procedures of the program while input is not negative
    while(x >= 0):
        x = float(input("Enter a non-negative number (negative to quit): "))
        if x < 0: 
            break
        else: 
            results.append(x)
    #Calculates sums and averages
    if(len(results) >= 1):
        for y in results:
            sumResults = sumResults + y

        avgResults = sumResults / len(results)
        print("  You entered " + str(len(results)) + " numbers.")
        print("  Their sum is {:.3f} and their average is {:.3f}.".format(float(sumResults), float(avgResults))) 
    else:
        print("  You didn't enter any numbers.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
