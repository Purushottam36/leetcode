class Solution {
    public int countPartitions(int[] nums) {
        int totalSum = 0;
        
        // Calculate the total sum of the array
        for (int num : nums) {
            totalSum += num;
        }
        
        // If total sum is even, all n - 1 partitions are valid.
        // If total sum is odd, no partition can have an even difference.
        if (totalSum % 2 == 0) {
            return nums.length - 1;
        } else {
            return 0;
        }
    }
}