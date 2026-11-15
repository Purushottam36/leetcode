# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self) -> int:
        while True:
            # Generate a uniform random number in the range [1, 49]
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            
            # Accept only [1, 40] to guarantee uniform distribution
            if idx <= 40:
                return (idx - 1) % 10 + 1