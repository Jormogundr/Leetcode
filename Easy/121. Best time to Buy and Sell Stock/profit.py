"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
# not optimal
class Solution:
    def maxProfit(self, prices) -> int:
        min = 10E4
        max = 0
        n = len(prices)

        for i in range(0, n):
            if prices[i] < min:
                min = prices[i]
            for j in range(i + 1, n):
                if prices[j] > max:
                    max = prices[j]
        
        profit = max - min
        return profit

def testCases(test_cases, expected_output):
    for i, case in enumerate(test_cases):
        solve = Solution().maxProfit(case)
        if solve == expected_output[i]:
            print(case, "Success")
        else:
            print(case, "Fail")

if __name__ == '__main__':
    expected_output = [5, 0]
    test_cases =  [[7,1,5,3,6,4], [7,6,4,3,1]]

    testCases(test_cases, expected_output)