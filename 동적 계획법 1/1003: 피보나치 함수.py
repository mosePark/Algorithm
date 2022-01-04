def fib_1(n) :
    if n == 0 :
        return 1

    elif n == 1 :
        return 0

    else :
        return fib_1(n-2) + fib_1(n-1)

def fib_2(n) :
    if n == 0 :
        return 0

    elif n == 1 :
        return 1

    else :
        return fib_2(n-2) + fib_2(n-1)

answer = []

for i in range(10) :
    answer.append([fib_1(i), fib_2(i)])

'''answer # 10 x 2 행렬'''

for _ in range(31) :
    a = answer[-1][0] + answer[-2][0]
    b = answer[-1][1] + answer[-2][1]
    answer.append([a, b]) # fib_1 결과 다음 값 계산

T = int(input())
for _ in range(T) :
    n = int(input())
    print(answer[n][0], answer[n][1], sep = ' ')
