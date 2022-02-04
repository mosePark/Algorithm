'''n과 m 시리즈 직접 구현 해보기'''

from itertools import product

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
arr = list(product(nums, repeat = m))
ans = sorted(arr)

for out in ans :
    print(' '.join(map(str, out)))
