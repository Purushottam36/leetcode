import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        
        half_counts = {}
        mid = ""
        half_len = 0
        
        # Identify mid character and capture half counts
        for char in sorted(counts.keys()):
            count = counts[char]
            if count % 2 == 1:
                mid = char
            half_counts[char] = count // 2
            half_len += count // 2
            
        # Compute the initial total permutations using full factorials just once
        total_perms = math.factorial(half_len)
        for count in half_counts.values():
            if count > 0:
                total_perms //= math.factorial(count)

        # Early exit if k is out of bounds
        if k > total_perms:
            return ""
        
        first_half = []
        rem_len = half_len
        current_perms = total_perms
        
        # Step 2: Construct the first half character by character
        for i in range(half_len):
            # Iterate through available characters alphabetically
            for char in sorted(half_counts.keys()):
                if half_counts[char] > 0:
                    # Calculate permutations if we choose 'char' using O(1) math
                    # Formula: current_perms * (count_of_char / rem_len)
                    possible_perms = (current_perms * half_counts[char]) // rem_len
                    
                    if k <= possible_perms:
                        # 'char' is the correct choice for this position
                        first_half.append(char)
                        half_counts[char] -= 1
                        rem_len -= 1
                        current_perms = possible_perms
                        break
                    else:
                        # Skip all permutations starting with this 'char' branch
                        k -= possible_perms
                        
        # Step 3: Mirror the string to reconstruct the full palindrome
        first_half_str = "".join(first_half)
        return first_half_str + mid + first_half_str[::-1]