class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = dict() 

        def dfs(i):
            if i in memo:
                return memo[i]

            if i <= 1:
                return cost[i]
            
            if i == len(cost):
                memo[i] = min(dfs(i-1), dfs(i-2))
            else:
                memo[i] =  cost[i] + min(dfs(i-1), dfs(i-2))
            
            return memo[i]

        return dfs(len(cost))