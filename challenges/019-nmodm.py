"""
https://www.codeeval.com/browse/62/

N Mod M

Challenge Description:

    Given two integers N and M, calculate N Mod M
    (without using any inbuilt modulus operator).


Input Sample:

    Your program should accept as its first argument a path to a filename.
    Each line in this file contains two comma separated positive integers.
    E.g.

    20,6
    2,3


Output Sample:

    You may assume M will never be zero.

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "19-nmodm-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######

import math


def main():
    for line in input_lines:
        number, mod = map(int, line.split(','))

        print modulus(number, mod)

def modulus(number, mod):
    return number - ((number / mod) * mod)

if __name__ == '__main__':
    main()
