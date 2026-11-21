import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        n = len(expression)
        i = 0

        while i < n:
            sign = 1
            if expression[i] in "+-":
                if expression[i] == "-":
                    sign = -1
                i += 1

            cur_num = 0
            while i < n and expression[i].isdigit():
                cur_num = cur_num * 10 + int(expression[i])
                i += 1

            # Skip '/'
            i += 1

            cur_den = 0
            while i < n and expression[i].isdigit():
                cur_den = cur_den * 10 + int(expression[i])
                i += 1

            num = num * cur_den + sign * cur_num * den
            den *= cur_den

            g = math.gcd(abs(num), den)
            num //= g
            den //= g

        return f"{num}/{den}"