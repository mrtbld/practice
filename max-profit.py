# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#     Input: [7,1,5,3,6,4]
#     Output: 5
#     Explanation:
#     Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#     Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
#
#     Input: [7,6,4,3,1]
#     Output: 0
#     Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    # t:O(n²), s:O(1)
    def maxProfit(self, prices):
        global_max_profit = 0
        for i, buy_price in enumerate(prices): # t:O(n)
            max_profit = 0
            for sell_price in prices[i+1:]: # t:O(n)
                max_profit = max(max_profit, sell_price - buy_price)
            global_max_profit = max(global_max_profit, max_profit)
        return global_max_profit

print(Solution().maxProfit([7,1,5,3,6,4]), 5)
print(Solution().maxProfit([7,6,4,3,1]), 0)
print(Solution().maxProfit([1,1,1,1,1]), 0)
print(Solution().maxProfit([10,2,11,1,12]), 11)
print(Solution().maxProfit(list(range(10000,0,-1)) + [0] * 10000), 0)
