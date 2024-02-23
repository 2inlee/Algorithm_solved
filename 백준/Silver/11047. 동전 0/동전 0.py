n, k= map(int, input().split())
a = list()
cnt = 0
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)

for x in a:
    if k >= x:
        cnt += k // x
        k %= x
        if k <= 0:
            break

print(cnt)