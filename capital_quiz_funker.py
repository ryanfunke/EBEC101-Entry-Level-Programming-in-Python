"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 04/11/2022

Description:
    This program takes input from a file and then creates a dictionary of keys and values in which states and their capitals are linked. Using the random library, the program will then
    select a random key and ask the user to provide the correct value for them -- which is the capital of the state printed out to the user.

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
def get_state_data():
    #This function takes the input from the file to create the dictionary and keys needed for the quiz
    file = "state_capitals.txt"
    output = []
    data = {}
    with open(file) as f:
        lines = f.readlines()
    #Cleaning up the keys and values in the dictionary
    f.close()
    for x in lines:
        a = x.split(",")
        a[1] = a[1][1:len(a[1]) - 1]
        data[a[1]] = a[0]
    return(data)

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Declares variables used later in program
    breakFlag = 1
    numCorrect = 0
    data = {}
    numAsked = 0
    data = get_state_data()
    #Runs the quiz for the user until they opt to end the program
    while (breakFlag and (len(data) != 0)):
        state = random.choice(list(data))   
        userChoice = str(input("What is the capital of {:s} (enter 0 to quit)? ".format(state)))
        #Checks if the user opts to end the program
        if userChoice.isnumeric():
            if int(userChoice) == 0:
                breakFlag = 0
        elif userChoice.lower() == str(data.get(state)).lower():
            print("  That is correct!")
            numCorrect += 1
            numAsked += 1
        else:
            print("  That is incorrect.")
            print("  The capital of {:s} is {:s}.".format(state, data.get(state)))
            numAsked += 1
        del data[state]    
    print("You answered {:d} out of {:d} questions correctly.".format(numCorrect, numAsked))

"""Do not change anything below this line."""
if __name__ == '__main__':
    main()

