# 9012: 괄호
t = int(input())

for _ in range(t) :
    s = input().rstrip()
    stk = []
    answer = 0
    for i in s :

        if len(stk) == 0 and i == ")" :
            answer += 1
            break

        if i == "(" :
            stk.append(i) # PUSH
            answer += 1
        else :
            if stk :
                stk.pop() # POP
                answer -= 1
            else :
                stk.append(")")

    if answer == 0 :
        print("YES")
    else :
        print("NO")
