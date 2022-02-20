# 1439: 뒤집기

def solution(s) :
    global one_cnt, zero_cnt

    for i in range(len(s)) :
        if s[0] == "0" :
            if s[i] == s[0]:
                continue
            else:
                zero_cnt += 1
                solution(s[i:])
        else :
            if s[i] == s[0]:
                continue
            else:
                one_cnt += 1
                solution(s[i:])

one_cnt = 0
zero_cnt = 0

solution(str(input()))

print(min(zero_cnt, one_cnt))
