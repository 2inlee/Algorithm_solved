from collections import deque

n = int(input())

a = deque()
b = deque()
for i in range(n):
  a.append(input())

for i in range(n-1):
  b.append(input())

while b:
  if a[0] == b[0]:
    a.popleft()
    b.popleft()
  else:
    a.append(a.popleft())
  
print(a[0])