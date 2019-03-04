# -*- coding: utf-8 -*-
"""

TIC TOC GAME

Created on Sat Feb 16 03:04:38 2019

@author: Mathias Salva
"""

def startmenu():
    '''
    SHOW MENU
    '''
    print("{0:^40}".format("TIC TAC TOE"))
    print("1. Play")
    print("0. Quit")

def player_input():
    '''
    DESCRIPTION: Names and launch
    '''
    player1 = list([input('Player 1: '), input('Select Marker (X or O): ')])
    if player1[1] != 'O' and player1[1] != 'X':
        while player1[1] != 'O' and player1[1] != 'X':
            player1[1] = input('Please, select a valid marker: ')
            if player1[1] == 'O':
                player2 = list([input('Player 2: '), 'X'])
            else:
                player2 = list([input('Player 2: '), 'O'])
    elif player1[1] == 'O':
        player2 = list([input('Player 2: '), 'X'])
    else:
        player2 = list([input('Player 2: '), 'O'])
        
def display_board(board):
    '''
    DESCRIPTION: Tic Toe board graphics
    '''
    display_board = ['#',1,2,3,4,5,6,7,8,9]
    i = range(1,10)
    for index in i:
        if index % 3 != 0:
            print(' {} |'.format(board[index]), end = '')
        else:
            print(' {} \n'.format(board[index]))
    
def place_marker(board, marker, position):
    '''
    DESCRIPTION: Function to place a marker
    '''
    ##print("{}'s Turn, please select a position: ".format(player)
    board[position] = marker
    
def win_check(board, marker):
    '''
    DESCRIPTION: Checks for a winner
    '''
    won_counter = 0
    for upper_markers in board:
        if won_counter < 3:    
            if board[upper_markers] == marker:
                won_counter += 1
            else won_counter = 0
        else  return "Winner!"
    
    for vertical in board:
        if board
    
    
    if board[1] == marker:
        if board[5] == marker:
            if board[9] == marker:
                return "Winner!"
    if board[3] == marker:
        if board[5] == marker:
            if board[7] == marker:
                return "Winner!"
    
                
    


startmenu()

if eval(input('Select an option: ') = 1:
    launch game
elif eval(input('Select an option: ')) = 0:
    quitgame

