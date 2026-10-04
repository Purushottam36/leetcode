class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        k = len(primes)
        ugly = [0] * n
        ugly[0] = 1
        
        # pointers[i] tracks the index in the 'ugly' array that primes[i] multiplies next
        pointers = [0] * k
        # next_candidates[i] holds the precalculated value of primes[i] * ugly[pointers[i]]
        next_candidates = list(primes)
        
        for i in range(1, n):
            # The next super ugly number is the minimum of all current candidates
            next_ugly = min(next_candidates)
            ugly[i] = next_ugly
            
            # Advance pointers and update candidates for all primes that produced this minimum
            for j in range(k):
                if next_candidates[j] == next_ugly:
                    pointers[j] += 1
                    next_candidates[j] = primes[j] * ugly[pointers[j]]
                    
        return ugly[-1]