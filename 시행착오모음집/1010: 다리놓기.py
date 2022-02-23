from itertools import combinations
t = int(input())

for _ in range(t) :
    r, n = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    print(len(list(combinations(arr, r))))

# nCr = (n-1)C(r-1) + (n-1)C(r)

def combi(n, r) :
    if n == r or r == 0 :
        return 1
    else :
        ans = combi(n - 1, r - 1) + combi(n-1, r)
        return ans

t = int(input())

for _ in range(t) :
    r, n = map(int, input().split())
    print(combi(n, r))
