"""
https://www.codeeval.com/browse/24/

Sum of Integers from File

Challenge Description:

    Print out the sum of integers read from a file.


Input Sample:

    The first argument to the program will be a text file containing
    a positive integer, one per line. E.g.

    5
    12


Output Sample:

    Print out the sum of all the integers read from the file. E.g.

    17

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "11-sumofintegersfromfile-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### IO Boilerplate ######

def main():
    print sum(map(int, input_lines))

if __name__ == '__main__':
    main()
