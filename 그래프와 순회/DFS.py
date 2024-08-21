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
기본적인 설명 구조
'''

    A
   / \
  B   C
 / \   \
D   E   F


# (1) root 노드 'A'를 stack에 push합니다.
Stack: [A]
Visited: {A}

# (2) stack에서 노드 A를 pop하고, 방문 처리합니다. 그리고 A의 인접 노드 B, C를 스택에 push합니다.
Stack: [C, B]
Visited: {A}

# (3) 이하 동문
Stack: [F, B]
Visited: {A, C}

# (4) 이하 동문
Stack: [B]
Visited: {A, C, F}

# (5) 이하 동문
Stack: [E, D]
Visited: {A, C, F, B}

# (6)

Stack: [D]
Visited: {A, C, F, B, E}

# (7)

Stack: []
Visited: {A, C, F, B, E, D}
