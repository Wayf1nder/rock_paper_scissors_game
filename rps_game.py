#Uzdevums 1 : modificēt kodu lai atkārtojas (Done)

import random
turns = ['rock', 'paper', 'scissors']


while (True):
    human_turn = input('Enter your turn, or exit!:')
    computer_turn = random.choice(turns)

    if human_turn == 'exit':
        break

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('human wins!')
    else:
        print('computer wins!')
