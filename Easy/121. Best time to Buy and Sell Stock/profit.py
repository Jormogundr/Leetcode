"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Constraints:

1 <= prices.length <= 10E5
0 <= prices[i] <= 10E4

"""
# not optimal - O(nlogn)
class Solution:
    def maxProfit(self, prices) -> int:
        min = 10E4
        max = 0
        profit = 0
        n = len(prices)

        if n == 0 or n == 1: # check for empty price list, or only one price
            return 0

        # This function runs in O(nlogn) due to this for loop. 
        # We want to exclude the last index n from consideration of the min index i - because we cannot sell and make a profit if we buy at the very last price! 
        # The index j is used to scan through indices greater than i and find the max price. If the min index position i changes, then j must be 
        # re-evaluated. The for loop maximizes profit as defined in the problem - it does not find global mins or maxs!
        for i in range(0, n - 1):
            j = i + 1
            if prices[i] < min:
                min = prices[i]
                max = min # max must be reset with min to ensure that the index position of max does not fall behind min
            if prices[j] > max:
                max = prices[j]
            if profit < max - min:
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
    expected_output = [4, 0, 4, 6, 2, 5, 0, 0, 0]
    test_cases =  [[3,2,6,5,0,3], [1], [0, 1, 2, 3, 4], [3, 5, 1, 7, 0], [2,4,1], [7,1,5,3,6,4], [7,6,4,3,1], [6,6,6], []] 
    testCases(test_cases, expected_output)