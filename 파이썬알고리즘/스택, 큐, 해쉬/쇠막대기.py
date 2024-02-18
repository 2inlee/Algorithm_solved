# 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.
# 입력으로 주어진 괄호 문자열은 항상 올바르게 구성되어 있다.
# 여러분은 그렇게 배치된 쇠막대기를 절단하는 레이저가 몇 개인지 계산하여 출력해야 한다.

a = input()
stack = []
cnt = 0
for i in range(len(a)):
  if a[i] == '(':
    stack.append(a[i])
  else:
    stack.pop()
    if a[i-1] == '(':
      cnt += len(stack)
    else:
      cnt += 1
print(cnt)
