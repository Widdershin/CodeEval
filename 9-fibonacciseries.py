"""
https://www.codeeval.com/browse/22/

Fibonacci Series

Challenge Description:

    The Fibonacci series is defined as: F(0) = 0; F(1) = 1;
    F(n) = F(n-1) + F(n-2) when n>1. Given a positive integer 'n',
    print out the F(n).


Input Sample:

    The first argument will be a text file containing a positive integer,
    one per line. E.g.

    5
    12


Output Sample:

    Print to stdout, the fibonacci number, F(n). E.g.

    5
    144

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "9-fibonacciseries-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### IO Boilerplate ######

def main():
    
    for line in input_lines:
        print fibonnaci(int(line))

def fibonnaci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonnaci(n - 1) + fibonnaci(n - 2)

if __name__ == '__main__':
    main()
