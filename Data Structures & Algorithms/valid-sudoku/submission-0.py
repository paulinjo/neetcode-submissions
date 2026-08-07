class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            if not self.is_valid_section(board[row]):
                return False
        
        for col in range(9):
            if not self.is_valid_section([board[i][col] for i in range(9)]):
                return False
        
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                sub_box = []

                for row_offset in range(3):
                    for col_offset in range(3):
                        sub_box.append(board[start_row+row_offset][start_col+col_offset])

                if not self.is_valid_section(sub_box):
                    return False
        
        return True

    def is_valid_section(self, entries: List[str]):
        seen = set()

        for x in entries:
            if x == ".":
                continue
            if x in seen:
                return False
            
            seen.add(x)
        return True
        