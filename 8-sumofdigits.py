"""
https://www.codeeval.com/browse/21/

Sum of Digits

Challenge Description:

    Given a positive integer, find the sum of its constituent digits.


Input Sample:

    The first argument will be a text file containing positive integers,
    one per line. E.g.

    23
    496


Output Sample:

    Print to stdout, the sum of the numbers that make up the integer,
    one per line. E.g.

    5
    19

"""

import sys

if len(sys.argv) < 2:
    input_file_name = "8-sumofdigits-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

def main():
    for line in input_lines:
        print sum(map(int, list(line)))

if __name__ == '__main__':
    main()
