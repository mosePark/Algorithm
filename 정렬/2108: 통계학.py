# 2108: 통계학
# n은 홀수
import sys
n = int(input())
arr = []
dic = {}

if n == 1 :
    x = int(sys.stdin.readline())
    print(x)
    print(x)
    print(x)
    print(0)

else :
    for i in range(n) :
        x = int(sys.stdin.readline())
        arr.append(x)

        if x in dic :
            dic[x] = dic[x] + 1
        else :
            dic[x] = 1

    arr = sorted(arr)

    dic_result = sorted(dic.items(), key = lambda x : (-x[1], -x[0])) # 최빈값 두번째로 작은 값 찾기, 정렬 조건 2개 기입

    mode = []
    for key, value in dic_result: # value로 key 값 찾기
        if max(dic.values()) == value:
            mode.append(key)

    print(round(sum(arr)/len(arr)))
    print(arr[((1+n) // 2)-1])

    if len(mode) > 1 :
        print(mode[-2])
    else :
        print(mode[0])

    print(arr[len(arr)-1]-arr[0])
