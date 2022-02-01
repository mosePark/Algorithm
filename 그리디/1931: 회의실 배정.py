# 1931: 회의실 배정
import sys
n = int(sys.stdin.readline()) # 회의 수
arr = []

for _ in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr = sorted(arr, key = lambda x : (x[1], x[0]))

cnt = 0
end = 0 # end point 0

for a, b in arr :
    if a >= end :
        cnt += 1
        end = b
print(cnt)

'''회의를 최대한 많이 + 회의가 끝나는시간과 시작시간이 같은 경우 이어갈 수 있다는 점'''
'''정렬을 끝나는시간으로 먼저한 후 끝나는 시간이 동일하면 시작시간이 빠른걸로'''
