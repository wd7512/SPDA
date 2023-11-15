#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:09:08 2022

@author: ej20262
"""
from TicTacToe import Board, Player

print('Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.')
#create an instance of the board
TTTboard= Board()
TTTboard.create_board()
#printout the initail form of the board 
TTTboard.print_board()

#users can choose symbols to play with 
p1_letter= input("player 1 letter (default x): ") 
#if empty give a default x
if(p1_letter.strip()==""):p1_letter='x'

#if empty give a default o
p2_letter= input("player 2 letter (default o): ") 
if(p2_letter.strip()==""):p2_letter='o'
    
# Create instances of players and initailaise it with a symbol
player1= Player(p1_letter)
player2= Player(p2_letter)

#outer loop for offering to play again
while(True):
    TTTboard.create_board()
    #printout the initail form of the board 
    TTTboard.print_board()
    #untill we have a winner or board is full, in case of winner the loop will break
    winner= False
    while not(TTTboard.isBoardFull()):
        #player 1 starts
        pos= input("Player 1 move:" )
    
        #try again if the move is invalid
        while not player1.make_move(pos,TTTboard):
            pos= input("Player 1 move :")
        
        #when successful print the board
        TTTboard.print_board()
        
        #Check if there is a wiinner
        if(TTTboard.check_winner(player1.getletter())):
            print("Player 1 won")
            player1.increment_score()
            winner= True
            break
        #player 2 turn
        pos= input("Player 2 move :")
        
        #Try untill a valid move
        while not player2.make_move(pos,TTTboard):
            pos= input("Player 2 move :")
        #print the board and check for winner
        TTTboard.print_board()
        if(TTTboard.check_winner(player2.getletter())):
            print("Player 2 won")
            player2.increment_score()
            winner= True
            break
    #after getting out of the loop, if winner is false for both players, then it is a tie
    if (not winner):print('Game is a tie! No more spaces left to move.')
    
    #display score:
    print("current score: player 1("+ player1.getletter()+"):", player1.getscore()," player 2("+ player2.getletter()+"):", player2.getscore())
    
    #offering to play again
    response = input("play again? (y/n): ")
    if not response.lower() in['y', 'yes']:
        break
        
