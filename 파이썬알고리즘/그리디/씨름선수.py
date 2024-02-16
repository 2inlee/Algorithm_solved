n = int(input())

sunsu = []
for _ in range(n):
  k, m = map(int, input().split())
  sunsu.append((k, m))
sunsu.sort(reverse=True)
largest = 0
cnt = 0
for x, y in sunsu:
  if y > largest:
    largest = y
    cnt += 1

print(cnt)