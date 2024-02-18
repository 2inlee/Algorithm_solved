# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하시오.
# 중위표기식은 우리가 흔히 쓰은 표현식이다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있
# 는 표기식을 말한다. 후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식을 말
# 한다. 예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현된다.
# 만약 3*(5+2)-9 의 후위표기식은 352+*9- 로 표현된다.


# 1. 연산자의 우선순위를 정한다.
# 2. 중위표기식을 순회하면서 피연산자는 바로 출력하고, 연산자는 스택에 넣는다.
# 3. 연산자의 우선순위가 높거나 같은 것이 스택에 있으면 pop하고 출력한다.

a = input()
stack = []
res = ''
for x in a:
  if x.isdecimal():
    res += x
  else:
    if x == '(':
      stack.append(x)
    elif x == '*' or x == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(x)
    elif x == '+' or x == '-':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(x)
    elif x == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop()

while stack:
  res += stack.pop()
print(res)

