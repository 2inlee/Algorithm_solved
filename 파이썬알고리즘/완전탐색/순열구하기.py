def DFS(L, n, m):
  global cnt
  if L == m:  # m개를 모두 선택했으면 출력
    print(' '.join(map(str, combination)))
    cnt += 1
    return
  for i in range(1, n + 1):
    if not visited[i]:  # 아직 선택되지 않았으면 (0으로 표시)
      visited[i] = 1  # 선택 상태로 변경 (1로 표시)
      combination[L] = i  # 현재 위치에 구슬 번호를 할당
      DFS(L + 1, n, m)  # 다음 구슬 선택을 위해 재귀 호출
      visited[i] = 0  # 방문 상태를 되돌림 (0으로 표시)

if __name__ == "__main__":
  n, m = map(int, input().split())  # n과 m 입력 받기
  cnt = 0  # 경우의 수를 세기 위한 변수
  visited = [0] * (n + 1)  # 각 구슬의 선택 여부를 체크하기 위한 리스트 (0으로 초기화)
  combination = [0] * m  # 현재까지 선택된 구슬의 조합을 저장하는 리스트
  DFS(0, n, m)  # DFS 시작
  print(cnt)  # 총 경우의 수 출력
