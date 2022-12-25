# libraries and blocs import
import numpy as np
import random
import time
from Blocs import seCircle, seTriangle, seDiamond, se

########################################################################################################
########################################## VARIABLES: ##################################################
score = 0
p = 0
saved = []
matrix = 0
game = 0
column_selected = 0
line_selected = 0
lives = 3
bloc_used = 0
a = 0
b = 0
c = 0
# Bloc used for the in range parts
bloc1 = [0, 0, 0, 0, 0], \
        [0, 1, 1, 1, 0], \
        [0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0], \
        [1, 1, 0, 0, 0]


# Biggest function defined in two parts: #
# First one works for the 4 first lines, it prints the matrix the user chose, but at the end of each
# line it prints the one or three randomly chose bloc(s), the second part just prints the rest of
# the matrix, so from 4 until the length of the matrix. The variables a,b and c are defined so that
# they can become a random bloc from the 'se' list and return its value at the end. We need to define
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
    if BlocsInTheGame == 2:
        print('     1           2           3     ')
        for i in range(5):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrix_for_functions[0])):
                if matrix_for_functions[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrix_for_functions[i][j] == 0:
                    print(' ', end=' ')
                if matrix_for_functions[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            for y in range(5):
                if i == 0 and y == 0:
                    print(u'\u25EF', end=' ')
                elif a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            for y in range(5):
                if i == 0 and y == 0:
                    print(u'\u25EF', end=' ')
                elif b[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            for y in range(5):
                if i == 0 and y == 0:
                    print(u'\u25EF', end=' ')
                elif c[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('')
    else:
        print('')
        for i in range(5):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrix_for_functions[0])):
                if matrix_for_functions[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrix_for_functions[i][j] == 0:
                    print(' ', end=' ')
                if matrix_for_functions[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            for y in range(5):
                if i == 0 and y == 0:
                    print(u'\u25EF', end=' ')
                elif a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            print('')
    if level == 3:
        for i in range(5, 10):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrix_for_functions[0])):
                if matrix_for_functions[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrix_for_functions[i][j] == 0:
                    print(' ', end=' ')
                if matrix_for_functions[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            if i == 6:
                print('        ****************', end='')
            if i == 7:
                print('           Score =', score, end='')
            if i == 9:
                print('        ****************', end='')
            if i == 8:
                print('           lives =', lives, end='')
            if i == 5:
                if BlocsInTheGame == 2:
                    print('   chose a block from 1 to 3:', end='')
            print('')
    else:
        for i in range(5, len(matrix_for_functions)):
            print(chr(i + 65), end=' ║')
            for j in range(len(matrix_for_functions[0])):
                if matrix_for_functions[i][j] == 2:
                    print(u'\u25A0', end=' ')
                if matrix_for_functions[i][j] == 0:
                    print(' ', end=' ')
                if matrix_for_functions[i][j] == 1:
                    print(u'\u00B7', end=' ')
            print('║', end=' ')
            if i == 8:
                print('        ****************', end='')
            if i == 9:
                print('           Score =', score, end='')
            if i == 11:
                print('        ****************', end='')
            if i == 10:
                print('           lives =', lives, end='')
            if i == 6:
                if BlocsInTheGame == 2:
                    print('   chose a block from 1 to 3:', end='')
            print('')
    print('  ╚══════════════════════════════════════╝', end='')
    return a, b, c


# Function used to print the bloc with squares and hyphens and zeros and ones
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
def verify_grid(matrix_for_function):
    for i in range(len(a)):
        for j in range(len(a)):
            if any(matrix_for_function[line_selected + i]) > 13 and any([column_selected + j]) > 13:
                return False
            else:
                if matrix_for_function[line_selected + i][column_selected + j] != 1 and bloc_used[i][j] == 1:
                    print(f'{"Not possible to play here":-^40}')
                    return False
    return True


def interact():
    fn = input("Enter a filename: ")
    return fn


def load_maze(fn):
    myfile = open(fn)
    maze_txt = myfile.read()
    myfile.close()
    return maze_txt


# Function reading the grid used to verify if you can place a bloc somewhere, it compares the value of
# the bloc and the value of the grid, at the place where we want to place it. v and w are local variables
# used to place the cubes, it uses the verify_grid() to know if we can place it here.
def read_grid(matrix_for_function):
    if verify_grid(matrix_for_function):
        for i in range(len(bloc_used)):
            for j in range(len(bloc_used)):
                v = line_selected + i
                w = column_selected + j
                if matrix_for_function[v][w] == 1 and bloc_used[i][j] == 1:
                    matrix_for_function[v][w] = 2


# Function that is supposed to delete a column if it's full (Not working rn)
def col_delete(matrix_for_functions, score, lives):
    n = 0
    for j in range(len(matrix_for_functions)):
        m = 0
        for i in range(len(matrix_for_functions)):
            if matrix[i][j]==1:
                m+=1
        if m == 0:
            for i in range(len(matrix_for_functions)):
                if matrix[i][j]==2:
                    matrix[i][j]=1
                    n+=1
                score += n
                lives += 1
            print('You have filled out column', j + 1, 'it will reset, You have obtained', n,
                      'point(s) and 1 life!')
    return True,score,lives


# Function that deletes a line if it's full , takes an argument 'matrix_for_functions' that corresponds to the matrix
# on which we use, returns 'Pointnbr' that will increment the score depending on how many actual cubes got
# deleted
def line_delete(matrix_for_functions, score, lives):
    n = 0
    if level == 3:
        for i in range(7):
            for j in range(17):
                if 1 not in matrix_for_functions[i]:
                    for j in range(len(matrix_for_functions)):
                        if matrix_for_functions[i][j] == 2:
                            matrix_for_functions[i][j] = 1
                            n += 1
                    score += n
                    lives += 1
                    print('You have filled out line', i + 1, 'it will reset, You have obtained', n,
                          'point(s) and 1 life!')
                    return True, score, lives
        return False, score, lives
    if level == 1 or level == 2 or level == 4:
        for i in range(len(matrix_for_functions)):
            for j in range(len(matrix_for_functions[0] - 1)):
                if 1 not in matrix_for_functions[i]:
                    for j in range(len(matrix_for_functions)):
                        if matrix_for_functions[i][j] == 2:
                            matrix_for_functions[i][j] = 1
                            n += 1
                    score += n
                    lives += 1
                    print('You have filled out line', i + 1, 'it will reset, You have obtained', n,
                          'point(s) and 1 life!')
                    return True, score, lives
        return False, score, lives


print('\033[0;31;40m')
print('\033[1m')
print(f'{"TETRIS GAME":-^40}')
print(f'{"Created by Gaspard and Max":-^40}')
print('1: Play the game')
print('2: How to play')
print('To exit the game at any point you just have to enter 99')

# first menu
while (game <= 0) or (game > 2) and game != 99:
    game = int(input(''))
while game != 1:
    if game == 99:
        exit()
    if game == 2:
        print('The rules are simple: You will play a tetris like game, if you fill a line or a column with the blocs')
        print('you will gain points and one life, if you misplace a block 3 times: GAME OVER, now press 1 to play')
        game = int(input(''))

# The menu for the different grids
if game == 1:
    level = 9
    while level > 5 or level < 1 and level != 99:
        print('What level do you want to play?')
        print('1:Diamond 2:Circle 3:Triangle 4:Chose your own level')
        level = int(input(''))
        # the code asks for an input depending on which he will transform the txt file into a matrix
        if level == 1:
            matrix = np.loadtxt('diamond', usecols=range(19))
            se = seDiamond
        if level == 2:
            matrix = np.loadtxt('rond', usecols=range(19))
            se = seCircle
        if level == 3:
            matrix = np.loadtxt('triangle', usecols=range(19))
            se = seTriangle
        if level == 4:
            print('You can customize your own level in the file test, 1 will be the places where you can play and 0 '
                  'will be voids')
            print('You can change the file test for that')
            matrix = np.loadtxt('test', usecols=range(19))
        if level == 99:
            exit()
        # BlocsInTheGame will take a value of 1 or 2, depending on which he will play with 3 or 1 random bloc
        BlocsInTheGame = 0
        while (BlocsInTheGame > 2 or BlocsInTheGame < 1) and BlocsInTheGame != 99:
            BlocsInTheGame = int(input('Do you want to play with one(1) or three blocs(2)?'))
        while lives > 0:
            a, b, c = transfo_grid(matrix, se)
            if BlocsInTheGame == 99:
                exit()
            if BlocsInTheGame == 2:
                # the code asks the user to choose a bloc between 1 and 3, depending on which he will
                # assign a block to the variable
                whatbloc = 0
                while (whatbloc > 4 or whatbloc < 1) and whatbloc != 99:
                    whatbloc = int(input('Choose a bloc from 1 to 3 '))
                if whatbloc == 1:
                    bloc_used = a
                if whatbloc == 2:
                    bloc_used = b
                if whatbloc == 3:
                    bloc_used = c
                if whatbloc == 99:
                    exit()
            else:
                print('\n', 'Lives:', lives)
                print(' Score:', score)
                bloc_used = a
                print()
            line_selectedstring = str(input('Choose a line : '))
            line_selected = ord(line_selectedstring)-65
            if level == 3:
                while (line_selected >= 8) or (line_selected < 0) and line_selected != 99:
                    if line_selected == 99:
                        exit()
                    print('Not a valid line')
                    line_selected = (input('Choose a line : '))

            else:
                print(line_selected)
                while (line_selected >= 18) or (line_selected < 0):
                    if line_selected == 99:
                        exit()
                    print('Not a valid line')
                    line_selected = (input('Choose a line : '))
            column_selectedstring = (input('Choose a column : '))
            column_selected = ord(column_selectedstring)-97
            if column_selected == 99:
                exit()
            while (column_selected >= 15) or (column_selected < 0) and column_selected != 99:
                if column_selected == 99:
                    exit()
                print('Not a valid column')
                column_selected = int(input('Choose a column : '))
            if not verify_grid(matrix):
                lives -= 1
            read_grid(matrix)
            if lives == 0:
                print(f'{"GAME OVER":-^40}')
                reset = int(input('PRESS 1 TO PLAY AGAIN:'))
                if reset == 1:
                    lives = 3
            with open('SavedGame.py', 'w') as file:
                # saved.append(matrix[i][j])
                file.write('Saved=')
                Danslefile = str(matrix)
                file.write(Danslefile)
            if level == 99:
                exit()
            l, score, lives = line_delete(matrix, score, lives)
            line_delete(matrix, score, lives)
            col_delete(matrix, score, lives)
            time.sleep(2)
