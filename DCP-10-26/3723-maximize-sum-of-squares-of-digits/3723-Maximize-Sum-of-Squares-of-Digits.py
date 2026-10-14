class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the required sum is impossible to achieve even with all 9s
        if sum > 9 * num:
            return ""
        
        # Calculate how many 9s we can use and what the remainder is
        nines = sum // 9
        remainder = sum % 9
        
        if remainder > 0:
            # Place 9s first, then the remainder digit, then pad the rest with 0s
            return "9" * nines + str(remainder) + "0" * (num - nines - 1)
        else:
            # Place 9s first, then pad the remaining places with 0s
            return "9" * nines + "0" * (num - nines)