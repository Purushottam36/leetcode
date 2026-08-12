class Solution {
    public int diagonalPrime(int[][] nums) {
        int n = nums.length;
        int maxPrime = 0;
        
        for (int i = 0; i < n; i++) {
            int primary = nums[i][i];
            int secondary = nums[i][n - i - 1];
            
            // Check primary diagonal element
            if (primary > maxPrime && isPrime(primary)) {
                maxPrime = primary;
            }
            
            // Check secondary diagonal element
            if (secondary > maxPrime && isPrime(secondary)) {
                maxPrime = secondary;
            }
        }
        
        return maxPrime;
    }
    
    // Helper method to check primality in O(sqrt(X)) time
    private boolean isPrime(int num) {
        if (num <= 1) return false;
        if (num <= 3) return true;
        if (num % 2 == 0 || num % 3 == 0) return false;
        
        for (int i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}