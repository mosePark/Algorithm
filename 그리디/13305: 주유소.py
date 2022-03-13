# 13305: 주유소
n = int(input()) # 도시의 수
km = list(map(int, input().split())) # 각 도시 사이 거리 (n-1)개
city = list(map(int, input().split())) # n개 도시
result = km[0] * city[0]

for i in range(1, n-1) :
    if city[i-1] > city[i] :
        result += km[i] * city[i]
    else : # 전것이 다음것보다 더 싸면 그대로 유지
        city[i] = city[i-1]
        result += km[i] * city[i]

print(result)
