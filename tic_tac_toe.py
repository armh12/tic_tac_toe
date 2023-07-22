from copy import deepcopy
import numpy as np
from tkinter import *
from tabulate import tabulate

class TicTacToe:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.gameboard = [['-' for _ in range(0,3)] for _ in range(0,3)]
        
    def get_open_slots(self):
        open_slots = []
        for i,row in enumerate(self.gameboard):
            for j,elem in enumerate(row):
                if elem == '-':
                    open_slots.append((i,j))
        return open_slots
    
    def make_move(self,step_row,step_column,step):
        if step % 2 != 0:
            pic = 'X'
        else:
            pic = 'O'
        
        for i,row in enumerate(self.gameboard):
            for j in range(len(row)):
                if step_row == i and step_column == j:
                    self.gameboard[i][j] = self.gameboard[i][j].replace('-',pic)
        return self.gameboard
    
    winner = True
    
    def check_for_winner(self):
        copied_gameboard = deepcopy(self.gameboard)
        transposed_gameboard = np.transpose(copied_gameboard)
        gameboard_2 = []
        for row in transposed_gameboard:
            row = list(row)
            gameboard_2.append(row)
        
        for row in self.gameboard:
            if row.count('X') == 3:
                print('Player 1 wins')
                self.winner = False
                break
            elif row.count('O') == 3:
                print('Player 2 win')
                self.winner = False
                break 
            
        for row in gameboard_2:
            if row.count('X') == 3:
                print('Player 1 wins')
                self.winner = False
                break
            elif row.count('O') == 3:
                print('Player 2 win')
                self.winner = False
                break
        
        if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] == 'X':
            print('Player 1 wins')
            self.winner = False
        elif self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] == 'O':
            print('Player 2 wins')
            self.winner = False
        elif self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0] == 'X':
            print('Player 1 wins')
            self.winner = False
        elif self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0] == 'O':
            print('Player 2 wins')
            self.winner = False

def print_board():
    game = TicTacToe(2)
    step = 1

    while game.winner:
        open_slots = game.get_open_slots()
        print(open_slots)
        
        if step % 2 != 0:
            print('Players 1 turn')
        else:
            print('Players 2 turn')
        
        row = int(input('Input row: '))
        column = int(input('Input column: '))
        if (row,column) not in open_slots:
            print('Invalid move')
            continue
        game_display = game.make_move(row,column,step)
        step += 1
        
        print(tabulate(game_display,tablefmt='grid'))
        
        game.check_for_winner()
        if open_slots is None:
            game.winner = False
    
    print('Game Over')
    repeat = input('Do you want to play again?(Y-again, any key to quit): ')
    if repeat == 'Y':
        return print_board()
    else:
        print('Thank you!')
        
print_board()
