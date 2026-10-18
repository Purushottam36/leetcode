from typing import List
import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Number of ways to combine left and right subtrees while maintaining internal order
            combinations = math.comb(len(left) + len(right), len(left))
            
            # Recursively compute ways for left and right, multiplied by current interleavings
            return (combinations * dfs(left) % MOD * dfs(right)) % MOD
        
        # Subtract 1 to exclude the original arrangement itself
        return (dfs(nums) - 1) % MOD