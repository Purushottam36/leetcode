import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: list[int]):
        # Initialize a dictionary to map each number to a list of its indices
        self.indices = defaultdict(list)
        for index, num in enumerate(nums):
            self.indices[num].append(index)
        

    def pick(self, target: int) -> int:
        # Retrieve the index list for the target and choose one at random
        return random.choice(self.indices[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)