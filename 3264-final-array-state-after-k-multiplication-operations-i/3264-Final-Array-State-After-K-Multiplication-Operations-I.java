public class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        // Perform the operation k times
        for (int step = 0; step < k; step++) {
            int minIdx = 0;
            
            // Find the index of the first minimum value
            for (int i = 1; i < nums.length; i++) {
                if (nums[i] < nums[minIdx]) {
                    minIdx = i;
                }
            }
            
            // Update the minimum value
            nums[minIdx] *= multiplier;
        }
        
        return nums;
    }
}