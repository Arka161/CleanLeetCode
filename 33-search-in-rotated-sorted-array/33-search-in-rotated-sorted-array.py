class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find minimum 
        low_val = 0
        high_val = len(nums) - 1
        
        while low_val < high_val:
            mid = int((low_val + high_val)/2)
            
            if nums[mid] > nums[high_val]:
                low_val = mid + 1
                
            else:
                high_val = mid
                
        # start here is the index of the minimum value
        start = low_val
        end = len(nums) - 1
        new_low = 0
        new_high = 0
        if target >= nums[start] and target <= nums[end]:
            new_low = start
            new_high = end
        else:
            new_low = 0
            new_high = start
        
        while new_low <= new_high: 
            mid = int((new_low + new_high) / 2)
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                new_high = mid - 1
            else:
                new_low = mid + 1
        return -1
        
        
        
        