def DFS(len, last_num):
  if last_num > a[len]: # 마지막으로 결과값에 넣은 값이 다음 검사할 값보다 크다면, cut
    return
  if len == 1:
    return a[0]
  else:
    max()

if __name__ =="__main__":
  n = int(input())
  a = list(map(int, input().split()))
  dy = [0] * (n+1)
  a.insert(0,0)
  dy[1] = 1
  res = 0
  for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
      if a[j]<a[i] and dy[j]>max:
        max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
      res=dy[i]

print(res)