class Solution:
    def _max_water(self, heights: List[int], l, r) -> int:
        return min(heights[l], heights[r]) * (r - l)

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result: int = 0 
        while l < r:
            result = max(result, self._max_water(heights, l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result