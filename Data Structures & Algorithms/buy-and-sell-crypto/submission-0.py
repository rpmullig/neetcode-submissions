class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        delta_prices: List[int] = [(prices[i] - prices[i-1]) for i in range(1, len(prices), 1)]
        max_gain: int = 0
        current: int = 0
        for i in range(len(delta_prices)):
            current = max(0, current + delta_prices[i])
            max_gain = max(max_gain, current)
        return max_gain