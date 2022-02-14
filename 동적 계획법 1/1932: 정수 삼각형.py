# 1932: 정수 삼각형
## 시행착오 코드
n = int(input())
arr = []
for _ in range(n) :
    nums = list(map(int,input().split()))
    arr.append(nums)

ans = 0

for i in range(1, n) :
    ans += max(arr[i-1][], arr[i-1][]) + arr[i][]

print(ans)
