import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # The number of bulbs that remain ON is equal to the number of perfect squares <= n.
        # math.isqrt(n) efficiently returns the exact integer square root of n.
        return math.isqrt(n)