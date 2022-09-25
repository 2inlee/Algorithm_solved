board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def checkRow(x,a):
    for i in range(9):
        if a == board[x][i]:
            return (0)
    return (1)

def checkCol(y,a):
    for i in range(9):
        if a == board[i][y]:
            return (0)
    return (1)

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == board[nx+i][ny+j]:
                return (0)
    return (1)

def DFS(index):
    if index == len(zeros):
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        x = zeros[index][0]
        y = zeros[index][1]

        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            board[x][y] = i
            DFS(index + 1)
            board[x][y] = 0

DFS(0)