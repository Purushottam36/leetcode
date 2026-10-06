class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                # We need a matching closing parenthesis later
                close_needed += 1
            else:  # char == ')'
                if close_needed > 0:
                    # Match it with a previously opened '('
                    close_needed -= 1
                else:
                    # No '(' available, so we must add an opening parenthesis
                    open_needed += 1
                    
        # The total insertions required is the sum of unmatched open and close brackets
        return open_needed + close_needed