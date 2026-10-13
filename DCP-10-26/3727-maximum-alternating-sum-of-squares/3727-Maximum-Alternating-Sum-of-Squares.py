class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Convert all numbers to their squares
        squares = [x ** 2 for x in nums]
        
        # Sort squares in descending order
        squares.sort(reverse=True)
        
        # Calculate how many elements will have a positive sign: ceil(n / 2)
        n = len(nums)
        positive_count = (n + 1) // 2
        
        # Sum the largest squares and subtract the smallest squares
        return sum(squares[:positive_count]) - sum(squares[positive_count:])