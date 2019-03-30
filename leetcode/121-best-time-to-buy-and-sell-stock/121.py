class Solution:
    # t:O(n), s:O(1)
    def maxProfit(self, prices):
        """Return the max profit possible from given array of prices which is in
        chronological order).

        >>> _ = Solution()
        >>> _.maxProfit([7,1,5,3,6,4])
        5
        >>> _.maxProfit([7,6,4,3,1])
        0
        >>> _.maxProfit([1,1,1,1,1])
        0
        >>> _.maxProfit([10,2,11,1,12])
        11
        >>> _.maxProfit(list(range(10000,0,-1)) + [0] * 10000)
        0
        """
        max_delta = 0
        if not prices:
            return max_delta
        low = prices[0]
        for price in prices: # t:O(n)
            if price < low:
                low = price
            else:
                delta = price - low
                if delta > max_delta:
                    max_delta = delta
        return max_delta
