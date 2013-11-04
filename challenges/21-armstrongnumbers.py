"""
https://www.codeeval.com/browse/82/

Armstrong Numbers

Challenge Description:

    An Armstrong number is an n-digit number that is equal to the sum of
    the n'th powers of its digits. Determine if the input numbers
    are Armstrong numbers.


Input Sample:

    Your program should accept as its first argument a path to a filename.
    Each line in this file has a positive integer. E.g.

    6
    153
    351


Output Sample:

    Print out True/False if the number is an Armstrong number or not. E.g.

    True
    True
    False

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "21-armstrongnumbers-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        number = int(line)

        print is_armstrong(number)

def is_armstrong(n):
    return n == sum(int(x) ** len(str(n)) for x in str(n))

if __name__ == '__main__':
    main()
