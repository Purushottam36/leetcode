class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # Step 1: Find the minimum element in the array
        min_val = min(nums)
        
        # Step 2: Sum the difference between each element and the minimum element
        moves = 0
        for num in nums:
            moves += num - min_val
            
        return moves