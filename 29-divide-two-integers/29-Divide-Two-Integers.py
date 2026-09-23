class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer boundaries
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle the edge case that causes a 32-bit signed integer overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        # Determine if the result should be negative using the XOR operator
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers to simplify subtraction logic
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # Exponentially subtract the divisor from the dividend
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            # Double the divisor (shift left) as long as it fits inside the remaining dividend
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            # Deduct the largest chunk possible and add the multiple to the quotient
            abs_dividend -= temp_divisor
            quotient += multiple
            
        # Apply the determined sign to the quotient
        if is_negative:
            quotient = -quotient
            
        # Clamp the final answer within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))