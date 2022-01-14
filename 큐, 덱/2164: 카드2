# 2164 : 카드2
import sys
import collections
n = int(sys.stdin.readline()) # n장의 카드
card = [i for i in range(1, n + 1)]
card = collections.deque(card)

while True : # 카드가 한장 남을 때 까지
    if n == 1 :
        print(card[0])
        break

    card.popleft()

    temp = card[0]
    card.popleft()
    card.append(temp)

    n -= 1
