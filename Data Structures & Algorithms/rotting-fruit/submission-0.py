class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        total_oranges = 0
        q = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r,c))
                
                if grid[r][c] > 0:
                    total_oranges += 1

        if total_oranges == 0: return 0

        # BFS
        moves = [[0,1], [1,0], [-1,0], [0,-1]]
        visited = set()
        minutes = -1
        rotten_oranges = 0
        while len(q) > 0:
            n = len(q)
            minutes += 1
            for _ in range(n):
                r, c = q.popleft()
                if (r,c) in visited:
                    continue
                
                visited.add((r,c))
                rotten_oranges += 1

                for move in moves:
                    inc_r, inc_c = move[0], move[1]
                    new_r, new_c = r + inc_r, c + inc_c
                    if 0 <= new_r and new_r < len(grid) and 0 <= new_c and new_c < len(grid[0]) and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                        #grid[new_r][new_c] = 2
                        q.append((new_r,new_c))

        if rotten_oranges == total_oranges:
            return max(0, minutes)
        else:
            return -1