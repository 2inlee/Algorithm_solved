K = int(input())
stack = []
for i in range(K):
    cmd = int(input())
    if cmd == 0:
        stack.pop()
    else:
        stack.append(cmd)

print(sum(stack))