# 11729: 하노이 탑 이동 순서
'''

n번째 원판을 목적지(third)에 두고 - (1)
1부터 (n-1)번째 원판을 중간 기둥에 옮긴다. (2)

(2) 의 과정을 recursion 한다.
n-1번째 원판을 목적지에 두고
1부터 (n-2) 원판을 다른 기둥에 옮긴다.

원판이 최종으로 1개가 남을 때까지 재귀 호출을 한다.

'''

n = int(input())

print((2**n) - 1) # 옮긴 횟수 K

# second는 보조 역할, N-1 개의 작은 순 원판을 놓을 자리, third는 가장 큰 원판을 놓을 자리
def Move_Hanoi(N, start, end, mid) : # n개의 원판을 start에서 end로 간다. (mid는 보조 자리 역할, 즉 2번)
  if N == 1 : # 종료조건, 원판이 단 하나 남았을때 종료
    print(start, end) # 1개를 start에서 end로 간다.
    return
  else :
    Move_Hanoi(N-1, start, mid, end) # n-1개의 작은 원판(가장 큰 밑바닥 원판 제외)를 보조(mid)로 옮긴다.
    print(start, end) # 위 과정에서 남은 가장 밑바닥 원판을 end로 옮긴다.
    Move_Hanoi(N-1, mid, end, start) # 보조에 있던 n-1개를 목표지점(end)로 옮긴다.

Move_Hanoi(n, 1, 3, 2)
