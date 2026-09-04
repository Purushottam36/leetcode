class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        
        // 1. Precompute suffix minimums
        int[] suffMin = new int[n];
        int currentMin = Integer.MAX_VALUE;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] < currentMin) {
                currentMin = nums[i];
            }
            suffMin[i] = currentMin;
        }
        
        // 2. Track prefix maximum on the fly and check stability
        int currentMax = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentMax) {
                currentMax = nums[i];
            }
            
            // Cast to long to handle potential edge case overflows defensively
            if ((long) currentMax - suffMin[i] <= k) {
                return i; // Found the first (smallest) stable index
            }
        }
        
        return -1;
    }
}