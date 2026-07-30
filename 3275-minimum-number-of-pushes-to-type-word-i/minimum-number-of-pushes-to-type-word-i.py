class Solution:
    def minimumPushes(self, word: str) -> int:
        length = len(word)
        pushes = 0
        
        # Iterate through each character by index
        for i in range(length):
            # i // 8 gives 0 for first 8 keys, 1 for next 8 keys, etc.
            pushes += (i // 8) + 1
            
        return pushes