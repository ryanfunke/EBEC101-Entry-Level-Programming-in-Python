"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 04.1 - Falling
Date: 02/28/2022

Description:
    This program calculates the distance an object falls according to a formal, which is then output through loops
    and a user created function.

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
# Function that calculates the distance an object falls in given time 
def falling_dist(time):
    gravForce = 8.87
    distance = (0.5) * gravForce * (time ** 2)
    return distance

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Printing of output statements
    print("Time (s)  Distance (m)")
    print("----------------------")
    # Prints each time interval
    for x in range (5, 55, 5):
        print("{:>8d}  {:>12.1f}".format(x, falling_dist(x)))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()