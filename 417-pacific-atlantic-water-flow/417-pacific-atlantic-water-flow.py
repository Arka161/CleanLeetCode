class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return 
        
        # Row
        m = len(heights)
        
        # Column
        n = len(heights[0])
        
        atlantic = [[False for x in range(n)] for y in range(m)] 
        pacific = [[False for x in range(n)] for y in range(m)]
        
        ans = []
        visited = [[False for x in range(n)] for y in range(m)] 
        
        def dfs(mat, isPacific, i, j):
            
            if isPacific:
                visited = atlantic 
            else: 
                visited = pacific

            if visited[i][j]:
                return
            visited[i][j] = True
            
            if atlantic[i][j] and pacific[i][j]:
                ans.append([i, j])
            if i + 1 < m and mat[i + 1][j] >= mat[i][j]:
                dfs(mat, isPacific, i+1, j)
            
            if i - 1 >= 0 and mat[i - 1][j] >= mat[i][j]:
                dfs(mat, isPacific, i - 1, j)
            
            if j + 1 < n and mat[i][j + 1] >= mat[i][j]:
                dfs(mat, isPacific, i, j + 1)
                
            if j - 1 >= 0 and mat[i][j - 1] >= mat[i][j]:
                dfs(mat, isPacific, i, j - 1)
        
        for i in range(0, m):
            dfs(heights, True, i, 0)
            dfs(heights, False, i, n-1)
        for i in range(0, n):
            dfs(heights, True, 0, i)
            dfs(heights, False, m - 1, i)
            
        return ans
            
        