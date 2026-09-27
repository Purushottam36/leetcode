class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # An empty tree is 1 unique structural arrangement
        dp[1] = 1  # A tree with 1 node is 1 unique structural arrangement
        
        # Fill the DP table
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]