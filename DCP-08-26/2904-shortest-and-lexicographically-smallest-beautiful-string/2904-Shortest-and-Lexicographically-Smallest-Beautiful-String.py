class Solution:
    def shortestBeautifulString(self, s: str, k: int) -> str:
        # Quick check: if the total number of '1's is less than k, no solution exists
        if s.count('1') < k:
            return ""
        
        ans = ""
        min_len = float('inf')  # Track the shortest valid length found so far
        left = 0                # Left pointer of our sliding window
        current_ones = 0        # Count of '1's inside the current window
        
        # Expand the right pointer to explore the string
        for right in range(len(s)):
            if s[right] == '1':
                current_ones += 1
                
            # Shrink the window from the left as long as we have exactly k '1's
            while current_ones == k:
                # A minimal beautiful substring must start and end with a '1'.
                # If s[left] is '0', we can safely discard it without breaking the condition.
                if s[left] == '1':
                    current_len = right - left + 1
                    current_sub = s[left:right+1]
                    
                    # Update answer if we found a shorter substring
                    if current_len < min_len:
                        min_len = current_len
                        ans = current_sub
                    # If lengths match, choose the lexicographically smaller one
                    elif current_len == min_len:
                        if current_sub < ans:
                            ans = current_sub
                            
                    # Drop the '1' at the left pointer to look for other windows
                    current_ones -= 1
                
                # Move the left pointer forward
                left += 1
                
        return ans

    # ALIAS METHOD:
    # Some variations of this LeetCode problem expect 'shortestBeautifulSubstring'
    # instead of 'shortestBeautifulString'. This ensures compatibility with both.
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        return self.shortestBeautifulString(s, k)
