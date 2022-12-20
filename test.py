import numpy as np
import random

########################################################################################################
########################################## VARIABLES: ##################################################
Endgame = False
score = 0
matrix = 0
LB = random.randint(1, 5)
lvl = 0
game = 0
pointnbr = 0
column_selected = 0
lign_selected = 0
lives = 3
bloc_used = 0
a = 0
b = 0
c = 0
# bloc :
bloc1 = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]
bloc2 = [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
bloc3 = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
bloc4 = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
se = [bloc3, bloc2, bloc1, bloc4]
B1n1 = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B1n2 = [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B1n3 = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B2n1 = [[1, 0, 0], [1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]


# Biggest function defined in two parts: #
# First one works for the 4 first ligns, it prints the matrix the user chose, but at the end of each
# lign it prints the one or three randomly chose bloc(s), the second part just prints the rest of
# the matrix, so from 4 until the lengh of the matrix. The variables a,b and c are defined so that
# they can become a random bloc from the 'se' list and return it's value at the end. We need to define
# here so that they have a value and can be printed.

def transfo_grid(matrix_for_functions, AllBlocs):
    a = random.choice(AllBlocs)
    b = random.choice(AllBlocs)
    c = random.choice(AllBlocs)
    print('*', end="  ")
    for j in range(len(matrix_for_functions[0])):
        print(chr(j + 97), end=' ')
    print('')
    print('  ╔══════════════════════════════════════╗', end='')
    print()
    if BlocsInTheGame == 2:
        for i in range(3):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrix_for_functions[0])):
                if matrix_for_functions[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrix_for_functions[i][j] == 0:
                    print(' ', end=' ')
                if matrix_for_functions[i][j] == 1:
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
            for j in range(len(matrix_for_functions[0])):
                if matrix_for_functions[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrix_for_functions[i][j] == 0:
                    print(' ', end=' ')
                if matrix_for_functions[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            for y in range(4):
                if a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            print('')
    for i in range(3, len(matrix_for_functions)):
        print(chr(i + 65), end=' ║')
        for j in range(len(matrix_for_functions[0])):
            if matrix_for_functions[i][j] == 2:
                print(u'\u25A0', end=' ')
            if matrix_for_functions[i][j] == 0:
                print(' ', end=' ')
            if matrix_for_functions[i][j] == 1:
                print(u'\u00B7', end=' ')
        print('║', end=' ')
        print('')
    print('  ╚══════════════════════════════════════╝', end='')
    return a, b, c


# Function used to print the bloc with blocs and blanks and not with 0 and 1
def affichage(bloc):
    for i in range(len(bloc1)):
        print('')
        for j in range(3):
            if bloc[i][j] == 1:
                print('\u25A0', end=' ')
            if bloc[i][j] == 0:
                print('\u00B7', end=' ')
    print('')


# Function that verifies if all the bloc fits in the grid, so if the user tries to put the bloc on one
# side it doesn't fit completely then it will return false
def verify_grid():
    for i in range(len(a)):
        for j in range(len(a)):
            if matrix[lign_selected + i][column_selected + j] != 1 and bloc_used[i][j] == 1:
                print(f'{"Not possible to play here":-^40}')
                return False
    return True


# Function reading the grid used to verify if you can place a bloc somewhere, it compares the value of
# the bloc and the value of the grid, at the place where we want to place it. v and w are local variables
# used to place the cubes, it uses the verify_grid() to know if we can place it here.
def read_grid():
    if verify_grid():
        for i in range(len(bloc_used)):
            for j in range(len(bloc_used)):
                v = lign_selected + i
                w = column_selected + j
                if matrix[v][w] == 1 and bloc_used[i][j] == 1:
                    matrix[v][w] = 2


# Fonction that is supposed to delete a column if it's full (Not working rn)
def col_delete(matrix_for_functions, pointnbr):
    for i in range(len(matrix_for_functions)):
        for j in range(len(matrix_for_functions[0])):
            if 1 not in matrix_for_functions[j]:
                for i in range(len(matrix_for_functions)):
                    if matrix_for_functions[i][j] == 2:
                        matrix_for_functions[i][j] = 1
                        return pointnbr


# Function that deletes a lign if it's full , takes an argument 'matrice' that corresponds to the matrix
# on which we use, returns 'Pointnbr' that will increment the score depending on how many actual cubes got
# deleted
def lign_delete(matrix_for_functions, pointnbr):
    for i in range(len(matrix_for_functions)):
        for j in range(len(matrix_for_functions[0])):
            if 1 not in matrix_for_functions[i]:
                for j in range(len(matrix_for_functions)):
                    if matrix_for_functions[i][j] == 2:
                        matrix_for_functions[i][j] = 1
                    return True


# Function increasing the score by using the returned of both functions lign and column delete


print('\033[0;31;40m')
print('\033[1m')
print(f'{"TETRIS GAME":-^40}')
print(f'{"Created by Gaspard and Max":-^40}')
print('1: Play the game')
print('2: How to play')

# first menu
while (game <= 0) or (game > 2):
    game = int(input(''))
while game != 1:
    if game == 2:
        print('The rules are simple: You will play a tetris like game, if you fill a lign or a column with the blocs')
        print('you will gain points, if you missplace a block 3 times: GAME OVER, now press 1 to play')
        game = int(input(''))

# menu for the levels
if game == 1:
    level = 9
    while (level < 0) or (level > 3):
        print('What level do you want to play?')
        while level > 3 or level < 1:
            print('1:Diamond 2:Circle 3:Triangle')
            level = int(input(''))
        # the code asks for an input depending on which he will transform the txt file into a matrix
        if level == 1:
            matrix = np.loadtxt('diamond', usecols=range(19))
        if level == 2:
            matrix = np.loadtxt('rond', usecols=range(19))
        if level == 3:
            matrix = np.loadtxt('triangle', usecols=range(19))
        # BlocsinTheGame will take a value of 1 or 2, depending on which he will play with 3 or 1 random bloc
        print('Do you want to play with one(1) or three blocs(2)? ')
        BlocsInTheGame = 0
        BlocsInTheGame = int(input(''))
        a, b, c = transfo_grid(matrix, se)
        while lives > 0:
            if BlocsInTheGame == 2:
                print('')
                print('1', end='')
                print('2', end='')
                print('3', end='')
                # the code asks the user to choose a bloc between 1 and 3, depending on which he will
                # assign a block to the variable
                bloc_used = int(input('Choose a bloc from 1 to 3 '))
                if bloc_used == 1:
                    bloc_used = a
                if bloc_used == 2:
                    bloc_used = b
                if bloc_used == 3:
                    bloc_used = c
            else:
                bloc_used = a
                print()
            lign_selected = int(input('Choose a lign : '))
            if level == 3:
                while (lign_selected >= 8) or (lign_selected < 0):
                    print('Not a valid lign')
                    lign_selected = int(input('Choose a lign : '))
            else:
                while (lign_selected >= 18) or (lign_selected < 0):
                    print('Not a valid lign')
                    lign_selected = int(input('Choose a lign : '))

            column_selected = int(input('Choose a column : '))
            while (column_selected >= 18) or (column_selected < 0):
                print('Not a valid column')
                column_selected = int(input('Choose a column : '))
            read_grid()
            transfo_grid(matrix, se)
            lign_delete(matrix, pointnbr)
            col_delete(matrix, pointnbr)
            if lign_delete:
                score = +1
            print(score)
