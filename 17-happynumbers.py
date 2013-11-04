"""
https://www.codeeval.com/browse/39/

Happy Numbers

Challenge Description:

    A happy number is defined by the following process. Starting with any
    positive integer, replace the number by the sum of the squares of its
    digits, and repeat the process until the number equals 1 (where it
    will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy numbers, while
    those that do not end in 1 are unhappy numbers.


Input Sample:

    The first argument is the pathname to a file which contains test data,
    one test case per line. Each line contains a positive integer. E.g.

    1
    7
    22


Output Sample:

    If the number is a happy number, print out 1. If not, print out 0. E.g

    1
    1
    0

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "17-happynumbers-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        print int(is_happy(int(line)))

def is_happy(n):

    cycles = 0
    while n != 1:

        if cycles > 1000:
            return False
        
        n = sum(map(lambda x: x ** 2, map(int, str(n))))

        cycles += 1
    return True


if __name__ == '__main__':
    main()
