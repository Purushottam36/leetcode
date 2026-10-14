class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        array_sum = sum(nums)
        
        # Calculate the base case: F(0)
        current_f = sum(i * val for i, val in enumerate(nums))
        max_f = current_f
        
        # Iteratively compute F(1) to F(n-1) using the recurrence formula: F(k) = F(k-1) + sum(nums) - n * nums[n-k]
        for k in range(1, n):
            current_f = current_f + array_sum - n * nums[n - k]
            if current_f > max_f:
                max_f = current_f
                
        return max_f