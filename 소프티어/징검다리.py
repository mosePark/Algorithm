##% 1차시도
import sys
input = sys.stdin.readline

N = int(input()) # 돌의 개수
arr = list(map(int, input().split()))

def stone(N, arr) :
    
    walk = []
    
    if N != len(arr) :
        arr.pop(0)
    else :
        pass

    walk.append(arr[0])
    
    for i in range(len(arr)-1) :
        if arr[i] > arr[i+1] :
            stone(N-1, arr)
        else :
            walk.append(arr[i+1])
            stone(N-1, arr)
    return len(walk)

print(stone(N, arr))


##% 2차시도
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[-1] * (N + 1) for _ in range(N)]

def stone(index, prev_index):
    if index == N:
        return 0

    if dp[index][prev_index + 1] != -1:
        return dp[index][prev_index + 1]

    length = stone(index + 1, prev_index)

    if prev_index == -1 or arr[index] > arr[prev_index]:
        length = max(length, 1 + stone(index + 1, index))

    dp[index][prev_index + 1] = length
    return length

print(stone(0, -1))
