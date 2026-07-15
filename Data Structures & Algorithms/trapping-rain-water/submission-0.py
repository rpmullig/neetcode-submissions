class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max: List[int] = [0] * len(height)
        current_max: int = 0
        for i in range(len(height)):
            current_max = max(current_max, height[i])
            prefix_max[i] = current_max
        
        current_max = 0
        postfix_max: List[int] = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            current_max = max(current_max, height[i])
            postfix_max[i] = current_max
 

        result: int = 0
        for i in range(len(height)):
            result += max(0, min(prefix_max[i], postfix_max[i]) -  height[i])

        return result