#include<algorithm>

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        // Approach - Dynamic Programming
        
        int curMax = 1;
        int curMin = 1;
        
        int result = nums[0]; 
        
        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            int currentNum = nums[i];
            
            std::vector<int> maxList = {currentNum, currentNum * curMin, currentNum * curMax};
            int maxFromList = *std::max_element(maxList.begin(), maxList.end());
            int minFromList = *std::min_element(maxList.begin(), maxList.end());
            
            curMax = maxFromList;
            curMin = minFromList;
            
            result = std::max(result, curMax);
        }
        
        return result;
    }
};