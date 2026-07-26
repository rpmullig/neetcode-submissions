class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        current_max_area = 0
        moves = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    curr_area = 0
                    stack = [(r,c)]
                    while len(stack) > 0:
                        curr_r, curr_c = stack.pop()
                        if grid[curr_r][curr_c] == 1:
                            curr_area += 1
                            grid[curr_r][curr_c] = 0
                            for move in moves:
                                inc_r, inc_c = move
                                next_r, next_c = curr_r + inc_r, curr_c + inc_c
                                if 0 <= next_r and next_r < len(grid) and 0 <= next_c and next_c < len(grid[r]):
                                    stack.append((next_r, next_c))
                    
                    current_max_area = max(current_max_area, curr_area)



        return current_max_area # after traversal 