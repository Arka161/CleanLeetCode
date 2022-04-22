class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: [1,2,3,4]
        # Form Left Array - [1, 1, 2, 6]
        # Form Right Array - [24,12, 4, 1]
        
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)
        
        left_val = 1
        for index, val in enumerate(nums):
            left_arr[index] = left_val
            left_val *= nums[index]
        
        right_val = 1
        index_b = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            right_arr[index_b] = right_val
            index_b -= 1
            right_val *= nums[index]
        
        final_arr = [0] * len(nums)
        
        
        for i in range(len(nums)):
            final_arr[i] = right_arr[i] * left_arr[i]
            
        return final_arr
        
        