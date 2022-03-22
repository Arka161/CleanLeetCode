class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longestVal = 0
        
        for n in nums:
            if (n - 1) not in numSet:
                leng = 0
                while (n + leng) in numSet:
                    leng += 1
                longestVal = max(longestVal, leng)
        return longestVal