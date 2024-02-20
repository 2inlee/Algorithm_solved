# 가장 윗줄에 1~N까지 숫자가 한 개씩 적혀있다. 그리고 둘째 줄부터 차례대로 파스칼의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다.

import sys

def DFS(L, sum):
  if L == n and sum == k:
    for x in p:
      print(x, end = ' ')
    sys.exit(0)
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1
        p[L] = i
        DFS(L+1, sum+(p[L]*b[L]))
        ch[i] = 0

if __name__ =="__main__":
  n, k = map(int, input().split())
  p = [0] * n # 순열 리스트
  b = [1] * n # 가중치 리스트
  ch = [0] * (n+1) # 해당 숫자를 썼는 지 안썼는지 체크용 리스트
  for i in range(1, n):
    b[i] = b[i-1]*(n-i)//i
  DFS(0, 0)