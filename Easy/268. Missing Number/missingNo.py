"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(self, nums):
        sum = 0
        nums.sort()
        numRange = range(0, len(nums))
        for i, num in enumerate(nums):
            if numRange[i] != num:
                return numRange[i]
            

def main():
    cases = [[9,6,4,2,3,5,7,0,1]]
    output = [8] 
    

    for i, case in enumerate(cases):
        solve = Solution().missingNumber(case)

        if solve == output[i]:
            print("Noice")
        else:
            print("wtf")

if __name__ == "__main__":
    main()