class Solution:
        
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0 
        
        prior, prev, curr = 0, 0, 1
        for i in range(n):
            tmp = curr
            tmp_prev = prev
            curr += prev
            prev = tmp
            prior = tmp_prev

        return curr