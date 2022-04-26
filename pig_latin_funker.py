"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 04/04/22

Description:
    This program takes input from the user and then converts the string from the user into 
    Pig Latin.

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
def pig(s):
    output = ""
    # Splits the input into a list to modify the words
    y = s.split()
    i = 0
    # Manipulation of each list item into pig latin compatible word
    for x in y:
        x = x.lower()
        temp = x[0]
        if i == 0:
            output += x[1].upper()
        else:
            output += x[1]
        output += x[2:]
        output += (temp.lower())
        output += ("ay ")
        i += 1
    if output[-1] == " ":
        output = output[:-1]
    else:
        output = output
    return output
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Input, calling function, output
    s = input("Enter a string: ")
    output = pig(s)
    print("Pig latin: {:s}".format(output))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()