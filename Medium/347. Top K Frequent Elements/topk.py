"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

1 <= nums.length <= 10E5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""


class Solution:
    def topKFrequent(self, nums, k):
        numsSet = set(nums)
        frequencyMap = {k:0 for k in numsSet}
        for num in nums:
            frequencyMap[num] += 1
        
        # sort frequencyMap keys by the frequency -- take the sorted (descending order) keys and place them in a list that is sliced from 0 to k
        ret = [x[0] for x in sorted(frequencyMap.items(), key=lambda item: item[1], reverse=True)][0:k]
        return ret


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [ 
        [ [1,2,2,3,3,3], 2 ],
        [ [1], 1 ],
        [ [-1,-1], 1]
    ]
    output = [
        [2,3], 
        [1],
        [-1]
        ]
    for i,case in enumerate(cases):
        nums = case[0]
        k = case[1]
        solve = Solution().topKFrequent(nums, k) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()