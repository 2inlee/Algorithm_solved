def DFS(L, sum, time):
  global res
  if time > m: # time이 주어진 m보다 크면 edge-cut  
    return
  if L == n:
    if sum > res:
      res = sum
  else:
    DFS(L+1, sum+pv[L], time+pt[L]) # 해당문제를 풀 때
    DFS(L+1, sum, time) # 해당문제를 풀지 않을 때
    


if __name__ == "__main__":
  n, m = map(int, input().split())
  pv = []
  pt = []
  for i in range(n):
    score, t = map(int, input().split())
    pv.append(score)
    pt.append(t)
  res = 0
  DFS(0, 0, 0)
  print(res)
  