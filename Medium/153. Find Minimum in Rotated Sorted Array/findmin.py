"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

from typing import List
import timeit

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Check for empty list and single element 
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Check if list is rotated. If not, we know the first element is the min. Checking this outright can save us a lot of time in the cases where the list is not rotated.
        if nums[0] < nums[-1]:
            return nums[0]

        # Binary search. Splits search for min in nums by half with each iteration. New index is determined by neighbors of the middle element.
        left, right = 0, len(nums)

        while right >= left:
            mid = left + (right - left) // 2

            # Check for the inflection point i.e. the contiguous two elements that define the where the max becomes min
            if nums[mid] < nums[mid - 1]: 
                return nums[mid]
            if nums[mid] > nums[mid + 1]: 
                return nums[mid + 1]
            if nums[mid] > nums[0]: # look right of mid
                left = mid + 1
            else: # look left of mid
                right = mid - 1
            


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    # Leetcode test cases. Arrays are rotated AT LEAST once, and no more then n times (where n is the length of the array). Note that n rotations results in the 'appearance' of no rotations.
    cases = [[5,1,2,3,4], [2,3,4,5,1],[0,1,2,3,4,5,6,7], [4,5,6,7,0,1,2], [3,4,5,1,2]]
    output = [1, 1, 0, 0, 1]
    for i,case in enumerate(cases):
        solve = Solution().findMin(case) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()
        