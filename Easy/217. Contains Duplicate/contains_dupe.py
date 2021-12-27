# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
import timeit 

class Solution:

    # This function works but it's way too slow! In the worst case, it's O(logn). Not bad, but not good enough to pass.
    def containsDuplicateSlow(self, nums) -> bool:
        # Look ahead at every element in the list starting from index i for a matching integer. 
        # We don't need to look behind if we look ahead for every index.
        dupes = [i for i, num in enumerate(nums) if (num in nums[i+1::])]
        if len(dupes) == 0:
            return False
        else: 
            return True

    # Better yet, convert nums to a set -- the lookup times in a set are extraordinarily faster than lookup times in a list, it's O(1)!
    # We exploit a unique property of sets here - namely, that every element in a set is UNIQUE. Therfore, if we match the length of the passed
    # list (where elements can be duplicates) against the length of the set, we can determine if the list contains duplicates! If len(nums) != len(set(nums)),
    # then there is a duplicate.
    def containsDuplicateFast(self, nums) -> bool:
        if len(nums) != len(set(nums)):
            return True # list contains a duplicate
        else:
            return False


def testCases(test_cases, expected_output):
    for i, case in enumerate(test_cases):
        solve = Solution().containsDuplicateFast(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")

if __name__ == '__main__':
    expected_output = [True, False, True, True, False, True, True, False]
    test_cases =  [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2], [1,1,1], [], [3,3,2,1], [1,2,3,2,1], [-3, 0, 3]]

    testCases(test_cases, expected_output)

