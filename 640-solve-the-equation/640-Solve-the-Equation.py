class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate(expr: str) -> tuple[int, int]:
            x_coeff = 0
            const = 0
            sign = 1
            i = 0
            n = len(expr)

            while i < n:
                if expr[i] == '+':
                    sign = 1
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1
                elif expr[i] == 'x':
                    # Implicit coefficient of 1 or -1 (e.g., "x", "-x")
                    x_coeff += sign
                    i += 1
                else:
                    # Parse full multi-digit number
                    num = 0
                    while i < n and expr[i].isdigit():
                        num = num * 10 + int(expr[i])
                        i += 1

                    # Check if the number is a coefficient for 'x' (e.g., "2x", "0x")
                    if i < n and expr[i] == 'x':
                        x_coeff += sign * num
                        i += 1
                    else:
                        const += sign * num

            return x_coeff, const

        left_expr, right_expr = equation.split('=')
        left_x, left_const = evaluate(left_expr)
        right_x, right_const = evaluate(right_expr)

        total_x = left_x - right_x
        total_const = right_const - left_const

        if total_x == 0:
            return "Infinite solutions" if total_const == 0 else "No solution"

        return f"x={total_const // total_x}"