from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        frequencies = Counter()
        max_length = 0
        left = 0
        
        for right in range(len(nums)):
            frequencies[nums[right]] += 1
            
            # Shrink the window from the left if the frequency condition is violated
            while frequencies[nums[right]] > k:
                frequencies[nums[left]] -= 1
                left += 1
                
            # Update the maximum length of a valid subarray
            max_length = max(max_length, right - left + 1)
            
        return max_length