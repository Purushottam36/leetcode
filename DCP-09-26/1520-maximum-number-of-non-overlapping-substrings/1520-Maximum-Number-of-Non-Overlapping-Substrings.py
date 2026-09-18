class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record the first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        valid_intervals = []
        
        # Step 2: Build and expand valid intervals for each character
        for ch in first:
            left = first[ch]
            right = last[ch]
            
            i = left
            is_valid = True
            while i <= right:
                curr_ch = s[i]
                left = min(left, first[curr_ch])
                right = max(right, last[curr_ch])
                
                # If the left bound stretches before the starting character's first index,
                # this interval will be fully processed when evaluating that earlier character.
                if left < first[ch]:
                    is_valid = False
                    break
                i += 1
                
            if is_valid:
                valid_intervals.append((left, right))
                
        # Step 3: Sort intervals by their start index to process greedily
        valid_intervals.sort()
        
        ans = []
        last_right = -1
        
        for left, right in valid_intervals:
            # Case 1: No overlap with the previously chosen interval -> Add it
            if left > last_right:
                ans.append(s[left:right + 1])
                last_right = right
            # Case 2: Nested inside the previous interval -> Replace with the smaller one
            # to minimize total length and maximize remaining room.
            elif right <= last_right:
                ans[-1] = s[left:right + 1]
                last_right = right
                
        return ans