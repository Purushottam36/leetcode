class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Optimize by choosing the smaller direction to reduce loop iterations
        k = min(m - 1, n - 1)
        N = m + n - 2
        
        res = 1
        for i in range(1, k + 1):
            res = res * (N - k + i) // i
            
        return res