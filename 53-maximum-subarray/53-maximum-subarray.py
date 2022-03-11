class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        basicSum = nums[0]
        maxVal = nums[0]
        # [-2,1,-3,4,-1,2,1,-5,4]
        # Output: 6
        #[1, 2, 3, 4]
        for i in range(1, len(nums)):
            basicSum = nums[i] + basicSum
            
            if basicSum < nums[i]:
                basicSum = nums[i]
            
            #print("BASIC SUM HERE IS", basicSum)
            maxVal = max(maxVal, basicSum)
            #print("MAX VAL HERE IS", )
            if basicSum < 0:
                basicSum = 0
        return maxVal