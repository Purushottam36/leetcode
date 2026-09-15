class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        i = 0  # Tracks the start of the valid remaining string search area
        
        # Iterate through every possible end index of a potential palindrome
        for r in range(n):
            # 1. Check for a valid palindrome of length k ending at r
            l1 = r - k + 1
            if l1 >= i and s[l1:r+1] == s[l1:r+1][::-1]:
                count += 1
                i = r + 1  # Greedily jump past this palindrome
                continue
                
            # 2. Check for a valid palindrome of length k + 1 ending at r
            l2 = r - k  # equivalent to r - (k + 1) + 1
            if l2 >= i and s[l2:r+1] == s[l2:r+1][::-1]:
                count += 1
                i = r + 1  # Greedily jump past this palindrome
                continue
                
        return count