class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1      
        count = 9       
        start = 1       
        
        #Identify which digit-length group n falls into
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
            
        #Find the exact number that contains the nth digit (n - 1) is used for 0-indexed offset shifting
        target_num = start + (n - 1) // length
        
        #Find the specific digit within that target number
        digit_idx = (n - 1) % length
        
        # Convert to a string to pull out the precise digit index, then return as an integer
        return int(str(target_num)[digit_idx])