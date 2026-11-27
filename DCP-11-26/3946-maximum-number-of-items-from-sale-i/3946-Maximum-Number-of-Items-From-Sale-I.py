class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Find the maximum factor to bound our frequency array and multiple checks
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        
        # Count how many times each factor appears in items
        for f, _ in items:
            freq[f] += 1
            
        # Precompute (price, free_copies_gained) for buying the 1st copy of each item
        items_with_free = []
        for f, p in items:
            free_count = -1  # Start at -1 to exclude the item itself (since j != i)
            for mult in range(f, max_factor + 1, f):
                free_count += freq[mult]
            items_with_free.append((p, free_count))
            
        # Sort by price descending: whenever we add an item in DP, 
        # it is guaranteed to be the cheapest item in our chosen subset so far
        items_with_free.sort(key=lambda x: x[0], reverse=True)
        
        # dp[c] = max items gained by buying a subset of distinct items with exact cost c
        dp = [-1] * (budget + 1)
        dp[0] = 0
        ans = 0
        
        for price, free_count in items_with_free:
            # First copy of this item gives 1 purchased copy + all triggered free copies
            val = 1 + free_count
            
            # Traverse backwards for 0/1 Knapsack (each item used at most once for freebies)
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + val)
                    
                    # Spend any leftover budget on extra copies of this current cheapest item
                    extra_copies = (budget - c) // price
                    ans = max(ans, dp[c] + extra_copies)
                    
        return ans