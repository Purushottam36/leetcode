class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of distinct subsequences matching t[0...j-1]
        dp = [0] * (n + 1)
        
        # Base case: an empty t can always be formed by an empty subsequence of s
        dp[0] = 1 
        
        # Iterate through each character of s
        for i in range(1, m + 1):
            # Iterate backwards to ensure we use values from the previous iteration of s
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] = dp[j] + dp[j-1]
                    
        return dp[n]