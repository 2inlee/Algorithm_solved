n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
commands = [list(map(int, input().split())) for _ in range(m)]

for command in commands:
    row, direction, amount = command
    row -= 1  # 인덱스는 0부터 시작하므로
    amount %= n  # 회전 횟수를 N으로 나눈 나머지만큼만 회전하면 됨
    if direction == 0:  # 왼쪽으로 회전
        matrix[row] = matrix[row][amount:] + matrix[row][:amount] # 파이썬의 특징을 이용해서 [1,2,3,4,5] -> [3,4,5] + [1,2] => [3,4,5,1,2]
    else:  # 오른쪽으로 회전
        matrix[row] = matrix[row][-amount:] + matrix[row][:-amount]

sum = 0
lt = rt = n//2
for i in range(n):
  for j in range(lt, rt+1):
    sum += matrix[i][j]
  if i < n//2:
    lt -= 1
    rt += 1
  else:
    lt += 1
    rt -= 1

print(sum)
