import numpy as np
import random
from Functions import *
import keyboard

Endgame = False
Score = 0
LB = random.randint(1, 5)
Lebloc = 0
lvl = 0
game = 0
column_selected = 0
line_selected = 0
lives = 3

# bloc :
bloc1 = [0, 0, 0,0], [0, 0, 0,0], [0, 1, 1,0],[1, 1, 0,0]
bloc2 = [1, 0, 0,0], [1, 1, 0,0], [1, 1, 1,0],[1, 1, 0,0]
bloc3 = [1, 0, 0,0], [1, 1, 0,0], [1, 1, 1,0],[1, 1, 0,0]
bloc4 = [1, 0, 0,0], [1, 1, 0,0], [1, 1, 1,0],[1, 1, 0,0]
bloc5 = [1, 1, 1,0], [1, 1, 1,0], [1, 1, 1,0],[1, 1, 0,0]
se = [bloc1, bloc2, bloc3, bloc4, bloc5]

def transfo_grid(matrixx, AllBlocs):
    a = random.choice(AllBlocs)
    b = random.choice(AllBlocs)
    c = random.choice(AllBlocs)
    print('*', end="  ")
    for j in range(len(matrixx[0])):
        print(chr(j + 97), end=' ')
    print('')
    print('  ╔══════════════════════════════════════╗', end='')
    print()
    if BlocsInTheGame == 2:
        for i in range(4):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrixx[0])):
                if matrixx[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrixx[i][j] == 0:
                    print(' ', end=' ')
                if matrixx[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            for y in range(4):
                if a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            for y in range(4):
                if b[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            for y in range(4):
                if c[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('')
    else:
        for i in range(3):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrixx[0])):
                if matrixx[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrixx[i][j] == 0:
                    print(' ', end=' ')
                if matrixx[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            for y in range(4):
                if a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            print('')
    for i in range(3, len(matrixx)):
        print(chr(i + 65), end=' ║')
        for j in range(len(matrixx[0])):
            if matrixx[i][j] == 2:
                print(u'\u25A0', end=' ')
            if matrixx[i][j] == 0:
                print(' ', end=' ')
            if matrixx[i][j] == 1:
                print(u'\u00B7', end=' ')
        print('║', end=' ')
        print('')
    print('  ╚══════════════════════════════════════╝', end='')
    return a, b, c

def affichage(bloc):
    for i in range(len(bloc1)):
        print('\r')
        for j in range(3):
            if bloc[i][j] == 1:
                print('\u25A0', end=' ')
            if bloc[i][j] == 0:
                print('\u00B7', end=' ')
    print('\r')


def verify_grid():
    for i in range(len(bloc1)):
        for j in range(len(bloc1[0])):
            if matrix[l + i][c + j] != 1 and Lebloc[i][j] == 1:
                texti = "You can't play here"
                print(f'{texti:-^40}')
                return False
    return True


def read_grid():
    if verify_grid():
        for i in range(len(Lebloc)):
            for j in range(len(Lebloc)):
                v = l + i
                w = c + j
                if matrix[v][w] == 1 and Lebloc[i][j] == 1:
                    matrix[v][w] = 2


print('\033[0;31;40m')
print('\033[1m')
text = 'TETRIS GAME'
text1 = 'Created by Gaspard and Max'
print(f'{text:-^40}')
print(f'{text1:-^40}')
print('1: Play the game')
print('2: How to play')

# first menu
while (game <= 0) or (game > 2):
    game = int(input(''))
while game != 1:
    if game == 2:
        print('Rules')
        game = int(input(''))
    # menu for the levels
if game == 1:
    level = 9
    while (level < 0) or (level > 3):
        print('What level do you want to play?')
        while level > 3 or level < 1:
            print('1:Diamond 2:Circle 3:Triangle')
            level = int(input(''))
        if level == 1:
            matrix = np.loadtxt('diamond', usecols=range(19))
            transfo_grid(matrix,se)
        if level == 2:
            matrix = np.loadtxt('rond', usecols=range(19))
            transfo_grid(matrix,se)
        if level == 3:
            matrix = np.loadtxt('triangle', usecols=range(19))
            transfo_grid(matrix,se)
        print('Do you want to play with one(1) or three blocs(2)? ')
        BlocsInTheGame = int(input(''))
        while (lives > 0):
            if BlocsInTheGame == 2:
                print('\r')
                print('1', end='')
                a = random.choice(se)
                affichage(a)
                print('2', end='')
                b = random.choice(se)
                affichage(b)
                print('3', end='')
                c = random.choice(se)
                affichage(c)
                Lebloc = int(input('Choose a bloc from 1 to 3 '))
                if Lebloc == 1:
                    Lebloc = a
                if Lebloc == 2:
                    Lebloc = b
                if Lebloc == 3:
                    Lebloc = c
            else:
                Lebloc = random.choice(se)
                affichage(Lebloc)
            l = int(input('Choose a line : '))
            if level == 3:
                while (l >= 8) or (l < 0):
                    print('Not a valid lign')
                    l = int(input('Choose a line : '))
            else:
                while (l >= 18) or (l < 0):
                    print('Not a valid lign')
                    l = int(input('Choose a line : '))

            c = int(input('Choose a column : '))
            while (c >= 18) or (c < 0):
                print('Not a valid column')
                c = int(input('Choose a column : '))
            read_grid()
            transfo_grid(matrix, se)
            print('Score =', Score)
