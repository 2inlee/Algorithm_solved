n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  while x > 0:
    sum += x % 10 # 1의 자리 수
    x = x // 10 # 1의 자리수를 제외한 나머지 몫 부분 -> 다시 while문으로
  return sum

max = 0
for x in a:
  total = digit_sum(x)
  if total > max:
    max = total
    res = x

print(res)