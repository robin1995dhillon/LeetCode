import sys


class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        buyPrice = sys.maxsize
        profit = 0
        for i in range(0,n):
            if (buyPrice>prices[i]):
                buyPrice = prices[i]
            else:
                profit = max(profit,prices[i] - buyPrice)
        return profit

s = Solution()
values = [7,1,5,3,6,4]
val = s.maxProfit(values)
print(val)