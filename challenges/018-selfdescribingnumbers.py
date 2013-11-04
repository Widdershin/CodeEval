"""
https://www.codeeval.com/browse/40/

Self Describing Numbers

Challenge Description:

    A number is a self-describing number when (assuming digit positions
    are labeled 0 to N-1), the digit in each position is equal to the
    number of times that that indice appears in the number.


Input Sample:

    The first argument is the pathname to a file which contains test data,
    one test case per line. Each line contains a positive integer.
    E.g.

    
    2020
    22
    1210


Output Sample:

    If the number is a self-describing number, print out 1. If not, print
    out 0. E.g.

    1
    0
    1

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "18-selfdescribingnumbers-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######

from collections import Counter

def main():
    for line in input_lines:
        print int(is_self_describing(line))
        

def is_self_describing(n):
    c = Counter(str(n))
    
    return all([int(char) == c[str(i)] for i, char in enumerate(str(n))])


if __name__ == '__main__':
    main()
