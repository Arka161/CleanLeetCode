class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        bestSum = nums[0]
        
        for i in range(1, len(nums)):
            if currentSum >= 0:
                currentSum += nums[i]
            else:
                currentSum = nums[i]
            
            if currentSum > bestSum:
                bestSum = currentSum
        return bestSum