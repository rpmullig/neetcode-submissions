class Solution:
    def dfs(self, i: int, j: int, board: List[List[str]], curr_trie: Dict, words_found: List[str], current_path: List[str], visited: Set[tuple]):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited:
            return 

        current_letter = board[i][j]
        
        if current_letter not in curr_trie:
            return
        
        visited.add((i, j))
        
        next_node = curr_trie[current_letter]
        current_path.append(current_letter)

        if "\n" in next_node:
            words_found.append(''.join(current_path))
            next_node.pop("\n", None) 
        
        moves = [[0, 1], [1,0], [-1, 0], [0, -1]]
        for move in moves:
            inc_i, inc_j = move[0], move[1]
            self.dfs(i+inc_i, j+inc_j, board, next_node, words_found, current_path, visited)
            
        visited.remove((i, j))
        current_path.pop()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = dict()
        for word in words:
            curr = trie_root
            for letter in word:
                if letter not in curr:
                    curr[letter] = dict()
                curr = curr[letter]
            curr["\n"] = None
        
        words_found = list()
        visited = set()
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                visited.clear()
                self.dfs(r, c, board, trie_root, words_found, [], visited)
                
        return words_found