class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Base array to store generated ugly numbers in sorted order
        ugly = [0] * n
        ugly[0] = 1  # The first ugly number is always 1
        
        # Pointers tracking the indices of numbers multiplied by 2, 3, and 5
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            # Compute the next possible candidates
            next_2 = ugly[p2] * 2
            next_3 = ugly[p3] * 3
            next_5 = ugly[p5] * 5
            
            # The next ugly number is always the minimum of the candidates
            next_ugly = min(next_2, next_3, next_5)
            ugly[i] = next_ugly
            
            # Increment pointers for any candidate that matched the minimum (handles duplicates)
            if next_ugly == next_2:
                p2 += 1
            if next_ugly == next_3:
                p3 += 1
            if next_ugly == next_5:
                p5 += 1
                
        return ugly[-1]