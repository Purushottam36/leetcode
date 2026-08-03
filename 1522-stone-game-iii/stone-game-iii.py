class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        # Track dp values for i+1, i+2, and i+3
        # Base case: looking past the end of the array yields 0 points
        dp_1, dp_2, dp_3 = 0, 0, 0
        
        # Iterate backwards from the end of the stone row
        for i in range(n - 1, -1, -1):
            # Option 1: Take 1 stone
            take_1 = stoneValue[i] - dp_1
            
            # Option 2: Take 2 stones (if available)
            take_2 = float('-inf')
            if i + 1 < n:
                take_2 = stoneValue[i] + stoneValue[i + 1] - dp_2
                
            # Option 3: Take 3 stones (if available)
            take_3 = float('-inf')
            if i + 2 < n:
                take_3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp_3
            
            # Current maximum relative score
            current_dp = max(take_1, take_2, take_3)
            
            # Shift the variables for the next iteration (moving left)
            dp_3 = dp_2
            dp_2 = dp_1
            dp_1 = current_dp
            
        # dp_1 now holds the maximum relative score Alice can get starting at index 0
        if dp_1 > 0:
            return "Alice"
        elif dp_1 < 0:
            return "Bob"
        else:
            return "Tie"