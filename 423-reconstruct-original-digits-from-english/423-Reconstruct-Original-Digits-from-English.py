from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count the frequency of each letter in the input string
        count = Counter(s)
        
        # Array to store the frequency of each digit from 0 to 9
        out = [0] * 10
        
        # Phase 1: Unique character checks
        out[0] = count['z']
        out[2] = count['w']
        out[4] = count['u']
        out[6] = count['x']
        out[8] = count['g']
        
        # Phase 2: Characters shared with already deduced numbers
        out[3] = count['h'] - out[8]
        out[5] = count['f'] - out[4]
        out[7] = count['s'] - out[6]
        
        # Phase 3: Remaining digits
        out[1] = count['o'] - out[0] - out[2] - out[4]
        out[9] = count['i'] - out[5] - out[6] - out[8]
        
        # Build the final sorted string of digits
        result = []
        for digit in range(10):
            result.append(str(digit) * out[digit])
            
        return "".join(result)