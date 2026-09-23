class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # If the target is exactly 0, we must remove all elements
        if target == 0:
            return len(nums)
        
        # If the target is negative, the array sum is smaller than x, so it's impossible
        if target < 0:
            return -1
        
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the longest subarray that sums up to 'target'
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we hit the exact target, track the maximum subarray length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If a valid subarray was found, subtract its length from the total elements
        return len(nums) - max_len if max_len != -1 else -1