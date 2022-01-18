# 10866: 덱
import sys
from collections import deque
n = int(sys.stdin.readline())

deq = deque()

for _ in range(n) :
    order = str(sys.stdin.readline())
    if 'push_front' in order :
        deq.appendleft(int(order.split()[1]))

    elif 'push_back' in order :
        deq.append(int(order.split()[1]))

    elif 'pop_back' in order :
        if len(deq) != 0  :
            print(deq[-1])
            del deq[-1]
        else :
            print(-1)

    elif 'pop_front' in order :
        if len(deq) != 0  :
            print(deq[0])
            del deq[0]
        else :
            print(-1)

    elif 'size' in order :
        print(len(deq))

    elif 'empty' in order :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)

    elif 'front' in order :
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    else :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[-1])
