class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0      # Total number of insertions needed
        need = 0     # Number of right parentheses ')' currently required
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                need += 2  
                
                # If 'need' becomes odd, a previous '(' only got ONE ')' , We must immediately insert a ')' right now to fix it.
                if need % 2 != 0:
                    res += 1
                    need -= 1
                i += 1
            else:
                # We encountered a ')'. Check if there's a consecutive ')' next to it.
                if i + 1 < n and s[i + 1] == ')':
                    i += 2  
                else:
                    res += 1  
                    i += 1    
                
                # Now match the pair of '))' with a left parenthesis '('
                if need > 0:
                    need -= 2  
                else:
                    res += 1   
                    
        # Return any insertions made, plus any remaining ')' still needed at the end
        return res + need