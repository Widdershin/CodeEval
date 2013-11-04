"""
https://www.codeeval.com/browse/31/

Rightmost Char

Challenge Description:

    You are given a string 'S' and a character 't'. Print out the position of
    the rightmost occurrence of 't' (case matters) in 'S' or -1 if there is
    none. The position to be printed out is zero based.


Input Sample:

    The first argument is a file, containing a string and a character, comma
    delimited, one per line. Ignore all empty lines in the input file. E.g.
    

    Hello World,r
    Hello CodeEval,E


Output Sample:

    Print out the zero based position of the character 't' in string 'S',
    one per line. Do NOT print out empty lines between your output.
    
    E.g.

    8
    10

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "16-rightmostchar-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        string, char = line.split(',')
        print string.rfind(char)


if __name__ == '__main__':
    main()
