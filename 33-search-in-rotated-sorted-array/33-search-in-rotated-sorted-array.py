class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First Compute the Minimum Value in the Rotated Sorted Array
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = int((low + high)/2)
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        start = low
        
        #print("Low here is", start)
        
        low = 0
        high = len(nums) - 1
        
        if nums[start] <= target and nums[high] >= target:
            low = start
        else:
            high = start
        
        # Singular Element Edge case, can also decide to fix this by using <= in the main binary search API call.
        while low <= high:
            mid = int((low + high)/2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
                