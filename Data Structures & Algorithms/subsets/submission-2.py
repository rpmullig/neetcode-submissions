class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        stack = [(0, [])]

        while len(stack) > 0:
            i, current_list = stack.pop()

            if i == len(nums):
                result.append(list(current_list))
            else:
                stack.append((i+1, current_list + [nums[i]]))
                stack.append((i+1, current_list))

        return result