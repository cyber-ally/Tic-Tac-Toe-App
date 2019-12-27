import sys 
import random

def display_board(testBoard):

    print(testBoard[7]+' | '+ testBoard[9]+' | '+ testBoard[6]+"\n---------")
    print(testBoard[2]+' | '+ testBoard[5]+' | '+ testBoard[4]+"\n---------")
    print(testBoard[3]+' | '+ testBoard[8]+' | '+ testBoard[1]+"\n---------")

def winCheck(testBoard, mark):
    return ( mark == testBoard[9] == testBoard[5] == testBoard[8] ) or (mark == testBoard[7] == testBoard[2] == testBoard[3]) or (mark == testBoard[6] == testBoard[4] == testBoard[1]) or(mark == testBoard[7] == testBoard[9] == testBoard[6]) or (mark == testBoard[2] == testBoard[5] == testBoard[4]) or (mark == testBoard[3] == testBoard[8] == testBoard[1]) or(mark == testBoard[7] == testBoard[5] == testBoard[1]) or (mark == testBoard[6] == testBoard[5] == testBoard[3])

def place_marker(testBoard, marker, position):
    testBoard[position] = marker

def coin_toss():    
    coin = ['player1','player2']
    return random.choice(coin)

def space_check(testBoard,pos):
    return testBoard[pos] != 'x' and testBoard[pos] != 'o'

def full_board_check(testBoard):
    for i in range(1,10):
        if space_check(testBoard,i):
            return False
    return True

def player_input():

    player1 = input("Player1 Choose your mark: (x/o) ")
    player2 = input("Player2 Choose your mark: (x/o) ")
    
    return [player1,player2]

def player_choice(testBoard,turn):

    pos = 0

    while pos not in range(1,10):
        print(turn)
        pos = int(input(": Choose your position: "))

    return pos

def replay():

    choice = input("Do you want to play again? (yes/no) ")
    return choice == 'yes'

def player1_turn(tb,mark,pos):
    place_marker(tb,mark,pos)

def player2_turn(tb,mark,pos):

    place_marker(tb,mark,pos)

print("Welcome to Tic Tac Toe!!")

while True:
    
    tb = ['0','1','2','3','4','5','6','7','8','9']
    players_mark = player_input()
    turn = coin_toss() 
    print(turn +" goes first.")

    play_game = input("Ready to play? y/n: ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'player1':
            display_board(tb)
            pos = player_choice(tb,turn)
            player1_turn(tb,players_mark[0],pos)
            if(winCheck(tb,players_mark[0])):
                display_board(tb)
                print("Player1 has won!!")
                game_on = False
            else:
                if full_board_check(tb):
                    display_board(tb)
                    print("Game Tie")
                    game_on = False
                else:
                    turn = 'player2'
        else:
            display_board(tb)
            pos = player_choice(tb,turn)
            player2_turn(tb,players_mark[1],pos)
            if(winCheck(tb,players_mark[1])):
                display_board(tb)
                print("Player2 has won!!")
                game_on = False
            else:
                if full_board_check(tb):
                    display_board(tb)
                    print("Game Tie")
                    game_on = False
                else:
                    turn = 'player1'
    if not replay():
        break


    



        