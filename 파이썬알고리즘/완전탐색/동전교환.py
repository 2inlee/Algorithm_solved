def DFS(L, sum):
  global min_count  # 최소 동전 개수를 전역 변수로 관리
  if sum > m or L >= min_count:  # 현재 합계가 목표 금액을 초과하거나 이미 찾은 최소 개수보다 많은 경우, 탐색 중지
    return
  if sum == m:  # 목표 금액에 도달한 경우
    min_count = min(min_count, L)  # 최소 동전 개수 업데이트
    return
  else:
    for x in k:
      DFS(L+1, sum + x)  # 다음 동전 추가

if __name__ == "__main__":
  n = int(input())
  k = list(map(int, input().split()))
  m = int(input())
  k.sort(reverse=True)  # 동전을 큰 단위부터 정렬
  min_count = float('inf')
  DFS(0, 0)
  print(min_count)  # 최소 동전 개수 출력