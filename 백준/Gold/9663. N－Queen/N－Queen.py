def is_valid(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i] - col[x]) == x-i:
            return (0)
    return (1)

def DFS(x):
    global res
    if x == n:
        res += 1
        return (0)
    for i in range(n):
        col[x] = i
        if is_valid(x):
            DFS(x + 1)

n = int(input())
res = 0
col = [0] * 15

DFS(0)
print(res)