# 10814: 나이순 정렬
n = int(input())
arr = []

for i in range(n) :
    x, y = input().split()
    x = int(x)
    y = str(y)
    arr.append([x, y, i])

arr = sorted(arr, key = lambda x : (x[0], x[2]))

for result in arr :
    print(result[0], result[1], sep = ' ')
