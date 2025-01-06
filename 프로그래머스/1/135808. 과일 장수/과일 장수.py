# i = 0
#     0 ~ 3
# i = 1
#     4 ~ 7
# i = 2
#     8 ~ 11

def solution(k, m, score):

    score.sort(reverse=True)

    appl = []
    for i in range(0, len(score), m) :
        chunk = score[i:i+m]
        if len(chunk) != m :
            break
        appl.append(chunk)

    sales = []
    for ck in appl :   
        p = min(ck)
        sales.append(p * m)

    ans = sum(sales)
    return ans

# 1 ~ k점까지 사과가 있음
# 한상자에 m개씩, 가격은 min() * m
# 남는사과 버림
# 

# 최저사과점수 p
# 한상자에 담긴 사과 갯수 onebox_app
# 상자의 개수 box_nums

