import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int missingMultiple(int[] nums, int k) {
        // Convert the array to a HashSet for O(1) lookups
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        // Start checking from the first positive multiple of k
        int multiple = k;
        
        // Increment by k until a missing multiple is found
        while (numSet.contains(multiple)) {
            multiple += k;
        }
        
        return multiple;
    }
}