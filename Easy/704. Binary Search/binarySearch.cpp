#include <vector>
#include <cmath>
class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid;

        while (low <= high) {
            mid = floor((low + high)/2);
            if (nums[mid] < target) {low = mid + 1;}
            else if (nums[mid] > target) {high = mid -1;}
            else {return mid;}
        }
        return -1;
    }
};