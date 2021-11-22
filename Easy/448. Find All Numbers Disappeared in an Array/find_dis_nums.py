# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums):
        # disappeared = [num for num in range(1, len(nums) + 1) if num not in nums] -- this brute force both take O(n^2), way too long for large lists!
        
        
        
            
        



if __name__ == '__main__':
    test_cases = [[4,3,2,7,8,2,3,1], [1,1]]

    for nums in test_cases:
        solved = Solution().findDisappearedNumbers(nums)
        print(solved)