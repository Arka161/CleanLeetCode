import sys

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Inspired by https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time)
        # As my initial code read like trash using a hash map approach 
        
        final_answer = []
        nums.sort()
        
        # Why range from 0 to len(nums) - 2? We are caring about only a Triplet. 
        for i in range(len(nums) - 2):
            
            # We compare ONLY RHS as it's sorted. If the element is > 0, we can skip the pass. 
            if nums[i] > 0:
                continue
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            # Renaming this for the sake of code readability 
            static_ptr = i
            
            while left < right: 
                sum_of_triplet = nums[static_ptr] + nums[left] + nums[right]
                
                if sum_of_triplet < 0:
                    left += 1
                elif sum_of_triplet > 0:
                    right -= 1
                else:
                    final_answer.append([nums[static_ptr], nums[left], nums[right]])
                    
                    # Why do we need this? Skil duplicate calculation. The question mentions the array should NOT have duplicate triplets
                    # If the question was more relaxed, you can get by without this tbh 
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    
                    left += 1
                    right -= 1
        # Return the final ans
        return  final_answer
        
        