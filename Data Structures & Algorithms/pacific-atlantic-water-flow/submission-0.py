class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        atlantic_stack = list()
        pacific_stack = list()
        for r in range(len(heights)):
            for c in range((len(heights[r]))):
                if r == 0 or c == 0:
                    pacific_stack.append((r,c))
                if r == len(heights) - 1 or c == len(heights[r]) - 1:
                    atlantic_stack.append((r,c))
        

        moves = [[1,0], [0,1], [-1,0], [0,-1]]
        atlantic_visited = set()
        pacific_visited = set()
        def dfs(stack, visited):
            while len(stack) > 0:
                r, c = stack.pop() 
                if (r,c) in visited:
                    continue 

                visited.add((r,c))
                for move in moves:
                    inc_r, inc_c = move[0], move[1]
                    new_r, new_c = r + inc_r, c + inc_c
                    if 0 <= new_r and new_r < len(heights) and 0 <= new_c and new_c < len(heights[0]) and (new_r,new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                        stack.append((new_r, new_c))

        dfs(atlantic_stack, atlantic_visited)
        dfs(pacific_stack, pacific_visited)
        common_locations = atlantic_visited & pacific_visited # overlap
        result = list()
        for r, c in common_locations:
            result.append([r,c])
        

        return result 
