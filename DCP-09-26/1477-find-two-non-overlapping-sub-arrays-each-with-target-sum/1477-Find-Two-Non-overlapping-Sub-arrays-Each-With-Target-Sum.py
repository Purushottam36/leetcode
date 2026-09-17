class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len_so_far[i] stores the minimum length of a sub-array with sum == target in arr[0...i]
        min_len_so_far = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_sum_lengths = float('inf')
        best_len_till_now = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window if the sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            # If we found a valid sub-array
            if current_sum == target:
                current_len = right - left + 1
                
                # Check if a valid non-overlapping sub-array exists before 'left'
                if left > 0 and min_len_so_far[left - 1] != float('inf'):
                    min_sum_lengths = min(min_sum_lengths, current_len + min_len_so_far[left - 1])
                
                # Update the best length seen up to the current right index
                best_len_till_now = min(best_len_till_now, current_len)
            
            min_len_so_far[right] = best_len_till_now
            
        return min_sum_lengths if min_sum_lengths != float('inf') else -1