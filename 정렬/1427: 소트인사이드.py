# 1427: 소트인사이드
import sys
n = str(sys.stdin.readline())
answer = sorted(n, reverse=True)
answer.pop()

print(int(''.join(answer)))

## 다른 풀이
print(sorted(input())[::-1], sep='')
