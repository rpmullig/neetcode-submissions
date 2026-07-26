class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        moves = [[0,1], [1,0], [-1,0], [0, -1]]
        visited = set()
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r,c) in visited:
                    continue
                
                visited.add((r,c))
                if grid[r][c] == "1":
                    stack = [(r,c)]
                    while len(stack) > 0:
                        curr_r, curr_c = stack.pop()
                        for move in moves:
                            inc_r, inc_c = move[0], move[1]
                            new_r, new_c = curr_r + inc_r, curr_c + inc_c
                            if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) and (new_r, new_c) not in visited and grid[new_r][new_c] == "1":
                                visited.add((new_r, new_c))
                                stack.append((new_r, new_c))


                    island_count += 1


        return island_count