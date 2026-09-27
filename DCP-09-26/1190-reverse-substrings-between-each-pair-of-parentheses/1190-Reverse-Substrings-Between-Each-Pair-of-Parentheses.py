class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until we find the matching '('
                current_substring = []
                while stack and stack[-1] != '(':
                    current_substring.append(stack.pop())
                
                # Pop the opening parenthesis '(' itself
                if stack:
                    stack.pop()
                
                # Push the reversed characters back onto the stack
                for c in current_substring:
                    stack.append(c)
            else:
                # Push current character (letters and '(') onto the stack
                stack.append(char)
                
        return "".join(stack)