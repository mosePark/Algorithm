board = [[0 for j in range(100)] for i in range(100)] # 100 x 100 행렬

for _ in range(4) :
    a, b, c, d = map(int, input().split())
    for i in range(a, c) :
        for j in range(b, d) :
            if board[i][j] == 1 :
                continue
            else :
                board[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 :
            ans += 1

print(ans)
