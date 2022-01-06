# 10773: 제로

import sys
k = int(sys.stdin.readline())
stk = []
for _ in range(k) :
    n = int(sys.stdin.readline())
    if n != 0 :
        stk.append(n)
    else :
        stk.pop()

print(sum(stk))
