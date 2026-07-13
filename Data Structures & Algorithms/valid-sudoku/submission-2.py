class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: List[Set[str]] = [set() for _ in range(len(board))] ## cannot do [set()] * len(board), why? 
        columns: List[Set[str]] = [set() for _ in range(len(board))]
        sections: List[Set[str]] = [set() for _ in range(len(board))]
        
        EMPTY_SPACE: str = "."

        for row_index in range(len(board)):
            for col_index in range(len(board)):
                elm: str = board[row_index][col_index]

                if EMPTY_SPACE == elm:
                    continue

                if elm in rows[row_index]:
                    return False
                rows[row_index].add(elm)

                if elm in columns[col_index]:
                    return False
                columns[col_index].add(elm)


                section_index: int = (col_index // 3) + (row_index // 3) * 3
                if elm in sections[section_index]:
                    return False
                sections[section_index].add(elm)

        return True 