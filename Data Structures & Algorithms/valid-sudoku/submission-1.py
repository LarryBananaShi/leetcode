class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # given an array of 9 arrays of length 9
        # each array cannot have duplicates besides .
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False 
                seen.add(cell)

        # each index across all arrays must contain a unique value or .
        for i in range(9):
            seen = set()
            for row in board:
                cell = row[i]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        boxes = defaultdict(set) #automatically ignore duplicates added to a key
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                box_key = (r//3, c//3) #create a coordinate mapping of the 9 total sub-boxes in 1 sudoku
                if cell in boxes[box_key]: #check if a value is within the sub box for this row/column value
                    return False
                boxes[box_key].add(cell)

        return True




        # index 1-3 of arrays 1-3 must contain unique values ^ 
        # index 1-3 of arrays 4-6 must contain unique values ^
        # index 1-3 of arrays 7-9 must contain unique values

        # index 4-6 of arrays 1-3 must contain unique values ^
        # index 4-6 of arrays 4-6 must contain unique values ^ 
        # index 4-6 of arrays 7-9 must contain unique values

        # index 7-9 of arrays 1-3 must contain unique values ^
        # index 7-9 of arrays 4-6 must contain unique values ^
        # index 7-9 of arrays 7-9 must contain unique values 

