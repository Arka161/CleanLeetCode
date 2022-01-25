/*

This solution uses O(n) space and O(1) time. The logic is directly inspired by https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach

*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // Example Input: [1, 2, 3, 4]
        
        // Why am I using static_cast? The size operator in C++ returns a size_t datatype, which is not the same as int.
        int arrSize = static_cast<int>(nums.size());
        
        if (arrSize <= 1) {
            return nums;
        }
        
        std::vector<int> left(arrSize);
        std::vector<int> right(arrSize);
        
        int leftMost = 1;
        int prodLeft = 1;
        
        left[0] = 1;
        
        for (int i = 1; i < arrSize; i++) {
            prodLeft = prodLeft * nums[i - 1];  
            left[i] = prodLeft;
        }
        
        // Example LeftArray: [1,1,2,6]

        right[arrSize - 1] = 1;
        int prodRight = 1;
        for (int i = arrSize - 2; i >= 0; i--) {
            prodRight = prodRight * nums[i + 1];
            right[i] = prodRight;
        }
        // Example RightArray: [24, 12, 4, 1]
        
        // Multiply Left and Right to get the answer
        for (int j = 0 ; j < arrSize ; j++) {
            auto prevLeft = left[j];
            left[j] = prevLeft * right[j];
        }
        return left;
    }
};
