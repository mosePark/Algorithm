# 11399: ATM
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sorted_arr = sorted(arr)

ans = 0
for i in range(n) :
    ans += sum(sorted_arr[:i+1])

print(ans)
