"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 03/21/2022

Description:
    This program uses the random library to create a rock paper scissors game between the user and the program, which then displays the winner and choices.

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
import random

"""Write new functions below this line (starting with unit 4)."""
# Function that generates random choice for computer
def get_computer_choice():
    answers = ["rock", "paper", "scissors"]   
    return random.choice(answers)
# Function that accepts input from the user for their choice
def get_player_choice():
    choice = ''
    while(choice not in ["rock", "paper", "scissors"]):
        choice = input("Choose rock, paper, or scissors: ")
        if choice not in ["rock", "paper", "scissors"]:
            print("You made an invalid choice. Please try again.")
    return choice
# Function that determines the winner of the game
def get_winner(compPick, userPick):
    winner = ""
    if compPick == userPick:
        winner = "tie"
    elif compPick == "scissors":
        if userPick == "rock":
            winner = "player"
        else:
            winner = "computer"
    elif compPick == "rock":
        if userPick == "paper":
            winner = "player"
        else:
            winner = "computer"
    elif compPick == "paper":
        if userPick == "scissors":
            winner = "player"
        else:
            winner = "computer"
    return winner
    
def main():
    """Write your mainline logic below this line (then delete this line)."""
    compPick = ""
    userPick = ""
    winner = ""
    exitFlag = 0
    # Gets input for choices
    while exitFlag < 1:        
        compPick = get_computer_choice()
        userPick = get_player_choice()
        winner = get_winner(compPick, userPick)
        # Result outputting with conditional statements
        print("  The computer chose " + compPick + ", and you chose " + userPick + ".")
        if winner == "tie":    
            print("  Its a tie. Starting over.")
            print("")
        elif winner == "computer":
            print("  {:s} beats {:s}".format(compPick, userPick))
            print("  You lost.  Better luck next time.")
            print("Thanks for playing.")
            exitFlag = 1
        elif winner == "player":
            print("  {:s} beats {:s}".format(userPick, compPick))
            print("  You won the game!")
            print("Thanks for playing.")
            exitFlag = 1


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
