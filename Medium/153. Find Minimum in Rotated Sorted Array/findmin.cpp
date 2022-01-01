#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        // Check for empty arrays and arrays of length 1.
        if (nums.size() == 0) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }

        // Check if the array is rotated or not. 
        if (nums[0] < nums[nums.size() - 1]) {
            return nums[0];
        }

        // Use binary search to find the minimum element. 
        int left = 0;
        int right = nums.size();

        while (right >= left) {
            int mid = left + (right - left) / 2;

            // Check for the inflection point, i.e. the contiguous two elements where max becomes min over indices n and n + 1
            if (nums[mid] < nums[mid - 1]) {
                return nums[mid];
            }
            if (nums[mid] > nums[mid + 1]) {
                return nums[mid + 1];
            }
            if (nums[mid] > nums[0]) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return 0;
    }
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void testCases() {
    vector<vector<int>> cases {
                                {5,1,2,3,4}, 
                                {2,3,4,5,1},
                                {0,1,2,3,4,5,6,7}, 
                                {4,5,6,7,0,1,2},
                                {3,4,5,1,2}
    };
    
    vector<int> output {1, 1, 0, 0, 1};
    for (int i = 0; i < cases.size(); i++) {
        int solution = Solution().findMin(cases[i]);

        if (solution == output[i]) {
            cout << "Success " << endl;
        }
        else {
            cout << "Fail " << endl;
        }
    }
}

int main() {
    testCases();
    return 0;
}