class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        resultVal = len(nums)
        
        for i in range(len(nums)):
            resultVal ^= i
            resultVal ^= nums[i]
        return int(resultVal)