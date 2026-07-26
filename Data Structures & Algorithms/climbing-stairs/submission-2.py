

class Solution:
        
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0 
        
        prior, prev, curr = 0, 0, 1
        for i in range(1, n):
            tmp = curr
            tmp_prev = prev
            curr = 1 + prev + 1 + prior 
            prev = tmp
            prior = tmp_prev

        return curr 