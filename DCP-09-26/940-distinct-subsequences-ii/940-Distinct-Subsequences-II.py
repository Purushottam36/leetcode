class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Tracks the number of subsequences ending with each character
        # last[0] for 'a', last[1] for 'b', etc.
        last = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            
            # The number of new subsequences we can form ending with 'char' is equal to (total subsequences so far) + 1  We add 1 for the single-character subsequence itself
            new_ends_with_char = (sum(last) + 1) % MOD
            
            # Update the count for the current character
            last[idx] = new_ends_with_char
            
        # The answer is the sum of subsequences ending in all possible characters
        return sum(last) % MOD