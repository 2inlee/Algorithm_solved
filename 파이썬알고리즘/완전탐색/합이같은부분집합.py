def DFS(idx, sum):
    if idx == n:  # 모든 원소를 고려했을 때
        if sum == (total - sum):  # 현재 부분집합의 합과 나머지 부분집합의 합이 같다면
            return True
        else:
            return False
    else:
        # 현재 원소를 포함시키는 경우
        if DFS(idx + 1, sum + a[idx]):
            return True
        # 현재 원소를 포함시키지 않는 경우
        if DFS(idx + 1, sum):
            return True
    return False

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)  # 전체 집합의 합
    if DFS(0, 0):  # DFS 시작, 인덱스 0부터 시작, 초기 합은 0
        print("YES")
    else:
        print("NO")
