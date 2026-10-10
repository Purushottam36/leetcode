class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Total operations we can perform across both arrays
        k = k1 + k2
        
        # Determine the maximum absolute difference possible from constraints
        max_diff = 100000
        freq = [0] * (max_diff + 1)
        
        # Populate the frequency array with absolute differences
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            freq[diff] += 1
            
        # Greedily reduce the largest differences first
        for d in range(max_diff, 0, -1):
            if freq[d] == 0:
                continue
                
            # Take as many elements at this difference level as our operations allow
            take = min(k, freq[d])
            
            # Shift the modified elements to the lower difference level (d - 1)
            freq[d] -= take
            freq[d - 1] += take
            k -= take
            
            # If we run out of modifications, we can exit early
            if k == 0:
                break
                
        # Calculate the final sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if freq[d] > 0:
                ans += freq[d] * (d ** 2)
                
        return ans