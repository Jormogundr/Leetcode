"""Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

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
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."""

class Solution:
    # This is my original take on the problem. As usual, it's O(n^2). This will BLOW up for something like [1,2,3,4,...,n], where all n[i] > 0 and n[i+1] = n[i] + 1. I looked into how to approximate a factorial of a large number (Stirling's approximation)
    # but this only complicates the problem, as I would still need to parse the entire string to make sure that all n[i] > 0 and n[i+1] = n[1], so I'm not really saving much time by making the calculation of such a rare
    # testcase faster.

    # def maxProduct(self, nums) -> int:
    #     maxproduct = nums[0]*nums[1] 
    #     maxsubarr = []

    #     i = 1
    #     while i < len(nums):
    #         product = 1
    #         for j in range(i + 1, len(nums)):
    #             product *= nums[i]*nums[j]
    #             if product > maxproduct:
    #                 maxproduct = product
    #                 i = j
    #                 break # subarr is not continuous - reset indices
    #             i += 1
    #             break 
    
    #     return maxproduct


    # No shame, stole this from the discussion board. This works much faster. My initial concern when looking this over was that it could not guarantee the maximum product of a continuous subarray, but the clever use of
    # the max() function seems to guarantee it. 
    def maxProduct(self, nums) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
            res = max(res, curMax)
            
        return res


if __name__ == '__main__':
    expected_output = [0, 6]
    test_cases =  [[-2,0,-1], [2,3,-2,4]]

    for i, case in enumerate(test_cases):
        solve = Solution().maxProduct(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")