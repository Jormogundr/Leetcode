"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order."""

# My original solution.
class Solution:
    def isValid(self, s: str) -> bool:
        
        open_parans = ['(', '[', '{']
        closing_parans = [')', ']', '}']

        # s must be of even length to be valid. Also if first char is closing parans, return false. If last char is open parans, return false.
        if len(s) % 2 != 0 or s[0] in closing_parans or s[-1] in open_parans:
            return False


        counter_round = 0 # ()
        counter_square = 0 # []
        counter_curly =  0 # {}
        must_close_next = '' # priority queue

        # Goes through each character in string s. Tracks the sum of each parans style where an open paran adds 1 to the sum and a close paran substracts 1. 
        # must_close_next maintains the order of closing for each parans style. The order must be maintained to remain valid. If the order is violated, 
        # false is returned for isValid() immediately, as no other chars need to be checked. The sum can only be checked after parsing the entire string.
        for i, char in enumerate(s):
            if char == '(': 
                counter_round += 1
                must_close_next += '('
                continue
            
            if char == ')': 
                counter_round -= 1
                if must_close_next != '':
                    if must_close_next[-1] != '(':
                        return False
                    must_close_next = must_close_next[:-1]
                continue

            if char == '[': 
                counter_square += 1
                must_close_next += '['
                continue

            if char == ']': 
                counter_square -= 1
                if must_close_next != '':
                    if must_close_next[-1]!= '[':
                        return False
                    must_close_next = must_close_next[:-1]
                continue
            if char == '{': 
                counter_curly += 1
                must_close_next += '{'
                continue

            if char == '}': 
                counter_curly -= 1
                if must_close_next != '':
                    if must_close_next[-1]!= '{':
                        return False
                    must_close_next = must_close_next[:-1]
                continue

        # The sums for each paran style will be zero if each open parans has a matching closing parans. Also, the must_close_next string will be empty 
        # after iterating through each character when the string contains valid parans. 
        if counter_round == 0 and counter_square == 0 and counter_curly == 0 and must_close_next == '':
            return True
        else: 
            return False

# MUCH cleaner/succinct solution.
class Solution2:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            print(s)
            if s == '' :
                return True
        return False

if __name__ == '__main__':
    expected_output = [True, False, False, False, True, False, True, True, False]
    test_cases =  ["[({(())}[()])]", "()))", "(){}}{", "){", '{[]}', '([)]', '()', '()[]{}', '(]']

    for i, case in enumerate(test_cases):
        solve = Solution().isValid(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")