def DFS(len):
  if dy[len]>0: # 이미 0이 아닌 다른 값이 memorization 되어있다면 바로 출력
    return dy[len]
  
  if len == 1 or len == 2:
    return len
  else:
    dy[len]=DFS(len-1)+DFS(len-2)
    return dy[len]

if __name__ =="__main__":
  n = int(input())
  dy = [0] * (n+1)
  print(DFS(n))