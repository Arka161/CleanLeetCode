class Solution:
    def findMin(self, nums: List[int]) -> int:
        startPtr = 0
        endPtr = len(nums) - 1
        
        while startPtr < endPtr:
            mid = int((startPtr + endPtr)/2)
            
            if nums[mid] > nums[endPtr]:
                startPtr = mid + 1
            else: 
                endPtr = mid
        return nums[startPtr]