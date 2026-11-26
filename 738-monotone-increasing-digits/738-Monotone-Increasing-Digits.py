class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        marker = len(digits)
        
        # Traverse from right to left
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i
                
        # Set all digits after the last decrement point to '9'
        for i in range(marker, len(digits)):
            digits[i] = '9'
            
        return int("".join(digits))