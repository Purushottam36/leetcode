class Solution:
    def reachNumber(self, target: int) -> int:
        # Symmetry allows us to treat negative targets the same as positive ones
        target = abs(target)
        
        total_sum = 0
        moves = 0
        
        # Keep taking steps until we reach or pass target, 
        # AND the overshoot (total_sum - target) is even
        while total_sum < target or (total_sum - target) % 2 != 0:
            moves += 1
            total_sum += moves
            
        return moves