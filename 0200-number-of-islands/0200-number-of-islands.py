class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        cnt = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        for i in range(rows) :
            for j in range(cols) :
                if grid[i][j] == "1" :
                    cnt += 1
                    self.DFS(grid, i, j, rows, cols, directions)

        return cnt         
                 
    def DFS(self, grid, i, j, rows, cols, directions) :
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1' :
            return

        grid[i][j] = "0"

        for d in directions :
            ii = i + d[0]
            jj = j + d[1]
            self.DFS(grid, ii, jj, rows, cols, directions)