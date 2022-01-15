"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:

1 <= s.length <= 10E5
s consists of only uppercase English letters.
0 <= k <= s.length

"""


class Solution:

    # This function works but exceeds the time limit. This is O(n^2) in the worst case. 
    # Current flaw is that it does not really account for preceding characters to s[i]. In some cases, the maximum length depends on a long substring of matching chars that come later in s. 
    # For example, for an input ("ABBB", 2) we'd get an output of 3 when it should be 2.
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """
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
            k_remaining = k
            charCount = 1
            current_sstring = s[i]
            true_substring = 1
            for j in range(i + 1, n):
                if s[i] == s[j]: # matching chars in substring
                    charCount += 1
                    current_sstring += s[j]
                    true_substring += 1
                elif k_remaining > 0: # non-matching chars but we have chars we can replace
                    k_remaining -= 1
                    charCount += 1
                    current_sstring += s[i]
                    true_substring = 1 # reset the length of the un-altered substring of matching chars
                else: # non-matching chars and k == 0
                    break
    
            i = i + true_substring # set the loop index to be next in position relative to last element of non-replaced matching substring

            if charCount + k_remaining > max:
                max = charCount
                maxString = len(current_sstring) + k_remaining # accounts for replacing chars if we reach the end of the string with k > 0
                largest_sstring = current_sstring
                if maxString > n: 
                    maxString = n # set the new max substring
        
        return maxString

                
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////                       DO NOT INCLUDE BELOW LINES IN LEETCODE SUBMISSION                      ////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def testCases():
    cases = [("IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR", 2), ("ABBB", 2), ("BAAA", 0), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0), ("B", 1), ("", 0), ("AABABBA", 1), ("ABAB", 2)]
    output = [6, 4, 3, 1, 1, 0, 4, 4]
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