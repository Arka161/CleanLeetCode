class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valDict = dict()
        for index,value in enumerate(nums):
            diffSum = target - value
            
            if diffSum in valDict:
                return valDict[diffSum], index
            else:
                valDict[value] = index
        return []
            
        