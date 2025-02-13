def dfs(node):
    # 현재 노드를 방문 처리
    visited[node] = True
    print(f"Visited {node}")  # 방문한 노드를 출력 (디버깅/확인 용도)
    
    # 현재 노드의 모든 인접 노드에 대해 DFS 수행
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

# 예제: 그래프와 방문 배열 초기화
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

visited = {node: False for node in graph}

# DFS 시작 (예: 0번 노드부터)
dfs(0)
