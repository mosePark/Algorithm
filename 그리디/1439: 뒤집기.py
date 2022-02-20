# 1439: 뒤집기
import sys
s = sys.stdin.readline()

zero_cnt = 0
one_cnt = 0

for i in range(len(s) - 1) :
    if s[i] != s[i+1] and s[i] == "0" :
        zero_cnt += 1
    elif s[i] != s[i+1] and s[i] == "1" :
        one_cnt += 1

print(min(one_cnt, zero_cnt))
