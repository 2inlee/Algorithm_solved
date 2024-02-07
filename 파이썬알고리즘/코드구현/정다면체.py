n, m = map(int, input().split())
a =list()
counter = [0]*(n+m+1) # 0으로 초기화된 카운터 리스트 생성 / 마방진 로직으로 몇번 나오는지 카운트
max = 0

for i in range(1, n+1):
  for j in range(1, m+1):
    counter[i+j] += 1

for i in range(n+m+1):
  if counter[i] > max:
    max=counter[i]
    
for i in range(n+m+1):
  if counter[i] == max:
    print(i, end=' ')