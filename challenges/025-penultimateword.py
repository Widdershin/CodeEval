"""
https://www.codeeval.com/browse/92/

Penultimate Word

Challenge Description:

    Write a program which finds the next-to-last word in a string.


Input Sample:

    Your program should accept as its first argument a path to a filename. Input example is the following

    some line with text
    another line


Output Sample:

    Each line has more than one word.

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "025-penultimateword-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        print line.split(' ')[-2]


if __name__ == '__main__':
    main()
