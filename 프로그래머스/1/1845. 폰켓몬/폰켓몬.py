def solution(nums):
    
    unq = set(nums)    
    ans = len(nums) // 2
    answer = min(ans, len(unq))

    return answer