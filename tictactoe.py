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

    return player1,player2

def display_board(board):
    '''
    DESCRIPTION: Tic Toe board graphics
    :parameter: list
    '''
    i = range(1, 10)
    for index in i:
        if index % 3 != 0:
            print(' {} |'.format(board[index]), end='')
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
    wincounter = 0
    win = False
    for elements in board:
        if elements == marker:
            wincounter += 1
            if wincounter == 3:
                win = True
                break
        else:
            wincounter = 0

    if win:
        return win

    for elements in board[1:10:3]:
        if elements == marker:
            win = True
        else:
            win = False
            break
    if win:
        return win

    for elements in board[2:10:3]:
        if elements == marker:
            win = True
        else:
            win = False
            break

    if win:
        return win

    for elements in board[3:10:3]:
        if elements == marker:
            win = True
        else:
            win = False

    if win:
        return win

    for elements in board[3:9:2]:
        if elements == marker:
            win = True
        else:
            win = False
    if win:
        return win

    for elements in board[1:10:3]:
        if elements == marker:
            win = True
        else:
            win = False
    return False


import random


def choose_first():
    '''
    DESCRIPTION: Asigns first turn randomly
    '''
    if random.randint(1, 2) == 1:
        return 1
    else:
        return 2

def space_check(board, position):
    '''

    DESCRIPTION: Indicate if position is empty
    '''

    if position == 'X' or position == 'O':
        return False
    else:
        return True

def full_board_check(board):
    '''
    DESCRIPTION: Checks if board is full
    :param board:
    :return TRUE if board is full
    '''

    for position in board:
        if position == 'X' or 'O':
            continue
        else:
            return False
    return True

def player_choice(board):
    '''
    :DESCRIPTION: Indicates if there's a free spot selected by the player
    :param board:
    :return: Bool for available slot
    '''
    position = int(input("Please enter the position: ")
    if space_check(board, position):
        return position
    else:
        print("Occupied!")
        return False

def replay():
    '''
    DESCRIPTION: Returns True if player wants to play again
    :return: Bool
    '''

    choice = str(input("Do you want to play again? Y/N"))
    if choice == 'Y':
        return True
    else:
        return False

##Module import
import time

##Game
print ("========================= TIC TAC TOE =========================")

while True:
    startmenu()
    menu_option = int(input("Select the option: "))
    if menu_option == 1:
        game_on = True
        while game_on:
            #Players input their names and markers
            player1, player2 = player_input()
            #Random first turn selection
            if choose_first() == 1:
                print(f'{player1[0]} goes first')

                time.sleep(5)

                print(chr(27) + "[2J")
                display_board()

                




    else:
        break



