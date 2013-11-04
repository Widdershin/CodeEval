"""
https://www.codeeval.com/browse/29/

Unique Elements

Challenge Description:

    You are given a sorted list of numbers with duplicates.
    Print out the sorted list with duplicates removed.


Input Sample:

    File containing a list of sorted integers, comma delimited, one per line.
    E.g.
    

    1,1,1,2,2,3,3,4,4
    2,3,4,5,5


Output Sample:

    Print out the sorted list with duplicates removed, one per line.
    
    E.g.

    1,2,3,4
    2,3,4,5

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "14-uniqueelements-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######

def main():
    for line in input_lines:
        numbers = line.split(',')
        print ",".join(sorted(set(numbers)))


if __name__ == '__main__':
    main()
