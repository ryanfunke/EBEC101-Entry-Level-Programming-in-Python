"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 09.2 - World Series
Date: 04/11/2022

Description:
    This program takes input from a file and then creates two dictionaries about statistics relating to world series wins. One dictionary contains information about the total amount of wins a team has in the world series,
    whereas the other has a dictionary which keeps the value (a team name) of a key (a certain year) relating to that year's world series winner. 

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
def load_winners_data():
    #This function takes the input from the file
    file = "WorldSeriesWinners.txt"
    teamNames = {}
    years = {}
    with open(file) as f:
        lines = f.readlines()
    #Assigning the values for each key
    f.close()
    i = 1903
    for x in lines:
        x = x[:-1]
        if teamNames.get(x) == None:
            teamNames[x] = 1
        else:
            teamNames[x] += 1
        if (i == 1904) or (i == 1994):
            years[i + 1] = x
            i += 1
        else:
            years[i] = x
        i += 1
    #Returns the two dictionaries
    return(teamNames, years)

def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Gathers user input
    userInput = int(input("Enter a year in the range 1903 -- 2021: "))
    #Returns the output of the year that a user selected 
    teamNames, years = load_winners_data()
    if (userInput > 2021) or (userInput < 1903):
        print("  Data for the year {:d} is not included in this system.".format(userInput))
    elif (userInput == 1904) or (userInput == 1994): 
        print("  The World Series wasn't played in the year {:d}.".format(userInput))
    else:
        winner = years.get(userInput)
        amountWin = teamNames.get(winner)
        print("  The {:s} won the World Series in {:d}.".format(winner, userInput))
        print("  They have won the World Series {:d} times.".format(amountWin))

"""Do not change anything below this line."""
if __name__ == '__main__':
    main()

