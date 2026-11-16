import bisect
import random

class Solution:

    def __init__(self, rects: list[list[int]]):
        self.rects = rects
        self.prefix_sums = []
        total_points = 0
        
        for a, b, x, y in rects:
            # Count total integer points inside and on the perimeter
            points = (x - a + 1) * (y - b + 1)
            total_points += points
            self.prefix_sums.append(total_points)

    def pick(self) -> list[int]:
        # Pick a random 1-indexed point across the combined pool of all rectangles
        target = random.randint(1, self.prefix_sums[-1])
        
        # Binary search to find which rectangle owns this target index
        rect_idx = bisect.bisect_left(self.prefix_sums, target)
        a, b, x, y = self.rects[rect_idx]
        
        # Pick a uniform random integer coordinate inside the chosen rectangle
        u = random.randint(a, x)
        v = random.randint(b, y)
        return [u, v]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()