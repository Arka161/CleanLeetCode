class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val_dict = dict() 
        for i in nums:
            if i in val_dict:
                return True
            else:
                val_dict[i] = 0
        return False