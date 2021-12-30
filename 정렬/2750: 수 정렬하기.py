# 2750: 수 정렬하기
n = int(input())
nums = []
for _ in range(n) :
    nums.append(int(input()))

for i in sorted(nums) :
    print(i)
