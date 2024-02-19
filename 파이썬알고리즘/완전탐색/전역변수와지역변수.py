# 전역변수와 지역변수

# 지역변수와 전역변수가 한 함수내에서 둘 다 쓰일 수 있으면, 지역변수가 먼저 작동함
# 글로벌에서 선언한 변수를 함수 내에서 사용하고 싶을 때는 global을 사용하면 됨

def DFS1():
  cnt = 3
  print(cnt)

def DFS2():
  global cnt
  if cnt == 5:
    cnt = cnt + 1
    print(cnt)


def DFS3():
  a[0] = 7 # a라는 리스트의 0번 인덱스의 값을 참조한다고 인식되기 때문에 global을 사용하지 않아도 됨
  print(a)
  a = a + [4] # a라는 리스트에 4를 추가하려고 하기 때문에 global을 사용하지 않으면 오류가 발생함

if __name__ == "__main__":
  cnt = 5
  a = [1, 2, 3]
  DFS1()
  DFS2()
  DFS3()
  print(cnt)