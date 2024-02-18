# 11 -> 11/2 = 5..1
# 5 -> 5/2 = 2..1
# 2 -> 2/2 = 1..0
# 1

def DFS(x):
  if x == 1:
    print(1, end='')
    return
  else:
    DFS(x//2)
    print(x % 2, end='')


if __name__ == '__main__':
  n = int(input())
  DFS(n)