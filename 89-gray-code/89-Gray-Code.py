class Solution:
    def grayCode(self, n: int) -> list[int]:
        # There are 2^n elements in a valid n-bit gray code sequence
        total_elements = 1 << n
        
        # Generate the sequence directly using the formula: i ^ (i >> 1)
        return [i ^ (i >> 1) for i in range(total_elements)]