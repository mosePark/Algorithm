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
