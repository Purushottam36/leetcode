class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        # Every local inversion is also a global inversion.
        # For global inversions == local inversions, there can be NO non-local inversions
        # (i.e., no pair (i, j) with j >= i + 2 and nums[i] > nums[j]).
        # In a permutation of [0..n-1], this holds iff every element is at most 1 index away from its value.
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False
                
        return True