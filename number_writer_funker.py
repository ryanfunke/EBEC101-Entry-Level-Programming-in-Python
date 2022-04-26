"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 08.4 - Number Writer
Date: 04/04/22

Description:
    This program asks the user for input on how many numbers they would like randomly created in a new file,
    and then it generates these numbers in a file called random_numbers.txt. These numbers are in a range of 1019 through 1215.

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

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Asking users for input to define the amount of numbers to create
    num = int(input("How many numbers would you like? "))
    f = open("random_numbers.txt", "w+")
    i = 0
    # Loop to create numbers in the new file up until a certain quantity
    while i < num:
        f.write("{:d}\n".format(random.randint(1019, 1215)))
        i += 1

    f.close()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()