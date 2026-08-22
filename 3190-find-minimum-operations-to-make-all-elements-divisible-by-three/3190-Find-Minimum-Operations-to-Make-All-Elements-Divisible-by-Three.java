class Solution {
    public int minimumOperations(int[] nums) {
        int operations = 0;
        
        // Iterate through each number in the array
        for (int num : nums) {
            // If the number is not already divisible by 3, 
            // it always takes exactly 1 operation (either +1 or -1) to make it divisible.
            if (num % 3 != 0) {
                operations++;
            }
        }
        
        return operations;
    }
}