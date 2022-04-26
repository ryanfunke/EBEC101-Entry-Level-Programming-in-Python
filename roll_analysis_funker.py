"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 03/28/2022

Description:
    This program simulates the rolling of two d6 die, and then outputs the frequency of their roll combinations to the user.

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
def roll_d6():
    # Generates a random roll
    output = random.randint(1, 6)
    return output
def get_2d6_rolls(n):
    i = 0
    output = []
    # Generates a random two dice roll
    while i < n:
        roll = roll_d6() + roll_d6()
        output.append(roll)
        i += 1
    return output

def main():
    """Write your mainline logic below this line (then delete this line)."""
    n = 1000000
    numList = get_2d6_rolls(n)
    frequencyList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Adds total occurances of number rolls
    for x in numList:
        frequencyList[x - 2] += 1
    print("Roll  Frequency")
    i = 2
    # Prints the frequency percentages of each roll combination
    for x in frequencyList: 
        print(" {:2d}    {:5.2f}%".format(i, x/(n / 100)))
        i += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
