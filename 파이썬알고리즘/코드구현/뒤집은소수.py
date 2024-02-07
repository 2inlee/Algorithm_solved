# 1. 입력받은 수를 뒤집는 함수 reverse를 만든다.
# 2. 소수인지 판별하는 함수 isPrime을 만든다.
# 3. 입력받은 수를 뒤집어서 소수인지 판별한다.
# 4. 소수이면 출력한다.

n = int(input())
a = list(map(int, input().split()))

def reverse(x):
  return int(str(x)[::-1])

def isPrime(x):
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

for x in a:
  reversed = reverse(x)
  if isPrime(reversed):
    print(reversed, end=' ')
