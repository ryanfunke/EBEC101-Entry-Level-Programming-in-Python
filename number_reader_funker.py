"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 08.5 - Number Reader
Date: 04/04/22

Description:
    This program builds upon the number_writer program and reads the lines of input. It then calculates 
    statistics about the numbers within the file such as max, min, avg, etc.
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
    # Initializes stats about the file
    num = 0
    min = 0
    max = 0
    avg = 0
    sum = 0
    # Reads file input line by line
    file = 'random_numbers.txt'
    with open(file) as f:
        lines = f.readlines()
    f.close()
    # Calculates file statistics and then outputs it to the user
    for x in lines:
        sum += int(x)
        if num == 0:
            min = int(x)
        if int(x) < min:
            min = int(x)
        if int(x) > max:
            max = int(x)
        num += 1
    avg = sum / num
    # Outputs results to the user
    print("{:,d} numbers were read from the file.".format(num))
    print("Min: {:,d}".format(min))
    print("Max: {:,d}".format(max))
    print("Sum: {:,d}".format(sum))
    print("Avg: {:,.1f}".format(avg))
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()