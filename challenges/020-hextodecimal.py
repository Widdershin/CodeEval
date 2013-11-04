"""
https://www.codeeval.com/browse/67/

Hex to Decimal

Challenge Description:

    You will be given a hexadecimal (base 16) number.
    Convert it into decimal (base 10).


Input Sample:

    Your program should accept as its first argument a path to a filename.
    Each line in this file contains a hex number. You may assume that
    the hex number does not have the leading 'Ox'. Also all alpha
    characters (a through f) in the input will be in lowercase.
    E.g.

    9f
    11


Output Sample:

    Print out the equivalent decimal number. E.g.

    159
    17

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "20-hextodecimal-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        print int(line, 16)


if __name__ == '__main__':
    main()
