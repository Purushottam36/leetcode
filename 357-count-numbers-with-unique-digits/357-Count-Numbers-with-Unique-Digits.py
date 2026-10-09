class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
            
        res = 10          # Base count for n = 1 (numbers 0 to 9)
        unique_digits = 9 
        available_number = 9
        
        # Calculate unique numbers for length 2 up to n
        for i in range(2, n + 1):
            unique_digits *= available_number
            res += unique_digits
            available_number -= 1
            
        return res