class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        ans = 0
        def dfs(grid, i, j):
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    ans += 1
            
            
        return ans
