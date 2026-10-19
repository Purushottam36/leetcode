import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int lessThanTarget = 0;
        int equalToTarget = 0;
        
        // Count how many numbers are smaller than and equal to the target
        for (int num : nums) {
            if (num < target) {
                lessThanTarget++;
            } else if (num == target) {
                equalToTarget++;
            }
        }
        
        // Generate the indices based on the counts
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < equalToTarget; i++) {
            result.add(lessThanTarget + i);
        }
        
        return result;
    }
}