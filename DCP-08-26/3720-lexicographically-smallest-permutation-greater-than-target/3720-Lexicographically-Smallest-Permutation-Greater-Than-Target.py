from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Step 1: Count available characters in s
        counts = Counter(s)
        n = len(s)
        res = []
        
        # Step 2: Try to match target character by character
        def build(idx: int, is_greater: bool) -> bool:
            if idx == n:
                return is_greater
            
            # Case 1: We have already made the prefix strictly greater.
            # Pick the smallest available characters greedily.
            if is_greater:
                for ch_ord in range(97, 123):  # 'a' to 'z'
                    ch = chr(ch_ord)
                    if counts[ch] > 0:
                        counts[ch] -= 1
                        res.append(ch)
                        if build(idx + 1, True):
                            return True
                        res.pop()
                        counts[ch] += 1
                return False
            
            # Case 2: We are still matching target's prefix so far.
            # Subcase A: Try to keep matching target[idx]
            tgt_ch = target[idx]
            if counts[tgt_ch] > 0:
                counts[tgt_ch] -= 1
                res.append(tgt_ch)
                if build(idx + 1, False):
                    return True
                res.pop()
                counts[tgt_ch] += 1
            
            # Subcase B: Break away and make this position strictly greater
            for ch_ord in range(ord(tgt_ch) + 1, 123):
                ch = chr(ch_ord)
                if counts[ch] > 0:
                    counts[ch] -= 1
                    res.append(ch)
                    if build(idx + 1, True):
                        return True
                    res.pop()
                    counts[ch] += 1
            
            return False

        return "".join(res) if build(0, False) else ""