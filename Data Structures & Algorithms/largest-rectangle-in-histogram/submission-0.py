class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monotonic_stack = []
        max_area: int = 0

        for i, height in enumerate(heights):
            start_index = i 

            while monotonic_stack and monotonic_stack[-1][0] > height:
                pop_height, index = monotonic_stack.pop()
                current_area = (i - index) * pop_height
                max_area = max(max_area, current_area)
                start_index = index
            
            # print(monotonic_stack)
            monotonic_stack.append((height, start_index))

        while monotonic_stack:
            pop_height, index = monotonic_stack.pop()
            current_area = (len(heights) - index) * pop_height
            max_area = max(max_area, current_area)


        return max_area