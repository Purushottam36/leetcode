class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            # Number of subarrays containing arr[i]
            total_subarrays = (i + 1) * (n - i)
            # Number of odd-length subarrays containing arr[i]
            odd_subarrays = (total_subarrays + 1) // 2
            
            total_sum += odd_subarrays * arr[i]
            
        return total_sum