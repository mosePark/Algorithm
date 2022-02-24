# 3036: 링
import math

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, len(arr)) :
  if arr[0] % arr[i] == 0 :
    m = arr[0] // arr[i]
    print('{0}/1'.format(m) )
  else :
    g = math.gcd(arr[0], arr[i])
    m = arr[0] // g
    s = arr[i] // g
    print('{0}/{1}'.format(m,s))
