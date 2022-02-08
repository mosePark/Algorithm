# 1037: 약수
n = int(input())
arr = list(map(int, input().split()))
sorted = sorted(arr)

if n == 1 :
    print(arr[0]**2)
else :
    print(sorted[0]*sorted[-1])
