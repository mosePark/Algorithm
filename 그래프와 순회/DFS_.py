# DFS using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    # 현재 노드에서 할 수 있는 모든 작업 수행
    # 예를 들어, 노드를 출력하거나 특정 조건을 만족하는지 확인
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# DFS using stack (iterative approach)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            
            # 현재 노드에서 할 수 있는 모든 작업 수행
            # 예를 들어, 노드를 출력하거나 특정 조건을 만족하는지 확인
            
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return visited

'''
기본적인 설명 구조 (recursion)
'''

    A
   / \
  B   C
 / \   \
D   E   F

# (1) dfs(graph, 'A', set()) 함수가 호출됩니다.
    '''
    노드 A를 방문 처리하고 출력합니다.
    노드 A의 인접 노드인 B, C에 대해 재귀 호출을 합니다.
    
    Call Stack: dfs(graph, 'A', set())
    Visited: {'A'}
    Output: A
    '''

# (2) 노드 B에 대한 dfs(graph, 'B', set()) 함수가 호출됩니다.
    '''
    노드 A를 방문 처리하고 출력합니다.
    노드 A의 인접 노드인 B, C에 대해 재귀 호출을 합니다.

    Call Stack: dfs(graph, 'B', set())
    Visited: {'A', 'B'}
    Output: A B
    '''

# (3) 노드 D ~
    '''
    노드 D를 방문 처리하고 출력합니다.
    노드 D는 말단 노드이므로 더 이상 재귀 호출이 없습니다.

    Call Stack: dfs(graph, 'D', set())
    Visited: {'A', 'B', 'D'}
    Output: A B D
    '''

# (4) 노드 E ~

    '''
    노드 E를 방문 처리하고 출력합니다.
    노드 E의 인접 노드인 F에 대해 재귀 호출을 합니다.
    '''
    Call Stack: dfs(graph, 'E', set())
    Visited: {'A', 'B', 'D', 'E'}
    Output: A B D E

# (5) 노드 C ~

    '''
    노드 C를 방문 처리하고 출력합니다.
    노드 C의 인접 노드인 F에 대해 재귀 호출을 합니다.
    
    Call Stack: dfs(graph, 'C', set())
    Visited: {'A', 'B', 'D', 'E', 'C'}
    Output: A B D E C
    '''


# (5) 노드 F ~

    '''
    노드 F를 방문 처리하고 출력합니다.
    노드 F는 말단 노드이므로 더 이상 재귀 호출이 없습니다.
    '''
    Call Stack: dfs(graph, 'F', set())
    Visited: {'A', 'B', 'D', 'E', 'F'}
    Output: A B D E F

# (6) 모든 재귀 호출이 종료되면 DFS 알고리즘이 완료

'''
기본적인 설명 구조2 (stack)
'''

# (1) root 노드 'A'를 stack에 push합니다.
Stack: [A]
Visited: {A}

# (2) stack에서 노드 A를 pop하고, 방문 처리합니다. 그리고 A의 인접 노드 B, C를 스택에 push합니다.
Stack: [C, B]
Visited: {A}

# (3) " 이하 동문
Stack: [F, B]
Visited: {A, C}

# (4) 
Stack: [B]
Visited: {A, C, F}

# (5) 
Stack: [E, D]
Visited: {A, C, F, B}

# (6)

Stack: [D]
Visited: {A, C, F, B, E}

# (7)

Stack: []
Visited: {A, C, F, B, E, D}



