class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            currMin = 1
            currMax = 1
            
            # We keep nums[0] here for the singular element case.
            answer = nums[0]
            for i in nums:
                tempArray = [i, i * currMin, i * currMax]
                currMax = max(tempArray)
                currMin = min(tempArray)
                
                answer = max(answer, currMax)
                
            return answer