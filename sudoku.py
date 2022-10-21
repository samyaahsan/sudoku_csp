#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""
import sys

ROW = "ABCDEFGHI"
COL = "123456789"



def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

#backtracking with forward checking
def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    solved_board = backtrack(board)
    return solved_board

def backtrack(board):
    if complete(board):
        #no zeroes in board
        return board
    var = select_unassigned_variable(board)
    for value in range(1,10):
    #for value in (1,10) [or can do] for value in var domain
        if consistent(value, board, var, csp):
            board[var] = value
            infer = forward_checking(board, infer, board, var, value)
            if infer != None:
                #TODO: add inferences to assignment here
                added = backtrack(board, csp)
                if added != None:
                    return added





# def combine(ROW, COLUMN):
#     domain_map = {}
#
#     for i in ROW:
#         for j in COL:
#             domain_map[i + j] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def consistent(value, assignment, var, board):
    return all(assignment[var] != value for constraint in csp[var])
#isSafe

def forward_checking(board):


def select_unassigned_variable(board):
    #minimum remaining variable -- pick the one with least num of options
    mrv_size = sys.maxsize
    mrv = None
    for r in ROW:
        for c in COL:
            tile = str(r) + str(c)
            if board[tile] == 0:
                chosen = is_possible(board, tile)
                #get smaller domain
                if mrv_size > len(chosen):
                    mrv = tile
                    mrv_size = len(chosen)
    return mrv


def is_possible(board, tile):
    possibilities =


def complete(board):
    # no zeroes in board
    for r in ROW:
        for c in COL:
            if board[str(r) + str[c]] == 0:
                return False
    return True







if __name__ == '__main__':
    if len(sys.argv) > 1:
        
        # Running sudoku solver with one board $python3 sudoku.py <input_string>.
        print(sys.argv[1])
        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(sys.argv[1][9*r+c])
                  for r in range(9) for c in range(9)}       
        
        solved_board = backtracking(board)
        
        # Write board to file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    else:
        # Running sudoku solver for boards in sudokus_start.txt $python3 sudoku.py

        #  Read boards from source.
        src_filename = 'sudokus_start.txt'
        try:
            srcfile = open(src_filename, "r")
            sudoku_list = srcfile.read()
        except:
            print("Error reading the sudoku file %s" % src_filename)
            exit()

        # Setup output file
        out_filename = 'output.txt'
        outfile = open(out_filename, "w")

        # Solve each board using backtracking
        for line in sudoku_list.split("\n"):

            if len(line) < 9:
                continue

            # Parse boards to dict representation, scanning board L to R, Up to Down
            board = { ROW[r] + COL[c]: int(line[9*r+c])
                      for r in range(9) for c in range(9)}

            # Print starting board. TODO: Comment this out when timing runs.
            print_board(board)

            # Solve with backtracking
            solved_board = backtracking(board)

            # Print solved board. TODO: Comment this out when timing runs.
            print_board(solved_board)

            # Write board to file
            outfile.write(board_to_string(solved_board))
            outfile.write('\n')

        print("Finishing all boards in file.")