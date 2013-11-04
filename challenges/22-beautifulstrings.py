"""
https://www.codeeval.com/browse/83/

Beautiful Strings

Challenge Description:

    Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon.
    

    When John was a little kid he didn't have much to do. There was no
    internet, no Facebook, and no programs to hack on. So he did the only
    thing he could... he evaluated the beauty of strings in a quest to
    discover the most beautiful string in the world.
    

    Given a string s, little Johnny defined the beauty of the string as the
    sum of the beauty of the letters in it. The beauty of each letter is an
    integer between 1 and 26, inclusive, and no two letters have the
    same beauty. Johnny doesn't care about whether letters are uppercase
    or lowercase, so that doesn't affect the beauty of a letter.
    (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)
    

    You're a student writing a report on the youth of this famous hacker.
    You found the string that Johnny considered most beautiful. What is the
    maximum possible beauty of this string?


Input Sample:

    Your program should accept as its first argument a path to a filename.
    Each line in this file has a sentence. E.g.

    ABbCcc
    Good luck in the Facebook Hacker Cup this year!
    Ignore punctuation, please :)
    Sometimes test cases are hard to make up.
    So I just go consult Professor Dalves


Output Sample:

    Print out the maximum beauty for the string. E.g.

    152
    754
    491
    729
    646

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "22-beautifulstrings-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######

import re
from collections import Counter

BEAUTY_REGEX = r'[^a-z]'

def main():
    for line in input_lines:
        print beauty(line)

def beauty(string):
    string = re.sub(BEAUTY_REGEX, '', string.lower())
    c = Counter(string)

    return sum((26 - i) * string.count(char) for i, (char, n) in enumerate(c.most_common()))

if __name__ == '__main__':
    main()
