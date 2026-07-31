class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Track sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before shifting
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
                
            res = res * 10 + digit
            
        return res * sign