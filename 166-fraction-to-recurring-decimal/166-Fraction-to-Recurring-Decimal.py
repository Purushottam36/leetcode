class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
            
        res = []
        
        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
            
        # Get absolute values (Python handles large integers automatically, no overflow issues)
        num = abs(numerator)
        den = abs(denominator)
        
        # Integer part
        res.append(str(num // den))
        remainder = num % den
        
        if remainder == 0:
            return "".join(res)
            
        # Fractional part
        res.append(".")
        remainder_map = {}
        
        while remainder != 0:
            # If the remainder has been seen before, we found the recurring loop
            if remainder in remainder_map:
                index = remainder_map[remainder]
                res.insert(index, "(")
                res.append(")")
                break
                
            # Store the current index where the next quotient digit will be placed
            remainder_map[remainder] = len(res)
            
            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den
            
        return "".join(res)