n = int(input())
a = list(map(int, input().split()))

cnt = 0
cur = 0
word = []
left = 0
right = n - 1

while left <= right:
    temp = []
    if a[left] > cur:
        temp.append((a[left], 'L'))
    if a[right] > cur:
        temp.append((a[right], 'R'))
    
    temp.sort()
    if len(temp) == 0:
        break
    
    cur, direction = temp[0]
    if direction == 'L':
        left += 1
    else:
        right -= 1
    word.append(direction)
    cnt += 1

print(cnt)
print(''.join(word))
