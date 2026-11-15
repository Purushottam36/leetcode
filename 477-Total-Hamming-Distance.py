class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        n = len(nums)
        total_distance = 0

        # Since 0 <= nums[i] <= 10^9 (< 2^30), check bits 0 through 29
        for bit in range(30):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1
            
            zeros = n - ones
            total_distance += ones * zeros

        return total_distance