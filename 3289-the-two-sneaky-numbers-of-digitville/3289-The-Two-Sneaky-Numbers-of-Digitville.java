import java.util.HashSet;

class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        // Create an array of size 2 to store our answers
        int[] result = new int[2];
        int index = 0;
        
        // Use a HashSet to track numbers we have already encountered
        HashSet<Integer> seen = new HashSet<>();
        
        for (int num : nums) {
            // If the number is already in the set, it's a duplicate (sneaky number)
            if (seen.contains(num)) {
                result[index] = num;
                index++;
                
                // Once we find both sneaky numbers, we can stop early
                if (index == 2) {
                    break;
                }
            } else {
                // Otherwise, add it to our seen tracking set
                seen.add(num);
            }
        }
        
        return result;
    }
}