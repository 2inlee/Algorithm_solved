n = int(input())
for i in range(n):
  a = input().upper()
  reversed_a = a[::-1] # 슬라이싱으로 리버스 시키기
  if a == reversed_a:
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))