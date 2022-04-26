"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 03/28/2022

Description:
    This program takes input from the user for 10 float numbers, and then returns the highest number, lowest number, total value, and average
    of all the numbers.

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


"""Write new functions below this line (starting with unit 4)."""
def get_number_list():
    i = 0
    output = []
    # Loop to accept input from the user and populate the output array
    while i < 10:
        output.append(float(input("  number {:2d} of 10: ".format(i + 1))))
        i += 1
    return output
def main():
    """Write your mainline logic below this line (then delete this line)."""
    high = 0.0
    total = 0.0
    print("Enter 10 numbers:")
    numList = get_number_list()
    low = numList[0]
    # Calculates statistics for the numList with each increment of the contents
    for x in numList:
        total += x
        if x > high:
            high = x
        elif x < low:
            low = x
    avg = total / 10.0   
    # Output of the numList statistics
    print("Highest number: {:2.2f}".format(high))
    print("Lowest number: {:2.2f}".format(low))
    print("Total: {:2.2f}".format(total))
    print("Average: {:2.2f}".format(avg))



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
