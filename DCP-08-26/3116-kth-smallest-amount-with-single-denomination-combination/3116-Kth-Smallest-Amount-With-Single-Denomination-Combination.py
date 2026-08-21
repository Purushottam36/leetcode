import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        
        # 1. Precompute LCM and Inclusion-Exclusion sign for all coin combinations
        for i in range(1, 1 << n):
            current_lcm = 1
            cnt = 0
            for j in range(n):
                if (i >> j) & 1:
                    cnt += 1
                    current_lcm = (current_lcm * coins[j]) // math.gcd(current_lcm, coins[j])
            
            # Odd number of coins -> Add (+1), Even number of coins -> Subtract (-1)
            sign = 1 if cnt % 2 == 1 else -1
            subsets.append((current_lcm, sign))
        
        # Helper function to count unique multiples <= mid
        def count_amounts(mid: int) -> int:
            total_count = 0
            for lcm_val, sign in subsets:
                total_count += sign * (mid // lcm_val)
            return total_count

        # 2. Binary Search for the exact value
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # We need a larger number to reach k elements
                
        return ans