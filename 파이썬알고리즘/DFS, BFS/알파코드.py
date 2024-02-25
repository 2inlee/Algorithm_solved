def DFS(L, P):
  global cnt
  if L == n:
    cnt += 1
    for j in range(P):
      print(chr(res[j] + 64), end='')
    print()
  else:
    for i in range(1, 27):
      if code[L] == i: # 한자리일 때
        res[P] = i
        DFS(L+1, P+1) # res의 인덱스로 사용할 포지션 위치를 1칸만 이동함
      elif i >= 10 and code[L] == i // 10 and code[L+1] == i % 10:  # 두자리일 때
        res[P] = i
        DFS(L+2, P+1) # res의 인덱스로 사용할 포지션 위치를 2칸만 이동함

if __name__ == "__main__":
  code = list(map(int, input()))
  n = len(code)
  code.insert(n, -1) # for문 돌릴 때 마지막 인덱스에서 out of index error 회피용
  res = [0] * (n+3) # 가능한 문자열 출력용
  cnt = 0
  DFS(0, 0)
  print(cnt)
