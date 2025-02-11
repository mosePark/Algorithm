def solution(k, dungeons):
    
    n = len(dungeons)
    visited = [False] * len(dungeons)
    max_count = 0
    
    def DFS(curr_k, cnt) :
        nonlocal max_count
        max_count = max(cnt, max_count)

        for i in range(n) :
            if not visited[i] and dungeons[i][0] <= curr_k :
                visited[i] = True
                DFS(curr_k-dungeons[i][1], cnt+1)
                visited[i] = False
    
    DFS(k, 0)
    
    return max_count




