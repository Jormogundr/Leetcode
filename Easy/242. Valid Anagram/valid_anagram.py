"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters."""

class Solution:

    # This is O(n), where n is the size of the strings. This function iterates through chars c in string s and finds the first matching char
    # in string t at index j, then breaks the string t into two parts, omitting the index j before joining the two substrings together. If c
    # is not found in t, then return false. 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        for c in s:
            if c in t:
                j = t.index(c) # find the index of the first occurence of c in t 
                t = t[:j] + t[j+1:] # then remove that char from the string. Strings are immutable in Python so do it inplace
                continue
            else:
                return False
        return True
    
    # This method below makes use of the Counter dictionary subclass. A Counter is a dict subclass for counting hashable objects. 
    # It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Note
    # that a hashable object in python is any immutable object - such as a string (s,t)! Check here for more info:
    # https://docs.python.org/3/library/collections.html#collections.Counter

    # def isAnagram(self, s: str, t: str) -> bool:
	# return collections.Counter(s) == collections.Counter(t)


def testCases(test_cases, expected_output):
    for i, case in enumerate(test_cases):
        s, t = case[0], case[1]
        solve = Solution().isAnagram(s, t)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")

if __name__ == '__main__':
    expected_output = [False, True, False, True, False, True, False, False]
    test_cases =  [["aacc", "ccac"], ["anagram", "nagaram"], ["rat", "car"], ["", ""], ["a", "c"], ["maltmaangiao", "amalgamation"], ["a", "ab"], ["man", "a"]]
    testCases(test_cases, expected_output)
