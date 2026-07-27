class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = dict() 

        def dfs(i):
            if i >= len(nums):
                cache[i] = 0
                return 0 
            
            if i in cache:
                return cache[i] 
            else:
                return max(dfs(i+2) + nums[i], dfs(i+1))

        return dfs(0)