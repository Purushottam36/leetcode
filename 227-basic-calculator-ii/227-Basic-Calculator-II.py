class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        last_number = 0
        current_number = 0
        operation = '+'
        n = len(s)
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if char in "+-*/" or i == n - 1:
                if char != ' ' or i == n - 1:
                    if operation == '+' or operation == '-':
                        result += last_number
                        last_number = current_number if operation == '+' else -current_number
                    elif operation == '*':
                        last_number = last_number * current_number
                    elif operation == '/':
                        last_number = int(last_number / current_number)
                    
                    operation = char
                    current_number = 0
                    
        result += last_number
        return result