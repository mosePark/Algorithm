# 9184: 신나는 함수 실행
A = {}

def w(a, b, c) :

    if (a, b, c) in A :
        return A[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0 :
        A[(a, b, c)] = 1
        return A[(a, b, c)]

    if a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    if a < b and b < c :
        A[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return A[(a, b, c)]

    else :
        A[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return A[(a, b, c)]


while True :

    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1 :
        break

    print("w(%d, %d, %d)"%(a, b, c), "=",int(w(a, b, c)))
