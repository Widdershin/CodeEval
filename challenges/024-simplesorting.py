"""
https://www.codeeval.com/browse/91/

Simple Sorting

Challenge Description:

    Write a program which sorts numbers.


Input Sample:

    Your program should accept as its first argument a path to a filename. Input example is the following

    70.920 -38.797 14.354 99.323 90.374 7.581
    -37.507 -3.263 40.079 27.999 65.213 -55.552


Output Sample:

    Print sorted numbers in the following way.

    -38.797 7.581 14.354 70.920 90.374 99.323
    -55.552 -37.507 -3.263 27.999 40.079 65.213

    -38.797 7.581 14.354 70.92 90.374 99.323
    -55.552 -37.507 -3.263 27.999 40.079 65.213

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "024-simplesorting-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        numbers = map(float, line.split(' '))
        print " ".join(map(lambda x: "{:.3f}".format(x), sorted(numbers)))


if __name__ == '__main__':
    main()
