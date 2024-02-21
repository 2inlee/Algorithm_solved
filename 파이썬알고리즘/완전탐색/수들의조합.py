def DFS(L, idx):
  global cnt
  if L == k: # 깊이가 k에 도달했을 때
    sum_value = 0
    for j in range(L):
      sum_value += res[j]
    if sum_value % m == 0: # 합이 m의 배수인지 직접 검사
      cnt += 1
  else:
    for i in range(idx, n):
      res[L] = a[i]
      DFS(L+1, i+1)

if __name__ == "__main__":
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  m = int(input())
  max_sum = sum(a) # 들어온 리스트의 합으로, 가능한 6의 배수의 최댓값을 구하기 위함
  res = [0]*(k) # 매 재귀때 마다 들어 갈 값들의 리스트
  cnt = 0 # 6의 배수가 몇개인 지
  DFS(0, 0) # L = DFS의 깊이레벨, idx = a의 몇번째 인덱스에 있는 값인 지
  print(cnt) # 마지막에 최종 cnt값 출력