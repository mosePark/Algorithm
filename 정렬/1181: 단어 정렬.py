# 1181: 단어 정렬

n = int(input())
arr = set()
for _ in range(n) :
    st = input()
    arr.add(st)


answer = sorted(arr, key = lambda x : (len(x), x))

for ans in answer :
    print(ans)
