class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = {}
        good_pairs = 0
        
        for num in nums:
            # If the number was seen before, it forms new pairs
            if num in count:
                good_pairs += count[num]
                count[num] += 1
            else:
                count[num] = 1
                
        return good_pairs