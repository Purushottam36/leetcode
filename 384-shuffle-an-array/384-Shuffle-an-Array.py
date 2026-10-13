import random

class Solution:

    def __init__(self, nums: list[int]):
        """
        Initializes the object with the integer array nums.
        """
        # Store a copy of the original array to safely reset later
        self.original = list(nums)
        # Store a mutable working array that will be shuffled in place
        self.array = list(nums)

    def reset(self) -> list[int]:
        """
        Resets the array to its original configuration and returns it.
        """
        self.array = list(self.original)
        return self.array

    def shuffle(self) -> list[int]:
        """
        Returns a random shuffling of the array.
        """
        # Fisher-Yates shuffle algorithm
        for i in range(len(self.array) - 1, 0, -1):
            # Pick a random index from 0 to i inclusive
            j = random.randint(0, i)
            # Swap elements at indices i and j
            self.array[i], self.array[j] = self.array[j], self.array[i]
            
        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()