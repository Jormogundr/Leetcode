"""
Given a string s, find the length of the longest substring without repeating characters.

0 <= s.length <= 5 * 10E4
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    # Original implementation. Fails several test cases.
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     longest_substring = []
    #     substring = []

    #     for i in range(0, len(s)):
    #         substring.append(s[i])
    #         for j in range(i + 1, len(s)):
    #             if s[j] not in substring:
    #                 substring.append(s[j])
    #                 break
    #             else:
    #                 substring = []
                    
    #         if substring not in longest_substring:
    #             longest_substring.append(substring)
    
    #     # Check if any longest substring was found - if so, return 0. Otherwise, return the length.
    #     if len(longest_substring) == 0:
    #         return 0
    #     else:
    #         ret = max([len(i) for i in longest_substring])
    #         return ret

    # Sliding window implementation. Often used in finding substrings. 
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            used[c] = i

        
        return max_length
                
if __name__ == '__main__':

    test_cases = ["abcabcbb", "dvdf", "aab" ,"bbbbb", "pwwkew", ""]
    expected_output = [3,3,2,1,3,0]
    for i, string in enumerate(test_cases):
        sol = Solution().lengthOfLongestSubstring(string)
        if sol == expected_output[i]:
            print(string, sol, " correct!")
        else:
            print(string, sol, " incorrect!")