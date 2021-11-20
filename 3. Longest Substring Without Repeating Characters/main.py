class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_substring = []
        substring = []

        for i in range(0, len(s)):
            substring.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in substring:
                    substring.append(s[j])
                    break
                else:
                    substring = []
                    
            if substring not in longest_substring:
                longest_substring.append(substring)
    
        # Check if any longest substring was found - if so, return 0. Otherwise, return the length.
        if len(longest_substring) == 0:
            return 0
        else:
            ret = max([len(i) for i in longest_substring]) # generates a the maximum from a list of lengths from the list of lists (longest_substring).
            return ret
                



if __name__ == '__main__':

    test_cases = ["dvdf", "aab", "abcabcbb","bbbbb", "pwwkew", ""]
    expected_output = [3,2,3,1,3,0]
    for i, string in enumerate(test_cases):
        sol = Solution().lengthOfLongestSubstring(string)
        if sol == expected_output[i]:
            print(string, sol, " correct!")
        else:
            print(string, sol, " incorrect!")