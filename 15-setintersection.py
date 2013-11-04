"""
https://www.codeeval.com/browse/30/

Set Intersection

Challenge Description:

    You are given two sorted list of numbers (ascending order). The lists
    themselves are comma delimited and the two lists are semicolon
    delimited. Print out the intersection of these two sets.


Input Sample:

    File containing two lists of ascending order sorted integers, comma
    delimited, one per line. E.g.
    

    1,2,3,4;4,5,6
    20,21,22;45,46,47
    7,8,9;8,9,10,11,12


Output Sample:

    Print out the ascending order sorted intersection of the two lists,
    one per line. Print empty new line in case the lists have
    no intersection. E.g.
    

    4
    
    8,9

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "15-setintersection-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######


def main():
    for line in input_lines:
        string_sets = line.split(';')
        sets = [set(string_set.split(',')) for string_set in string_sets]

        intersection = sorted(sets[0].intersection(sets[1]))
        print ",".join(intersection)



if __name__ == '__main__':
    main()
