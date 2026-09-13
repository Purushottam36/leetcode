from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Extract coordinates of all '1's in both images
        img1_ones = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        img2_ones = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        
        # Track how many times each specific shift vector occurs
        shift_counts = defaultdict(int)
        max_overlap = 0
        
        # Calculate the transformation vector for every pair of '1's
        for r1, c1 in img1_ones:
            for r2, c2 in img2_ones:
                shift_vector = (r2 - r1, c2 - c1)
                shift_counts[shift_vector] += 1
                if shift_counts[shift_vector] > max_overlap:
                    max_overlap = shift_counts[shift_vector]
                    
        return max_overlap