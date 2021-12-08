class Solution:
    def romanToInt(self, s: str):
        roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900}

        n = len(s)
        sum = 0

        # We can't use a for loop here because we need stricter control over the index
        i = 0   
        while i in range(0, n):
            c = s[i]

            # Check if we're at the end of the numeral or not (avoid taking index out of range). True -> not at end, False -> at the end
            if i + 1 <= n - 1:

                # define special case boolean terms
                bool_4or9 = (c == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'))
                bool_40or90 = (c == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'))
                bool_400or900 = (c == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'))

                if bool_4or9 or bool_40or90 or bool_400or900:
                    sum += roman_nums[c + s[i+1]]
                    i += 2
                else:
                    sum += roman_nums[c] 
                    i += 1

            # We're at the last digit of the roman numeral
            else:
                sum += roman_nums[c]
                i += 1

        return sum

if __name__ == '__main__':
    expected_output = [1476, 3, 4, 9, 58, 1994]
    test_cases = ["MCDLXXVI", "III", "IV", "IX", "LVIII", "MCMXCIV"]

    for i, case in enumerate(test_cases):
        solve = Solution().romanToInt(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")

