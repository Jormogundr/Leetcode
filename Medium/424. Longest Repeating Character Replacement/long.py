"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:

1 <= s.length <= 10E5
s consists of only uppercase English letters.
0 <= k <= s.length

"""


class Solution:

    # Current flaw is that it does not really account for preceding characters to s[i]. In some cases, the maximum length depends on a long substring of matching chars that come later in s. 
    # For example, for an input ("ABBB", 2) we'd get an output of 3 when it should be 2.
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        # Check for empty string and string of one char size
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return n
        if k == n:
            return n

        i, max = 0, 0
        while i < n:
            removeCount = k
            charCount = 1
            largestString = s[i]
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    charCount += 1
                    largestString += s[j]
                elif removeCount > 0: 
                    removeCount -= 1
                    charCount += 1
                    largestString += s[i]
                else:
                    i = j - 1
                    break
            i += 1
            if charCount > max:
                max = charCount
                maxString = len(largestString)
        
        return maxString
                
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [("ABBB", 2), ("BAAA", 0), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0), ("B", 1), ("", 0), ("AABABBA", 1), ("ABAB", 2)]
    output = [4, 3, 1, 1, 0, 4, 4]
    for i,case in enumerate(cases):
        s, k = case[0], case[1]
        solve = Solution().characterReplacement(s, k) 
        
        if solve == output[i]:
            print("Success ", case, solve, " = ", output[i])
        else:
            print("Fail ", case, solve, " =/= ", output[i])


def main():
    testCases()

if __name__ == '__main__':
    main()