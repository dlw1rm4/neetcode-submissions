class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bought = prices[0]

        for sell in prices:
            profit = max(profit, sell - bought)
            bought = min(bought, sell)
        return profit
        