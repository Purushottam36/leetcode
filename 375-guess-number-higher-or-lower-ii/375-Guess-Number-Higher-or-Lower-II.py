class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] will store the minimum cost to guarantee a win for the range [i, j]
        # We use a size of n + 2 to safely handle x - 1 and x + 1 boundary checks
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Iterate over the length of the number intervals (from length 2 up to n)
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                
                min_cost = float('inf')
                # Try every possible guess 'x' in the current range [i, j]
                for x in range(i, j + 1):
                    # Cost is the current guess + worst-case outcome of left/right segments
                    cost = x + max(dp[i][x - 1], dp[x + 1][j])
                    if cost < min_cost:
                        min_cost = cost
                        
                dp[i][j] = min_cost
                
        return dp[1][n]