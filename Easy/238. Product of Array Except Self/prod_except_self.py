""""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""
from itertools import accumulate
from operator import mul

class Solution:
    # # This algo is too slow! It takes O(n*n).
    # def productExceptSelf(self, nums):
    #     # no product to return for a single elemenent list
    #     nums  = np.array(nums)
    #     if len(nums) == 1:
    #         return []

    #     prod_arr = []
    #     for i, num in enumerate(nums):
    #         prod = 1
    #         # for loop to find the product of indices past the excluded index i
    #         for j in range(i + 1, len(nums)):
    #             prod *= nums[j]
    #         # for loop to find the product of indices before the excluded index i
    #         for j in range(0, i):
    #             prod *= nums[j]
    #         prod_arr.append(prod)
    
    #     return prod_arr

    # This runs in O(n). The indices of prefix and suffix in the list comprehension ensure that i is excluded from the product of all other elements in nums. This is not an original solution.
    # For more information, check out https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach
    def productExceptSelf(self, nums):
        if len(nums) == 1:
            return []
        prefix, suffix, n = list(accumulate(nums, mul)), list(accumulate(nums[::-1], mul))[::-1], len(nums)
        return [(prefix[i-1] if i else 1) * (suffix[i+1] if i+1 < n else 1) for i in range(n)]

if __name__ == '__main__':
    expected_output = [[1, 1, 1], [9, 9], [24,12,8,6], [0,0,9,0,0], [], []]
    test_cases =  [[-1, -1, -1], [9,9], [1,2,3,4], [-1,1,0,-3,3], [], [1]]

    for i, case in enumerate(test_cases):
        solve = Solution().productExceptSelf(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")