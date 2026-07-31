class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count of odd numbers up to high minus count of odd numbers up to low-1
        return (high + 1) // 2 - low // 2
