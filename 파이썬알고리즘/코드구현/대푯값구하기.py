n = int(input())
a = list(map(int, input().split()))

avg = round(sum(a)/n)
min = 2147483647
for i, score in enumerate(a):
  tmp = abs(score-avg)
  if tmp < min:
    min = tmp
    score = score
    result = i+1
  elif tmp == min:
    if score > a[result-1]:
      result = i+1
print(avg, result)
