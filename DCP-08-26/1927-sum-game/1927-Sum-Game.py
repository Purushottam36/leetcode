class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        # Split into left and right halves
        left_half = num[:mid]
        right_half = num[mid:]
        
        # Calculate sums and counts for left half
        left_sum = sum(int(c) for c in left_half if c.isdigit())
        left_q = left_half.count('?')
        
        # Calculate sums and counts for right half
        right_sum = sum(int(c) for c in right_half if c.isdigit())
        right_q = right_half.count('?')
        
        # Calculate differences
        sum_diff = left_sum - right_sum
        q_diff = left_q - right_q
        
        # Bob wins if the total balance matches 0
        # This requires q_diff to be even if sum_diff is to be balanced by 9 * (q_diff / 2)
        return sum_diff * 2 != -q_diff * 9