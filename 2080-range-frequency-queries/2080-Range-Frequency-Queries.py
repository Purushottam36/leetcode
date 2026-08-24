import bisect
from collections import defaultdict
from typing import List

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        # Map each value to a list of its indices
        self.val_to_indices = defaultdict(list)
        for idx, val in enumerate(arr):
            self.val_to_indices[val].append(idx)

    def query(self, left: int, right: int, value: int) -> int:
        # If the value doesn't exist in the array, its frequency is 0
        if value not in self.val_to_indices:
            return 0
            
        indices = self.val_to_indices[value]
        
        # Find the insertion point for 'right' and 'left'
        # right_idx will match the first element strictly greater than 'right'
        right_idx = bisect.bisect_right(indices, right)
        # left_idx will match the first element greater than or equal to 'left'
        left_idx = bisect.bisect_left(indices, left)
        
        # The number of valid indices in the range is the difference
        return right_idx - left_idx

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)