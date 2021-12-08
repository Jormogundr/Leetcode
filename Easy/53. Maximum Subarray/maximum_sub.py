""""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""


class Solution:
    def maxSubArray(self, nums) -> int:
        pass
        

if __name__ == '__main__':
    expected_output = [[1, 1, 1], [9, 9], [24,12,8,6], [0,0,9,0,0], [], []]
    test_cases =  [[-1, -1, -1], [9,9], [1,2,3,4], [-1,1,0,-3,3], [], [1]]

    for i, case in enumerate(test_cases):
        solve = Solution().productExceptSelf(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")