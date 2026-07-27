class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = dict() 
        cache[-1] = 0
        cache[-2] = 0

        def dfs(i):
            
            if i in cache:
                return cache[i] 
            else:
                cache[i] = max(dfs(i-2) + nums[i], dfs(i-1))
                return cache[i]

        return dfs(len(nums) - 1)