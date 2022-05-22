"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 1E4
-1E4 < nums[i], target < 1E4
All the integers in nums are unique.
nums is sorted in ascending order.
"""

class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1

def testCases():
    nums = [-1,0,3,5,9,12]
    target = 9
    output = 4
    solve = Solution().search(nums, target)
    if solve == output:
        print("pog")
    else:
        print("not pog")

def main():
    testCases()

if __name__ == "__main__":
    main()