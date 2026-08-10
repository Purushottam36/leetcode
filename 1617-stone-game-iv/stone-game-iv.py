class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will store if the player starting with i stones can win
        dp = [False] * (n + 1)
        
        # Iteratively calculate the outcome for all stone counts up to n
        for i in range(1, n + 1):
            k = 1
            # Check every valid perfect square move from the current state
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check further
                k += 1
                
        return dp[n]