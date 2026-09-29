class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row for duplicates
        for row in board:
            seen = set()
            for index in row: # index is just a cell. should keep naming consistent to not get confused
                if index == '.':
                    continue
                if index in seen:
                    return False
                seen.add(index)

        # check every single unique index for duplicates
        for i in range(9):
            seen = set()
            for row in board:
                if row[i] == '.':
                    continue
                if row[i] in seen:
                    return False
                seen.add(row[i])

        # check every group of 3x3 boxes for duplicates
        boxes = defaultdict(set)
        # default dict is same as a dict (seen = {}) but assigns default value
        # to missing keys. when we pass set as argument, that is the default val
        # (ie. this key gets a new set() for a value)

        #so, 
        for c in range(9):
            for r in range(9):
                cell = board[c][r]
                if cell == '.':
                    continue
                # based on the cell coords, we can map to a specific box out of the 9
                # this becomes the key
                box_number = (c//3, r//3) 

                # since we are creating a new set for each new key, we can check in the 
                # set belonging to this specific key for if the number already exists (ex. 1,2,3)
                if cell in boxes[box_number]:
                    return False
                
                # if not, we add this number to the set for this box
                boxes[box_number].add(cell)
        return True




