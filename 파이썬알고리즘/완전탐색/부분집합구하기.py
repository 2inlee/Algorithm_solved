# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 모든 부분집합을 출력하는 프로그램을 작성하세요.

def DFS(x):
  if x == n+1:
    for i in range(1, n+1):
      if ch[i] == 1:
        print(i, end=' ')
    print()
  else:
    ch[x] = 1
    DFS(x+1)
    ch[x] = 0
    DFS(x+1)  

if __name__ == "__main__":
  n = int(input())
  ch = [0] * (n+1)
  DFS(1)
