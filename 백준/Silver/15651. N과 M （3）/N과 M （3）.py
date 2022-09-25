n, m = map(int, input().split())
lst = []

def DFS(cnt):
    if cnt - 1 == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(1, n+1):
        lst.append(i)
        DFS(cnt + 1)
        lst.pop()

DFS(1)