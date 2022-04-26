"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 04/04/22

Description:
    This program accepts input from a user for a phone number, and then replaces any letters in the phone number
    with their numeric values.

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
def convert_number(s):
    output = ""
    # Loops through each component of the string
    for x in s:
        # Standardizes characters
        y = x.lower()
        # Modifies value depending if it is numeric or not
        if x == "-":
            output += x
        elif x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            output += x
        else:
            z = x.lower()
            if z in ["a", "b", "c"]:
                output += ("2")
            elif z in ["d", "e", "f"]:
                output += ("3")
            elif z in ["g", "h", "i"]:
                output += ("4")
            elif z in ["j", "k", "l"]:
                output += ("5")
            elif z in ["m", "n", "o"]:
                output += ("6")
            elif z in ["p", "q", "r", "s"]:
                output += ("7")
            elif z in ["t", "u", "v"]:
                output += ("8")
            elif z in ["w", "x", "y", "z"]:
                output += ("9")
    return output
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Input, calling function, output
    s = input("Enter a telephone number: ")
    output = convert_number(s)
    print("The phone number is {:s}".format(output))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()