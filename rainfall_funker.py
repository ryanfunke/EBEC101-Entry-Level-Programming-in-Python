"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 03.3 - Rainfall
Date: 02/21/2022

Description:
    This progrma asks user to choose a number of years to record rainfall for, and then loops through each month to store rainfall data in a list. Afterwards, it averages and sums the quantities
    entered and outputs these results to the user. 

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
    #Declaring initial variables for data storage
    years = 0 
    counter = 0
    totalRainfall = 0.0
    avgRainfall = 0.0
    totals = []
    #Asks the user for input
    years = int(input("Enter the number of years: "))
    #Validity check for input
    if years < 1: 
        print("Invalid input; years must be greater than 0.")
    else: 
        #Asks the user for input for each month in the year and then outputs results
        while counter < years:
            month = 1
            print("  For year No. {:d}".format(counter + 1))
            while month <= 12:
                rain = -1.0
                monStr = ""
                if month == 1:
                    monStr = "Jan."
                elif month == 2:
                    monStr = "Feb."
                elif month == 3: 
                    monStr = "Mar."
                elif month == 4:
                    monStr = "Apr."
                elif month == 5:
                    monStr = "May."
                elif month == 6:
                    monStr = "Jun."
                elif month == 7:
                    monStr = "Jul."
                elif month == 8:
                    monStr = "Aug."
                elif month == 9:
                    monStr = "Sep."
                elif month == 10:
                    monStr = "Oct."
                elif month == 11:
                    monStr = "Nov."
                else:
                    monStr = "Dec."               
                while (rain < 0.0):
                    rain = float(input("    Enter the rainfall for " + monStr + ": "))

                    if rain < 0.0:
                        print("    Invalid input; rainfall cannot be negative.")
                    else:
                        totals.append(rain)               
                month += 1
            counter += 1           
        for x in totals:
            totalRainfall += x
        avgRainfall = totalRainfall / (years * 12)
        print("There are " + str(int(years * 12)) + " months.")
        print("The total rainfall was {:.2f} inches.".format(totalRainfall))
        print("The monthly average rainfall was {:.2f} inches.".format(avgRainfall))
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()