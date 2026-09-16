import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        total_objects = n + k - 1
        choose_slots = 2 * k
        
        # If we need to pick more slots than points available, it's impossible
        if choose_slots > total_objects:
            return 0
        
        # Compute the binomial coefficient and apply the modulo
        return math.comb(total_objects, choose_slots) % MOD