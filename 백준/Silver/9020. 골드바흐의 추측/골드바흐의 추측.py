def is_prime(n):
  i = 2
  if (n <= 1):
    return (0)
  while (i*i <= n):
    if (n % i ==0):
      return (0)
    i += 1
  return (1)

T = int(input())
for _ in range(T):
  n = int(input())
  a, b = n//2, n//2
  for i in range(10000):
    if is_prime(a) and is_prime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1