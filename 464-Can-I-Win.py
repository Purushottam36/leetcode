class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Edge case 1: First player wins immediately if target is 0 or less
        if desiredTotal <= 0:
            return True
        
        # Edge case 2: Total sum of all available numbers is less than desiredTotal
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        
        memo = {}

        def can_win(used_mask: int, remaining: int) -> bool:
            if used_mask in memo:
                return memo[used_mask]
            
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i
                # Check if number i is not yet used
                if (used_mask & bit) == 0:
                    # Win immediately or force the opponent into a losing state
                    if i >= remaining or not can_win(used_mask | bit, remaining - i):
                        memo[used_mask] = True
                        return True
            
            memo[used_mask] = False
            return False

        return can_win(0, desiredTotal)