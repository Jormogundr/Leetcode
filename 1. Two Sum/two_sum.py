class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    obj = Solution().twoSum(nums, target)
    print()