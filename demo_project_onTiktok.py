Test_board=['']*10
def display_board(board):
    print(board[7] + '__|__' + board[8]  + '__|__' + board[9])
    print(board[4] + '__|__' + board[5] + '__|__' + board[6])
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])

display_board(Test_board)



def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker= input('Player1, please select "X" or "O":').upper()
    player1=marker

    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)



def mark_pos(board,pos,mark):
    board[pos]= mark


def check_win(board,mark):
    return((board[0]==board[1]==board[2]==mark) or
           (board[3] == board[4] == board[5] == mark) or
           (board[6] == board[7] == board[8] == mark) or
           (board[0] == board[3] == board[6] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[0] == board[4] == board[8] == mark) or
           (board[2] == board[4] == board[6] == mark))

import random

def choose_player():

     turn= random.randint(0,1)
     if turn==1:
         return 'Player1'
     else:
         return 'Player2'

def space_check(board,pos):

    return board[pos]== ''

def full_board(board):

    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def player_choice(board):

    pos= 0

    while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
        pos= int(input('Select any position from 1 to 9: '))
        return pos

def replay():
    select= input('Do you want to play again: Y or N: ').upper()
    return select

#Combine all togetther:

print('Welcome to TIC TAC TOE game')

while True:  # play game coding
##logic: board->player select-> pos for mark
     the_board= ['']*10
     player1_marker, player2_marker = player_input()
     print(f'Player1 has selected {player1_marker}')
     print(f'Player2 should use {player2_marker}')
     turn = choose_player()
     print(turn + ' will go first')
     play_game= input('Ready to Play? Y or N:').upper()
     if play_game=='Y':
         game_on= True
     else:
         game_on= False
     while game_on:
         if turn=='Player1':
             display_board(the_board)
             pos= player_choice(the_board)
             mark_pos(the_board, pos, player1_marker)
             if check_win(the_board,player1_marker):
                 display_board(the_board)
                 print('Player1 has won!')
                 game_on= False
             else:
                 if full_board(the_board):
                     display_board(the_board)
                     print('Its a TIE!')
                     game_on= False
                 else:
                     turn=='Player2'
         else:
             display_board(the_board)
             pos = player_choice(the_board)
             mark_pos(the_board, pos, player2_marker)
             if check_win(the_board, player2_marker):
                 display_board(the_board)
                 print('Player2 has won!')
                 game_on = False
             else:
                 if full_board(the_board):
                     display_board(the_board)
                     print('Its a TIE!')
                     game_on = False
                 else:
                     turn=='Player1'

     if not replay():
         break


