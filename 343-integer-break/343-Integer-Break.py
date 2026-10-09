class Solution:
    def integerBreak(self, n: int) -> int:
        # Base cases: for n = 2 and n = 3, we must break them into at least k = 2 parts
        if n == 2: return 1 
        if n == 3: return 2  
        
        res = 1
        # Keep extracting factors of 3 until n is 4 or less
        while n > 4:
            res *= 3
            n -= 3
            
        # Multiply by the remaining part (which will be 2, 3, or 4)
        return res * n