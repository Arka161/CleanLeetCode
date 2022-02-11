class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        result = 0
        start_ptr = 0
        end_ptr = len(height) - 1
        
        # Two pointer, optimize and find the best window
        # When h[i] == h[j], it should not matter which path you're taking as a choice. 
        
        while start_ptr != end_ptr:
            area_here = (end_ptr - start_ptr) * min(height[start_ptr], height[end_ptr])
            result = max(result, area_here)
            
            if height[start_ptr] < height[end_ptr]:
                start_ptr += 1
            else:
                end_ptr -= 1
        return result
            