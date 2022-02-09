# 1149: RGB 거리

# 정답 풀이
n = int(input())
arr = []
for _ in range(n) :
  rgb = list(map(int, input().split()))
  arr.append(rgb)

for i in range(1, len(arr)) :
  arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
  arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
  arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))
''''''
# 시행착오 풀이
n = int(input())
ans = []
for _ in range(n) :
    arr = list(map(int, input().split()))
    ans.append(arr)

result = []
result.append(min(ans[0])) # 첫번째 배열은 최소값

for i in range(1, len(ans)) :
    rgb = [0, 1, 2]
    except_num = ans[i-1].index(result[i-1])
    rgb.pop(except_num)
    result.append(min(ans[i][rgb[0]], ans[i][rgb[1]]))

print(sum(result))
