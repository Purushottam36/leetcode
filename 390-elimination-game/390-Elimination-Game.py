class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            # Head updates if going left-to-right, OR if going right-to-left with an odd count
            if left_to_right or (remaining % 2 == 1):
                head += step
                
            # Each step doubles the gap, and elements reduce by half
            step *= 2
            remaining //= 2
            # Flip direction
            left_to_right = not left_to_right
            
        return head