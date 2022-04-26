"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 08.3 - File Stats
Date: 04/04/22

Description:
    This program analyzes the contents of a file and then outputs statistics about the number of words, lines and average number of words per line
    within the document.

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
    # Initializes stats
    numLines = 0
    numWords = 0
    avgWords = 0

    # Reads file input
    file = 'frontiero_v_richardson.txt'
    with open(file) as f:
        lines = f.readlines()
    f.close()

    # Calculates file statistics and then outputs it to the user
    for x in lines:
        numLines += 1
        y = x.split()
        for x in y:
            numWords += 1
    
    avgWords = numWords/numLines

    print("Total number of words: {:d}".format(numWords))
    print("Total number of lines: {:d}".format(numLines))
    print("Average number of words per line: {:.1f}".format(avgWords))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()