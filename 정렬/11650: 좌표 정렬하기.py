'''정답'''
# 11650: 좌표 정렬하기
import sys
n = int(input())
arr = []
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))

answer = sorted(arr, key = lambda x : (x[0], x[1]), reverse = False)


for ans in answer :
    print(*ans)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 시행착오
import sys
n = int(input())
dic = {}
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    dic[x] = y

answer = sorted(dic.items(), key = lambda item : (item[0], item[1]), reverse=False)

'''dict 배열에서 숫자가 겹쳐서 들어가짐'''
