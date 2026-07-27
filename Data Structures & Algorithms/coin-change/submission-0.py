class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = dict() 
        min_coins = math.inf
        stack = [(0, 0)]
        while len(stack) > 0: 
            current_value, coin_count = stack.pop()

            if current_value == amount:
                min_coins = min(coin_count, min_coins)

            for coin in coins:
                if current_value + coin <= amount:
                    stack.append((current_value + coin, coin_count + 1))
        
        if min_coins == math.inf:
            return -1

        return min_coins 