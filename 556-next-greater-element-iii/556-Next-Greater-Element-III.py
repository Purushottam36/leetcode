class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        
        # 1. Find the first decreasing element from the right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # If the entire number is non-increasing, no greater permutation exists
        if i == -1:
            return -1
            
        # 2. Find the smallest digit to the right of i that is larger than digits[i]
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # 3. Swap them
        digits[i], digits[j] = digits[j], digits[i]
        
        # 4. Reverse the suffix to get the smallest possible order
        digits[i + 1:] = reversed(digits[i + 1:])
        
        res = int("".join(digits))
        
        # 5. Check 32-bit signed integer limit
        return res if res <= 2**31 - 1 else -1