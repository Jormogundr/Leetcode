"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Constraints:

The input must be a binary string of length 32.

"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([x for x in bin(n) if '1' in x])


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [int(0b00000000000000000000000000001011), int(0b00000000000000000000000010000000)]
    output = [3, 1]
    for i,case in enumerate(cases):
        solve = Solution().hammingWeight(case) 
    
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()