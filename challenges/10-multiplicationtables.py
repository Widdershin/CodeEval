"""
https://www.codeeval.com/browse/23/

Multiplication Tables

Challenge Description:

    Print out the grade school multiplication table upto 12*12.


Input Sample:

    There is no input for this program.


Output Sample:

    Print out the table in a matrix like fashion, each number formatted
    to a width of 4 (The numbers are right-aligned and strip out
    leading/trailing spaces on each line). The first 3 line will look like:

    
    1   2   3   4   5   6   7   8   9  10  11  12
    2   4   6   8  10  12  14  16  18  20  22  24
    3   6   9  12  15  18  21  24  27  30  33  36
    

"""

def main():
    print_times_tables(12)
    
def print_times_tables(n):
    for row in range(1, n + 1):
        row_output = ""
        for cell in range(1, n + 1):
            cell_string = "{:>4}"

            row_output += cell_string.format(row * cell)

        print row_output.lstrip()

if __name__ == '__main__':
    main()
