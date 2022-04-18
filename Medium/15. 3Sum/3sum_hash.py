"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

0 <= nums.length <= 3000
-105 <= nums[i] <= 10E5
"""

# So close -- just can't eliminate triplet duplicates! Most solutions rely on sorting nums first then using binary search.
# Currently incomplete until I can figure out the duplicate triplet problem.
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return []
            
        output = []
        map = {x:i for (i,x) in enumerate(nums)}

        for i in range(0, n):
            b = 0 - nums[i]
            for j in range(i, n):
                if i == j:
                    continue
                nums_k = b - nums[j]
                if nums_k in map:
                    k = map[nums_k]
                    if k != j and i != k:
                        output.append([nums[i], nums[j], nums[k]])
                    del map[nums_k]

        return output


            


        

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