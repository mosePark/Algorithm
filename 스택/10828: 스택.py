# 10828: 스택
import sys
n = int(sys.stdin.readline())

stk = []
for _ in range(n) :
    order = str(sys.stdin.readline())
    if 'push' in order :
        stk.append(int(order.split()[1]))

    elif 'pop' in order :
        if len(stk) != 0  :
            print(stk[-1])
            del stk[-1]
        else :
            print(-1)

    elif 'size' in order :
        print(len(stk))

    elif 'empty' in order :
        if len(stk) == 0 :
            print(1)
        else :
            print(0)

    else :
        if len(stk) == 0 :
            print(-1)
        else :
            print(stk[-1])
