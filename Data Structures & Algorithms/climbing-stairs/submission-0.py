import functools

class Solution:

    @functools.lru_cache(None)
    def dfs(self,n: int) -> int:
        if n <= 1:
            return 1
        return self.dfs(n-1) + self.dfs(n-2)
        

    def climbStairs(self, n: int) -> int:
        return self.dfs(n)