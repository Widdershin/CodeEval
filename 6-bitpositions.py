"""
https://www.codeeval.com/browse/19/

Bit Positions

Challenge Description:

    Given a number n and two integers p1,p2 determine if the bits in
    position p1 and p2 are the same or not. Positions p1 and p2 and 1 based.


Input Sample:

    The first argument will be a text file containing a comma separated list
    of 3 integers, one list per line. E.g.

    86,2,3
    125,1,2


Output Sample:

    Print to stdout, 'true'(lowercase) if the bits are the same,
    else 'false'(lowercase). E.g.

    true
    false

"""

import sys

if len(sys.argv) < 2:
    input_file_name = "6-bitpositions-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
	input_data = input_file.read().strip()


def main():

    for line in input_data.split('\n'):
        n, pos1, pos2 = map(int, line.split(','))

        binary = bin(n)

        print str(binary[-pos1] == binary[-pos2])

if __name__ == '__main__':
    main()