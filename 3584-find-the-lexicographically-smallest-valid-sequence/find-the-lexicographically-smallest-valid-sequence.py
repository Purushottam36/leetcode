class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        
        # last[j] will store the maximum index in word1 
        # that can match the suffix word2[j:] greedily from the right.
        last = [-1] * (m + 1)
        last[m] = n
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
                
        ans = []
        j = 0
        changed = False
        
        for i in range(n):
            if j == m:
                break
                
            # Case 1: Characters match perfectly
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Case 2: Mismatch, but we can change at most one character
            elif not changed and (i + 1 <= last[j + 1]):
                ans.append(i)
                j += 1
                changed = True
                
        return ans if len(ans) == m else []