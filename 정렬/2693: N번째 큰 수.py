# 2693: N번째 큰 수
t = int(input())
for _ in range(t) :
    nums = list(map(int, input().split()))
    ans = sorted(nums, reverse=True)
    print(ans[2])
