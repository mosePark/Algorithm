# 11651: 좌표 정렬하기 2
import sys
n = int(input())
arr = []
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x,y])

answer = sorted(arr, key = lambda x : (x[1], x[0]), reverse = False)


for ans in answer :
    print(*ans)
