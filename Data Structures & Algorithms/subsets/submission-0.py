class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()

        def dfs(i, current_list):
            if i == len(nums):
                result.append(list(current_list))
                return 
            
            current_list.append(nums[i])
            dfs(i+1, current_list)
            current_list.pop()
            dfs(i+1, current_list)

        current_list = []
        dfs(0, current_list)

        return result