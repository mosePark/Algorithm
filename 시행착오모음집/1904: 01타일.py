import sys
n = int(sys.stdin.readline())
def d(i) :
    if i == 1 :
        return 1
    if i == 2 :
        return 2

    else :
        return (d(i-1) + d(i-2)) % 15746

print(d(n))

'''배열에 미리 저장해서 불러오는게 더 쉬운데 이건 시간도 오래걸리고 리커전 에러도 남'''
