# 2609: 최대공약수와 최소공배수 
import math
a, b = map(int, input().split())

def lcm(a,b):
  return (a * b) // math.gcd(a,b)

print(math.gcd(a, b))
print(lcm(a, b))
