import numpy as np
import os

def isInRow(game,num,r):
    for c in range(len(game)):
        if game[r][c]==num:
            return True
    return False

def isInCol(game,num,c):
    for r in range(len(game)):
        if game[r][c]==num:
            return True
    return False

def isInBox(game,num,r,c):
    rowMultiple=r//3
    colMultiple=c//3
    for i in range(rowMultiple*3,(rowMultiple+1)*3):
        for j in range(colMultiple*3,(colMultiple+1)*3):
            if game[i][j]==num:
                return True
    return False

def possible(game,num,r,c):
    return not isInRow(game,num,r) and not isInCol(game,num,c) and not isInBox(game,num,r,c)

def play():
    global game
    for r in range(len(game)):
        for c in range(len(game)):
            if not game[r][c]:#try to fill a num in blank place
                for num in range(1,10):
                    if possible(num,r,c):
                        game[r][c]=num
                        play()
                        game[r][c]=0
            #if no number can be assigned to that position then return to previous state
            if not game[r][c]:
                return
    print(game)
    write_back(game)

def play1(game):
    isFull = True
    i = -1
    j = -1

    for i1 in range(len(game)):
        for j1 in range(len(game[0])):
            if game[i1][j1] == 0:
                isFull = False
                i = i1 
                j = j1
                break
        if not isFull:
            break

    if isFull:
        write_back(game)
        return True

    for val in range(1,10):
        if possible(game,val,i,j):
            game[i][j] = val
            if play1(game):
                return True
            game[i][j] = 0
    return False

def write_back(game):
    with open('output.txt','w+') as output:
        for row in game:
            output.write(str(list(row))+"\n")

def read_sudoku():
    game = []

    if os.path.exists('output.txt'):
        os.remove('output.txt')

    with open('input.txt','r') as input_file:
        text = input_file.read()
        text = text.split('\n')
        for row in text:
            elements = row.split(',')
            temp = []
            for emelement in elements:
                if emelement and emelement != '\n':
                    temp.append(int(emelement))
            game.append(temp.copy())
    return game



if __name__=="__main__":
    game = read_sudoku()
    play1(game)

