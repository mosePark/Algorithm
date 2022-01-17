# 1966: 프린터 큐
from collections import deque
t = int(input()) # 테스트 케이스 수
for _ in range(t) :
    n, m = map(int, input().split()) # 문서의 수 n, 몇번째로 인쇄되었는지 궁금한 m
    importance = list(map(int, input().split()))  # n 개의 문서 중요도
    que = deque(i for i in range(1, n+1)) # idx
    que[m] = 'target'

    order = 0

    while True :
        if importance[0] == max(importance) :
            order += 1

            if que[0] == 'target' :
                print(order)
                break
            else :
                importance.pop(0)
                que.popleft()

        else :
            importance.append(importance.pop(0))
            que.append(que.popleft())
