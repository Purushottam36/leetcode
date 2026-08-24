class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Compute prefix sums
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + stones[i]
            
        # Base case: if forced to take all stones
        ans = pref[-1]
        
        # Iterate backwards from n-2 down to 1 (0-indexed corresponds to index 2 to n-1)
        for i in range(n - 2, 0, -1):
            ans = max(ans, pref[i] - ans)
            
        return ans