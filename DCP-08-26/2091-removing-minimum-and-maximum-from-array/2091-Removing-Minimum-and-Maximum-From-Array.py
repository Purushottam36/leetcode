class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
            
        # Find the indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Calculate deletions for the 3 scenarios
        from_front = j + 1
        from_back = n - i
        from_both = (i + 1) + (n - j)
        
        # Return the minimum of all three options
        return min(from_front, from_back, from_both)