c, n = map(int, input().split())
dogs = []

for i in range(n):
  dogs.append(int(input()))

def DFS(index, sum, dogs, c, n):
    # 탈출 조건: 모든 바둑이를 고려했을 때
    if index == n:
        return sum if sum <= c else 0
    # 현재바둑이를 포함했을 때와 안했을 때 경우 중 최댓값 반환
    return max(DFS(index + 1, sum + dogs[index], dogs, c, n), DFS(index + 1, sum, dogs, c, n))

if __name__ == "__main__":
	print(DFS(0, 0, dogs, c, n))