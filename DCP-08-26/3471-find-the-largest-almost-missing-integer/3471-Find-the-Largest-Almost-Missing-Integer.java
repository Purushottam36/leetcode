import java.util.HashMap;
import java.util.Map;

class Solution {
    // Renamed from largestAlmostMissingInteger to largestInteger to match the driver
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        Map<Integer, Integer> counts = new HashMap<>();
        
        // Count global frequencies of each number
        for (int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        
        // Case 1: k equals the full length of the array
        if (k == n) {
            int maxVal = -1;
            for (int num : nums) {
                maxVal = Math.max(maxVal, num);
            }
            return maxVal;
        }
        
        // Case 2: k is 1
        if (k == 1) {
            int ans = -1;
            for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
                if (entry.getValue() == 1) {
                    ans = Math.max(ans, entry.getKey());
                }
            }
            return ans;
        }
        
        // Case 3: 1 < k < n
        int ans = -1;
        if (counts.get(nums[0]) == 1) { // Fixed: explicitly using index 0
            ans = Math.max(ans, nums[0]);
        }
        if (counts.get(nums[n - 1]) == 1) {
            ans = Math.max(ans, nums[n - 1]);
        }
        
        return ans;
    }
}