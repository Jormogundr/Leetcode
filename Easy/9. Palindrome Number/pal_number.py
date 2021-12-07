# Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int):
        rem = 0
        div = x
        check = ''

        # Special cases - negatives can never be palindromes, and 0 is a palindrome
        if x < 0:
            return False
        if x == 0:
            return True

        while div != 0:
            rem = div % 10 # this operation allows us to 'pop' the most significant digit from x
            div = div // 10 
            check += str(rem)
        
        if check == str(x):
            return True
        else:
            return False

def testCases(test_cases, expected_output):
    for i, case in enumerate(test_cases):
        solve = Solution().isPalindrome(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")

if __name__ == '__main__':
    expected_output = [True, True, False, False, False]
    test_cases =  [0, 121, -121, 10, -101]
    testCases(test_cases, expected_output)
        

            