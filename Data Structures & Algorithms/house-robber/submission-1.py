class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = dict() 
        cache[-1] = 0
        cache[-2] = 0

        def dfs(i):
            
            if i in cache:
                return cache[i] 
            else:
                return max(dfs(i-2) + nums[i], dfs(i-1))

        return dfs(len(nums) - 1)