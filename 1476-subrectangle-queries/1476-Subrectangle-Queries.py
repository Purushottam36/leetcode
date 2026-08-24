from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle
        # Stores history as: (row1, col1, row2, col2, newValue)
        self.history = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # Record the update in O(1) time
        self.history.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # Check updates from newest to oldest
        for r1, c1, r2, c2, val in reversed(self.history):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        
        # If no updates modified this cell, return original value
        return self.grid[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)