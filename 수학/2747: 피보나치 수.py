# 2747: 피보나치 수
arr = [0] * 46
arr[0], arr[1], arr[2] = 0, 1, 1

for i in range(3, len(arr)) :
    arr[i] = arr[i-1] + arr[i-2]

print(arr[int(input())])
