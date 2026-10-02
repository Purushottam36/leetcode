class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize the DP array with float('inf') 
        # dp[i] will store the minimum number of perfect squares to reach sum i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 requires 0 perfect squares
        
        # Compute the minimum squares for all values up to n
        for i in range(1, n + 1):
            j = 1
            # Check all perfect squares j*j that are less than or equal to i
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]