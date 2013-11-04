"""
https://www.codeeval.com/browse/18/

Multiples of a Number

Challenge Description:

    Given numbers x and n, where n is a power of 2, print out the smallest
    multiple of n which is greater than or equal to x.
    Do not use division or modulo operator.


Input Sample:

    The first argument will be a text file containing a comma separated list
    of two integers, one list per line. E.g.

    13,8
    17,16


Output Sample:

    Print to stdout, the smallest multiple of n which is greater than
    or equal to x, one per line. E.g.

    16
    32

"""

import sys

input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_data = input_file.read()

def main():
    for line in input_data.split('\n'):
        if line != '':
            x, n = map(int, line.split(','))

            print multiple_ge_size(x, n)

def multiple_ge_size(x, n):
    i = 1

    while True:
        multiple = n * i
        if multiple >= x:
            return multiple
        i += 1


if __name__ == '__main__':
    main()