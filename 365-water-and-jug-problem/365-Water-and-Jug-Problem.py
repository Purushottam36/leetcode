import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Condition 1: Target amount cannot exceed total capacity of both jugs
        if x + y < target:
            return False
            
        # Condition 2: Target must be divisible by the GCD of x and y
        return target % math.gcd(x, y) == 0