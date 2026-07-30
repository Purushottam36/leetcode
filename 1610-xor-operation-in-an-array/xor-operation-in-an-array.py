class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Helper function to compute 1 ^ 2 ^ ... ^ x
        def computeXOR(x):
            if x % 4 == 0: return x
            if x % 4 == 1: return 1
            if x % 4 == 2: return x + 1
            return 0

        # Compute the shifted prefix XORs
        shifted_start = start // 2
        shifted_end = shifted_start + n - 1
        
        # XOR sum from shifted_start to shifted_end
        shifted_xor = computeXOR(shifted_start - 1) ^ computeXOR(shifted_end)
        
        # Shift back left by 1 bit
        result = shifted_xor << 1
        
        # Compute the least significant bit (LSB)
        # LSB is 1 only if start is odd and n is odd
        if (start & 1) and (n & 1):
            result |= 1
            
        return result