#include<algorithm>

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        // Approach - Dynamic Programming
        
        int curMax = 1;
        int curMin = 1;
        
        int result = nums[0]; 
        
        // Why do we need to store the minimum value? Because negative values can shift the maximum value, and thus the answer.

        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            int currentNum = nums[i];
            
            std::vector<int> maxList = {currentNum, currentNum * curMin, currentNum * curMax};
            curMax = *std::max_element(maxList.begin(), maxList.end());
            curMin = *std::min_element(maxList.begin(), maxList.end());
            
            result = std::max(result, curMax);
        }
        
        return result;
    }
};