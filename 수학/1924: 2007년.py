x, y = map(int, input().split())
day = {
    0:'SUN',
    1:'MON',
    2:'TUE',
    3:'WED',
    4:'THU',
    5:'FRI',
    6:'SAT'
}

month = {
    0 : 0,
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
sums = 0
if x == 1 :
    print(day[y % 7])
else :
    for i in range(x) :
        sums += month[i]

    print(day[(sums+y) % 7])
