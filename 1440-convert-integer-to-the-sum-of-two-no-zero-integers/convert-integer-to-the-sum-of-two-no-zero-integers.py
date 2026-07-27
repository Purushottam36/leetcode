class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Iterate from 1 up to n
        for a in range(1, n):
            b = n - a
            
            # Check if neither a nor b contains '0' in their decimal representation
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]