import numpy as np
import random
BlocsInTheGame = 0
Endgame = False
Score = 0
LB = random.randint(1, 5)
Lebloc = 0
lvl = 0
game = 0
column_selected = 0
line_selected = 0
lives = 3
l = 0
c = 0
matrix = []
bloc1 =[[1 ,0 ,1 ,0],[0,1,1,1],[0,0,1,1],[0,1,1,1]]
bloc2 =[[1 ,0 ,0 ,0],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
bloc3 =[[0 ,0 ,1 ,0],[0,1,1,1],[1,0,1,1],[0,1,1,0]]
bloc4 =[[1 ,1 ,1,1],[0,1,1,1],[0,0,1,1],[0,1,1,1]]

B1n1 = [[1, 0,0,0],[1, 1, 0, 0],[0,0,0,0],[0,0,0,0]]
B1n2 = [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B1n3 = [[1, 1, 0, 0], [1 , 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B1n4 = [[0, 1, 0, 1], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B2n1 =[[1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B2n2 =[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
B2n3 =[[1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B2n4 =[[0, 1, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
B3n1 =[[0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B3n2 =[[1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
B3n3 =[[1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
B3n4 =[[1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
B4n1 =[[0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
se = [B1n1,B1n2,B1n3,B1n4]


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
                if a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            for y in range(5):
                if b[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            for y in range(5):
                if c[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('')
    else:
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
                if a[i][y] == 1:
                    print(u'\u25A0', end=' ')
                else:
                    print(u'\u00B7', end=' ')
            print('', end='  ')
            print('')
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
        print('')
    print('  ╚══════════════════════════════════════╝', end='')
    return a, b, c



def verify_grid():
    for i in range(len(bloc1)):
        for j in range(len(bloc1[0])):
            if matrix[l + i][c + j] != 1 and Lebloc[i][j] == 1:
                texti = "You can't play here"
                print(f'{texti:-^40}')
                return False
    return True



def affichage(bloc):
    for i in range(len(3)):
        print('\r')
        for j in range(3):
            if bloc[i][j] == 1:
                print('\u25A0', end=' ')
            if bloc[i][j] == 0:
                print('\u00B7',end=' ')
    print('\r')


def read_grid():
    if verify_grid():
        for i in range(len(Lebloc)):
            for j in range(len(Lebloc)):
                v = l + i
                w = c + j
                if matrix[v][w] == 1 and Lebloc[i][j] == 1:
                    matrix[v][w] = 2


def line_delete(matrice):
    Pointnbr = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if 1 not in matrice[i]:
                for j in range(len(matrice)):
                    if matrice[i][j] == 2:
                        matrice[i][j] = 1
                        Pointnbr = Pointnbr + 1
    return Pointnbr