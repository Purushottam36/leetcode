import java.util.HashSet;

class Solution {
    public int missingInteger(int[] nums) {
        // Step 1 & 2: Find the longest sequential prefix sum
        int prefixSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                prefixSum += nums[i];
            } else {
                break;
            }
        }
        
        // Step 3: Put all elements in a HashSet for O(1) lookups
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        // Increment prefixSum until it's missing from the set
        while (set.contains(prefixSum)) {
            prefixSum++;
        }
        
        return prefixSum;
    }
}