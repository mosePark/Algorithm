# 11866: 요세푸스 문제 0
import sys
import collections

n, k = map(int, sys.stdin.readline().split())

que = collections.deque(i for i in range(1, n+1))

answer = []

while True :
    if len(que) == 0 :
        break

    else :
        que.rotate(-k)
        answer.append(que.pop())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")
