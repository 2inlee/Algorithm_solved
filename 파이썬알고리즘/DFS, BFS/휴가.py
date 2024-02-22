def DFS(L, sum):
    global res
    if L == n:  # 모든 날짜를 고려했을 때
        if sum > res:
            res = sum
    else:
        if L + tl[L] <= n:  # 상담을 진행할 경우, 상담이 끝나는 날짜가 휴가 시작 전이면
            DFS(L + tl[L], sum + pl[L])
        DFS(L + 1, sum)  # 상담을 진행하지 않을 경우

if __name__ == "__main__":
    n = int(input())
    tl = []
    pl = []
    res = 0
    for i in range(n):
        t, p = map(int, input().split())
        tl.append(t)
        pl.append(p)

    DFS(0, 0)
    print(res)
