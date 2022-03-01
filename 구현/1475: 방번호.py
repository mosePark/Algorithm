# 1475: 방번호
n = str(input())

numbers = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
}

for num in n :
    num = int(num)
    if num == 9 :
        numbers[6] += 1
    else :
        numbers[num] += 1

if numbers[6] % 2 == 0 :
    numbers[6] = int(numbers[6]) // 2
else :
    numbers[6] = (int(numbers[6]) // 2) + 1

print(max(numbers.values()))
