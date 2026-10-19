class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        #Sort the array to easily find the median
        nums.sort()
        
        #The median is at the middle index
        median = nums[len(nums) // 2]
        
        #Sum the absolute differences between each element and the median
        moves = 0
        for num in nums:
            moves += abs(num - median)
            
        return moves