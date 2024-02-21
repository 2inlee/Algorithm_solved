# 4 2 -> 1 2 / 1 3 / 1 4 / 2 3 / 2 4 / 3 4
# 맨 앞꺼 냅두고 그 다음거 냅두고 그 다다음것부터 쓰면 되는데, 이게 썼던거 또 쓰면 안되고, 뒤에 나오는 숫자가 앞에꺼보다 더 크면 안된 다는 점을 조건
# ch[0] * n 개 만들어서 썼는 지 안썼는 지 1, 0 왔다갔다 하면서 체크 쓰면 1, 안쓰면 0
# 


def DFS(L, idx):
  global cnt
  if L == n:
    cnt+=1
    print()
  else:
    ch[L] = 1
    DFS(L+1)
    ch[L] = 0

  



if __name__ =="__main__":
  n, m = map(int, input().split())
  ch = [0]*n
  cnt = 0
  DFS(0, 0)