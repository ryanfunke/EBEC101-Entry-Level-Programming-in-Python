"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 11.1 - Dice
Date: 04/25/2022

Description:
    This program creates a class called Dice and then assigns the attribute of "sides", which are used to simulate rolling the dice and how many times the dice are
    rolled in the roll and n_rolls functions. The results are then printed to the user.

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
import random

"""Write new functions below this line (starting with unit 4)."""
# Creating the Dice class
class Dice:
    # Initialization
    def __init__(self, sides):
        self.sides = sides
    # Roll function to choose random number
    def roll(self):
        output = random.randint(1, self.sides)
        return output
    # Simulates rolling a certain amount of times
    def n_rolls(self, n):
        output = ""
        for x in range(n):
            output = output + str(self.roll()) + ", "
        print("Rolling a {:d} sided die {:d} times: {:s}".format(self.sides, n, output[:-2]))

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Creating the die
    sixSided = Dice(6)
    tenSided = Dice(10)
    twentySided = Dice(20)
    # Rolling them
    sixSided.n_rolls(10)
    tenSided.n_rolls(10)
    twentySided.n_rolls(10)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
