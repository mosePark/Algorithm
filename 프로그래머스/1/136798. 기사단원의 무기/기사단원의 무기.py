def div_cnt(number) :
    count = 0
    for i in range(1, int(number**0.5)+1) :
       if number % i == 0 :
        if i**2 == number :
            count += 1
        else :
            count += 2

    return count

def solution(number, limit, power):
    ans = []    
    for num in range(1, number+1) :
        cnt = div_cnt(num) # 약수 세기    
        ans.append(cnt)
    for idx in range(len(ans)) :
       if ans[idx] > limit : 
        ans[idx] = power
        
    return sum(ans)