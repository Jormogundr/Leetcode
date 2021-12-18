/*
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
*/

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int curMax = 1;
        int curMin = 1;
        int res = nums[0];

        for(int i = 0; i < nums.size(); i++){
            int n = nums[i];
            vector<int> vals = {n, n* curMax, n * curMin};
            curMax = *max_element(vals.begin(), vals.end());
            curMin = *min_element(vals.begin(), vals.end());
            res = max(res, curMax);
        }

        return res;
    }
};

void testCases(vector<vector<int>> test_cases, vector<int> expected_output){
    for (int i = 0; i < test_cases.size(); i++){
        int solve = Solution().maxProduct(test_cases[i]);
        if (solve == expected_output[i]){
            cout << " Success" << endl;
        }
        else{
            cout << " Fail" << endl;
        }
    }
}

int main(){
    vector<int> expected_output = {0, 6};
    vector<vector<int>> test_cases =  {{-2,0,-1}, 
                                       {2,3,-2,4}};
    testCases(test_cases, expected_output);
    return 0;
}