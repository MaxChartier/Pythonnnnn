B4n1 = [[0, 1, 0,],
        [1, 1, 1,]]

def bloc(bloc):
    m = []
    for i in range(len(bloc), 4):
        for i in range(2):
            m.append(0)
        bloc.append(m)
    for j in range(len(bloc), 4):
        for j in range(2):
            m.append(0)
        bloc.append(m)
    print(bloc)
print('B4n1 =', end='')
bloc(B4n1)