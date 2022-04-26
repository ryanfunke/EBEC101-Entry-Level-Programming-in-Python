"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 03/21/2022

Description:
    This program generates two random numbers and then asks the user to calcualte the result of them. If the user is correct, it will return a status message saying such
    and will print the correct answer if the user is incorrect.

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
import random

"""Write new functions below this line (starting with unit 4)."""
# Function that generates random numbers for the math quiz
def random_number(digits):
    rangeInt = 0
    startRange = 0
    output = 0

    # Sets range of random number to generate
    if digits == 1:
        rangeInt = 9
    elif digits == 2:
        rangeInt = 99
        startRange = 10
    elif digits == 3:
        rangeInt = 999
        startRange = 100

    output = random.randint(startRange, rangeInt)
    
    return output

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Generates random numbers 
    x = random_number(2)
    y = random_number(3)
    print("{:5d}".format(x))
    print("+{:4d}".format(y))
    print("-----")
    # User input to try and solve math quiz, provides feedback after
    answer = int(input("= "))
    if answer == x + y:
        print("Correct -- Good Work!")
    else:
        print("Incorrect. The correct answer is {:d}.".format(x + y))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
