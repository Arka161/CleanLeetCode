class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: [1,2,3,4]
        # Form Left Array - [1, 1, 2, 6]
        # Form Right Array - [24,12, 4, 1]
        
        left_arr = [0] * len(nums)
        
        left_arr[0] = 1
        
        for index in range(1, len(nums)):
            left_arr[index] = left_arr[index - 1] * nums[index - 1]
            
        right_arr = [0] * len(nums)
        
        right_arr[len(nums) - 1] = 1
        
        for index in range(len(nums) - 1, 0, -1):
            right_arr[index - 1] = right_arr[index] * nums[index]
        
        return [num1 * num2 for num1, num2 in zip(left_arr, right_arr)]
        
        
        
        