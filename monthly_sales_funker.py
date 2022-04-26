"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 04/18/2022

Description:
    This program takes input from the user to fill monthly sales results for each month, and then adds it to
    an array which is then used to print out a pie chart of the resulting sales.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Variable declaration and initialization for each of the months and their colors
    fig, ax = plt.subplots()
    inputAr = []
    i = 0
    c = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']
    l = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Takes input for each month and stores it in an array
    for i in range(len(l)):
        usrIn = float(input(f"Enter the sales for {l[i]}: "))
        inputAr.append(usrIn)
        i += 1
    
    # Shows the resulting graph to the user
    ax.set_title("Monthly Sales Values")
    ax.pie(inputAr, colors=c, labels=l)
    plt.show()
    return

"""Do not change anything below this line."""
if __name__ == '__main__':
    main()

