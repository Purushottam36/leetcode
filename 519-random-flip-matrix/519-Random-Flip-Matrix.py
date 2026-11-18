import random

class Solution:

    def __init__(self, m: int, n: int):
        self.n = n
        self.total = m * n
        self.rem = self.total
        self.swapped = {}

    def flip(self) -> list[int]:
        r = random.randint(0, self.rem - 1)
        self.rem -= 1        
        actual_idx = self.swapped.get(r, r)
        self.swapped[r] = self.swapped.get(self.rem, self.rem)
        
        return [actual_idx // self.n, actual_idx % self.n]

    def reset(self) -> None:
        self.rem = self.total
        self.swapped.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()