# N장의 카드가 있다. 1가 제일 위에 N이 가장 아래에 있다.
# 계속 반복하는데 제일 위에 있는 카드를 바닥에 버린다.
# 제일 위에있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 그렇게 N이 주어졌을때 가장 마지막에 남는 카드를 구하는 프로그램을 작성해라

from collections import deque

N = int(input())
card = deque([i for i in range(1, N+1)])

while(len(card) > 1):
    card.popleft()
    count = card.popleft()
    card.append(count)

print(card[0])