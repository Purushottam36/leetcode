class Solution {
    public int maxLength(int[] nums) {
        int n = nums.length;
        int maxLen = 0;
        
        // Define the upper limit for LCM * GCD to prune loops safely
        // Maximum possible LCM for numbers 1 to 10 is 2520
        int maxLcmGcdLimit = 2520 * 10; 

        // Check every possible subarray starting at index i
        for (int i = 0; i < n; i++) {
            long prod = 1;
            long currentLcm = nums[i];
            long currentGcd = nums[i];

            for (int j = i; j < n; j++) {
                int val = nums[j];
                
                prod *= val;
                
                // If product exceeds the maximum possible LCM * GCD,
                // it can never be valid. Stop to prevent overflow.
                if (prod > maxLcmGcdLimit) {
                    break;
                }

                currentGcd = gcd(currentGcd, val);
                currentLcm = lcm(currentLcm, val);

                // Check the product equivalent condition
                if (prod == currentLcm * currentGcd) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }

    // Helper method to find Greatest Common Divisor
    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // Helper method to find Least Common Multiple
    private long lcm(long a, long b) {
        return (a * b) / gcd(a, b);
    }
}