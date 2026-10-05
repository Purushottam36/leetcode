class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                # If the current ')' immediately follows a '(', we found a core "()" pair
                if s[i - 1] == '(':
                    score += 1 << depth  # 1 << depth is a fast bitwise way to compute 2^depth
                    
        return score