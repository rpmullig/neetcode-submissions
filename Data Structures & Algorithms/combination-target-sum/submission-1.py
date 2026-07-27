class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()

        def dfs(start_index, curr_list, curr_sum):
            if curr_sum == target:
                result.append(curr_list.copy())
            
            if curr_sum > target:
                return
            
            for i in range(start_index, len(nums)):
                if curr_sum + nums[i] <= target:
                    curr_list.append(nums[i])
                    curr_sum += nums[i]
                    dfs(i, curr_list, curr_sum)
                    curr_list.pop()
                    curr_sum -= nums[i]
                


        dfs(0, list(), 0)

        return result 