class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Step 1: Count character frequencies
        char_counts = [0] * 26
        for char in s:
            char_counts[ord(char) - ord('a')] += 1
            
        first_half = []
        center_char = ""
        
        # Step 2: Build the first half lexicographically
        for i in range(26):
            if char_counts[i] > 0:
                char = chr(ord('a') + i)
                # Check for an odd frequency character
                if char_counts[i] % 2 != 0:
                    center_char = char
                # Add half of the characters to the first half
                first_half.append(char * (char_counts[i] // 2))
                
        # Join the list to form the first half string
        first_half_str = "".join(first_half)
        
        # Step 3: Mirror the first half around the center character
        return first_half_str + center_char + first_half_str[::-1]