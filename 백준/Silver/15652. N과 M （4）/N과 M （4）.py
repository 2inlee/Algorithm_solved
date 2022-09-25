n, m = map(int, input().split())
lst = []

def DFS(cnt, index):
    if cnt - 1 == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(index, n + 1):
        lst.append(i)
        DFS(cnt + 1, i)
        lst.pop()

DFS(1,1)