/*

This solution uses O(n) space and O(1) time. This builds up on 1.cpp. 

This is the same as 1.cpp but the only difference is that the answer array acts as the answerArray array, 
and then we multiply the left array as a variable in a separate pass. 

*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int arrSize = static_cast<int>(nums.size());
        
        if (arrSize <= 1) {
            return nums;
        }
        
        // answerArray is the right array (same logic from 1.cpp)
        std::vector<int> answerArray(arrSize);
        answerArray[arrSize - 1] = 1;  
        
        // The prod array holds the product of every element to the right of i
        int prod = 1;
        for (int i = arrSize - 2; i >= 0; i--) {
            prod = prod * nums[i + 1];
            answerArray[i] = prod;
        }
        int leftProd = 1;
        for (int i = 0; i < arrSize; i++) {
            answerArray[i] = answerArray[i] * leftProd;
            leftProd = leftProd * nums[i];
        }
        
        return answerArray;
    }
};
