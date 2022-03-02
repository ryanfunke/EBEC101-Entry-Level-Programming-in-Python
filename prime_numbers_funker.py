"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 02/28/2022

Description:
    This program takes input from the user to determine if the number they enter is a prime through user defined functions.

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
import math

"""Write new functions below this line (starting with unit 4)."""
# User defined boolean function that determines if an inputted integer is prime or not 
def is_prime(n):
    result = True
    if ((n == 0) or (n == 1)):
        result = False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
               result = False
               break
    return result

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Asks the user for input
    n = int(input("Enter a positive integer (-1 to quit): "))

    # Condition to check that the user entered valid input, then calling function for result
    if n > 0: 
        if is_prime(n) == False:
            print("  " + str(n) + " is not prime.")
        else:
            print("  " + str(n) + " is prime!")
    else:
        quit

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()