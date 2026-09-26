class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the negative exponent case
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        current_product = x
        
        # Iterative Binary Exponentiation (Exponentiation by Squaring)
        while n > 0:
            # If the current bit of n is 1 (odd number), multiply by current_product
            if n % 2 == 1:
                res *= current_product
            
            # Square the base and halve the power
            current_product *= current_product
            n //= 2
            
        return res