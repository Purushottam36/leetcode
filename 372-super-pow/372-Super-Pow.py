class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        
        # Base case for recursion
        if not b:
            return 1
        
        # Extract the last digit of the exponent array
        last_digit = b.pop()
        
        # Using the property: a^(10*x + y) = (a^x)^10 * a^y
        part1 = pow(self.superPow(a, b), 10, MOD)
        part2 = pow(a, last_digit, MOD)
        
        return (part1 * part2) % MOD