class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = 10001
        max_val = -1
        # [7,1,5,3,6,4]
        for i in prices: 
            min_val = min(i, min_val)
            max_temp = i - min_val
            max_val = max(max_val, max_temp)
        return max_val