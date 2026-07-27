class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the two largest numbers found so far
        max1 = 0
        max2 = 0
        
        # Track the two highest values in a single pass
        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
                
        # Return the maximum product of the two elements decremented by 1
        return (max1 - 1) * (max2 - 1)