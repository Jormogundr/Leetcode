"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs):
        # Check length of the list of words - if one, return the word.
        if len(strs) == 1:
            return strs[0]

        common_prefix = ""
        longest_word = max(strs, key = len)
        

        # Checks if all items in strs are the same word. If so, return the word.
        if strs.count(strs[0]) == len(strs):
            return longest_word

        for i, c in enumerate(longest_word): # for character in the longest word in the list
            common_chars_bool = []
            common = False # flag is true when the checked char is common amongst checked words so far.
            for j, word in enumerate(strs):
                
                # Check if the word exists.
                if word == "": 
                    common = False

                # Check that we're not comparing chars in the longest word in the list.
                if word == longest_word:
                    common = True

                #  Check that we're not checking for chars that excede the length of the checked word.
                if word != longest_word and i < len(word):       
                    if c == word[i]:  
                        common = True
                    else:
                        common = False
                if word != longest_word and i >= len(word): # we're not comparing a word to itself and the char index is outside the range of the current word i.e. i >= len(word)
                    common = False 
                                       
                common_chars_bool.append(common)

            if all(common_chars_bool):
                common_prefix += c

            # if no common chars exist at ith position, return
            else:
                return common_prefix

        return common_prefix

            
                    
            

        


if __name__ == '__main__':
    expected_output = ["", "a", "", "", "flower", "fl", "a", ""]
    test_cases =  [["","b"], ["ab", "a"], ["b","cb","cab"], ["abab","aba",""],  ["flower","flower","flower","flower"], ["flower","flow","flight"], ["a"], ["dog","racecar","car"]]

    for i, case in enumerate(test_cases):
        solve = Solution().longestCommonPrefix(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")