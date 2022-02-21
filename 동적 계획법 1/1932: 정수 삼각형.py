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

# 정답 코드
def sol(arr) :
    for i in range(1, len(arr)) :
        for j in range(i+1) :
            if j == 0 :
                arr[i][j] += arr[i-1][j]
            elif j == i :
                arr[i][j] += arr[i-1][j-1]
            else :
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
    return max(arr[-1])

n = int(input())
arr = []
for _ in range(n) :
    nums = list(map(int,input().split()))
    arr.append(nums)

print(sol(arr))
