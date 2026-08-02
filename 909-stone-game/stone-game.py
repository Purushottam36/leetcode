class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        memo = {}
        
        def get_max_diff(i: int, j: int) -> int:
            if i == j:
                return piles[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Maximize: current choice - opponent's optimal future net score
            pick_left = piles[i] - get_max_diff(i + 1, j)
            pick_right = piles[j] - get_max_diff(i, j - 1)
            
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
        
        # If Alice's final net score relative to Bob is > 0, she wins
        return get_max_diff(0, len(piles) - 1) > 0