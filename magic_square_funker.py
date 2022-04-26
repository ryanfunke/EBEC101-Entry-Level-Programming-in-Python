"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 07.4 - Magic Square
Date: 03/28/2022

Description:
    This program defines whether a 3x3 array of numbers is determined to be a magic square, and returns to the user
    the output and results of the test ran on the array of numbers.

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
def print_square(numList):
    # Outputs the square of the number list by printing arrays
    print("  {:d} {:d} {:d}".format(numList[0][0], numList[0][1], numList[0][2]))
    print("  {:d} {:d} {:d}".format(numList[1][0], numList[1][1], numList[1][2]))
    print("  {:d} {:d} {:d}".format(numList[2][0], numList[2][1], numList[2][2]))
def is_magic(numList):
    testRange = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Tests the conditions to determine if the square is magic or not
    if (numList[0][0] + numList[0][1] + numList[0][2] == 15):
        if (numList[1][0] + numList[1][1] + numList[1][2] == 15):
            if (numList[2][0] + numList[2][1] + numList[2][2] == 15):
                if (numList[0][0] + numList[1][1] + numList[2][2] == 15):
                    if (numList[0][0] + numList[1][0] + numList[2][0] == 15):
                        if (numList[0][1] + numList[1][1] + numList[2][1] == 15):
                            if (numList[0][2] + numList[1][2] + numList[2][2] == 15):
                                if (numList[2][0] + numList[1][1] + numList[0][2] == 15):
                                    for x in numList:
                                        for y in x:
                                            if y in testRange:
                                                testRange.remove(y)
    # Returns true or false depending on magic square or not
    if (len(testRange) == 0):
        output = True                                     
    else:
        output = False
    
    return output

def main():
    """Write your mainline logic below this line (then delete this line)."""
    numList = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    numList2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    numList3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    # Outputs the magic square and result of being magic or not
    print("Your square is:")
    print_square(numList2)
    if is_magic(numList2) == True:
        print("It is a Lo Shu magic square!\n")
    else:
        print("It is not a Lo Shu magic square.\n")
    print("Your square is:")
    print_square(numList)
    if is_magic(numList) == True:
        print("It is a Lo Shu magic square!\n")
    else:
        print("It is not a Lo Shu magic square.\n")
    print("Your square is:")
    print_square(numList3)
    if is_magic(numList3) == True:
        print("It is a Lo Shu magic square!\n")
    else:
        print("It is not a Lo Shu magic square.\n")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
