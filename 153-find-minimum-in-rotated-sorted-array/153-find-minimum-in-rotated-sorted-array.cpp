class Solution {
public:
    int findMin(vector<int>& nums) {
        // Algorithm - Simple Binary Search. 
        int start = 0;
        int end = static_cast<int>(nums.size());
        end--;
        
        while (start < end) {
            if (nums[start] < nums[end]) {
                // Already sorted correctly or in a normal array segment
                return nums[start];
            }
            
            int mid = (start + end) / 2;
            
            if (nums[mid] >= nums[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return nums[start];
    }
};