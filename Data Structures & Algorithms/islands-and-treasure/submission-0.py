class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        moves = [[1,0], [0,1], [-1, 0], [0, -1]]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    q = collections.deque()
                    q.append((r,c))
                    distance = 0 
                    visited = set()
                    while len(q) > 0:
                        n = len(q)
                        for _ in range(n):
                            curr_r, curr_c = q.popleft()
                            if (curr_r,curr_c) in visited:
                                continue
                        
                            visited.add((curr_r, curr_c))
                            if grid[curr_r][curr_c] != -1:
                                grid[curr_r][curr_c] = min(grid[curr_r][curr_c], distance)
                                
                                for move in moves:
                                    inc_r, inc_c = move[0], move[1]
                                    new_r, new_c = curr_r + inc_r, curr_c + inc_c
                                    if 0 <= new_r and new_r < len(grid) and 0 <= new_c and new_c < len(grid[0]) and grid[new_r][new_c] > distance + 1:
                                        q.append((new_r,new_c)) 
                        distance += 1
