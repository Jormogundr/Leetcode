"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

0 <= nums.length <= 3000
-105 <= nums[i] <= 10E5
"""

# https://www.youtube.com/watch?v=jzZsG8n2R9A
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        r = n - 1
        res = []

        for i, x in enumerate(nums):
            # avoid triplet duplicates since nums is sorted
            if i > 0 and x == nums[i - 1]:
                continue

            l = i + 1
            # use binary search and fact that list is sorted to make decisions about which direction to slide l,r pointers
            while l < r:
                threeSum = x + nums[l] + nums[r]
                if threeSum > 0:
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    res.append([x, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [
        [-1,0,1,2,-1,-4]
    ]
    output = [
        [[-1,-1,2],[-1,0,1]]
    ]

    for i,case in enumerate(cases):
        solve = Solution().threeSum(case) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()