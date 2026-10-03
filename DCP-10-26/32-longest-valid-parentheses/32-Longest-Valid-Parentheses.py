class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left = right = 0
        
        # Pass 1: Left-to-Right Scan
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0
                
        # Reset counters for the reverse pass
        left = right = 0
        
        # Pass 2: Right-to-Left Scan
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0
                
        return max_len