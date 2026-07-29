from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Step 1 & 2: Calculate digit sums and group frequencies
        group_sizes = Counter()
        
        for i in range(1, n + 1):
            # Calculate the sum of digits for number i
            digit_sum = 0
            temp = i
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            group_sizes[digit_sum] += 1
            
        # Step 3: Find the size of the largest group
        max_size = max(group_sizes.values())
        
        # Step 4: Count how many groups share this largest size
        return sum(1 for size in group_sizes.values() if size == max_size)