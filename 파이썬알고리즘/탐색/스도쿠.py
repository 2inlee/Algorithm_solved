
# 가로줄을 확인하는 함수를 만드는데, 이를 1차원 리스트로 만든다. [0, 0, 0, 0, 0, 0, 0, 0, 0]이라면 0번째 인덱스부터 8번째 인덱스까지 확인한다.
# 예를들어 1이 나왔다면 0번째 인덱스를 1로 바꾸고, 3이 나오면 2번째 인덱스를 1로 바꾸고, 그렇게 모든 인덱스가 1로 바뀌면 YES를 출력한다.
# 세로줄을 확인하는 함수를 만드는데, 이를 1차원 리스트로 만든다. [0, 0, 0, 0, 0, 0, 0, 0, 0]이라면 0번째 인덱스부터 8번째 인덱스까지 확인한다.
# 예를들어 1이 나왔다면 0번째 인덱스를 1로 바꾸고, 3이 나오면 2번째 인덱스를 1로 바꾸고, 그렇게 모든 인덱스가 1로 바뀌면 YES를 출력한다.
# 3x3 정사각형을 확인하는 함수를 만드는데, 이를 1차원 리스트로 만든다. [0, 0, 0, 0, 0, 0, 0, 0, 0]이라면 0번째 인덱스부터 8번째 인덱스까지 확인한다.
# 예를들어 1이 나왔다면 0번째 인덱스를 1로 바꾸고, 3이 나오면 2번째 인덱스를 1로 바꾸고, 그렇게 모든 인덱스가 1로 바뀌면 YES를 출력한다.
# 모든 경우가 맞다면 YES를 출력한다.
# 하나라도 틀리다면 NO를 출력한다.

square = [list(map(int, input().split())) for _ in range(9)]


def row_check():
    for i in range(9):
        ch = [0]*10
        for j in range(9):
            ch[square[i][j]] = 1
        if sum(ch) != 9:
            return False
    return True

def col_check():
    for i in range(9):
        ch = [0]*10
        for j in range(9):
            ch[square[j][i]] = 1
        if sum(ch) != 9:
            return False
    return True

def square_check():
    for i in range(3):
        for j in range(3):
            ch = [0]*10
            for k in range(3):
                for s in range(3):
                    ch[square[i*3+k][j*3+s]] = 1
            if sum(ch) != 9:
                return False
    return True

if row_check() and col_check() and square_check():
    print('YES')
else:
    print('NO')
