class Solution {
    public int distinctIntegers(int n) {
        boolean[] onBoard = new boolean[n + 1];
        onBoard[n] = true; // Start with n on the board
        
        // Loop n times to ensure all cascading dependencies are caught
        for (int day = 0; day < n; day++) {
            // Check every number currently on the board
            for (int x = 1; x <= n; x++) {
                if (onBoard[x]) {
                    // Find all valid i values for this x
                    for (int i = 1; i <= n; i++) {
                        if (x % i == 1) {
                            onBoard[i] = true;
                        }
                    }
                }
            }
        }
        
        // Count how many numbers are marked true
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (onBoard[i]) {
                count++;
            }
        }
        
        return count;
    }
}