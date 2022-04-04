class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        atlantic = [[False for x in range(cols)] for y in range(rows)]
        pacific = [[False for x in range(cols)] for y in range(rows)]
        
        ans = []
        
        visited = [[False for x in range(cols)] for y in range(rows)]
        
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
                
            if i + 1 < rows and mat[i + 1][j] >= mat[i][j]:
                dfs(mat, isPacific, i + 1, j)

            if i - 1 >= 0 and mat[i - 1][j] >= mat[i][j]:
                dfs(mat, isPacific, i - 1, j)
            
            if j + 1 < cols and mat[i][j + 1] >= mat[i][j]:
                dfs(mat, isPacific, i, j + 1)
                
            if j - 1 >= 0 and mat[i][j - 1] >= mat[i][j]:
                dfs(mat, isPacific, i, j - 1)
        for i in range(0, rows):
            dfs(heights, True, i, 0)
            dfs(heights, False, i, cols-1)
        for i in range(0, cols):
            dfs(heights, True, 0, i)
            dfs(heights, False, rows - 1, i)
            
        return ans