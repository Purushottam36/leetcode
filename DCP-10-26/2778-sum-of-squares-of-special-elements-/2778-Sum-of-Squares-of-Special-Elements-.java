class Solution {
    public int sumOfSquares(int[] nums) {
        int n = nums.length;
        int totalSum = 0;
        
        // Loop through the array using 1-based indexing
        for (int i = 1; i <= n; i++) {
            // Check if 'i' divides 'n' evenly
            if (n % i == 0) {
                // Since Java arrays are 0-indexed, 
                // the 1-indexed position 'i' maps to nums[i - 1]
                totalSum += nums[i - 1] * nums[i - 1];
            }
        }
        
        return totalSum;
    }
}