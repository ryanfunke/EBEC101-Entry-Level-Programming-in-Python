"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 02/14/2022

Description:
    This program takes input from the user in three variables: temperature, velocity, and the diameter of a pipe. 
    It then prints the output of the Reynolds Number at the specified variables after calculating the result.

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
    # This line asks the user for input
    temp = int(input("Enter the temperature in °C as 5, 20, or 50: "))
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "))
    diameter = float(input("Enter the pipe's diameter (m): "))

    kinViscosity = 0.0 

    # This decision tree sets the kinematic viscosity depending on the temperature
    if temp == 5:
        kinViscosity = 1.52 * (10 ** -6)
    elif temp == 20:
        kinViscosity = 1.00 * (10 ** -6)
    elif temp == 50:
        kinViscosity = 5.54 * (10 ** -7)
    else:
        kinViscosity = 0

    # Output of the results
    reynoldsNumber = float((velocity * diameter) / kinViscosity)
    print("At " + str(temp) + ".0°C, the Reynolds number for flow at " + str(velocity) + " m/s in a " + str(diameter) + " m diameter pipe is " + "{:.2e}.".format(reynoldsNumber))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
