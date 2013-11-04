"""
https://www.codeeval.com/browse/20/

Lowercase

Challenge Description:

    Given a string write a program to convert it into lowercase.


Input Sample:

    The first argument will be a text file containing sentences, one per line.
    You can assume all characters are from the english language. E.g.

    HELLO CODEEVAL
    This is some text


Output Sample:

    Print to stdout, the lowercase version of the sentence,
    each on a new line. E.g.

    hello codeeval
    this is some text

"""

import sys

if len(sys.argv) < 2:
    input_file_name = "7-lowercase-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_data = input_file.read()

def main():
    for line in input_data.split('\n'):
        print line.lower()

if __name__ == '__main__':
    main()
