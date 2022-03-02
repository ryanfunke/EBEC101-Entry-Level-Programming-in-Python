"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 02/28/2022

Description:
    This program asks the user for input of grades up to a quantity of 5, shows their letter grade for each value and then returns the average grade and average letter to the user. 

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
# Determines if the input from the user is a legitimate grade 
def get_valid_score():
    
    result = -1.0
    while result < 0.0:
        score = float(input("Enter a score: "))
        if ((score <= 100.0) and (score >= 0.0)):
            result = score
        else:
            print("  Invalid Input. Please try again.")    
    return score

# Calculates the average score of the 5 entries from the user
def calc_average(scores):
    sum = 0.0
    len = 0.0
    for x in scores:
        sum += x
        len += 1.0
    return (sum/len)
# Determines the letter grade of the score input by the user 
def determine_grade(score):
    grade = ""
    if score >= 92.0 and score <= 100.0:
        grade = "A"
    elif score >= 82.0 and score < 92.0:
        grade = "B"
    elif score >= 73.0 and score < 82.0:
        grade = "C"
    elif score >= 64.0 and score < 73.0:
        grade = "D"
    else:
        grade = "F"
    
    return grade

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Variable initialization
    scores = []
    counter = 0

    # Asks the user for input and determines validity
    while counter < 5:
        score = get_valid_score()
        scores.append(score)
        print("  The letter grade for {:3.1f} is ".format(score) + determine_grade(score) + ".")
        counter += 1


    # Output of the results
    print("\nResults:")
    print("  The average score is {:4.2f}.".format(calc_average(scores)))
    print("  The letter grade for {:4.2f} is ".format(calc_average(scores)) + determine_grade(calc_average(scores)) + ".")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
