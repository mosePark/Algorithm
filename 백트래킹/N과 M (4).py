# 15652: N과 M (4)
from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
arr = list(combinations_with_replacement(nums, m))
ans = sorted(arr)

for out in ans :
    print(' '.join(map(str, out)))
    
'''백트래킹 기본예제 4개를 itertools 안쓰고 직접 구현해보기'''
