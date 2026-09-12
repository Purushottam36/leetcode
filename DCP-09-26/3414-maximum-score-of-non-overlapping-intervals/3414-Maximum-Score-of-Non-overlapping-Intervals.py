import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Structure: (right, left, weight, original_idx)
        # Sorting by the right endpoint is required for interval-based DP binary search
        sorted_intervals = sorted(
            (interval[1], interval[0], interval[2], idx) 
            for idx, interval in enumerate(intervals)
        )
        
        # Array of right endpoints for bisect lookup
        ends = [x[0] for x in sorted_intervals]
        n = len(intervals)
        
        # dp[p][i] stores a tuple: (max_weight, tuple_of_selected_indices)
        # Using exact counts preserves the correct structural path comparison
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(1, n + 1):
            right, left, weight, orig_idx = sorted_intervals[i - 1]
            
            # Find the largest index `j` where the interval's right endpoint < current left endpoint
            j = bisect.bisect_left(ends, left)
            
            for p in range(1, 5):
                # Choice 1: Skip the current interval
                skip_w, skip_idx = dp[p][i - 1]
                
                # Choice 2: Take the current interval
                prev_w, prev_idx = dp[p - 1][j]
                
                # If p > 1 and prev_idx is empty, it means it's an unreachable state
                if p > 1 and not prev_idx:
                    dp[p][i] = (skip_w, skip_idx)
                    continue
                
                take_w = prev_w + weight
                take_idx = tuple(sorted(prev_idx + (orig_idx,)))
                
                # Track the best maximum weight, tie-break with lexicographically smaller index tuple
                if take_w > skip_w:
                    dp[p][i] = (take_w, take_idx)
                elif skip_w > take_w:
                    dp[p][i] = (skip_w, skip_idx)
                else:
                    if not skip_idx or take_idx < skip_idx:
                        dp[p][i] = (take_w, take_idx)
                    else:
                        dp[p][i] = (skip_w, skip_idx)
                        
        # Traverse across all valid lengths (1 to 4) to locate the absolute best option
        ans_w, ans_idx = 0, ()
        for p in range(1, 5):
            w, idx = dp[p][n]
            if w > ans_w:
                ans_w, ans_idx = w, idx
            elif w == ans_w and idx:
                if not ans_idx or idx < ans_idx:
                    ans_idx = idx
                    
        # Return only the resulting list of indices
        return list(ans_idx)