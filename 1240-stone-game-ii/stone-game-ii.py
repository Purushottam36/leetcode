from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # suffix_sums[i] stores the total stones from index i to the end
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        # memo dictionary to store results of subproblems: (index, M)
        memo = {}
        
        def dp(i: int, m: int) -> int:
            # Base case: if no piles are left, 0 stones can be taken
            if i >= n:
                return 0
            
            # If the current player can take all remaining piles, take them all
            if i + 2 * m >= n:
                return suffix_sums[i]
            
            # Check if this state has already been computed
            if (i, m) in memo:
                return memo[(i, m)]
            
            # Find the best move by iterating through all possible choices of X
            max_stones = 0
            for x in range(1, 2 * m + 1):
                # Opponent's best result from the remaining piles
                opponent_score = dp(i + x, max(m, x))
                # Current player's score is remaining total minus opponent's best score
                current_score = suffix_sums[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            memo[(i, m)] = max_stones
            return max_stones
        
        # Alice starts at index 0 with M = 1
        return dp(0, 1)