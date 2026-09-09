class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        start = 1
        digits = 1
        
        while start <= n:
            # Upper bound for the current digit length
            end = min(n, start * 10 - 1)
            
            # Count how many numbers are in [start, end]
            count = end - start + 1
            
            # Commas for a number of this length
            commas_per_num = (digits - 1) // 3
            
            total_commas += count * commas_per_num
            
            # Shift to the next range
            start *= 10
            digits += 1
            
        return total_commas