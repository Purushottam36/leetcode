class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0  # Minimum possible open '('
        cmax = 0  # Maximum possible open '('
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmin -= 1  # if treated as ')'
                cmax += 1  # if treated as '('
            
            # If max possible open '(' drops below 0, there are too many ')'
            if cmax < 0:
                return False
            
            # cmin cannot drop below 0 (excess '*' can be treated as empty strings)
            if cmin < 0:
                cmin = 0
                
        # The string is valid if 0 open parentheses is a possible final state
        return cmin == 0