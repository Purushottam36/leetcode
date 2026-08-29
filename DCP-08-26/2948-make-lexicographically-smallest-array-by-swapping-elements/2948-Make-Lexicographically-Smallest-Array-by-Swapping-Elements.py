from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        # Pair each number with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        result = [0] * len(nums)
        
        # Group connected elements
        groups = []
        for val, idx in sorted_pairs:
            # Start a new group if empty or if difference exceeds limit
            if not groups or val - groups[-1][-1][0] > limit:
                groups.append([])
            groups[-1].append((val, idx))
        
        # Reassign values to the original indices within each group
        for group in groups:
            # Extract values and original indices
            values = [val for val, idx in group]
            indices = sorted([idx for val, idx in group])
            
            # Place sorted values into sorted index positions
            for val, idx in zip(values, indices):
                result[idx] = val
                
        return result