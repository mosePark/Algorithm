# 2579: 계단 오르기
n = int(input())
arr = []
for _ in range(n) :
    number = int(input())
    arr.append(number)

ans = [0] * (n+1)

ans[0] = arr[0]
ans[1] = arr[0] + arr[1]

for i in range(3, n) :
    a = ans[i-3] + arr[i-1] + arr[i]
    b = ans[i-2] + arr[i]
    ans[i] = max(a, b)

print(ans[-2])

## 첫항, 두번째항 max 처리
n = int(input())
arr = []
for _ in range(n) :
    number = int(input())
    arr.append(number)

ans = [0] * (n+1)

ans[0] = arr[0]
ans[1] = max(arr[0] + arr[1], arr[1])
ans[2] = max(arr[0]+arr[2],arr[1]+arr[2])

for i in range(3, n) :
    a = ans[i-3] + arr[i-1] + arr[i]
    b = ans[i-2] + arr[i]
    ans[i] = max(a, b)

print(ans[-2])

### n = 1, n = 2 케이스
n = int(input())
arr = []
for _ in range(n) :
    number = int(input())
    arr.append(number)

if n == 1 :
    print(sum(arr))
elif n == 2 :
    print(sum(arr))
else :
    ans = [0] * (n+1)

    ans[0] = arr[0]
    ans[1] = max(arr[0] + arr[1], arr[1])
    ans[2] = max(arr[0]+arr[2],arr[1]+arr[2])

    for i in range(3, n) :
        a = ans[i-3] + arr[i-1] + arr[i]
        b = ans[i-2] + arr[i]
        ans[i] = max(a, b)

    print(ans[-2])
