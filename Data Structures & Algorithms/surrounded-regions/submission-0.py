class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []
        overall_visited = set()
        steps = [[0,1], [1,0], [-1,0], [0,-1]]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "X":
                    continue
                
                stack.append((r,c))
                current_visit = set()
                while len(stack) > 0:
                    i, j = stack.pop()
                    if board[i][j] ==  "O":
                        current_visit.add((i,j))
                        for step in steps:
                            inc_r, inc_c = step[0], step[1]
                            new_r, new_c = i + inc_r, j + inc_c
                            if new_r >= 0 and new_r < len(board) and new_c >= 0 and new_c < len(board) and (new_r, new_c) not in current_visit:
                                stack.append((new_r, new_c))
                
                if len(current_visit) > 1:
                    for coords in current_visit:
                        i, j = coords
                        board[i][j] = "X"
                
                overall_visited = current_visit & overall_visited

        