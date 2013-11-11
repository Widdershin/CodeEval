"""
https://www.codeeval.com/browse/93/

Capitalize Words

Challenge Description:

    Write a program which capitalizes words in a sentence.


Input Sample:

    Your program should accept as its first argument a path to a filename. Input example is the following

    Hello world
    javaScript language
    a letter


Output Sample:

    Print capitalized words in the following way.

    Hello World
    JavaScript Language
    A Letter

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "026-capitalizewords-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        words = line.split(' ')
        print " ".join(map(lambda x: x[0].capitalize() + x[1:], words))

if __name__ == '__main__':
    main()
