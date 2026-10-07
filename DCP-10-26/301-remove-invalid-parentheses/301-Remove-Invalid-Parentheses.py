class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Calculate the exact number of misplaced left and right parentheses
        left_rem = 0
        right_rem = 0
        
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
                    
        result = set()
        
        # DFS Backtracking helper function
        def backtrack(index, left_count, right_count, left_rem, right_rem, path):
            # Base case: reached the end of the string
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add("".join(path))
                return
            
            char = s[index]
            
            # Try discarding the current character if it's an invalid parenthesis
            if char == '(' and left_rem > 0:
                backtrack(index + 1, left_count, right_count, left_rem - 1, right_rem, path)
            elif char == ')' and right_rem > 0:
                backtrack(index + 1, left_count, right_count, left_rem, right_rem - 1, path)
                
            # Try keeping the current character
            path.append(char)
            if char not in ('(', ')'):
                # Non-parentheses characters are always kept
                backtrack(index + 1, left_count, right_count, left_rem, right_rem, path)
            elif char == '(':
                backtrack(index + 1, left_count + 1, right_count, left_rem, right_rem, path)
            elif char == ')' and left_count > right_count:
                # We only keep a ')' if there is a matching '(' available before it
                backtrack(index + 1, left_count, right_count + 1, left_rem, right_rem, path)
            
            # Backtrack step: clean up the path for the next branch
            path.pop()

        # Kickstart the recursion
        backtrack(0, 0, 0, left_rem, right_rem, [])
        return list(result)