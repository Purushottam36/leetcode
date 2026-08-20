class Solution {
    public int numberOfChild(int n, int k) {
        // Step 1: Time taken to travel from one end to the other
        int roundTime = n - 1;
        
        // Step 2 & 3: Find total completed passes and remaining seconds
        int rounds = k / roundTime;
        int rem = k % roundTime;
        
        // Step 4: Check direction based on parity of rounds
        if (rounds % 2 == 0) {
            // Even rounds -> Moving Forward (0 -> n-1)
            return rem;
        } else {
            // Odd rounds -> Moving Backward (n-1 -> 0)
            return roundTime - rem;
        }
    }
}