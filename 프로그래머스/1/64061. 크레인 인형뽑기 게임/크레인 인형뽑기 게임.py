def solution(board, moves):
    result = 0
    box = []
    for col in moves :
        for row in range(len(board)) :
            val = board[row][col-1]
            if val != 0 :
                if len(box) >= 1 and box[-1] == val :
                    box.pop()
                    result += 2
                    board[row][col-1] = 0
                else :
                    box.append(val)
                    board[row][col-1] = 0
                break
    return result