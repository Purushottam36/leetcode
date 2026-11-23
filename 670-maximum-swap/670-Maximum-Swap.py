class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        
        max_idx = n - 1
        swap_i = -1
        swap_j = -1
        
        for i in range(n - 2, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                swap_i = i
                swap_j = max_idx
                
        if swap_i != -1:
            digits[swap_i], digits[swap_j] = digits[swap_j], digits[swap_i]
            
        return int("".join(digits))