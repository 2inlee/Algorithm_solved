number, m = map(int, input().split())

number_list = list(map(int, str(number)))

stack = []
for x in number_list:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

print(''.join(map(str, stack)))