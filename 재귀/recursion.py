def recursive_function(parameter):
    # 종료 조건(base case)
    if  '조건':
        return '결과'
    
    # 재귀 호출
    return recursive_function('다음_parameter')

'''
return 뒤에 반드시 재귀함수를 추가하는 것은 아님

기본적인 구조는,

종료조건과 자기 자신을 호출하는 부분이 있으면 재귀.
'''
