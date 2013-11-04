"""
https://www.codeeval.com/browse/26/

File Size

Challenge Description:

    Print the size of a file in bytes.


Input Sample:

    The first argument to your program has the path to the file you need to check the size of.


Output Sample:

    Print the size of the file in bytes.
e.g.

    55

"""

import sys
import os

def main():
    file_name = sys.argv[1]
    print os.path.getsize(file_name)

if __name__ == '__main__':
    main()
