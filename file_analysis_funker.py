"""
Author: Ryan Funke, funker@purdue.edu
Assignment: 09.4 - File Analysis
Date: 04/11/2022

Description:
    This program takes input from two files, which are then processed into dictionaries. The words are converted to lower case and all leading or trailing punctuation is removed.
    The results of the processing of the words within the files are output to four files, two dedicated towards word frequency, one towards common words, and another towards unique but not common words.

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
import string
"""Write new functions below this line (starting with unit 4)."""
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Opens the file and reads the contents
    file = open("python_1.txt", 'r')
    file1 = file.read()
    file.close()
    words = file1.lower()
    words = words.split()
    uniqueWords = []
    freqFirst = {}
    # Stripping the words of any punctuation and checking for uniqueness in the first file
    for x in words:
        x = x.strip(string.punctuation)
        if x not in uniqueWords:
            uniqueWords.append(x)
        if freqFirst.get(x) == None:
            freqFirst[x] = 1
        else:
            freqFirst[x] += 1
    freqFirst = sorted(freqFirst.items())
    # Opens the second file and reads the contents
    file = open("python_2.txt", 'r')
    file2 = file.read()
    file.close()
    words2 = file2.lower()
    words2 = words2.split()
    uniqueWords2 = []
    freqSec = {}
    # Stripping the words of any punctuation and checking for uniqueness in the second file
    for x in words2:
        x = x.strip(string.punctuation)
        if x not in uniqueWords2:
            uniqueWords2.append(x)
        if freqSec.get(x) == None:
            freqSec[x] = 1
        else:
            freqSec[x] += 1
    freqSec = sorted(freqSec.items())
    # Creates the common words set and either but not both words set
    uSet = set(uniqueWords)
    uSet2 = set(uniqueWords2)
    commonWords = sorted(set(uSet.intersection(uSet2)))
    eitherNot = sorted(set(uSet ^ uSet2))
    f = open("python_1_word_frequency.txt", "w")
    for x in freqFirst:
        f.write(x[0] + ": " + str(x[1]) + "\n")
    f.close()
    f = open("python_2_word_frequency.txt", "w")
    for x in freqSec:
        f.write(x[0] + ": " + str(x[1]) + "\n")
    f.close()
    f = open("common_words.txt", "w")
    for x in commonWords:
        f.write("{:s}\n".format(x))
    f.close()
    f = open("eitherbutnotboth.txt", "w")
    for x in eitherNot:
        f.write("{:s}\n".format(x))
    f.close()
"""Do not change anything below this line."""
if __name__ == '__main__':
    main()

