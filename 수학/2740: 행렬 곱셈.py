# 2740: 행렬 곱셈
n, m = map(int, input().split())
a = []
for _ in range(n) :
    x = list(map(int, input().split()))
    a.append(x)

m, k = map(int, input().split())
b = []
for _ in range(m) :
    y = list(map(int, input().split()))
    b.append(y)

def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

for i in range(n) :
    print(*productMatrix(a, b)[i])
