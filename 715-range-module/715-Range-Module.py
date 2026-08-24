import bisect

class RangeModule:

    def __init__(self):
        # Stores a flat list of disjoint interval bounds: [start1, end1, start2, end2, ...]
        self.X = []

    def addRange(self, left: int, right: int) -> None:
        # Find where left and right would fit to maintain sorted order
        i = bisect.bisect_left(self.X, left)
        j = bisect.bisect_right(self.X, right)
        
        sub = []
        # If left is outside an active interval, it becomes a new start
        if i % 2 == 0:
            sub.append(left)
        # If right is outside an active interval, it becomes a new end
        if j % 2 == 0:
            sub.append(right)
            
        # Replace everything between index i and j with our new merged boundaries
        self.X[i:j] = sub

    def queryRange(self, left: int, right: int) -> bool:
        # Find the insertion point for left and right
        i = bisect.bisect_right(self.X, left)
        j = bisect.bisect_left(self.X, right)
        
        # 'i' must be odd (meaning 'left' is strictly inside a tracked interval)
        # 'i == j' ensures both 'left' and 'right' fall within that exact same interval
        return i % 2 == 1 and i == j

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.X, left)
        j = bisect.bisect_right(self.X, right)
        
        sub = []
        # If left cuts an active interval, that interval now ends at left
        if i % 2 == 1:
            sub.append(left)
        # If right cuts an active interval, a new interval starts at right
        if j % 2 == 1:
            sub.append(right)
            
        # Clear out everything tracked between i and j and replace with the slice boundaries
        self.X[i:j] = sub

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)