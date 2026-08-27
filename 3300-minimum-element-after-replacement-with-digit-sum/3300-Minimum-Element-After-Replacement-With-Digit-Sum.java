class Solution {
    public int minElement(int[] nums) {
        // Initialize minimum with the maximum possible value
        int minSum = Integer.MAX_VALUE;
        
        for (int num : nums) {
            int currentSum = 0;
            int temp = num;
            
            // Calculate sum of digits
            while (temp > 0) {
                currentSum += temp % 10;
                temp /= 10;
            }
            
            // Track the smallest digit sum found so far
            if (currentSum < minSum) {
                minSum = currentSum;
            }
        }
        
        return minSum;
    }
}