"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 09.3 - Course Info
Date: 04/11/2022

Description:
    This program creates a nested dicationary to describe details about classes, and then asks the user to provide input to see which class details they 
    would like to have returned. 

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
def get_course_data():
    #This function takes the input from the file
    course = { 'CS101' : {'room': '3004', 'instructor': 'Django', 'time': '9:00 a.m.'},
               'CS102' : {'room': '4501', 'instructor': 'Idle', 'time': '10:00 a.m.'},
               'CS103' : {'room': '6755', 'instructor': 'Rich', 'time': '11:00 a.m.'},
               'NT110' : {'room': '1244', 'instructor': 'Marshal', 'time': '12:00 p.m.'},
               'CM241' : {'room': '1411', 'instructor': 'Pickle', 'time': '2:00 p.m.'}} 
    #Returns the dictionary
    return(course)

def main():
    """Write your mainline logic below this line (then delete this line)."""
    course = get_course_data()
    #Gathers user input
    s = input("Enter a course number: ")
    #Returns the output of the year that a user selected 
    if course.get(s) != None:
        details = course.get(s)
        userRoom = details["room"]
        userInstr = details["instructor"]
        userTime = details["time"]
        print("  The details for course {:s} are:".format(s))
        print("    Instructor: {:s}".format(userInstr))
        print("          Room: {:s}".format(userRoom))
        print("          Time: {:s}".format(userTime))
    else:
        print("  {:s} is an invalid course number.".format(s))

"""Do not change anything below this line."""
if __name__ == '__main__':
    main()

