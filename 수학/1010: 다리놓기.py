# 1010: 다리 놓기
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
    return number

t = int(input())
for _ in range(t) :
    r, n = map(int, input().split())
    ans = factorial(n) // (factorial(r) * factorial(n-r) )
    print(ans)
