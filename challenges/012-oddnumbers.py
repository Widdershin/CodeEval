"""
https://www.codeeval.com/browse/25/

Odd Numbers

Challenge Description:

    Print the odd numbers from 1 to 99.


Input Sample:

    There is no input for this program.


Output Sample:

    Print the odd numbers from 1 to 99, one number per line.
    

"""

def main():
    numbers = [x for x in range(1, 100) if x % 2 != 0]
    for number in numbers:
        print number

if __name__ == '__main__':
    main()
