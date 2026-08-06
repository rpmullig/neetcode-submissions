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
            
            if i >= len(candidates) or current_sum > target:
                return
            
            elm = candidates[i]

            current_combination.append(elm)
            dfs(i+1, current_combination, current_sum + elm)
            current_combination.pop()

            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            
            dfs(next_i, current_combination, current_sum)

        
        dfs(0, list(), 0)

        return result