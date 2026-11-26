class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # 0 presses leaves all bulbs in their initial state
        if presses == 0:
            return 1
        
        # Only the first 3 bulbs determine the entire sequence
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        
        # For n >= 3:
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        
        # For presses >= 3, all 2^3 = 8 states of the first 3 bulbs are possible
        return 8