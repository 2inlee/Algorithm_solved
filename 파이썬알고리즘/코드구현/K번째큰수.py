n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set() # 중복을 제거하기 위해 set을 사용
for i in range(n):
  for j in range(i+1, n):
    for m in range(j+1, n):
      res.add(a[i]+a[j]+a[m])
res = list(res) # set을 list로 변환
res.sort(reverse=True) # 내림차순 정렬
print(res[k-1]) # k번째 큰 수 출력
