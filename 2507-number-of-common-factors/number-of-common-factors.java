class Solution {
    public int commonFactors(int a, int b) {
        // Step 1: Find the Greatest Common Divisor
        int gcd = gcd(a, b);
        int count = 0;
        
        // Step 2: Count the factors of the GCD up to its square root
        for (int i = 1; i * i <= gcd; i++) {
            if (gcd % i == 0) {
                count++; // 'i' is a factor
                if (i * i != gcd) {
                    count++; // 'gcd / i' is also a distinct factor
                }
            }
        }
        
        return count;
    }
    
    // Helper method to compute GCD using Euclidean algorithm
    private int gcd(int x, int y) {
        while (y != 0) {
            int temp = y;
            y = x % y;
            x = temp;
        }
        return x;
    }
}