class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        # The result array can hold at most m + n digits
        result = [0] * (m + n)
        
        # Multiply digit by digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Calculate the product of the two current digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array where this product contributes
                p1 = i + j
                p2 = i + j + 1
                
                # Add the product to any existing value (or carry) at position p2
                total = mul + result[p2]
                
                # Update positions with the single digit result and the carry
                result[p2] = total % 10
                result[p1] += total // 10
                
        # Convert the digit array back into a string, skipping leading zeros
        ans = []
        for digit in result:
            if not (len(ans) == 0 and digit == 0):
                ans.append(str(digit))
                
        return "".join(ans)