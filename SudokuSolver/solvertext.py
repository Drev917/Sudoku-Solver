# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:38:10 2021

@author: Drewb

The goal of this project is to use Deep Learning and the recursive backtracking algorithm to solve any sudoku puzzle.

"""
#create grid with prefilled digits
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def valid(grid, num, pos):

    #check row
    for i in range (len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range (len(grid[0])):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    #check position in reference
    box_x = pos[1] // 3
    box_y = pos[0] // 3

#draw grid function
def print_board(grid):
    
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
            
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

print_board(board)

#loops through board and finds null value and returns to call
def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j) #returns row, column order
