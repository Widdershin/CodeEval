"""
https://www.codeeval.com/browse/87/

Query Board

Challenge Description:

    There is a board (matrix). Every cell of the board contains one integer,
    which is 0 initially.
    

    The next operations can be applied to the Query Board:
    
SetRow i x: it means that all values in the cells on row "i" have been changed to value "x" after this operation.
    
SetCol j x: it means that all values in the cells on column "j" have been changed to value "x" after this operation.
    
QueryRow i: it means that you should output the sum of values
    on row "i".
    
QueryCol j: it means that you should output the sum of values on column "j".
    

    The board's dimensions are 256x256
    
    "i" and "j" are integers from 0 to 255
    
    "x" is an integer from 0 to 31
    


Input Sample:

    Your program should accept as its first argument a path to a filename.
    Each line in this file contains an operation of a query. E.g.

    SetCol 32 20
    SetRow 15 7
    SetRow 16 31
    QueryCol 32
    SetCol 2 14
    QueryRow 10
    SetCol 14 0
    QueryRow 15
    SetRow 10 1
    QueryCol 2


Output Sample:

    For each query, output the answer of the query. E.g.

    5118
    34
    1792
    3571

"""

###### IO Boilerplate ######
import sys

if len(sys.argv) < 2:
    input_file_name = "23-queryboard-in.txt"
else:
    input_file_name = sys.argv[1]

with open(input_file_name) as input_file:
    input_lines = map(lambda x: x.strip(), filter(lambda x: x != '', input_file.readlines()))

###### /IO Boilerplate ######

BOARD_SIZE = 256

class Board(object):

    def __init__(self, board_size):
        self.size = board_size
        self.data = [[0 for i in range(board_size)] for j in range(board_size)]
        self.commands = {'SetCol': self.set_column, 'SetRow': self.set_row, 'QueryCol': self.query_column, 'QueryRow': self.query_row}

    def print_board(self):
        for row in self.data:
            print " ".join(map(str, row))

    def set_column(self, column, new_value):
        for row in self.data:
            row[column] = new_value

    def set_row(self, row, new_value):
        self.data[row] = [new_value for i in range(self.size)]

    def query_column(self, column):
        print sum(zip(*self.data)[column])

    def query_row(self, row):
        print sum(self.data[row])


class Command(object):
    def __init__(self, board, command_string):
        super(Command, self).__init__()
        self.board = board
        self.command_string = command_string
        self.process_command(self.command_string)

    def process_command(self, command_string):
        parts = command_string.split(' ')

        self.func = self.board.commands[parts.pop(0)]
        self.args = map(int, parts)

    def __call__(self):
        self.func(*self.args)


def main():
    board = Board(BOARD_SIZE)

    for line in input_lines:
        command = Command(board, line)
        command()

if __name__ == '__main__':
    main()
