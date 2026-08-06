class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if len(candidates) == 0:
            return list() 

        candidates.sort()

        result = list()
        combination_added = set()

        def dfs(i, current_combination, current_sum): 
            if current_sum == target and tuple(current_combination) not in combination_added:
                result.append(current_combination.copy())
                combination_added.add(tuple(current_combination.copy()))
                return
            
            if i >= len(candidates) or current_sum > target or current_sum + candidates[i] > target:
                return
            
            elm = candidates[i]

            current_combination.append(elm)
            current_sum += elm
            dfs(i+1, current_combination, current_sum)
            current_combination.pop()
            current_sum -= elm
            
            dfs(i+1, current_combination, current_sum)

        
        dfs(0, list(), 0)

        return result