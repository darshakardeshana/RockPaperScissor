import random as r
from datetime import datetime
import os
def displaySelection(human,bot):
    selections = ['','']
    if human == 1:
        selections[0] = 'rock'
    elif human == 2:
        selections[0] = 'paper'
    elif human == 3:
        selections[0] = 'scissor'
    
    if bot == 1:
        selections[1] = 'rock'
    elif bot == 2:
        selections[1] = 'paper'
    elif bot == 3:
        selections[1] = 'scissor'

    print('both party selections are : ',selections)

def computerSelection():
    selection = r.randint(1,3)
    return selection

def yourSelection():
    selection = int(input('Choose one \n1) Rock \n2) Paper \n3) Scissor\n'))
    return selection

def wins(h,b):
    #h - human
    #b = bot
    if (h == 1 and b == 1) or (h == 2 and b == 2) or (h == 3 and b == 3):
        return 'tie'
    elif (h == 1 and b == 3) or (h == 2 and b == 1) or (h == 3 and b == 2):
        return 'human'
    else:
        return 'bot'

def driverCode():
    score = [0,0]
    while score[0] < 3 and score[1] < 3:
        your = yourSelection()
        comp = computerSelection()
        win = wins(your,comp)
        os.system('cls')
        displaySelection(your,comp)
        if win == 'human':
            score[0] += 1
            print('You won this round')
        if win == 'bot':
            print('Bot won this round')
            score[1] += 1
        if win == 'tie':
            print('Its tie in this round')
        print('Score is : ',score)
    if score[0] == 3:
        with open('RockPaperScissorLog.txt','a') as txt:
            writeText = str(datetime.now()) + ' You Won'
            txt.write(writeText)
        print('You Won')
    else:
        with open('RockPaperScissorLog.txt','a') as txt:
            writeText = str(datetime.now()) + 'You Won'
            txt.write(writeText)
        print('Bot Won')
        
driverCode()