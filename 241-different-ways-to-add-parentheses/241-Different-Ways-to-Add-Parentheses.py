class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}
        
        def compute(expr: str) -> list[int]:
            # Return memoized result if already calculated
            if expr in memo:
                return memo[expr]
            
            res = []
            # Base case: if expression is just a number
            if expr.isdigit():
                return [int(expr)]
                
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Divide: Split into left and right expressions
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    # Conquer: Combine results from left and right halves
                    for l in left_results:
                        for r in right_results:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            memo[expr] = res
            return res

        return compute(expression)