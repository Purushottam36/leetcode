class Solution {
    public int passThePillow(int n, int time) {
        // Step 1: Calculate the length of a single unidirectional round
        int roundLength = n - 1;
        
        // Step 2: Determine full rounds completed and remaining seconds
        int rounds = time / roundLength;
        int remaining = time % roundLength;
        
        // Step 3: Determine the position based on the direction (even = forward, odd = backward)
        if (rounds % 2 == 0) {
            return 1 + remaining; // Moving forward from 1
        } else {
            return n - remaining; // Moving backward from n
        }
    }
}