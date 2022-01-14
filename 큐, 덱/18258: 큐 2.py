# 18258: 큐 2
import sys
from collections import deque
n = int(sys.stdin.readline())

que = deque()
for _ in range(n) :
    order = str(sys.stdin.readline())
    if 'push' in order :
        que.append(int(order.split()[1]))

    elif 'pop' in order :
        if len(que) != 0  :
            print(que[0])
            del que[0]
        else :
            print(-1)

    elif 'size' in order :
        print(len(que))

    elif 'empty' in order :
        if len(que) == 0 :
            print(1)
        else :
            print(0)

    elif 'front' in order :
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    else :
        if len(que) == 0 :
            print(-1)
        else :
            print(que[-1])
