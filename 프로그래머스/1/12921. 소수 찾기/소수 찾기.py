# def solution(n):
    
#     nums = [i for i in range(1, n+1)]
    
#     cnt = 0
    
#     for i in nums :
#         numlist = []
#         for j in range(1, i+1) :
#             if i % j == 0 :
#                 numlist.append(j)
#         if len(numlist) == 2 :
#             cnt += 1
    
#     return cnt

# 테케 3개, 효율성 실패

# def prime_number(n) :
#     for i in range(2, int(n) :
#         if n % i == 0 :
#            return "not"

#     return "prime"
        

# def solution(n):
    
#     nums = [i for i in range(1, n+1)]
    
#     cnt = -1
    
#     for i in nums :
#         if prime_number(i) == 'prime' :
#             cnt += 1
#         else :
#             cnt += 0
    
#     return cnt

def solution(n):
    
    if n < 2:
        return 0
    
    isprime = [True] * (n + 1)
    isprime[0] = False
    isprime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if isprime[i]:
            for j in range(i * i, n + 1, i):
                isprime[j] = False

    return sum(isprime)