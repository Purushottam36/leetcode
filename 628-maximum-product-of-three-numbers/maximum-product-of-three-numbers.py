class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Product of the three largest numbers
        prod1 = nums[n-1] * nums[n-2] * nums[n-3]
        
        # Product of the two smallest (most negative) numbers and the largest number
        prod2 = nums[0] * nums[1] * nums[n-1]
        
        return max(prod1, prod2)
