"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

1 <= k <= nums.length <= 1E4
-1E4 <= nums[i] <= 1E4

"""

class Solution:
    # O(nlogn)
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]


def main():
    cases = [[[3,2,1,5,6,4], 2]]
    output = [5] 
    

    for i, case in enumerate(cases):
        k = case[1]
        nums = case[0]
        solve = Solution().findKthLargest(nums, k)

        if solve == output[i]:
            print("Noice")
        else:
            print("wtf")

if __name__ == "__main__":
    main()