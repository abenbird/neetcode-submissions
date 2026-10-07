class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        lens = len(prices)
        for i, v in enumerate(prices):
            j = i + 1
            while j < lens:
                diff = prices[j] - prices[i]
                if diff > maxPro:
                    maxPro = diff
                j += 1
        return maxPro