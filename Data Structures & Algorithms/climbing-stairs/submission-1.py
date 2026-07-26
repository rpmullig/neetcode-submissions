

class Solution:

    def dfs(self,n: int, memo: dict[int, int]) -> int:
        if n in memo:
            return memo[n]
        if n <= 1:
            return 1
        memo[n] = self.dfs(n-1, memo) + self.dfs(n-2, memo)
        return memo[n]
        

    def climbStairs(self, n: int) -> int:
        memo = dict() 
        return self.dfs(n, memo)