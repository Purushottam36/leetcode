class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        # Step 1: Sort the numbers to easily chain divisor properties
        nums.sort()
        n = len(nums)
        
        # dp[i] will store the maximum length of divisible subset ending at nums[i]
        dp = [1] * n
        # parent[i] will store the previous index in the chain to reconstruct the path
        parent = [-1] * n
        
        max_size = 1
        max_idx = 0
        
        # Step 2: Fill the DP table
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            
            # Keep track of the globally largest subset found so far
            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i
                
        # Step 3: Reconstruct the largest subset using the parent pointers
        result = []
        curr = max_idx
        while curr != -1:
            result.append(nums[curr])
            curr = parent[curr]
            
        return result[::-1]  # Return in ascending order