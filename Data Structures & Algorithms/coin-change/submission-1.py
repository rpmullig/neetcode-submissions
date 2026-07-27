class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        min_coins = math.inf
        stack = [(0, 0)]
        while len(stack) > 0: 
            current_value, coin_count = stack.pop()

            if current_value == amount:
                min_coins = min(coin_count, min_coins)

            for coin in coins:
                if current_value + coin <= amount:
                    multiplier =  (amount - current_value) // coin
                    stack.append((current_value + (coin * multiplier), coin_count + multiplier))
        
        if min_coins == math.inf:
            return -1

        return min_coins 