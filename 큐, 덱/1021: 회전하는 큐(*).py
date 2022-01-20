# 1021: 회전하는 큐
from collections import deque

n, m = map(int, input().split())
target_indexes = list(map(int, input().split()))
cnt = 0
arr = deque([i for i in range(1, n + 1)])

for target in target_indexes:
    while True:
        if arr[0] == target:
            arr.popleft()
            break
        else:
            if arr.index(target) <= len(arr) // 2:
                arr.rotate(-1)
            else:
                arr.rotate(1)
            cnt += 1
print(cnt)
