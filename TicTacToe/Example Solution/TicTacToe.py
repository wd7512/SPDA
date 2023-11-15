#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:51:45 2022

@author: ej20262
"""

class Board:
    def __init__(self):
        """initalise the board with empty array"""
        self.board = []
        
    def create_board(self):
        """Rcreate the board with empty strings, to begin or restart the game instead of creating a new instance"""
        self.board = [' ' for x in range(10)]
    
    def print_board(self):
        """ to enable prining the board at any time"""
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
    
    def check_winner(self, le):
        """ This is the main action function, it takes a symbol of either players and check if they win"""
        #list of lists defining the winnning scenarios
        runs = [
            # horizontal
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            # vertical
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            # diagonal
            [1, 5, 9],
            [3, 5, 7]
        ]
        #unpacking the list 
        for a, b, c in runs:
            if self.board[a] == self.board[b] == self.board[c] == le:
                return True
        return False
        
   
    def isBoardFull(self):
        """Return true if the board is full, false if not"""
        if self.board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
               return False
        return True
       
class Player:
    """ class manages players info and saves score"""
    def __init__(self, letter):
        """ initailiser takes the letter and zero score """
        self.letter=letter
        self.score=0
    
    def make_move(self, pos, b):
        """ Try to move the player to a specific position 
        given theh current baord, if the position occupied or not valid it returns false"""
        try:
            #if not int, except
            pos= int(pos)
            #if the cell is empty
            if (b.board[pos]==' '):
                b.board[pos]=self.letter
                return True
            else: 
                print ("Already occupied, try again")
                return False
        except: 
            print("\nThis is not a valid position, please try again.")
            return False

    def getletter(self):
        """getter for letter, for display"""
        return self.letter
    def getscore(self):
        """ getter for the score"""
        return self.score
        
    
    def increment_score(self):
        """updating the score for this player"""
        self.score+=1
    
        
        
