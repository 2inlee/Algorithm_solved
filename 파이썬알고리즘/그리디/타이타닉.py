n, m = map(int, input().split())
a = list(map(int, input().split()))
# 90 50 70 100 60
a.sort() # -> 50 60 70 90 100
cnt = 0

while(a):
	if len(a) == 1:
		cnt += 1
		break
	if a[0]+a[-1] > m:
		a.pop()
		cnt += 1
	else:
		a.pop(0)
		a.pop()
		cnt += 1
		
print(cnt)