# 1026: 보물

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

ans = 0

for i in range(n) :
    ans += a[i] * b[i]

print(ans)
