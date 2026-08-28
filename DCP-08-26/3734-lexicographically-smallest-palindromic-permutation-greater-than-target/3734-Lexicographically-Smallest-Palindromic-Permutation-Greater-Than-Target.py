from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        k = n // 2
        counts = Counter(s)
        
        # Check if a valid palindrome can be formed
        odd_chars = [c for c, v in counts.items() if v % 2 != 0]
        if len(odd_chars) > 1:
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        pool = {c: v // 2 for c, v in counts.items() if v // 2 > 0}
        candidates = []
        
        # Case 1: Palindrome branches off before index k
        for i in range(k):
            prefix_counts = Counter(target[:i])
            valid_prefix = True
            rem_pool = pool.copy()
            
            for c, v in prefix_counts.items():
                if rem_pool.get(c, 0) < v:
                    valid_prefix = False
                    break
                rem_pool[c] -= v
                if rem_pool[c] == 0:
                    del rem_pool[c]
                    
            if not valid_prefix:
                continue
                
            # Try setting a strictly larger character at position i
            for c in sorted(rem_pool.keys()):
                if c > target[i]:
                    first_half = list(target[:i]) + [c]
                    temp_pool = rem_pool.copy()
                    temp_pool[c] -= 1
                    if temp_pool[c] == 0:
                        del temp_pool[c]
                        
                    # Fill the remaining first-half characters optimally (ascending)
                    for rc in sorted(temp_pool.keys()):
                        first_half.extend([rc] * temp_pool[rc])
                        
                    first_half_str = "".join(first_half)
                    full_p = first_half_str + mid_char + first_half_str[::-1]
                    candidates.append(full_p)
                    
        # Case 2: Palindrome's first half matches target[:k] exactly
        prefix_counts = Counter(target[:k])
        if all(pool.get(c, 0) == v for c, v in prefix_counts.items()) and len(pool) == len(prefix_counts):
            first_half_str = target[:k]
            full_p = first_half_str + mid_char + first_half_str[::-1]
            if full_p > target:
                candidates.append(full_p)
                
        return min(candidates) if candidates else ""