class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each letter
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        
        # Sort frequencies in descending order
        freq.sort(reverse=True)
        
        total_pushes = 0
        for i in range(26):
            if freq[i] == 0:
                break
            # Calculate cost based on group of 8
            push_cost = (i // 8) + 1
            total_pushes += freq[i] * push_cost
            
        return total_pushes