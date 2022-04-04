class Solution:
    def __init__(self):
        self.islandCounter = 0
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        ans = 0
        self.islandCounter = 0
        maxCounter = 0
        def dfs(grid, i, j):
            if i >= rows or j >= cols or grid[i][j] != 1 or i < 0 or j < 0:
                return
            self.islandCounter = self.islandCounter + 1
            #print("Island Counter is", self.islandCounter)
            grid[i][j] = 2
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        for i in range(rows):
            for j in range(cols):
                #print("loop runs")
                if grid[i][j] == 1:
                    dfs(grid, i, j)
                    ans += 1
                    maxCounter = max(maxCounter, self.islandCounter)
                    self.islandCounter = 0
                    
            
            
        return maxCounter
