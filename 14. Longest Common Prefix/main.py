"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs):

        common_prefix = ""

        c = strs[0] # get the first character in the first word
        longest_word = max(strs, key = len)
        

        for i, c in enumerate(longest_word): # for character in the longest word in the list
            common = False
            for word in strs:
                if c == word[i]:
                    common = True
                else:
                    common = False

            if common:
                common_prefix += c

            # if no common chars exist at ith position, return
            else:
                return common_prefix

        return common_prefix

            
                    
            

        


if __name__ == '__main__':
    expected_output = ["fl", ""]
    test_cases = [["flower","flow","flight"], ["dog","racecar","car"]]

    for i, case in enumerate(test_cases):
        solve = Solution().longestCommonPrefix(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")