class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # Add symmetric pairs (1, -1), (2, -2), ... up to n // 2
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
            
        # If n is odd, append 0 to complete the array
        if n % 2 != 0:
            result.append(0)
            
        return result