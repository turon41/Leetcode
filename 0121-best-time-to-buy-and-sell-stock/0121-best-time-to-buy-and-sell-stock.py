class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        b = prices[0]
        for sell in (prices[1:]):
            if sell>b:
                prof = max(prof,sell-b)
            else:
                b = sell
        return prof            

        