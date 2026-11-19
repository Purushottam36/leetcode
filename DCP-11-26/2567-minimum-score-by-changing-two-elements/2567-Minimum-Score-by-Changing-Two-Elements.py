class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        
        # Option 1: Change two smallest elements
        change_two_smallest = nums[n - 1] - nums[2]
        
        # Option 2: Change two largest elements
        change_two_largest = nums[n - 3] - nums[0]
        
        # Option 3: Change one smallest and one largest element
        change_both_ends = nums[n - 2] - nums[1]
        
        return min(change_two_smallest, change_two_largest, change_both_ends)